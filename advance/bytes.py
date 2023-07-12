# 字符串由多个字符串构成，以字符为单位进行操作
# 字节串由多个字节构成

import hashlib

string = "123456"

m = hashlib.md5()       # 创建md5对象
str_bytes = string.encode(encoding='utf-8')
print(type(str_bytes))


m.update(str_bytes)   # update方法只接收bytes类型数据作为参数
str_md5 = m.hexdigest()     # 得到散列后的字符串

print('MD5散列前为 ：' + string)
print('MD5散列后为 ：' + str_md5)


f = open('data', 'wb')
text = '二进制写文件'
text_bytes = text.encode('utf-8')
f.write(text_bytes)
f.close()

f = open('data', 'rb')
data = f.read()
print(data, type(data))
str_data = data.decode('utf-8')
print(str_data)
f.close()

# 字符串与bytes类型数据转换
string = "爱我中华"
bstr = string.encode(encoding='utf-8')
print(bstr, type(bstr))

string = bstr.decode(encoding='utf-8')
print(string, type(string))