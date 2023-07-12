f = open('test.txt','a+',encoding='utf-8') # 如果有中文需要加入utf-8
text = 'sdsda'
f.write(text)
f.close()
f = open('test.txt','r',encoding='utf-8') # 如果有中文需要加入utf-8
print(f.read())

