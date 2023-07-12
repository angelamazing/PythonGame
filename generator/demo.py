def fibonaqie(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

def printIter(iterItem):
    while True:
        try:
            print(next(iterItem))
        except StopIteration as e:
            print(e)
            break


iter1 = fibonaqie(5)
printIter(iter1)

#如何把string变为迭代器
iter2 = iter('abcdfe')
printIter(iter2)




