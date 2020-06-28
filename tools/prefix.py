import os
from tools import parsing


if __name__=='__main__':
    files=os.listdir()

    for file in files:
        if os.path.isfile(file) and os.path.splitext(file)[1]=='.csv':
            with open(file,'r',encoding='utf-8') as fr:
                lines=fr.readlines()
            
            res=[]
            for line in lines:
                if line.count('\t')>1:
                    a,b=line.replace('\n','').split('\t')[1:3]
                    if b.startswith('-'):
                        b="'"+b
                    res.append((a,b))
            res.sort()
            
            with open(os.path.splitext(file)[0]+'.tsv','w',encoding='cp949') as fw:
                for r in res:
                    fw.write('\t'.join(r)+'\n')