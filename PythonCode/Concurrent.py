from multiprocessing import Process,Manager
import random

m = Manager()
q = m.Queue(5)

class produce(Process):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue
    def run(self):
        while True:
            item = random.randint(0,99)
            self.queue.put(item)
            print('生产者生产了%s'%item)

class consumer(Process):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue
    def run(self):
        while True:
            item = self.queue.get()
            print('消费者消费了%s'%item)

p = produce(q)
c = consumer(q)
p.start()
c.start()
p.join()
c.join()

