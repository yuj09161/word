import sys

START_NUM=1

if __name__=='__main__':
    with open('sel.csv','r',encoding='utf-8') as file:
        lines=file.readlines()
    if len(sys.argv)>1:
        if sys.argv[1]=='-r':
            tmp=[int(k)-START_NUM for k in sys.argv[2:]]
            with open('selout.csv','w',encoding='utf-8') as file:
                for k in range(len(lines)):
                    if not k in tmp:
                        file.write(lines[k])
        else:
            with open('selout.csv','w',encoding='utf-8') as file:
                for k in sys.argv[1:]:
                    if '-' in k:
                        a,b=k.split('-')
                        for j in range(int(a)-1,int(b)):
                            file.write(lines[j])
                    else:
                        index=int(k)-START_NUM
                        file.write(lines[index])
    else:
        print('Error: No Options Gived')