from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, Signal, Slot, QLocale)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QGuiApplication)
from PySide2.QtWidgets import *

from pygame import mixer
from pydub import AudioSegment
import os,sys,time,threading

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))+'\\'
sys.path.append(os.path.abspath(CURRENT_DIR+'..'))

from UI import PlayUI
from commons import tools

WORD_DIR,_,RETEST_DIR,SOUND_DIR,_=tools.get_path(CURRENT_DIR)

try:
    mixer.pre_init(24000,-16,1)
    mixer.init()
except Exception as e:
    print('Error with Pygame Mixer')
    print(e)
    sys.exit(1)


class Signal(QObject):
    s=Signal(tuple)
    p=Signal(int)


class PlayUI(QMainWindow,PlayUI):
    def __init__(self):
        def set_path():
            self.__origin=[]
            self.__origin_file,orign_path=tuple(tools.get_file(WORD_DIR))
            self.__origin_len=len(self.__origin_file)
            for dir in orign_path:
                self.__origin.append(tools.parsing(dir)[0])
            
            names,self.__files=[],[]
            for dir in (WORD_DIR,RETEST_DIR):
                tmp1,tmp2=tools.get_file(dir)
                names+=tmp1; self.__files+=tmp2
            self.comboName.clear()
            self.comboName.addItems(names)
            self.__refresh_mode=2
            self.__setFile()
        
        def rev():
            check()
            if self.chkRev.isChecked():
                self.chkRev.setText('K\u2192E')
            else:
                self.chkRev.setText('E\u2192K')
        
        def check():
            if self.__file_name!=self.__files[self.comboName.currentIndex()] or self.__rev!=self.chkRev.isChecked():
                self.__refresh_mode=2
                self.btnSet.setEnabled(True)
                self.btnSet.setStyleSheet('color: red')
            elif self.__repeat!=self.spinNum.value():
                if self.spinNum.value()<=self.__r: #r=repeat count-1
                    self.__refresh_mode=2
                    self.btnSet.setEnabled(True)
                    self.btnSet.setStyleSheet('color: red')
                else:
                    self.__refresh_mode=1
                    self.btnSet.setEnabled(True)
                    self.btnSet.setStyleSheet('color: blue')
            else:
                self.__refresh_mode=0
                self.btnSet.setStyleSheet('')
                self.btnSet.setEnabled(False)
        
        def cell_click_trigger(a):
            if self.__isStop:
                self.__manual_play(a)
            else:
                self.__stop(is_jump=a)
        
        def cell_click_trigger_2(k):
            assert type(k) is int
            if k:
                self.__start(n=k)
        
        super().__init__()
        self.setupUi(self,SCALE)
        
        self.__isStop=False
        self.__isPause=False
        self.__expanded=False
        self.__rev=False
        self.__refresh_mode=2
        self.__r=0
        self.__is_play_sapi=False
        
        set_path()
        
        self.__trigger=Signal()
        self.__trigger.s.connect(self.__refresh)
        self.__trigger.p.connect(cell_click_trigger_2)
        
        self.btnSet.clicked.connect(self.__setFile)
        self.btnRefresh.clicked.connect(set_path)
        self.btnPause.clicked.connect(self.__pause)
        self.btnStartStop.clicked.connect(self.__start)
        self.btnMore.clicked.connect(self.__tools)
        self.btnMake.clicked.connect(self.__onefile)
        self.twWord.cellDoubleClicked.connect(cell_click_trigger)
        self.comboName.currentIndexChanged.connect(check)
        self.spinNum.valueChanged.connect(check)
        self.chkRev.clicked.connect(rev)
    
    
    def __setFile(self):
        if self.__refresh_mode==1:
            self.__repeat=self.spinNum.value()
            self.pgBar.setRange(0,self.__length*self.__repeat)
            self.btnSet.setStyleSheet('')
            self.btnSet.setEnabled(False)
        elif self.__refresh_mode==2:
            #get count,filename,words
            self.__file_name=self.__files[self.comboName.currentIndex()]
            self.__words,_=tools.parsing(self.__file_name)
            self.__length=len(self.__words)
            self.twWord.setRowCount(self.__length)
            self.__repeat=self.spinNum.value()
            
            #setting table
            j=0
            for word in self.__words:
                for k in range(2):
                    self.twWord.setItem(j,k,QTableWidgetItem(word[k]))
                j+=1
            
            #resizing columns
            header = self.twWord.horizontalHeader()       
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
            
            #after setting table
            self.pgBar.setRange(0,self.__length*self.__repeat)
            self.pgBar.setFormat(u'%v/%m')
            self.__rev=self.chkRev.isChecked() #reverse set
            self.__stop()
            
            #set sound file's path
            last_lecture=0; self.__path=[]; names=[]
            for word in self.__words:
                if word in self.__origin[last_lecture]:
                    names.append(self.__origin_file[last_lecture].rsplit('.',1)[0] #name of original file
                                 +'\\'
                                 +str(self.__origin[last_lecture].index(word)+1) #number of the word
                                 )
                else:
                    for k in range(self.__origin_len):
                        if word in self.__origin[k]:
                            last_lecture=k
                            names.append(self.__origin_file[k].rsplit('.',1)[0] #name of original file
                                         +'\\'
                                         +str(self.__origin[k].index(word)+1) #number of the word
                                         )
                            break
            
            #make list of path
            for k in range(self.__length):
                if self.__rev: #reverse
                    self.__path.append(SOUND_DIR+names[k]+'_k.mp3')
                    self.__path.append(SOUND_DIR+names[k]+'_e.mp3')
                else: #normal
                    self.__path.append(SOUND_DIR+names[k]+'_e.mp3')
                    self.__path.append(SOUND_DIR+names[k]+'_k.mp3')
                
            self.__refresh_mode=0
            self.btnSet.setStyleSheet('')
            self.btnSet.setEnabled(False)
            
    
    def __refresh(self,num):
        r,n=num
        if r<100:
            a,b=divmod(n,2)
            if self.__rev: #reverse
                self.twWord.setCurrentCell(a,b^1)
            else: #normal
                self.twWord.setCurrentCell(a,b)
            self.pgBar.setValue((r*self.__length*2+n)//2+1)
        elif r==101:
            self.__stop()
        elif r==102:
            self.__stop(False)
        elif r==111:
            self.__stop()
            QMessageBox.information(self, 'Ended', 'Make File Ended')
        elif r==112:
            self.__stop()
            QMessageBox.warning(self, 'Ended', 'Make File Aborted')
            
    
    def __manual_play(self,a):
        self.__isStop=False
        threading.Thread(target=self.__play,args=(self.__path[a*2:(a+1)*2],),kwargs={'col':a,'manual':True},daemon=True).start()
    
    def __start(self,*,n=0):
        self.__isStop=False; self.__isPause=False
        self.btnPause.setEnabled(True)
        if self.__is_play_sapi:
            threading.Thread(target=self.__play_sapi,daemon=True).start()
        else:
            threading.Thread(target=self.__play,args=(self.__path,),kwargs={'col':n,'manual':False},daemon=True).start()
        tools.reconnect(self.btnStartStop.clicked,self.__stop)
        self.btnStartStop.setText(u'\u25a0')
    
    def __onefile(self):
        self.__isStop=False
        threading.Thread(target=self.__worker,args=(self.__path,),daemon=True).start()
        tools.reconnect(self.btnStartStop.clicked,self.__stop)
        self.btnStartStop.setText(u'\u25a0')
    
    def __pause(self):
        if not self.__isStop:
            if self.__isPause:
                self.__isPause=False
                self.btnPause.setStyleSheet('')
            else:
                self.__isPause=True
                mixer.music.stop()
                self.__n=(self.__n//2)*2
                self.btnPause.setStyleSheet('color: red')
    
    def __stop(self,move=True,is_jump=False):
        self.__isStop=True; self.__isPause=False
        self.__r=0
        mixer.music.stop()
        if is_jump:
            self.__trigger.p.emit(is_jump)
        else:
            self.pgBar.reset()
            self.btnPause.setEnabled(False)
            self.btnPause.setStyleSheet('')
            if move:
                self.twWord.setCurrentCell(0,0)
                self.twWord.setCurrentCell(0,3)
            tools.reconnect(self.btnStartStop.clicked,self.__start)
            self.btnStartStop.setText(u'\u25b6')
    
    #play sound process
    def __play(self,*args,**kwargs):
        kwarg_list=kwargs.keys() #list of command
        #if not word
        if not len(args)>0:
            raise ValueError
        #set manual flag
        if 'manual' in kwarg_list:
            assert type(kwargs['manual']) is bool
            manual=kwargs['manual']
        else:
            manual=False
        #set initial column
        if 'col' in kwarg_list:
            assert type(kwargs['col']) is int
            num=kwargs['col']*2
        else:
            num=0
        names=args[0]
        self.__n=num; length=len(names)
        
        if manual:
            for k in range(2):
                self.__trigger.s.emit((0,self.__n))
                mixer.music.load(os.path.abspath(names[k]))
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.2)
                self.__n+=1
            self.__trigger.s.emit((102,0))
        else:
            self.__r=0
            while self.__r<self.__repeat:
                while self.__n<length:
                    self.__trigger.s.emit((self.__r,self.__n))
                    if self.__isStop:
                        break
                    elif self.__isPause:
                        while self.__isPause:
                            time.sleep(1)
                    else:
                        mixer.music.load(os.path.abspath(names[self.__n]))
                        mixer.music.play()
                        while mixer.music.get_busy():
                            time.sleep(0.2)
                        if not self.__isPause:
                            if self.__n%2==1:
                                time.sleep(0.1)
                            self.__n+=1
                self.__n=0; self.__r+=1
            self.__trigger.s.emit((101,0))
    
    def __play_sapi(self):
        r=0
        
        tts_en=qtts()
        tts_ko=qtts()
        tts_en.setLocale(QLocale(QLocale.English))
        tts_ko.setLocale(QLocale(QLocale.Korean))
        
        for word in self.__words:
            print(self.__words[r])
            if self.__isStop:
                self.__trigger.s.emit((101,0))
                break
            elif self.__isPause:
                while self.__isPause:
                    time.sleep(0.5)
            self.__trigger.s.emit((0,r*2))
            tts_en.say(word[0])
            print(tts_en.state())
            time.sleep(3)
            '''
            while tts_en.state()==qtts.State.Speaking:
                time.sleep(1)
            '''
            self.__trigger.s.emit((0,r*2+1))
            tts_ko.say(word[1])
            time.sleep(3)
            '''
            while tts_ko.state()==qtts.State.Speaking:
                time.sleep(1)
            '''
            r+=1
        self.__trigger.s.emit((101,0))
    
    def __worker(self,*args,**kargs):
        names=args[0]
        res=AudioSegment.from_mp3(names[0])
        n=1
        for name in names[1:]:
            self.__trigger.s.emit((0,n))
            if self.__isStop:
                self.__trigger.s.emit((112,0))
                break
            res+=AudioSegment.from_mp3(name)
            if n%2==1:
                res+=AudioSegment.silent(100)
            n+=1
        file_name=os.path.splitext(os.path.basename(self.__file_name))[0]
        res.export(CURRENT_DIR+'..\\onefile\\%s.mp3' %file_name,format='mp3',bitrate='32k')
        if not self.__isStop:
            self.__trigger.s.emit((111,0))
    
    def __tools(self):
        if self.__expanded:
            self.setFixedSize(740*SCALE, 570*SCALE)
            self.btnMore.setText('>>')
            self.__expanded=False
        else:
            self.setFixedSize(870*SCALE, 570*SCALE)
            self.btnMore.setText('<<')
            self.__expanded=True


if __name__=='__main__':
    if '-c' in sys.argv:
        os.system('start /min "DO NOT CLOSE This Command Prompt, Otherwise TTS Player will be KILLED" cmd /c py -3.8 ttsplay.pyw')
    elif '-C' in sys.argv:
        os.system('start /min "DO NOT CLOSE This Command Prompt, Otherwise TTS Player will be KILLED" cmd /k py -3.8 ttsplay.pyw')
    else:
        import ctypes
        myappid = 'hys.ttsplay'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        app=QApplication()
        app.setWindowIcon(QIcon(CURRENT_DIR+'icon.png'))
        
        SCALE=tools.scale(app.desktop)
        
        playui=PlayUI()
        playui.show()
        
        sys.exit(app.exec_())
