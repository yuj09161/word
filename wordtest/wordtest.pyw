# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import os,sys,random,datetime,re

from UI import SelectUI,SettingUI,TestUI,SelectTestUI
from commons import tools

SHORT_ANSWER=0; CHOICE=1
testwin=None; fileName=[]; words=[]; seq=[]; masks={}; settings={}
check_word   = ('do','sb','sth')
ckeck_symbol = ('(','[','~','...','.')
setting_closed=True

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))+'\\'
WORD_DIR,LOG_DIR,RETEST_DIR,_,_=tools.get_path(CURRENT_DIR)

SHOW_TIME=1; SKIP_TIME=2; TMR_INTERVAL=25; TIME_YES=1000; TIME_NO=2000

class selectWin(QMainWindow,SelectUI):
    def __init__(self):
        def setting():
            if setting_closed:
                self.__setting.show()
            else:
                QMessageBox.information(self,'Information','Setting Screen is already opened.')
        
        super().__init__()
        self.setupUi(self,SCALE)
        self.__setting=settingWin(self)
        self.__get_file()
        
        #Connect Callback
        self.btnTest.clicked.connect(self.__add_word)
        self.btnRe.clicked.connect(self.__add_re)
        self.btnSetting.clicked.connect(setting)
        self.btnStart.clicked.connect(self.next)
        self.fileList.itemDoubleClicked.connect(self.__del_file)
    
    #get file lists
    def __get_file(self):
        self.__names={}; self.__paths={}
        mode=True
        
        for dir in (WORD_DIR,RETEST_DIR):
            display=[]
            files,paths=tools.get_file(dir)
            k=0
            for file in files:
                if len(file)>17:
                    display.append(file[:14]+'...')
                else: display.append(file)
                self.__paths[file]=paths[k]
                k+=1
            
            if mode:
                self.__names['word']=tuple(files)
                for name in display:
                    self.comboTest.addItem(name)
            else:
                self.__names['re']=tuple(files)
                for name in display:
                    self.comboRe.addItem(name)
            mode=False
    
    #add word-list to fileList
    def __add_word(self):
        self.fileList.addItem(self.__names['word'][self.comboTest.currentIndex()])
    
    #add retest-file to fileList
    def __add_re(self):
        self.fileList.addItem(self.__names['re'][self.comboRe.currentIndex()])
    
    def __del_file(self):
        self.fileList.takeItem(self.fileList.currentRow())
    
    #to test ui
    def next(self):
        global testwin,fileName,words,seq,masks
        mask=[]; tmp_mod=[]
        is_split=None; start_num=0; end_num=0
        
        #parsing split
        def split(dict):
            nonlocal start_num,end_num
            is_split=dict['split']
            if is_split:
                size=tmp['size']
                no=tmp['no']
                start=tmp['start']
                end=tmp['end']
        
        if setting_closed:
            n=self.fileList.count()
            self.__setting.get()
            
            mode=settings['mode']
            if n:
                for k in range(n):
                    name=self.fileList.item(k).text()
                    fileName.append(name)
                    tmp1,tmp2=tools.parsing(self.__paths[name])
                    words+=tmp1
                    if mode==SHORT_ANSWER:
                        if settings['pre']:
                            mask+=tmp2
                        else:
                            mask+=([[]]*len(tmp2))
                    else:
                        mask+=([[]]*len(tmp2))
                for k in range(len(words)):
                    masks[words[k][0]]=tuple(mask[k])
                
                #get exam mode
                if settings['etk']:
                    tmp_mod.append(0)
                if settings['kte']:
                    tmp_mod.append(1)
                #make random sequence
                for j in tmp_mod:
                    for k in range(len(words)):
                        seq.append(str(k)+str(j))
                for k in range(settings['shuffle']):
                    random.shuffle(seq)
                
                self.close()
                if mode==SHORT_ANSWER:
                    testwin=testWin(words,mask,seq,settings['ans'])
                else:
                    testwin=selectTestWin(words,seq,True,settings['timeout'],settings['time_show'],settings['time_sel'])
                testwin.show()
            else:
                QMessageBox.warning(self,'Error','No File Selected',buttons=QMessageBox.Ok)
        else:
            QMessageBox.warning(self,'Error','Setting screen is not closed',buttons=QMessageBox.Ok)


