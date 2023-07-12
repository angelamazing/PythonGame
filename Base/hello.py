
import random

result = random.randint(1,100)
i = 0
print('take a guess')
while True:
    num = int(input('input your guess: '))
    i += 1
    if num == result:
        print('congratulation')
        break
    if num < result:
        print('less')
    elif num > result:
        print('large')
    