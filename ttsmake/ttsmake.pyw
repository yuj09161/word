from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from gtts import gTTS as tts
import os,sys,threading
from pydub import effects,AudioSegment

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))+'\\'
sys.path.append(os.path.abspath(CURRENT_DIR+'..'))

from UI import MakeUI
from commons import tools

SPEED_K=1.3; ADD_ALL=False; TMPFILE=CURRENT_DIR+'tmp.mp3'

WORD_DIR,_,_,SOUND_DIR,TTS_DIR=tools.get_path(CURRENT_DIR)

class Sign(QObject):
    p=Signal(tuple)
    n=Signal(tuple)


class Make(MakeUI,QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self,SCALE)
        self.__stopped=True
        self.__get_file()
        
        self.__signal=Sign()
        self.__signal.p.connect(self.__print)
        self.__signal.n.connect(self.__refresh)
        
        self.btnFile.clicked.connect(self.__add_file)
        self.btnCheck.clicked.connect(self.__check)
        self.btnStart.clicked.connect(self.__process)
        self.btnManual.clicked.connect(self.__manual)
        self.fileList.itemDoubleClicked.connect(self.__del_file)
        
    #get file lists
    def __get_file(self):
        self.__names=[]; self.__paths={}
        display=[]
        files,paths=tools.get_file(TTS_DIR)
        k=0
        for file in files:
            if len(file)>17:
                display.append(file[:14]+'...')
            else:
                display.append(file)
            self.__paths[file]=paths[k]
            k+=1
        self.__names=tuple(files)
        for name in display:
            self.comboFile.addItem(name)
            self.comboName.addItem(name)
            if ADD_ALL:
                self.fileList.addItem(name)
    
    #add file to fileList
    def __add_file(self):
        self.fileList.addItem(self.__names[self.comboFile.currentIndex()])
    
    #del file from fileList
    def __del_file(self):
        self.fileList.takeItem(self.fileList.currentRow())
    
    #write to log widget
    def __print(self,text):
        self.pteLog.appendPlainText(' '.join([str(t) for t in text])+'\n')
    
    def __refresh(self,num):
        def end():
            self.__stopped=True
            self.btnStart.setText('Make')
            tools.reconnect(self.btnStart.clicked,self.__process)
            self.pgE.reset()
            self.pgC.reset()
        e,c=num
        if e<100:
            self.pgE.setValue(e)
            self.pgC.setValue(c)
        elif e==101:
            QMessageBox.information(self, 'Ended', 'Make File Ended')
            end()
        elif e==102:
            QMessageBox.warning(self, 'Aborted', 'Make File Aborted')
            end()
        elif e==103:
            QMessageBox.warning(self,'Error','No File Selected',buttons=QMessageBox.Ok)
            end()
        elif e==104:
            self.pgC.setRange(0,1)
            end()
        elif e==201:
            self.pgC.setRange(0,c)
    
    def __process(self):
        self.__stopped=False
        tools.reconnect(self.btnStart.clicked,self.__stop)
        self.btnStart.setText('Stop')
        self.pgE.setRange(0,self.fileList.count())
        threading.Thread(target=self.__worker,args=(True,)).start()
    
    def __stop(self):
        self.__stopped=True
        self.btnStart.setText('Stopping')
        tools.reconnect(self.btnStart.clicked,self.__process)
    
    def __check(self):
        threading.Thread(target=self.__worker,args=(False,)).start()
    
    def __manual(self):
        self.__stopped=False
        mod=self.rbEng.isChecked()
        if mod:
            mode='e'
        else:
            mode='k'
        if self.rbHere.isChecked():
            path=CURRENT_DIR+'out_%s.mp3' %mode
        else:
            path=(SOUND_DIR+
                os.path.splitext(self.comboName.currentText()+'\\')[0]+
                str(self.spNum.value())+
                '_%s.mp3' %mode)
        self.pgC.setRange(0,0)
        threading.Thread(target=self.__worker_manual,kwargs={'mode':mod,'text':self.lnToTts.text(),'out_path':path}).start()
    
    def __eng(self,text,out_path):
        #return tts(text,lang='en')
        with open(out_path,'wb') as out_file:
            #self.__eng(word[0]).write_to_fp(out_file)
            tts(text,lang='en').write_to_fp(out_path)
    
    def __kor(self,text,out_path):
        #return tts(text,lang='ko')
        with open(out_path,'wb') as out_file:
            #self.__kor(word[0]).write_to_fp(out_file)
            tts(text,lang='ko').write_to_fp(out_path)
    
    def __worker(self,do_work):
        #clear log
        self.pteLog.setPlainText('')
        
        #prepare
        paths=[]
        n=self.fileList.count()
        if n:
            for k in range(n):
                name=self.fileList.item(k).text()
                paths.append(self.__paths[name])
        else:
            self.__signal.n.emit((103,0))
            return
        #end prepare
        
        #work
        i=1
        for path in paths:
            #get word list
            self.__signal.p.emit((path,))
            words,_=tools.parsing(path)
            length=int(len(words))
            self.__signal.p.emit((words,length))
            if do_work:
                #set progress bar
                self.__signal.n.emit((201,length))
                #make sound file
                tools.safe_set_path(SOUND_DIR)
                k=1
                for word in words:
                    if not self.__stopped:
                        self.__signal.n.emit((i,k))
                        name=os.path.splitext(os.path.basename(path))[0]
                        out_l=tools.safe_set_path(SOUND_DIR+name)+str(k)
                        if word[0]:
                            self.__eng(word[0],out_l+'_e.mp3')
                            '''
                            with open(out_l+'_e.mp3','wb') as out_file:
                                self.__eng(word[0]).write_to_fp(out_file)
                            '''
                        if word[1]:
                            self.__kor(word[1],TMPFILE)
                            '''
                            with open(TMPFILE,'wb') as out_file:
                                self.__kor(word[1]).write_to_fp(out_file)
                            '''
                            #app.processEvents()
                            effects.speedup(AudioSegment.from_mp3(TMPFILE),SPEED_K).export(out_l+'_k.mp3',format="mp3", bitrate='32k')
                        self.__signal.p.emit((name,': ',k,'/',length))
                        #app.processEvents()
                        k+=1
                    else:
                        self.__signal.p.emit(('#####Force Stop#####',))
                        self.__signal.n.emit((102,0))
                        if os.path.isfile(TMPFILE):
                            os.remove(TMPFILE)
                        return
                if os.path.isfile(TMPFILE):
                    os.remove(TMPFILE)
                self.__signal.p.emit(('end\n',))
                i+=1
        #end work
        
        if not do_work:    
            self.__signal.p.emit(('All names:',[os.path.basename(p) for p in paths]))
            return
        else:
            self.__signal.p.emit(('\nEnded All',))
            self.__signal.n.emit((101,0))
            return
    
    def __worker_manual(self,*,mode,text,out_path):
        self.__signal.p.emit(('Manual Making Start\nOutput File is %s' %out_path,))
        try:
            if mode:
                self.__signal.p.emit(('English...',))
                self.__eng(word[0],out_path)
                '''
                with open(out_path,'wb') as file:
                    self.__eng(text).write_to_fp(file)
                '''
            else:
                self.__signal.p.emit(('Korean...',))
                self.__kor(word[1],TMPFILE)
                '''
                with open(TMPFILE,'wb') as file:
                    self.__kor(text).write_to_fp(file)
                '''
                effects.speedup(AudioSegment.from_mp3(TMPFILE),SPEED_K).export(out_path,format="mp3", bitrate='32k')
                if os.path.isfile(TMPFILE):
                    os.remove(TMPFILE)
        except Exception as e:
            self.__signal.p.emit(('An Error Occured\nTraceback:\n%s' %e,))
        else:
            self.__signal.p.emit(('Well Done',))
        finally:
            self.__signal.n.emit((104,0))
    
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


if __name__=='__main__':
    if '-q' in sys.argv:
        import ctypes
        myappid='hys.ttsmake'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        app=QApplication()
        app.setWindowIcon(QIcon(CURRENT_DIR+'icon.png'))
        SCALE=tools.scale()
        m=Make()
        m.show()
        sys.exit(app.exec_())
    elif '-C' in sys.argv:
        os.system('start /min "DO NOT CLOSE This Command Prompt, Otherwise TTS Maker will be KILLED" cmd /k py ttsmake.pyw -q')
    else:
        os.system('start /min "DO NOT CLOSE This Command Prompt, Otherwise TTS Maker will be KILLED" cmd /c py ttsmake.pyw -q')