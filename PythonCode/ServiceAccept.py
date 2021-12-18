import socket

server = socket.socket()
server.bind(('',9090))
server.listen(1024)

while True:
    conn,address = server.accept()
    while True:
        recv_data = conn.recv(1024)

        if recv_data:
            print(recv_data)
            conn.send(recv_data)
        else:
            conn.close()
            break