class settingWin(QDialog, SettingUI):
    def __init__(self,wid=None):
        super().__init__(parent=wid)
        self.setupUi(self,SCALE)
        
        self.__exam_type=SHORT_ANSWER
        self.__short_answer()
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)
        
        self.spinShow.setValue(SHOW_TIME)
        self.spinSel.setValue(SKIP_TIME)
        
        self.rbTypeW.clicked.connect(self.__short_answer)
        self.rbTypeC.clicked.connect(self.__choice)
        self.chkTimeout.stateChanged.connect(self.__timeout)
        #self.chkSplit.stateChanged.connect(self.__split)
        self.chkSplit.setEnabled(False)
        
        self.btnCancel.setEnabled(False)
        #self.btnCancel.clicked.connect(self.__cancel)
        self.btnApply.clicked.connect(self.__apply)
        self.btnStart.clicked.connect(self.__start)
    
    def __short_answer(self):
        self.__exam_type=SHORT_ANSWER
        self.timeout.hide()
        self.showPrefix.show()
        self.showAnswer.show()
    
    def __choice(self):
        self.__exam_type=CHOICE
        self.showPrefix.hide()
        self.showAnswer.hide()
        self.timeout.show()
    
    def __timeout(self):
        if self.chkTimeout.isChecked():
            self.spinShow.setEnabled(True)
            self.spinSel.setEnabled(True)
        else:
            self.spinShow.setEnabled(False)
            self.spinSel.setEnabled(False)
    
    def __split(self):
        if self.chkSplit.isChecked():
            self.setFixedSize(420*SCALE, 410*SCALE)
            self.split.setGeometry(10, 220, 401, 141)
            self.btnCancel.setGeometry(10, 370, 93, 28)
            self.btnApply.setGeometry(220, 370, 93, 28)
            self.btnStart.setGeometry(320, 370, 93, 28)
            self.splitWrap.show()
            self.chkSplit.setText('Enabled')
        else:
            self.setFixedSize(420*SCALE, 331*SCALE)
            self.split.setGeometry(10, 220, 401, 61)
            self.btnCancel.setGeometry(10, 290, 93, 28)
            self.btnApply.setGeometry(220, 290, 93, 28)
            self.btnStart.setGeometry(320, 290, 93, 28)
            self.splitWrap.hide()
            self.chkSplit.setText('Disabled')
    
    def get(self):
        global settings
        
        #common
        settings['etk']=self.chkEtK.isChecked()
        settings['kte']=self.chkKtE.isChecked()
        settings['shuffle']=self.spinShuffle.value()
        
        if self.__exam_type==SHORT_ANSWER:
            settings['mode']=SHORT_ANSWER
            settings['pre']=self.rbPreY.isChecked()
            settings['ans']=self.rbAnsY.isChecked()
        else: #exam type:choice
            settings['mode']=CHOICE
            settings['timeout']=self.chkTimeout.isChecked()
            settings['time_show']=self.spinShow.value()
            settings['time_sel']=self.spinSel.value()
        
        if self.chkSplit.isChecked():
            tmp={}
            tmp['size']  = self.spinSize.value()
            tmp['no']    = self.spinNo.value()
            tmp['start'] = self.spinStart.value()
            tmp['end']   = self.spinEnd.value()
            settings['split']=tmp
        else:
            settings['split']=None
        
        print(settings)
        return settings
    
    def __cancel(self):
        #todo: UnDo GUI
        self.close()
    
    def __apply(self):
        self.get()
        self.close()
    
    def __start(self):
        global selui
        self.get()
        self.close()
        selui.next()
    
    def closeEvent(self,event):
        global setting_closed
        setting_closed=True
        event.accept()
    
    def setVisible(self,var):
        global setting_closed
        if var:
            setting_closed=False
            super().setVisible(True)
        else:
            setting_closed=True
            super().setVisible(False)
        

