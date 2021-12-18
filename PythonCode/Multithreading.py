import socket
import threading

server = socket.socket()
server.bind(('',9090))
server.listen(1024)

def fun(conn):
    while True:
        recv_data = conn.recv(1024)
        if recv_data:
            print(recv_data)
            conn.send(recv_data)
        else:
            conn.close()
            break

while True:
    conn,addr = server.accept()
    t = threading.Thread(target=fun,args=(conn,))
    t.start()