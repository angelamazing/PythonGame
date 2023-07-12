import time

def my_print(content,count,sleep=1):
    for i in range(count):
        print(content)
        time.sleep(1)

my_print('like',5)

my_print(count=2, content='关键字参数', sleep=2) # 这样可以无视位置

# 可变参数
# 1.*args
# 2.**kargs
def func(*args):
    print(args, type(args))
    sum_res = 0
    for item in args:
        sum_res += item

    return sum_res

print(func(2))
print(func(2, 3, 4))

def print_score(**kwargs):
    print(kwargs, type(kwargs))
    for course, score in kwargs.items():
        print(course, score)


print_score(yuwen=89, shuxue=94)
