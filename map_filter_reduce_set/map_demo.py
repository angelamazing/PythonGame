"""
Map会将⼀个函数映射到⼀个输⼊列表的所有元素上。这是它的规范
map(function_to_apply, list_of_inputs)
"""

myList1 = [1,2,3]
result = list(map(lambda x:x**2,myList1))
print(result)

result = [value**2 for value in myList1 ]
print(result)