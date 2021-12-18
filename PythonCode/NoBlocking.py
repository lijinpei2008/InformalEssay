import socket

server = socket.socket()
server.setblocking(False)
server.bind(('',9090))
server.listen(1024)

conn_list = []
while True:
    try:
        conn,addr = server.accept()
        conn.setblocking(False)
        conn_list.append(conn)
    except BlockingIOError as message:
        pass

    del_list = [conn for conn in conn_list]
    for conn in del_list:
        try:
            recv_data = conn.recv(1024)
            if recv_data:
                print(recv_data)
                conn.send(recv_data)
            else:
                conn.close()
                conn_list.remove(conn)
        except BlockingIOError as message:
            pass

