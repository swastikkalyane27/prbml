# by 3 way we can do synchronization
# 1)Lock
'''
l = Lock()
def fun():
    1 lakh line of code # read
    l.acquire()    #calling acquire method which lock the below code for only one thread
       some impornt code which should be executed by only one thread #update
    l.release()    # to realese the lock for next thred
    1 lakh line of code #read
'''
from threading import *
import time
l = Lock()
def wish(name):
    for i in range(3):
        print(name, i * 2)
        time.sleep(1)
    # l.acquire()
    for i in range(5):
        print('good Evening :',end='')
        time.sleep(2)
        print(name,i)
    # l.release()

t1 = Thread(target=wish('swastik'))
t2 = Thread(target=wish('raj'))
# t3 = Thread(target=wish,args=('raj1',))
# t4 = Thread(target=wish,args=('raj2',))
# t5 = Thread(target=wish,args=('raj3',))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()