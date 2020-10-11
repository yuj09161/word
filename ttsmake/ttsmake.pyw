from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from gtts import gTTS as tts
import os,sys,threading
from pydub import effects,AudioSegment
from tempfile import gettempdir,_get_candidate_names

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))+'\\'
sys.path.append(os.path.abspath(CURRENT_DIR+'..'))

from UI import MakeUI
from commons import tools

SPEED_K=1.3
THREAD_MULTI=2
TMPFILE=CURRENT_DIR+'tmp.mp3'

WORD_DIR,_,_,SOUND_DIR,TTS_DIR,_=tools.get_path(CURRENT_DIR)
THREAD_COUNT=os.cpu_count()*THREAD_MULTI

class Sign(QObject):
    p=Signal(tuple)
    n=Signal(tuple)


class Make(MakeUI,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)
        
        self.__stopped=True
        self.__pte_log=[self.pteLog]
        
        self.__get_file()
        
        self.__signal=Sign()
        self.__signal.p.connect(self.__print)
        self.__signal.n.connect(self.__refresh)
        
        for k in range(THREAD_COUNT):
            self.__pte_log.append(self.makeTab(k+1))
        
        self.btnAddAll.clicked.connect(self.__add_all)
        self.btnAdd.clicked.connect(self.__add_file)
        self.btnDelAll.clicked.connect(self.__del_all)
        self.btnCheck.clicked.connect(self.__check)
        self.btnStart.clicked.connect(self.__process)
        #self.btnManual.clicked.connect(self.__manual)
        self.fileList.itemDoubleClicked.connect(self.__del_file)
        
    #get file lists
    def __get_file(self):
        self.__names=[]; self.__paths={}
        display=[]
        files,paths=tools.get_file(TTS_DIR)
        for file,path in zip(files,paths):
            if len(file)>17:
                display.append(file[:14]+'...')
            else:
                display.append(file)
            self.__paths[file]=path
        self.__names=tuple(files)
        for name in display:
            self.comboFile.addItem(name)
            #self.comboName.addItem(name)
    
    #add all file to fileList
    def __add_all(self):
        self.fileList.addItems(self.__names)
    
    #add file to fileList
    def __add_file(self):
        self.fileList.addItem(self.__names[self.comboFile.currentIndex()])
    
    #del file from fileList
    def __del_file(self):
        self.fileList.takeItem(self.fileList.currentRow())
    
    #del file from fileList
    def __del_all(self):
        self.fileList.clear()
    
    #write to log widget
    def __print(self,response):
        print(response)
        self.__pte_log[response[0]].appendPlainText(' / '.join([str(t) for t in response[1:]])+'\n')
    
    def __refresh(self,num):
        def end():
            self.__stopped=True
            self.btnStart.setText('Make')
            tools.reconnect(self.btnStart.clicked,self.__process)
            self.pgC.reset()
        thread,e=num
        if e==0:
            self.pgC.setValue(self.pgC.value()+1)
        elif e==101:
            self.__ended_thread+=1
            if self.__ended_thread==THREAD_COUNT:
                QMessageBox.information(self, 'Ended', 'Make File Ended')
                end()
        elif e==102:
            self.__ended_thread+=1
            if self.__ended_thread==THREAD_COUNT:
                QMessageBox.warning(self, 'Aborted', 'Make File Aborted')
                end()
        elif e==103:
            QMessageBox.warning(self,'Error','No File Selected',buttons=QMessageBox.Ok)
            end()
        elif e==104:
            self.pgC.setRange(0,1)
            end()
        else:
            raise ValueError
            sys.exit(0)
    
    def __eng(self,text,out_path):
        with open(out_path,'wb') as out_file:
            tts(text,lang='en').write_to_fp(out_file)
    
    def __kor(self,text,out_path):
        with open(out_path,'wb') as out_file:
            tts(text,lang='ko').write_to_fp(out_file)
    
    ##tts maker functions
    def __process(self):
        self.__stopped=False
        self.__ended_thread=0
        tools.reconnect(self.btnStart.clicked,self.__stop)
        self.btnStart.setText('Stop')
        self.pgC.setRange(0,0)
        
        #parse words
        count=self.fileList.count()
        if not count:
            self.__signal.n.emit((0,103))
            return
        
        word_path=[]
        for k in range(count):
            file_path=self.__paths[self.fileList.item(k).text()]
            file_name=os.path.splitext(os.path.basename(file_path))[0]
            words=tools.parsing(file_path)[0]
            for k,word in enumerate(words):
                word_path.append((
                    *word,
                    tools.safe_set_path(SOUND_DIR+file_name)+str(k+1),
                    f'{k+1} word @ file {file_name}'
                ))
        word_count=len(word_path)
        wot=word_count//THREAD_COUNT #wot=Word in One Thread
        
        for wid in self.__pte_log:
            wid.setPlainText('')
        
        self.pgC.setRange(0,word_count)
        self.pgC.setValue(0)
        
        for k in range(THREAD_COUNT-1):
            threading.Thread(target=self.__worker,args=(k+1,word_path[wot*k:wot*(k+1)])).start()
        k+=1
        threading.Thread(target=self.__worker,args=(k+1,word_path[wot*k:])).start()
    
    def __stop(self):
        self.__stopped=True
        self.btnStart.setText('Stopping')
        tools.reconnect(self.btnStart.clicked,self.__process)
    
    def __check(self):
        pass
    
    def __get_out_path(self):
        paths=[]
        if self.fileList.count():
            for name in self.fileList.items():
                paths.append(self.__paths[name])
        else:
            self.__signal.n.emit((0,103))
            return
    
    def __worker(self,thread_number,word_path):
        word_length=len(word_path)
        self.__signal.p.emit((thread_number,f'This thread will process {word_length} words'))
        
        temp_path=gettempdir()+'/'+next(_get_candidate_names())
        
        for k,(eng,kor,out_path,name) in enumerate(word_path):
            if not self.__stopped:
                self.__signal.n.emit((thread_number,0))
                if eng:
                    self.__eng(eng,out_path+'_e.mp3')
                if kor:
                    self.__kor(kor,temp_path)
                    effects.speedup(AudioSegment.from_mp3(temp_path),SPEED_K).export(out_path+'_k.mp3',format="mp3", bitrate='32k')
                self.__signal.p.emit((thread_number,name,f'{k} word of {word_length}'))
            else:
                self.__signal.p.emit((thread_number,'#####Force Stop#####'))
                self.__signal.n.emit((thread_number,102))
                if os.path.isfile(temp_path):
                    os.remove(temp_path)
                return
        if os.path.isfile(temp_path):
            os.remove(temp_path)
        self.__signal.p.emit((thread_number,'end\n'))
        self.__signal.n.emit((thread_number,101))
    ##end tts maker
    
    ##manual tts maker functions
    def __manual(self):
        self.__stopped=False
        mod=self.rbEng.isChecked()
        if mod:
            lang_suffix='e'
        else:
            lang_suffix='k'
        if self.rbHere.isChecked():
            path=CURRENT_DIR+f'out_{lang_suffix}.mp3'
        else:
            path=(
                SOUND_DIR+                                              #sound dir (base)
                os.path.splitext(self.comboName.currentText()+'\\')[0]+ #word list dir
                str(self.spNum.value())+f'_{lang_suffix}.mp3'           #file name
            )
        self.pgC.setRange(0,0)
        threading.Thread(target=self.__manual_worker,kwargs={'mode':mod,'text':self.lnToTts.text(),'out_path':path}).start()
    
    def __manual_worker(self,*,mode,text,out_path):
        self.__signal.p.emit((0,f'Manual Making Start\nOutput File is {out_path}'))
        try:
            if mode:
                self.__signal.p.emit((0,'English...'))
                self.__eng(text,out_path)
            else:
                self.__signal.p.emit((0,'Korean...'))
                self.__kor(text,TMPFILE)
                effects.speedup(AudioSegment.from_mp3(TMPFILE),SPEED_K).export(out_path,format="mp3", bitrate='32k')
                if os.path.isfile(TMPFILE):
                    os.remove(TMPFILE)
        except Exception as e:
            err="".join(traceback.format_exception(*sys.exc_info))
            self.__signal.p.emit((0,f'An Error Occured\nTraceback:\n{err}'))
        else:
            self.__signal.p.emit((0,'Well Done'))
        finally:
            self.__signal.n.emit((0,104))
    
    def closeEvent(self,event):
        if self.__stopped:
            event.accept()
            sys.exit(0)
        else:
            reply=QMessageBox.warning(self,'Confirm','Exit?',QMessageBox.Yes|QMessageBox.No)
            if reply==QMessageBox.Yes:
                event.accept()
                sys.exit(0)
            else:
                event.ignore()
    ##end manual tts maker


if __name__=='__main__':
    if '-q' in sys.argv:
        import ctypes
        myappid='hys.ttsmake'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        app=QApplication()
        app.setWindowIcon(QIcon(CURRENT_DIR+'icon.png'))
        
        SCALE=tools.scale(app.desktop)
        
        make=Make()
        make.show()
        
        sys.exit(app.exec_())
    elif '-C' in sys.argv:
        os.system('start /min "DO NOT CLOSE This Command Prompt, Otherwise TTS Maker will be KILLED" cmd /k py ttsmake.pyw -q')
    else:
        os.system('start /min "DO NOT CLOSE This Command Prompt, Otherwise TTS Maker will be KILLED" cmd /c py ttsmake.pyw -q')
