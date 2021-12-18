import time
import threading

print('外层start',time.asctime())

def fun():
    print('里层start',time.asctime())
    time.sleep(5)
    print('里层end',time.asctime())

p =  threading.Thread(target=fun)
p.start()
p.join()
time.sleep(5)
print('外层end',time.asctime())