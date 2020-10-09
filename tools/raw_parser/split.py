with open('out.txt','r',encoding='utf-8') as file:
    data=file.read()

data=data.split('\n'*4)
print(data)

for lecture in data:
    print(lecture)
    name,words=lecture.split('\n',1)
    with open(f'out/{name}.csv','w',encoding='utf-8') as file:
        file.write(words)
