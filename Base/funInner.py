builtins = globals()['__builtins__']
print(type(builtins))

max_function = builtins.max
print(max_function([1, 4, 6, 9]))
print(builtins.input("请输入一个整数:"))