class testWin(QMainWindow, TestUI):
    def __init__(self,words,mask,seq,showAns):
        self.__words=words; self.__mask=mask
        self.__isShowAns=showAns; self.__seq=seq
        self.__ln=(len(self.__seq),len(self.__words))
        
        super().__init__()
        self.setupUi(self,SCALE)
        
        self.__ans,self.__rb=[],[]
        self.__wrong={'etk':[],'kte':[]}
        
        self.__gradeChange()
        for k in range(0,self.__ln[0]):
            self.__addQus(self.__seq[k])
            self.__rb.append(None)
        
        self.btnEnd.clicked.connect(self.__check)
    
    def __gradeChange(self,t=None,etk=None,kte=None):
        if t==None:
            t='##/'
        else:
            t=str(t)+'/'
        if etk==None:
            etk='##/'
        else: etk=str(etk)+'/'
        if kte==None:
            kte='##/'
        else: kte=str(kte)+'/'
        
        self.resT.setText(t+str(self.__ln[1]))
        self.resEtK.setText(etk+str(self.__ln[1]))
        self.resKtE.setText(kte+str(self.__ln[1]))
    
    def __addQus(self,seqStr):
        #parsing seqStr
        num,mod=int(seqStr[:-1]),int(seqStr[-1])
        
        #generate widgets
        seq=QLabel(self.boxQus)
        qus=QLabel(self.boxQus)
        ans=QLineEdit(self.boxQus)
        sp2=QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        seq.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        qus.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        
        self.__ans.append(ans)
        
        #main layout
        n=self.gridMain.rowCount()
        self.gridMain.addWidget(seq, n, 0, 1, 1)
        self.gridMain.addWidget(qus, n, 1, 1, 1)
        self.gridMain.addWidget(ans, n, 2, 1, 1)
        self.gridMain.addItem(sp2, n, 3, 1, 1)
        
        
        #set txtAns & pre-enter
        txtAns=self.__words[num][mod]
        inv=mod^1 #inverse mod(0 or 1)
        txtPre=self.__mask[num][inv:inv+1] #IndexError-safe
        
        #question & pre-enter set
        seq.setText(str(n))
        if len(txtAns)>18:
            qus.setText(txtAns[:15]+'...: ')
            qus.setToolTip(txtAns)
        else:
            qus.setText(txtAns+': ')
        if txtPre:
            ans.setText(txtPre[0])
    
    def __parsingWord(self,n):
        return self.__words[int(self.__seq[n][:-1])]
    
    def __ansShow(self,n):
        eng,kor=self.__parsingWord(n)
        
        if self.__seq[n][-1]=='0':
            txtCor=kor
        else: txtCor=eng
        
        ansCor=QLabel(self.boxQus)
        ansCor.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        sp3=QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        self.gridMain.addWidget(ansCor, n+1, 4, 1, 1)
        self.gridMain.addItem(sp3, n+1, 5, 1, 1)
        
        if len(txtCor)>20:
            ansCor.setText(txtCor[:17]+'...')
            ansCor.setToolTip(txtCor)
        else: ansCor.setText(txtCor)
    
    #if answer right
    def __yes(self,n):
        #Show Result
        res=QLabel(self.boxQus)
        res.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.gridMain.addWidget(res,n+1,6,1,1)
        res.setText('O')
    
    #if answer wrong
    def __no(self,n,ans=None):
        eng,kor=self.__parsingWord(n)
        if ans==None:
            ans=self.__ans[n].text()
        if self.__seq[n][-1]=='0':
            if ans: 
                self.__wrong['etk'].append((eng,kor,ans))
            else: 
                self.__wrong['etk'].append((eng,kor))
        else:
            if ans:
                self.__wrong['kte'].append((eng,kor,ans))
            else:
                self.__wrong['kte'].append((eng,kor))
        
        #Show Result
        self.__ans[n].setStyleSheet('color: red')
        res=QLabel(self.boxQus)
        res.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        res.setStyleSheet('color: red')
        self.gridMain.addWidget(res,n+1,6,1,1)
        res.setText('X')
    
    #check answer
    def __check(self):
        '''
        mod=0 -> eng to kor
        mod=1 -> kor to eng
        '''
        end=True
        for k in range(0,self.__ln[0]):
            eng,kor=self.__parsingWord(k)
            ans=self.__ans[k].text()
            if self.__seq[k][-1]=='0':
                if ans=='':
                    self.__no(k,ans)
                elif ans in kor.split(', '):
                    self.__yes(k)
                elif ans in [re.sub('\(.+?\) ','',t) for t in kor.split(', ')]:
                    self.__yes(k)
                else:
                    end=False
                    self.__confirm(k)
            else:
                if ans=='':
                    self.__no(k,ans)
                elif ans==eng:
                    self.__yes(k)
                elif ans.lower()==eng.lower():
                    end=False
                    self.__confirm(k)
                else:
                    flag=True
                    for w in check_word:
                        if eng.endswith(w) or w+' ' in eng:
                            flag=False
                            break
                    for s in ckeck_symbol:
                        if s in eng:
                            flag=False
                            break
                    if flag:
                        self.__no(k,ans)
                    else:
                        end=False
                        self.__confirm(k)
                    '''
                    if (ans.lower()==eng.lower()) or (eng.endswith('do')) or ('do ' in eng) or ('~' in eng) or ('[' in eng):
                        end=False
                        self.__confirm(k)
                    else: self.__no(k,ans)
                    '''
            if self.__isShowAns:
                self.__ansShow(k)
        if end:
            ln=log(self.__wrong,'basic')
            self.__gradeChange(ln[2],ln[0],ln[1])
            self.btnEnd.setText('end')
            self.btnEnd.clicked.disconnect()
            self.btnEnd.clicked.connect(self.__end)
        else:
            self.btnEnd.setText('confirm')
            self.btnEnd.clicked.disconnect()
            self.btnEnd.clicked.connect(self.__end2)
        
        #scroll to top
        bar=self.scQus.verticalScrollBar()
        bar.setValue(bar.minimum())
    
    def __confirm(self,n):
        #show correct answer
        if not self.__isShowAns:
            self.__ansShow(n)
        ans=self.__ans[n]
        ansTxt=ans.text()
        if len(ansTxt)>7:
            ans.setToolTip(ansTxt)
        
        #generate OX button
        OXWidget = QWidget(self.boxQus)
        gridOX = QGridLayout(OXWidget)
        rbO = QRadioButton('O',OXWidget)
        spox = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        rbX = QRadioButton('X',OXWidget)
    
        #ox btn
        gridOX.addWidget(rbO, 0, 0, 1, 1)
        gridOX.addItem(spox, 0, 1, 1, 1)
        gridOX.addWidget(rbX, 0, 2, 1, 1)
        self.__rb[n]=([rbO,rbX])

        self.gridMain.addWidget(OXWidget, n+1, 6, 1, 1)

    def __end2(self):
        ok=True
        for chk in self.__rb:
            if chk:
                if not (chk[1].isChecked() or chk[0].isChecked()):
                    QMessageBox.warning(self,'Error','\n    Check All Combo(s)    \n',buttons=QMessageBox.Ok)
                    ok=False
                    break
        if ok:
            k=0
            for chk in self.__rb:
                if chk:
                    if chk[1].isChecked():
                        self.__no(k)
                    elif chk[0].isChecked():
                        self.__yes(k)
                k+=1
            ln=log(self.__wrong,'basic')
            self.__gradeChange(ln[2],ln[0],ln[1])
            self.btnEnd.setText('end')
            self.btnEnd.clicked.disconnect()
            self.btnEnd.clicked.connect(self.__end)
    
    def __end(self):
        self.close()
        sys.exit(0)

