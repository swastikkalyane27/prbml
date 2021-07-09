# # identification number(ident)  ident is implicite variable not a fun
# from threading import *
# def display():
#     print("child thread :",current_thread().ident)    # executed by child thread
# t = Thread(target=display,name='swastik kalyane')  # we can set name here also
# # t.setName('swastik kalyane') aslo
#
# t.start()
# print('main thread identification number :',current_thread().ident)     #for main thread
# print('child Thread identification Number :',t.ident)   #for child tread t is object of child thread    # here ident is instance variable of Thread class not method

# join method
from threading import  *
import time
def inf0():
    for i in range(10):
        print('hi',i)
        time.sleep(1)
def info1():
    for i in range(5):
        print('hello',i)
        time.sleep(1)
def info2():
    for i in range(7):
        print("am",i)
        time.sleep(1)
t1 = Thread(target=inf0)
t3 = Thread(target=info2)
t2 = Thread(target=info1)
t1.start()

t2.start()

t3.start()
t1.join()
t2.join()
t3.join()
# t.join()
# for i in range (10):
#     print('hello1',i)