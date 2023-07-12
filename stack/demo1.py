def ten2two(num):
    arr = []
    while num != 0:
        a = num % 2
        arr.append(a)
        num = num//2

    arr.reverse()
    print(str(arr))

ttete = 23


ten2two(ttete)
