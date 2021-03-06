import os,sys

def safe_set_path(name):
    if not os.path.isdir(name):
        os.mkdir(name)
    return name+'\\'

def get_path(current_dir):
    safe_set_path(current_dir+'..\\resources')
    WORD_DIR   = safe_set_path(current_dir+'..\\resources\\word')
    LOG_DIR    = safe_set_path(current_dir+'..\\log')
    RETEST_DIR = safe_set_path(current_dir+'..\\retest')
    SOUND_DIR  = safe_set_path(current_dir+'..\\resources\\audio')
    TTS_DIR    = safe_set_path(current_dir+'..\\resources\\ttsWords')
    return (WORD_DIR,LOG_DIR,RETEST_DIR,SOUND_DIR,TTS_DIR)

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