#Synchronization By using Lock concept in python:
#1]1st program
# from threading import *
# import time
# l=Lock()
# print(l)
# def wish(name,age):
#    for i in range(2):
#        l.acquire()
#        print(l)
#        print("Hi",name)
#        time.sleep(2)
#        print("Your age is",age)
#        l.release()
#        print(l)
# t1=Thread(target=wish, args=("Sireesh",15))
# t2=Thread(target=wish, args=("Nitya",20))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Main Thread")


#using r lock
from threading import *
import time
l=RLock()
print(l)
def wish(name,age):
   for i in range(1):
       l.acquire()
       l.acquire()
       l.acquire()
       print(l)
       print("Hi",name)
       time.sleep(2)
       print("Your age is",age)
       l.release()
       l.release()
       l.release()
       print(l)
t1=Thread(target=wish, args=("Sireesh",15))
t2=Thread(target=wish, args=("Nitya",20))
t1.start()
t2.start()
t1.join()
t2.join()
print("Main Thread")


#without using lock
# from threading import *
# import time
# def wish(name,age):
#    for i in range(3):
#        print("Hi",name)
#        time.sleep(2)
#        print("Your age is",age)
# t1=Thread(target=wish, args=("Sireesh",15))
# t2=Thread(target=wish, args=("Nitya",20))
# t1.start()
# t2.start()

#2.creating thread by extending Thread class
# from time import sleep
# from threading import *
# l = Lock()
# class Hello(Thread):
#     def run(self):
#         l.acquire()
#         for i in range(5):
#             print("Hello")
#             sleep(1)
#         l.release()
# class Hi(Thread):
#     def run(self):
#         l.acquire()
#         for i in range(5):
#             print("Hi")
#             sleep(1)
#         l.release()
# t1 = Hello()
# t2 = Hi()
# t1.start()
# #sleep(0.2)
# t2.start()
# t1.join()
# t2.join()
# print("Main Thread")


# from threading import *
# class Flight:
#     def __init__(self,available_seat):
#         self.available_seat=available_seat
#         self.l=Lock()
#
#     def reserve(self,need_seat):
#         self.l.acquire()
#         print("available seats:",self.available_seat)
#         if(self.available_seat >= need_seat):
#             name = current_thread().name
#             print(f'{need_seat} seat is allocated for {name}')
#             self.available_seat -= need_seat
#         else:
#             print("sorry all seats has allocated")
#         self.l.release()
# f= Flight(4)
# t1=Thread(target=f.reserve, args=(1,), name="Rahul")
# t2=Thread(target=f.reserve, args=(1,), name="Soham")
# t3=Thread(target=f.reserve, args=(1,), name="sushant")
# t4=Thread(target=f.reserve, args=(1,), name="swastik")
# t5=Thread(target=f.reserve, args=(1,), name="swapnil")
# t6=Thread(target=f.reserve, args=(1,), name="shubham")
# t7=Thread(target=f.reserve, args=(1,), name="prasad")
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()





#1]durga sir program


# from threading import *
# import time
# l=Lock()
# def wish(name):
#
#     l.acquire()
#     for i in range(2):
#         print("Good morning: ",end=" ")
#         time.sleep(2)
#         print(name)
#     l.release()
# t1=Thread(target=wish, args=("sushant",))
# t2=Thread(target=wish, args=("shubham",))
# t1.start()
# t2.start()





