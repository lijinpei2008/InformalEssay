import time
import threading
print(threading.current_thread())

def fun():
    print('里层start',time.asctime())
    print(threading.current_thread())
    print('里层end',time.asctime())

p = threading.Thread(target=fun)
p.start()
p = threading.Thread(target=fun)
p.start()
