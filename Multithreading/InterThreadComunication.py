'''
interThreadcomunication we can impliment by
------------------------------------------
1)event
2)condition
3)queue
---------------------
1)InterThread comunication by using event:
------------------------------------------
   METHODS
****************
   e = Event()
   a) set() ==>> e.set() ==>   # there are much thread which was in waiting for the state they become continue their execution.
   b) clear() ==>> e.clear() ==>  # which thread is not running or already in waiting, so they are still is in waiting
                                      for state and don’t continue there execution.
   c) wait() ==>>e.wait() ==> the wait() method in simple words we can say that thread waits until the execution of the
                              set() method . We can use time in it if we set a certain time then the execution will
                              stop until time overs after that it will execute still the set() of an event is remaining.
   d) isSet() ==>> e.isSet() ==> this method simplifies that the following event that we have created are set or not
# '''
from threading import *
import time
# e = Event()
# def consumer():
#    print('consumer thread waiting for updation....')
#    e.wait()
#    print('consumer thread got notification and consuming items....')
# def producer():
#    time.sleep(5)
#    print('producer thread producing items ...')
#    print('producer thread giving notification by setting event...')
#    e.set()
# t1 = Thread(target=producer)
# t2 = Thread(target=consumer)
# t3 = Thread(target=consumer)
# t1.start()
# t2.start()
# -----------------------------------------------------
# e=Event()
# def trafficpolice():
#    while True :
#       time.sleep(10)
#       print('traffic police giving GREEN single')
#       e.set()
#       time.sleep(20)
#       print('traffic police giving RED single')
#       e.clear()
# def driver():
#       num = 0
#       while True:
#          print('driver waiting for GREEN signal')
#          e.wait()
#          print('traffic signal is GREEN ...vehicles can move')
#          while e.isSet() :
#             num +=1
#             print('vehicle number : ',num,'crossing the signal')
#             time.sleep(2)
#          print('traffic signal is RED ...Driver have to wait')
# t1 = Thread(target=trafficpolice)
# t2 = Thread(target=driver)
# t1.start()
# t2.start()
# ---------------------------------------------------------------

# import time
#
# import threading
#
# class product:
#
#  def buyer(self):
#    print('John consumer is wait for product')
#    print('...............')
#    event_object.wait()
#    time.sleep(3)
#    print('buyer got product form seller')
#
#  def seller(self):
#    time.sleep(5)
#    print('Tom producer producing items')
#    print('tom goes to retailer')
#    event_object.wait()
#    # event_object.set()
#    time.sleep(2)
#    print('tom got product')
#
#  def retailer(self):
#    time.sleep(10)
#    print('retailer found and send it to seller ')
#    event_object.set()
#
# class_obj = product()
#
# event_object = threading.Event()
#
# T1 = threading.Thread(target=class_obj.buyer)
# T2 = threading.Thread(target=class_obj.seller)
# T3 = threading.Thread(target=class_obj.retailer)
#
# T1.start()
# T2.start()
# T3.start()
# --------------------------------------------------
# ------------------------------
from threading import *
# import time
# e = Event()
# def consumer():
#    print('consumer thread waiting for updation....')
#    e.wait()
#    print('consumer thread got notification and consuming items....')
# def producer():
#    time.sleep(5)
#    print('producer thread producing items ...')
#    print('producer thread giving notification by setting event...')
#    e.set()
# t1 = Thread(target=producer)
# t2 = Thread(target=consumer)
# t1.start()
# t2.start()
# -----------------------------------------------------
# e=Event()
# def trafficpolice():
#    while True :
#       time.sleep(10)
#       print('traffic police giving GREEN single')
#       e.set()
#       time.sleep(20)
#       print('traffic police giving RED single')
#       e.clear()
# def driver():
#       num = 0
#       while True:
#          print('driver waiting for GREEN signal')
#          e.wait()
#          print('traffic signal is GREEN ...vehicles can move')
#          while e.isSet() :
#             num +=1
#             print('vehicle number : ',num,'crossing the signal')
#             time.sleep(2)
#          print('traffic signal is RED ...Driver have to wait')
# t1 = Thread(target=trafficpolice)
# t2 = Thread(target=driver)
# t1.start()
# t2.start()
# ---------------------------------------------------------------
