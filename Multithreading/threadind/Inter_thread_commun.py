## Interthread Communication
## by using Event object
# from threading import *
# import time
# e = Event()
# def consumer():
#     print("consumer thread is waiting for updation....")
#     e.wait()
#     print("consumer thread got notification and conusming items....")

# def producer():
#     time.sleep(5)
#     print("Producer threads producing items....")
#     print("Producer thread giving notification by setting Event")
#     e.set()

# t1 = Thread(target=producer)
# t2 = Thread(target=consumer)
# t1.start()
# t2.start()



# from threading import *
# import time
# e = Event()
# def trafficpolice():
#     while True:
#         time.sleep(20)
#         print("Traffic police giving GREEN signal")
#         e.set()
#         time.sleep(20)
#         print("Traffic police giving RED signal")
#         e.clear()

# def driver():
#     num = 0
#     while True:
#         print("drivers waiting for GREEN signal")
#         e.wait()
#         print("Traffic signal is GREEN vehicles can move...")
#         while e.is_set():
#             num = num + 1
#             print("vehicle number:",num,"crossing the signal")
#             time.sleep(2)
#         print("The signal is RED .... Drivers have to wait")

# t1 = Thread(target=trafficpolice)
# t2 = Thread(target=driver)
# t1.start()
# t2.start()


# import threading
# import time

# def task(event, timeout):
#   print("Started thread but waiting for event...")
#   # make the thread wait for event with timeout set
#   event_set = event.wait(timeout)
#   if event_set:
#     print("Event received, releasing thread...")
#   else:
#     print("Time out, moving ahead without event...")
    
# if __name__ == '__main__':
#   # initializing the event object
#   e = threading.Event()
  
#   # starting the thread
#   thread1 = threading.Thread(name='Event-Blocking-Thread', target=task, args=(e,4))
#   thread1.start()
#   # sleeping the main thread for 3 seconds
#   time.sleep(3)
#   # generating the event
#   e.set()
#   print("Event is set.")
  
# ---------------------------------------------------------------------------------------------------

## by using Condition object
# from threading import *
# def consumer(c):
#     c.acquire()
#     print("consumer is waiting for updation.....") 
#     c.wait()
#     print("consumer got notification & consuming the items")
#     c.release()

# def producer(c):
#     c.acquire()
#     print("producer producing items....")
#     print("producer giving notification")
#     c.notify()
#     c.release()

# c = Condition()
# t1 = Thread(target=consumer,args=(c,))
# t2 = Thread(target=producer,args=(c,))
# t1.start()
# t2.start()


from threading import *
import time
from random import randint
items = []
def producer(c):
    while True:
        c.acquire()
        item = randint(1,60)
        print("producer producing item:",item)
        items.append(item)
        print("producer giving notification")
        c.notify()
        c.release()
        time.sleep(5)

def consumer(c):
    while True:
        c.acquire()
        print("consumer waiting for updation")
        c.wait()
        print("consumer consuming the items:",items.pop())
        c.release()
        time.sleep(5)

c = Condition()
t1 = Thread(target=consumer,args=(c,))
t3 = Thread(target=consumer,args=(c,))
t2 = Thread(target=producer,args=(c,))
t1.start()
t2.start()
t3.start()


# import threading
# import time
# from random import randint

# class SomeItem:
#   # init method
#   def __init__(self):
#     # initialize empty list
#     self.list = []
  
#   # add to list method for producer
#   def produce(self, item):
#     print("Adding item to list...")
#     self.list.append(item)
    
#   # remove item from list method for consumer
#   def consume(self):
#     print("consuming item from list...")
#     item = self.list[0]
#     print("Item consumed: ", item)
#     self.list.remove(item)

# def producer(si, cond):
#     r = randint(1,5)
#     # creating random number of items
#     for i in range(1, r):
#       print("working on item creation, it will take: " + str(i) + " seconds")
#       time.sleep(i)
#       print("acquiring lock...")
#       cond.acquire()
#       try:
#         si.produce(i)
#         cond.notify()
#       finally:
#         cond.release()
      
