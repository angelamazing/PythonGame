f = open('成绩单.txt','r',encoding='utf-8')

for line in f:
    line = line.rstrip()
    print(line)

import pickle

class Stu:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Stu('小明', 15)

f = open('stu_obj', 'wb')
pickle.dump(stu, f)

f = open('stu_obj','rb')
stu1 = pickle.load(f)
print(stu1.name)
f.close()
