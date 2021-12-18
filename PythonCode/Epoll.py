import socket
import selectors

epoll_selector = selectors.EpollSelector()

server = socket.socket()
server.bind(('',9090))
server.listen(1024)

def read(conn):
    recv_data = conn.recv(1024)
    if recv_data:
        print(recv_data)
        conn.send(recv_data)
    else:
        epoll_selector.unregister(conn)
        conn.close()

def accept(server):
    conn,addr = server.accept()
    epoll_selector.register(conn,selectors.EVENT_READ,read)

epoll_selector.register(server,selectors.EVENT_READ,accept)

while True:
    events = epoll_selector.select()
    for key,mask in events:
        callback = key.data
        sock = key.fileobj
        callback(sock)