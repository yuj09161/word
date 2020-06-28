import os,re

IN_DIR   = 'out\\'
OUT_NAME = 'onefile.tsv'

out_file=open(OUT_NAME,'w',encoding='cp949')

def natsort(l): 
    convert=lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l,key=alphanum_key)

names=natsort(os.listdir(IN_DIR))

for name in names:
    if os.path.isfile(IN_DIR+name) and name.endswith('.csv'):
        with open(IN_DIR+name,'r',encoding='utf-8') as file:
            lines=file.readlines()
        
        out_file.write('\n'+name.split('.')[0]+'\n')
        for line in lines:
            out_file.write('\t\t\t'.join(line.split('\t')[:2]))
        out_file.flush()

out_file.close()