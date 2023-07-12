# 1.%操作符

str_format = "I'm %s. I'm %d years old"
string = str_format % ('lilei', 14)
print(string)

"""
格式符
格式符有很多种，你需要根据实际需要来选择模板里的格式符

%s 字符串 (采用str()的显示)

%r 字符串 (采用repr()的显示)

%c 单个字符

%b 二进制整数

%d 十进制整数

%i 十进制整数

%o 八进制整数

%x 十六进制整数

%e 指数 (基底写为e)

%E 指数 (基底写为E)

%f 浮点数

%F 浮点数，与上相同

%g 指数(e)或浮点数 (根据显示长度)

%G 指数(E)或浮点数 (根据显示长度)

%% 字符"%"

"""

# 2.format
log = "{id}-{type}-{msg}"
print(log.format(id=1,type='debug',msg=u'测试连接'))



info = {
    'id':1,
    'type':'debug',
    'msg':u'测试连接'
}
log = "{0[id]}-{0[type]}-{0[msg]}".format(info)
print(log)



log = "{info[id]}-{info[type]}-{info[msg]}".format(info=info)
print(log)

info = (1,'debug',u'测试连接')
log = "{0[0]}-{0[1]}-{0[2]}".format(info)
print(log)

log = "{info[0]}-{info[1]}-{info[2]}".format(info=info)
print(log)