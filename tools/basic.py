import os,json

with open('change.json','r',encoding='utf-8') as file:
    changes=json.load(file)

def convert(txts):
    for k in range(len(txts)):
        txt=txts[k]
        for origin in changes:
            if origin in txt:
                txt=txt.replace(origin,changes[origin])
            txts[k]=txt
    return txts

if __name__=='__main__':
    files=os.listdir()
    for file in files:
        name,ext=os.path.splitext(file)
        if ext=='.txt':
            with open(file,'r',encoding='utf-8') as fin:
                lines=fin.readlines()
            lines=convert(lines)
            with open(name+'.csv','w',encoding='utf-8') as fout:
                for line in lines:
                    fout.write(line)
