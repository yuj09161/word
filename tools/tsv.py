import os
from tools import parsing


if __name__=='__main__':
    files=os.listdir()

    for file in files:
        if os.path.isfile(file) and os.path.splitext(file)[1]=='.csv':
            words,prefix=parsing(file)
            with open(os.path.splitext(file)[0]+'.tsv','w',encoding='cp949') as fr:
                for k in range(len(words)):
                    word=words[k]; pre=prefix[k]
                    if not len(pre):
                        fr.write('\t'.join((word[0],'','','',word[1],''))+'\n')
                    elif len(pre)==1:
                        fr.write('\t'.join((word[0],'','','',word[1],pre[0]))+'\n')
                    else:
                        fr.write('\t'.join((word[0],pre[1],'','',word[1],pre[0]))+'\n')