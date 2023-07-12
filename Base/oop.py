class Student():
    def __init__(self,name,chinese,math,engelish):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = engelish
    def display(self):
        pass

import os

stu = []
with open('成绩单.txt','r',encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(1,len(lines)):
        line = lines[i]
        arrs = line.split()
        s = Student(arrs[0],int(arrs[1]),int(arrs[2]),int(arrs[2]))
        stu.append(s)

print(stu[1].math)