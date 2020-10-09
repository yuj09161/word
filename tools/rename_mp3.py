import re,os,sys

#source: https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
def natsort(l): 
    convert=lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l,key=alphanum_key)

def rename():
    names=os.listdir()
    names=natsort(names)
    k=2
    for name in names:
        if name!=os.path.basename(os.path.abspath(__file__)):
            if '_k' in name:
                os.rename(name,str(k//2)+'_k.mp3')
            else:
                os.rename(name,str(k//2)+'_e.mp3')
            k+=1

if __name__=='__main__':
    rename()