class selectTestWin(QMainWindow, SelectTestUI):
    def __init__(self,words,seq,show_ans,is_timeout,time_show=1,time_skip=3):
        super().__init__()
        self.setupUi(self,SCALE)
        
        self.__words       = words
        self.__seq         = seq
        self.__ln          = (len(self.__seq),len(self.__words))
        self.__time_show   = time_show*1000
        self.__max_time    = time_show*1000+time_skip*1000
        
        self.__is_show_ans = show_ans
        self.__is_timeout  = is_timeout
        
        self.__wrong       = {'etk':[],'kte':[]}
        self.__num         = 0
        
        self.pgTime.setRange(0,self.__max_time)
        self.__update()
        
    def __update(self):
        #update time
        def update_tmr():
            current_time=self.pgTime.value()
            next_time=current_time+TMR_INTERVAL
            if self.__is_timeout:
                if current_time<self.__max_time:
                    self.pgTime.setValue(next_time)
                    if next_time==self.__time_show:
                        show()
                else:
                    no()
            else:
                if current_time<self.__time_show:
                    self.pgTime.setValue(next_time)
                    if next_time==self.__time_show:
                        show()
        
        #show answers
        def show():
            def connect(btn,text):
                btn.clicked.connect(lambda: no(text))
            nonlocal correct_num
            display=[correct]
            fakes=random.sample(self.__words,4)
            for fake in fakes:
                if fake!=word:
                    display.append(fake[inv])
                    if len(display)>3:
                        break
            random.shuffle(display)
            self.__set_text(ans1=display[0],
                            ans2=display[1],
                            ans3=display[2],
                            ans4=display[3])
            k=0
            for btn in self.btnAns:
                if display[k]==correct:
                    btn.clicked.connect(yes)
                    correct_num=k
                else:
                    connect(btn,btn.text())
                k+=1
        
        #stop timer and disable buttons
        def stop():
            nonlocal tmr
            tmr.stop()
            del(tmr)
            for btn in self.btnAns:
                btn.setEnabled(False)
        
        #yes or no
        def yes():
            stop()
            self.lbQus.setStyleSheet('color: green')
            if self.__is_show_ans:
                show_ans()
            next(TIME_YES)
        
        def no(ans=None):
            stop()
            self.lbQus.setStyleSheet('color: red')
            self.__no(self.__num,ans)
            if self.__is_show_ans:
                show_ans()
            next(TIME_NO)
        
        def show_ans():
            k=0
            for btn in self.btnAns:
                if k==correct_num:
                    btn.setStyleSheet('color: green')
                else:
                    btn.setStyleSheet('color: red')
                k+=1
        
        def next(time):
            def inner():
                if self.__num<self.__ln[0]-1:
                    self.__num+=1
                    self.__del_text()
                    for btn in self.btnAns:
                        btn.clicked.disconnect()
                        btn.setEnabled(True)
                    self.__update()
                else:
                    self.__end()
            QTimer.singleShot(time,inner)
        
        '''
        mod=0 -> eng to kor
        mod=1 -> kor to eng
        '''
        correct_num=None
        tmp=self.__seq[self.__num]
        num,mod=int(tmp[:-1]),int(tmp[-1])
        inv=mod^1
        word=self.__words[num]
        question,correct=word[mod],word[inv]
        self.__set_text(qus=question)
        self.lbPg.setText(str(self.__num+1)+' / '+str(self.__ln[0]))
        self.pgTime.setValue(0)
        
        tmr=QTimer(self)
        tmr.timeout.connect(update_tmr)
        tmr.start(TMR_INTERVAL)
    
    def __set_text(self,*args,**kwargs):
        keys=kwargs.keys()
        
        if 'qus' in keys:
            self.lbQus.setText(kwargs['qus'])
        if 'ans1' in keys:
            self.btnAns1.setText(kwargs['ans1'])
        if 'ans2' in keys:
            self.btnAns2.setText(kwargs['ans2'])
        if 'ans3' in keys:
            self.btnAns3.setText(kwargs['ans3'])
        if 'ans4' in keys:
            self.btnAns4.setText(kwargs['ans4'])
    
    def __del_text(self):
        self.lbQus.setText('')
        self.lbQus.setStyleSheet('color: black')
        for btn in self.btnAns:
            btn.setText('')
            btn.setStyleSheet('color: black')
    
    def __parsingWord(self,n):
        return self.__words[int(self.__seq[n][:-1])]
    
    #if answer wrong
    def __no(self,n,ans=''):
        eng,kor=self.__parsingWord(n)
        if self.__seq[n][-1]=='0':
            if ans: 
                self.__wrong['etk'].append((eng,kor,ans))
            else: 
                self.__wrong['etk'].append((eng,kor))
        else:
            if ans:
                self.__wrong['kte'].append((eng,kor,ans))
            else:
                self.__wrong['kte'].append((eng,kor))
    
    def __end(self):
        length=log(self.__wrong,'select')
        text='''
         All Type Wrongs: {2}/{3}         
         English to Korean: {0}/{3}         
         Korean to English: {1}/{3}         
        '''.format(*length)
        QMessageBox.information(self,'Wrongs',text)
        self.close()
        sys.exit(0)
    

