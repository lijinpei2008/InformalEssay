import socket
from multiprocessing import Pool,cpu_count
from multiprocessing.pool import ThreadPool

server = socket.socket()
server.bind(('',9090))
server.listen(1024)

def work_thead(conn):
    while True:
        recv_data = conn.recv(1024)
        if recv_data:
            print(recv_data)
            conn.send(recv_data)
        else:
            conn.close()
            break
def work_process(server):
    t_pool = ThreadPool((2*cpu_count()))
    while True:
        conn,addr = server.accept()
        t_pool.apply_async(work_thead,args=(conn,))
        while True:
            conn,addr = server.accept()
            t_pool.apply_async(work_thead,args=(conn,))

n = cpu_count()
p = Pool(n)
for i in range(n):
    p.apply_async(work_process,args=(server,))
p.close()
p.join()