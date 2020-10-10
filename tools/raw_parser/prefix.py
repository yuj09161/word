import os

ROOT_DIR    = '.\\'
KOREAN_PRE  = 0
ENGLISH_PRE = 1

IN_DIR  = ROOT_DIR+'in\\'
OUT_DIR = ROOT_DIR+'out\\'


if __name__=='__main__':
    names=os.listdir(IN_DIR)
    
    if not os.path.isdir(OUT_DIR):
        os.mkdir(OUT_DIR)

    for name in names:
        if os.path.isfile(IN_DIR+name) and name.endswith('.csv'):
            with open(IN_DIR+name,'r',encoding='utf-8') as file:
                words=file.readlines()
            
            with open(OUT_DIR+name,'w',encoding='utf-8') as out_file:
                for k,word in enumerate(words):
                    eng,kor=word.replace('\n','').split('\t')[:2]
                    eng_pre=eng[:ENGLISH_PRE]
                    kor_pre=kor[:KOREAN_PRE]
                    out_file.write(('\t').join((eng,kor,eng_pre,kor_pre))+'\n')
                out_file.flush()