import socket

client = socket.socket()
client.connect(('127.0.0.1',9090))

while True:
    message = input('请输入：')
    client.send(message.encode())
    data = client.recv(1024)
    print('这是服务器返回的数据：%s'%data.decode())