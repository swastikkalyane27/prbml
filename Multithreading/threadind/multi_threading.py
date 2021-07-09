## Multithreading
# import threading
# print("Current executing thread:",threading.current_thread().getName())


## creating thread without using class
# from threading import *
# def display():
#     print("this code (display function) is executed by Thread: ",current_thread().getName())

# t = Thread(target=display)
# t.start()
# #t = Thread(target=display).start()
# print("THIS CODE : ",current_thread().getName())


# def display():
#     for i in range(10):
#         print("child thread")

# t = Thread(target=display)
# t.start()
# for i in range(10):
#     print("Main thread")



## creating thread by extending Thread class
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Child Thread-2")

# t = MyThread()
# # t.start()
# for i in range(10):
#     print("Main Thread-2")




## creating thread without extending Thread class
# class Test:
#     def display(self):
#         for i in range(10):
#             print("Child Thread-2")

# obj = Test()
# t = Thread(target=obj.display)
# t.start()
# for i in range(10):
#     print("Main Thread-2")



## problem without using multithread concept
# import time
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("doubles:",2*n)

# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("squares:", n * n)

# numbers = [1,2,3,4,5,6]
# begintime = time.time()
# doubles(numbers)
# squares(numbers)
# endtime = time.time()
# print("total time taken:",endtime-begintime)



## problem using multithread concept
# from threading import *
# import time
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("doubles:",2 * n)

# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("squares:", n * n)

# numbers = [1,2,3,4,5,6]
# begintime = time.time()
# t1 = Thread(target=doubles,args=(numbers,),name="child thread 1")
# t2 = Thread(target=squares,args=(numbers,))
# print(t1.getName())
# # t1.setName("datta")
# print(t1.name)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# # endtime = time.time()
# print("total time taken:",endtime-begintime)



## getting and setting name
# from threading import *
# print("thread name:",current_thread().getName())
# current_thread().setName("shubham")
# print("thread name:",current_thread().getName())
# print("thread name:",current_thread().name)



## thread identification number(ident)
# from threading import *
# def display():
#     print("child thread:",current_thread().ident)
# t = Thread(target=display)
# t.start()
# print(id(t))
# print("Main thread identification number:",current_thread().ident)
# print("child thread identification number:",t.ident)



## active count of threads
# from threading import *
# import time
# def display():
#     print(current_thread().name,"started.....")
#     time.sleep(3)
#     print(current_thread().name,"ended.....")
# print("active count of threads:",active_count())
# t1 = Thread(target=display,name="child thread 1")
# t2 = Thread(target=display,name="child thread 2")
# t3 = Thread(target=display,name="child thread 3")
# t1.start()
# t2.start()
# t3.start()
# print("active count of threads:",active_count())
# time.sleep(10)
# print("active count of threads:",active_count())



## enumerate() method to get list of current active threads object
# from threading import *
# import time
# def display():
#     print(current_thread().name,"started.....")
#     time.sleep(3)
#     print(current_thread().name,"ended.....")
# print("active count of threads:",active_count())
# t1 = Thread(target=display,name="child thread 1")
# t2 = Thread(target=display,name="child thread 2")
# t3 = Thread(target=display,name="child thread 3")
# t1.start()
# t2.start()
# t3.start()
# l = enumerate()
# print(l)
# for i in l:
#     print("name:",i.name) 
#     print("Id no:",i.ident)
# time.sleep(10)
# print("after 10 second sleeping......")
# l = enumerate()
# for i in l:
#     print("name:",i.name) 
#     print("Id no:",i.ident)



## checking whether thread is alive or not using isAlive() method
# from threading import *
# import time
# def display():
#     print(current_thread().name,"started.....")
#     time.sleep(3)
#     print(current_thread().name,"ended.....")
# print("active count of threads:",active_count())
# t1 = Thread(target=display,name="child thread 1")
# t2 = Thread(target=display,name="child thread 2")
# t3 = Thread(target=display,name="child thread 3")
# t1.start()
# t2.start()
# t3.start()
# print(t1.name,"is alive",t1.is_alive)
# print(t2.name,"is alive",t2.is_alive)
# print(t3.name,"is alive",t3.is_alive)
# time.sleep(10)
# print(t1.name,"is alive",t1.is_alive)
# print(t1.name,"is alive",t1.is_alive)
# print(t1.name,"is alive",t1.is_alive)