# def consumer(si, cond):
#     cond.acquire()
#     while True:
#       try:
#         si.consume()
#       except:
#         print("No item to consume...")
#         # wait with a maximum timeout of 10 sec
#         val = cond.wait(10)
#         if val:
#           print("notification received about item production...")
#           continue
#         else:
#           print("waiting timeout...")
#           break
        
#     cond.release()
    
# if __name__=='__main__':
#   # condition object
#   cond = threading.Condition()
#   # SomeItem object
#   si = SomeItem()
#   # producer thread
#   p = threading.Thread(target=producer, args=(si,cond,))
#   p.start()
#   # consumer thread
#   c = threading.Thread(target=consumer, args=(si,cond,))
#   c.start()

#   #print('Waiting for producer and consumer threads...')
#   p.join()
#   c.join()
#   print("Done")
  
#------------------------------------------------------------------------------------------------------

## by using Queue object
# from threading import *
# import time 
# import random
# import queue
# def produce(q):
#     while True:
#         item = random.randint(1,50)
#         print("producer producing item:",item)
#         q.put(item)
#         print("producer giving notification")
#         time.sleep(5)

# def consume(q):
#     while True:
#         print("consumer waiting for updation")
#         print("consumer consuming items:",q.get())
#         time.sleep(5)

# q = queue.Queue()
# t1 = Thread(target=consume,args=(q,))
# t2 = Thread(target=produce,args=(q,))
# t1.start()
# t2.start()

## FIFO Queue  #first in first out
# import queue
# q = queue.Queue()
# q.put(10)
# q.put(13)
# q.put(5)
# q.put(8)
# q.put(0)
# #print(q.get())
# while not q.empty():
#     print(q.get(),end=" ")


## LIFO Queue   #last in first out
# import queue
# q = queue.LifoQueue()
# q.put(10)
# q.put(13)
# q.put(5)
# q.put(8)
# q.put(0)
# #print(q.get())
# while not q.empty():
#     print(q.get(),end=" ")



## Priority Queue
# import queue
# q = queue.PriorityQueue()
# q.put(10)
# q.put(13)
# q.put(5)
# q.put(8)
# q.put(0)
# #print(q.get())
# while not q.empty():
#     print(q.get(),end=" ")



# import queue
# q = queue.PriorityQueue()
# q.put((2,"akshay"))
# q.put((5,"swapnil"))
# q.put((3,"prasad"))
# q.put((1,"sushant"))
# q.put((4,"shubham"))
# q.put((6,"pratik"))
# #print(q.get())
# while not q.empty():
#     print(q.get(),end=" ")



# import queue
# q = queue.PriorityQueue()
# q.put("akshay")
# q.put("swapnil")
# q.put("prasad")
# q.put("sushant")
# q.put("shubham")
# q.put("pratik")
# #print(q.get())
# while not q.empty():
#     print(q.get(),end=" ")



# Python program to
# demonstrate implementation of
# queue using queue module


# from queue import Queue

# # Initializing a queue
# q = Queue(maxsize = 3)

# # qsize() give the maxsize
# # of the Queue
# print(q.qsize())

# # Adding of element to queue
# q.put('a')
# q.put('b')
# q.put('c')

# # Return Boolean for Full
# # Queue
# print("\nFull: ", q.full())

# # Removing element from queue
# print("\nElements dequeued from the queue")
# print(q.get())
# print(q.get())
# print(q.get())

# # Return Boolean for Empty
# # Queue
# print("\nEmpty: ", q.empty())

# q.put(1)
# print("\nEmpty: ", q.empty())
# print("Full: ", q.full())

# # This would result into Infinite
# # Loop as the Queue is empty.
# # print(q.get())


#------------------------------------------------------------------------------------------------------

## by using Timer object
# import threading

# def task():
#     print("timer object task running...")

# if __name__=='__main__':
#     t = threading.Timer(10, task)
#     t.start() # after 10 seconds, task will be executed


# import threading
# import time

# def task():
#   print("Timer object is getting executed...")

# if __name__=='__main__':
#   t = threading.Timer(5,task)
#   print("Starting the timer object...")
#   t.start() # after 5 seconds, task will be executed
  
#   # cancelling the timer object before start
#   print("cancelling the timer object")
#   t.cancel()

