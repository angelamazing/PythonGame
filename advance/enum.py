"""
def print_color(color_code):
    if color_code == 1:
        print('红色')
    elif color_code == 2:
        print('蓝色')
    elif color_code == 3:
        print('黑色')
"""


# 上面的代码不易维护也不清晰

import enum

# 可以继承enum.IntEnum，枚举值只能是int

class ColorCode(enum.Enum):
    RED = 1
    BLUE = 2
    BLACK = 3

def print_color(color_code):
    if color_code == ColorCode.RED.value:
        print('红色')
    elif color_code == ColorCode.BLUE.value:
        print('蓝色')
    elif color_code == ColorCode.BLACK.value:
        print('黑色')

print_color(1)


for color in ColorCode:
    print(color.name,color.value) # name value

print(ColorCode.RED == 1)       # False
"""
这是非常容易出错的地方，很多人相当然的认为ColorCode.RED与1是相等的，但真实的结果却是False
RED是一项枚举，枚举有name和value两个属性，必须通过value才能获得真实的枚举值
或者换一个思路，将枚举值转成枚举类型

print(ColorCode.RED == ColorCode(1))       # True
"""