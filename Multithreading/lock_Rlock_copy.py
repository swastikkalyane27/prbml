## Thread synchronization
# from threading import *
# import time
# l = Lock()
# def wish(name):
#     l.acquire()
#     for i in range(10):
#         print("Good Evening:",end= "")
#         time.sleep(3)
#         print(name)
#     l.release()
# t1 = Thread(target=wish,args=("dhoni",))
# t2 = Thread(target=wish,args=("kohli",))
# t1.start()
# t2.start()




import threading
import time
from random import randint                 
class SharedCounter(object):
  
    def __init__(self, val = 0):
        self.lock = threading.Lock()
        self.counter = val
        
    def increment(self):
        print("Waiting for a lock")
        self.lock.acquire()
        try:
            print('Acquired a lock, counter value: ', self.counter)
            self.counter = self.counter + 1
        finally:
            print('Released a lock, counter value: ', self.counter)
            self.lock.release()

def task(c):
    # picking up a random number
    r = randint(1,5)
    # running increment for a random number of times
    for i in range(r):
      c.increment()
    print('Done')

if __name__ == '__main__':
    sCounter = SharedCounter()

    t1 = threading.Thread(target=task, args=(sCounter,))
    t1.start()
    
    t2 = threading.Thread(target=task, args=(sCounter,))
    t2.start()

    print('Waiting for worker threads')
    t1.join()
    t2.join()
    
    print('Counter:', sCounter.counter)