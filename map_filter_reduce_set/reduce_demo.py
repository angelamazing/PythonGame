"""
reduce
"""
from functools import reduce
myList1 = [1,2,3]
result = reduce(lambda x,y:x+y,myList1)
print(result)