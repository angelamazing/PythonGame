some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# 交集
valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = {'red', 'brown'}
print(input_set.intersection(valid))

# 差集
valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = {'red', 'brown'}
print(input_set.difference(valid))