def log(wrong,type): #log file generator
    #variables
    etkOrign,kteOrign=wrong['etk'],wrong['kte']
    time=datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
    name=fileName[0].rsplit('.',1)[0]
    #duplicate remove
    error=set()
    for w in etkOrign: error.add(tuple(w[:2]))
    for w in kteOrign: error.add(tuple(w[:2]))
    error=sorted(error,key=lambda x: words.index(tuple(x)))
    n=(len(etkOrign),len(kteOrign),len(error),len(words))
    
    #set prifix & file name parsing
    if ']_' in name:
        prefix='[%s]_' %name.split(']_')[-1]+time
    else:
        prefix='[%s]_' %name+time
    
    if error: #if wrong answer(s) exist
        #file generate prepare
        etk=sorted(etkOrign,key=lambda x: words.index(x[:2]))
        kte=sorted(kteOrign,key=lambda x: words.index(x[:2]))
        #log file generation
        with open(LOG_DIR+prefix+'.txt','w',encoding='utf-8') as file:
            #log exam type
            file.write('--------Exam Type: %s--------\n' %type)
            #log exam file(s)
            file.write('-----------Exam File(s)-----------\n')
            for name in fileName:
                file.write(name+'\n')
            #log all type wrong(s)
            file.write('\n----------All type Wrongs----------\nTotal Wrong: %s/%s\n' %(n[2],n[3]))
            for w in error:
                file.write(' / '.join(w)+'\n')
            #log wrong(s) english to korean
            file.write('\n----------English to Korean----------\nwrong: %s/%s\n' %(n[0],n[3]))
            for w in etk:
                file.write(' / '.join(w)+'\n')
            #log wrong(s) korean to english
            file.write('\n----------Korean to English----------\nwrong: %s/%s\n' %(n[1],n[3]))
            for w in kte:
                w=list(w)
                w[0],w[1]=w[1],w[0]
                file.write(' / '.join(w)+'\n')
        #re-test file generator
        with open(RETEST_DIR+prefix+'.csv','w',encoding='utf-8') as file:
            for w in error:
                mask=masks[w[0]]
                file.write('\t'.join(w+mask)+'\n')
    else:
        with open(LOG_DIR+prefix+'.txt','w',encoding='utf-8') as file:
            #log exam type
            file.write('--------Exam Type: %s--------\n' %type)
            #log exam file(s)
            file.write('----------Exam File(s)----------\n')
            for name in fileName:
                file.write(name+'\n')
            file.write('\nNo Error')
    return n


if __name__=='__main__':
    if '-c' in sys.argv:
        os.system('start /min "DO NOT CLOSE This Command Prompt, Otherwise wordtest will be KILLED" cmd /c py wordtest.pyw')
    elif '-C' in sys.argv:
        os.system('start /min "DO NOT CLOSE This Command Prompt, Otherwise wordtest will be KILLED" cmd /k py wordtest.pyw')
    else:
        import ctypes
        myappid = 'hys.wordtest2'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(CURRENT_DIR+'icon.png'))
        SCALE=tools.scale()
        selui=selectWin()
        selui.show()
        app.exec_()