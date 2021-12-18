import time
import threading
time.sleep(5)
print(threading.current_thread().ident) #进程是 .pid

def fun():
    time.sleep(6)
t = threading.Thread(target=fun)
print('开始之前',t.ident)
t.start()
print('开始之后',t.ident)