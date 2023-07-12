s1 = '[()]]'


dic1 = set(')]')

def isValid(s):
    arr = []
    for value in s:
        try:
            if value not in dic1:
                arr.append(value)
            elif arr[-1] == '(' and value == ')':
                arr.pop()
            elif arr[-1] == '[' and value ==']':
                arr.pop()
        except IndexError as e:
            print(e)
            return False
    print(arr)
    if len(arr) == 0:
        return True
    else:
        return False

print(isValid(s1))



