import os,re

#IN_DIR   = 'out\\'
IN_DIR   = '.\\'
OUT_NAME = 'onefile.tsv'
TAB_NUM  = 3

def natsort(l): 
    convert=lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l,key=alphanum_key)

if __name__=='__main__':
    names=natsort(os.listdir(IN_DIR))

    for name in names:
        if os.path.isfile(IN_DIR+name) and name.endswith('.csv'):
            with open(IN_DIR+name,'r',encoding='utf-8') as file:
                lines=file.readlines()
    
    with open(OUT_NAME,'w',encoding='cp949') as out_file:
        out_file.write('\n'+name.split('.')[0]+'\n')
        for line in lines:
            out_file.write(('\t'*TAB_NUM).join(line.split('\t')[:2]))
        out_file.flush()