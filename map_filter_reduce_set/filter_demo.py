number_list = range(-5,5)
less_than_zero = list(filter(lambda x:x<0,number_list))
print(less_than_zero)
"""
大部分情况下，都可以用列表推导式取代
"""
less_than_zero_1 = [value for value in number_list if value < 0]
print(less_than_zero_1)