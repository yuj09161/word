import os,re

#IN_DIR      = 'out\\'
IN_DIR      = '.\\'
OUT_NAME    = 'onefile.tsv'
TAB_NUM     = 2
KOREAN_PRE  = 0
ENGLISH_PRE = 1

def natsort(l): 
    convert=lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l,key=alphanum_key)

if __name__=='__main__':
    names=natsort(os.listdir(IN_DIR))

    with open(OUT_NAME,'w',encoding='cp949') as out_file:
        for name in names:
            if os.path.isfile(IN_DIR+name) and name.endswith('.csv'):
                with open(IN_DIR+name,'r',encoding='utf-8') as file:
                    lines=file.readlines()
    
                out_file.write('\n'+name.split('.')[0]+'단원\n')
                out_file.write(('\t').join(('U','No.','Spelling','','K','E','한국어'))+'\n')
                
                for k,line in enumerate(lines):
                    eng,kor=line.split('\t')[:2]
                    eng_pre=eng[:ENGLISH_PRE]
                    kor_pre=kor[:KOREAN_PRE]
                    out_file.write(('\t').join(('',str(k+1),eng,eng_pre)+('',)*TAB_NUM+(kor,))+kor_pre)
                out_file.flush()