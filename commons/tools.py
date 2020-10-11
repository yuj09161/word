from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow

import os,sys,ctypes

GetSystemMetrics=ctypes.windll.user32.GetSystemMetrics

RESOL=(GetSystemMetrics(0),GetSystemMetrics(1))

class Get_Scale(QMainWindow):
    def __init__(self,app_desktop,wid): 
        if app_desktop and wid:
            tmp=app_desktop().screenGeometry(wid)
            self.__size=(tmp.width(),tmp.height())
        elif app_desktop:
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setStyleSheet('background:transparent')
            
            self.setGeometry(0,0,1,1)
            self.show()
            tmp=app_desktop().screenGeometry(self)
            self.__size=(tmp.width(),tmp.height())
            
            self.destroy()
        else:
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setStyleSheet('background:transparent')
            
            self.showFullScreen()
            self.__size=(self.size().width(),self.size().height())
            
            self.destroy()
    
    def get_resol(self):
        return self.__size


def safe_set_path(name):
    if not os.path.isdir(name):
        os.mkdir(name)
    return name+'\\'


def get_path(current_dir):
    safe_set_path(current_dir+'..\\resources')
    WORD_DIR    = safe_set_path(current_dir+'..\\resources\\word')
    LOG_DIR     = safe_set_path(current_dir+'..\\log')
    RETEST_DIR  = safe_set_path(current_dir+'..\\retest')
    SOUND_DIR   = safe_set_path(current_dir+'..\\resources\\audio')
    TTS_DIR     = safe_set_path(current_dir+'..\\resources\\ttsWords')
    ONEFILE_DIR = safe_set_path(current_dir+'..\\onefile')
    return (WORD_DIR,LOG_DIR,RETEST_DIR,SOUND_DIR,TTS_DIR,ONEFILE_DIR)


def scale(app=None,wid=None,base=1.25):
    scale_win=Get_Scale(app,wid)
    size=scale_win.get_resol()
    return size[0]/RESOL[0]/base if -0.1<size[0]/RESOL[0]-size[1]/RESOL[1]<0.1 else 1

#reconnect pyqt5/pyside2 signal
#obj: must be a signal, not QObject
def reconnect(obj,newCmd):
    try:
        obj.disconnect()
    except:
        pass
    obj.connect(newCmd)


def get_file(dir):
    names=[]; full_paths=[]
    files=os.listdir(dir)
    for file in files:
        full_path=dir+'\\'+file
        if os.path.isfile(full_path)&file.endswith('.csv'):
            names.append(file)
            full_paths.append(full_path)
    return names,full_paths


def parsing(file_path):
    #file read
    with open(file_path,'r',encoding='utf-8') as file:
        lines=file.readlines()
    #split by [tab]
    res=[]; mask=[]
    for line in lines:
        tmp=line.replace('\r','').replace('\n','').split('\t')
        if len(tmp)>1:
            res.append(tuple(tmp[:2]))
            mask.append(tuple(tmp[2:4]))
    return tuple(res),tuple(mask)


def duplicate_remove(hashable,iter_seq=None,*,tuple_out=True):
    res=list(set(hashable)) #duplicate remove
    if iter_seq: #sort by iter_seq
        res.sort(key=lambda x: iter_seq.index(x))
    if tuple_out: #if out as tuple
        return tuple(res)
    else: #if out as list
        return res

if __name__=='__main__':
    print(get_path(os.path.dirname(os.path.abspath(__name__))+'\\'))