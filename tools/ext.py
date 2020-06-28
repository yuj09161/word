import os

for file in os.listdir():
    name,ext=os.path.splitext(file)
    print(name,ext)
    if os.path.isfile(file) and ext=='.txt':
        os.rename(file,name+'.csv')