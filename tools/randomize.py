import random,sys
from tools import parsing

if __name__=='__main__':
    if len(sys.argv)>1:
        n=sys.argv[1]
    else:
        n=3
    
    words,prefix=parsing('rand.csv'); data=[]
    for k in range(len(words)):
        data.append([str(k+1),*words[k],*prefix[k]])
    for k in range(1,n+1):
        random.shuffle(data)
        with open('random%s.tsv' %k,'w',encoding='cp949') as file:
            for k in range(len(data)):
                d=data[k]; n=len(d)
                for k in range(n):
                    if d[k].startswith('-'):
                        d[k]="'"+d[k]
                if n==3:
                    #file.write('\t'.join((d[0],d[1],'','','',d[2],''))+'\n')
                    file.write('\t'.join((d[1],'','','',d[2],''))+'\n')
                elif n==4:
                    #file.write('\t'.join((d[0],d[1],'','','',d[2],d[3]))+'\n')
                    file.write('\t'.join((d[1],'','','',d[2],d[3]))+'\n')
                elif n==5:
                    #file.write('\t'.join((d[0],d[1],d[4],'','',d[2],d[3]))+'\n')
                    file.write('\t'.join((d[1],d[4],'','',d[2],d[3]))+'\n')