## join() method 
# from threading import *
# import time
# def display():
#     for i in range(10):
#         print("Child thread")
#         time.sleep(3)

# t = Thread(target=display)
# t.start()
# t.join(10)
# for i in range(10):
#     print("Main thread")



## Daemon threads
# import module
# from threading import *
# print(current_thread().setDaemon(True))



# from threading import *
# def job():
#     print("child thread")

# t = Thread(target=job)
# print(t.daemon)
# t.setDaemon(True)
# print(t.isDaemon())


# from threading import *
# import time
# def job():
#     print("child thread")
#     time.sleep(3)

# t = Thread(target=job)
# # t.setDaemon(True)
# t.start()
# time.sleep(5)


# from threading import *
# import time
# def job1():
#     print("job1 execution....")
#     print(current_thread().name,"is daemon:",current_thread().daemon)
#     ct = Thread(target=job2,name="childthread2")
#     ct.start()
#     print("ct is daemon:",ct.daemon)

# def job2():
#     print("job2 execution....")

# t = Thread(target=job1,name="childthread")
# t.setDaemon(True)
# t.start()
# time.sleep(10)







# Example 1
# import time
# import threading


# def thread1(i):
#     time.sleep(3)
#     print('No. printed by Thread 1: %d' % i)


# def thread2(i):
#     print('No. printed by Thread 2: %d' % i)


# if __name__ == '__main__':
#     t1 = threading.Thread(target=thread1, args=(10,))
#     t2 = threading.Thread(target=thread2, args=(12,))
#     # start the threads
#     t1.start()
#     t2.start()
#     # join the main thread
#     t1.join()
#     t2.join()





# Example 2
# import threading
# import time
# class MyThread(threading.Thread):
#     # overriding constructor
#     # def __init__(self, i):
#     #     # calling parent class constructor
#     #     threading.Thread.__init__(self)
#     #     self.x = i

#     # define your own run method
#     def run(self,x):
#         print("Value stored is: ", self.x)
#         time.sleep(3)
#         print("Exiting thread with value: ", self.x)


# thread1 = MyThread(1)
# thread1.start()
# thread2 = MyThread(2)
# thread2.start()






# from threading import Thread

# # A function that constitutes as the thread body in python

# def ThreadFunction(TupleData, KeywordDictionary):
#     print("Child Thread Started")

#     for item in TupleData:
#         print(item)

#     for key in KeywordDictionary:
#         print(key + ":" + KeywordDictionary[key])

#     print("Child Thread Exiting")


# print("Main Thread Started")

# # Thread initialisation data as a python tuple

# ThreadData1 = ("State1", "State2", "State3")

# # Thread initialisation data as a python dictionary

# ThreadData2 = dict([("Key1", "Value1"), ("Key2", "Value2"), ("Key3", "Value3")])

# # Construct a python thread object and initialise with data

# SamplePythonThread = Thread(target=ThreadFunction(ThreadData1, ThreadData2), name="ChildThread")

# # Print the name of the child thread

# print("Name of the Child Thread:" + SamplePythonThread.name)

# # Start the child thread

# SamplePythonThread.start()

# # Let the main thread wait for the child thread to complete

# SamplePythonThread.join()

# print("Main Thread Exiting")






from threading import *
import time
l = RLock
def factorial(n):
    l.acquire()
    if n == 0 and n == 1:
        return 1
    else:
        result = n*factorial(n-1)
    l.release()
    return result

def display(n):
    print("the factorial of",n,"is:",factorial(n))

t1 = Thread(target=display,args=(5,))
t2 = Thread(target=display,args=(9,))
t1.start()
t2.start()
