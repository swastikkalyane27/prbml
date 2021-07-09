'''

      Inter Thread Communication With Condition()
------------------------------------------------------------
ome following methods of Condition class we discuss below :

release()
acquire()
notify(n=1)  ==>When we want to send a notification to only one thread that is in
         waiting state then we always use notify() method.
wait()   ==>The wait() method can be used to make a thread wait till the notification got
            and also till the given time will end.
notifyAll() ==>the notifyAll() method is used to send notifications for all waiting threads.
# ----------------------------------------------------------
'''
import time
# from threading import *
# import random
#
#
# class appointment:
#
#
#     def patient(self,name):
#         condition_object.acquire()
#         print('patient {} waiting for appointment'.format(name))
#         condition_object.wait()  # Thread is in waiting state
#         print(name,'successfully got the appointment')
#         condition_object.release()
#
#     def doctor(self,name):
#         condition_object.acquire()
#         print('doctor {} checking the time for appointment'.format(name))
#         time = 0
#         time = random.randint(1, 13)
#         print('time checked')
#         print('oppointed time is {} PM'.format(time))
#         condition_object.notify(2)
#         condition_object.release()
#
# # l=Lock()
# condition_object = Condition()
# class_obj = appointment()
#
#
# T1 = Thread(target=class_obj.patient,args=('swastik',))
# T3 = Thread(target=class_obj.patient,args=('shubham',))
#
# T2 = Thread(target=class_obj.doctor,args=('prasad',))
# # T4 = Thread(target=class_obj.doctor,args=('swapnil',))
#
#
# T1.start()
# T3.start()
# T2.start()
# T4.start()




import threading
import time
class product:

 def buyer(self):
   event_object.acquire()
   print('John consumer is wait for product')
   print('...............')
   event_object.wait()
   # time.sleep(15)
   print('buyer got product form seller')
   event_object.release()

 def seller(self):
   event_object.acquire()
   time.sleep(5)
   print('Tom producer producing items')
   print('tom goes to retailer')
   event_object.wait()
   # event_object.notify()
   time.sleep(2)
   print('tom got product')
   event_object.release()
 def retailer(self):
   event_object.acquire()
   time.sleep(10)
   print('retailer found and send it to seller ')
   event_object.notifyAll()
   event_object.release()

class_obj = product()

event_object = threading.Condition()

T1 = threading.Thread(target=class_obj.buyer)
# T4 = threading.Thread(target=class_obj.buyer)
T2 = threading.Thread(target=class_obj.seller)
# T5 = threading.Thread(target=class_obj.seller)
T3 = threading.Thread(target=class_obj.retailer)
# T6 = threading.Thread(target=class_obj.retailer)

T1.start()
T2.start()
T3.start()
# T4.start()
# T5.start()
# T6.start()