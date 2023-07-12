import socket


url = 'www.zhangdongshengtech.com'
port = 80
# 创建TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务端
sock.connect((url, port))
# 创建请求消息头
request_url = 'GET /article-types/6/ HTTP/1.1\r\nHost: www.zhangdongshengtech.com\r\nConnection: close\r\n\r\n'
print(request_url)
# 发送请求
sock.send(request_url.encode())
response = b''
# 接收返回的数据
rec = sock.recv(1024)
while rec:
    response += rec
    rec = sock.recv(1024)

print(response.decode())
print(type(response))