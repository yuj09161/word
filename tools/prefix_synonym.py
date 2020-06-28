import os

if __name__=='__main__':
    files=os.listdir()

    for file in files:
        if os.path.isfile(file) and os.path.splitext(file)[1]=='.csv':
            with open(file,'r',encoding='utf-8') as fr:
                res=[line.replace('\n','').split('\t') for line in fr.readlines()]
            
            with open(os.path.splitext(file)[0]+'_pre.csv','w',encoding='utf-8') as fw:
                for r in res:
                    fw.write('\t'.join(r[2:])+'\n')