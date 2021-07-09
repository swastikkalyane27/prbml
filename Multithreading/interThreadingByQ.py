'''
interthread comunication by using Queue : -
 Queue internally has condition object
 that conditiom has lock object   ===> not require to warry about synchronization

import queue

queue--->module
Queue--->class
 put()---iternally lock aquire and rlease
 get()---internally wait
 '''
# -------------------------------------------------
# from threading import *
# import time
# import random
# import queue
#
# def produce(q):
#    while True:
#      item = random.randint(1,100)
#      print('producer producing item :',item)
#      q.put(item)  #-->internall has lock aquire and release,
#      print('producer giving notification\n')
#      time.sleep(5)
# def consumer(q):
#    # while True:
#        print('consumer waiting for updation\n')
#        print('consumer consume item :',q.get()) #---> internallya has wait until get the notification form put method
#        time.sleep(5)
#
# q = queue.Queue(maxsize=3)
# T1 = Thread(target=consumer,args=(q,))
# T3 = Thread(target=consumer,args=(q,))
# T4 = Thread(target=produce,args=(q,))
# T2 = Thread(target=produce,args=(q,))
# T1.start()
# T2.start()
# T4.start()
# T3.start()

# --------------------------------------
import queue

'''
python support 3 types of Queue

1) FIFO Queue
-----------------
'''
# import queue
# q = queue.Queue()
# q.put(10)
# q.put_nowait(20)
# q.put(23)
# q.put(5)
# while not q.empty():
#         print(q.get_nowait(),end=' ')


'''
 2) LIFO Queue
 -----------------
 '''
# import queue
# q = queue.LifoQueue()
# q.put(10)
# q.put(20)
# q.put(23)
# q.put(5)
# while not q.empty():
#      print(q.get(),end=' ')

'''
3) Priority Queue :
-------------------
'''
# import queue
# q = queue.PriorityQueue()
# q.put(10)
# q.put(20)
# q.put(23)
# q.put(5)
# while not q.empty():
#      print(q.get(),end=' ')
#
# q.put((3,"swapnil"))
# q.put((4,'prasad'))
# q.put((1,'bhandwalkar'))
# q.put((5,'madavi'))
# q.put((3,'swastik'))
# q.put((1,'akshay'))
# q.put((4,'sushant'))
# while not q.empty():
#      print(q.get(),end=' ')
# ----------------------------------
# with stetment
# from threading import *
# import time
# lock = Lock()
# def wish(name):
#           # lock.acquire()
#      with lock :
#           print('hello',name)
#           time.sleep(2)
#           # lock.release()
# t1 = Thread(target=wish,args=('raj',))
# t2 = Thread(target=wish,args=('swastik',))
# t3 = Thread(target=wish,args=('shubham',))
# t4 = Thread(target=wish,args=('sushant',))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# ----------------------------------
