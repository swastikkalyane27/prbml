## Thread synchronization
## Lock
# from threading import *
# import time
# l = Lock()
# def wish(name):
#     l.acquire()
#     for i in range(3):
#         print("Good Evening:",end= "")
#         time.sleep(2)
#         print(name)
#     l.release()
# t1 = Thread(target=wish,args=("dhoni",))
# t2 = Thread(target=wish,args=("kohli",))
# t1.start()
# t2.start()
# time.sleep(25)
# print("main thread wont require the lock")
# print(t1.is_alive())




# import threading
# import time
# from random import randint                 
# class SharedCounter(object):
  
#     def __init__(self, val = 0):
#         self.lock = threading.Lock()
#         self.counter = val
        
#     def increment(self):
#         print("Waiting for a lock")
#         self.lock.acquire()
#         try:
#             print('Acquired a lock, counter value: ', self.counter)
#             self.counter = self.counter + 1
#         finally:
#             print('Released a lock, counter value: ', self.counter)
#             self.lock.release()

# def task(c):
#     # picking up a random number
#     r = randint(1,5)
#     # running increment for a random number of times
#     for i in range(r):
#       c.increment()
#     print('Done')

# if __name__ == '__main__':
#     sCounter = SharedCounter()

#     t1 = threading.Thread(target=task, args=(sCounter,))
#     t1.start()
    
#     t2 = threading.Thread(target=task, args=(sCounter,))
#     t2.start()

#     print('Waiting for worker threads')
#     t1.join()
#     t2.join()
    
#     print('Counter:', sCounter.counter)



## RLock
# from threading import *
# l = RLock()
# print("Main thread acquire lock")
# l.acquire()
# print("Main thread acquire lock again")
# l.acquire()
# print("Main thread acquire same lock")




# from threading import *
# import time
# l = RLock()
# def factorial(n):
#     l.acquire()
#     if n == 0:
#         result = 1
#     else:
#         result = n*factorial(n-1)
#     l.release()
#     return result

# def results(n):
#     print("the factorial of",n,"is:",factorial(n))

# t1 = Thread(target=results,args=(5,))
# t2 = Thread(target=results,args=(9,))
# t1.start()
# t2.start()




## semaphore
# from threading import *
# import time
# s = Semaphore()
# def wish(name):
#     s.acquire()
#     for i in range(3):
#         print("good morning:",end="")
#         time.sleep(2)
#         print(name)
#     s.release()

# t1 = Thread(target=wish,args=("Dhoni",))
# t2 = Thread(target=wish,args=("Kohli",))
# t3 = Thread(target=wish,args=("Rohit",))
# t4 = Thread(target=wish,args=("Raydu",))
# t5 = Thread(target=wish,args=("Dravid",))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()



# from threading import *
# s = Semaphore(2)
# s.acquire()
# s.acquire()
# s.release()
# s.release()
# s.release()
# s.release()
# s.release()
# print("end")




## Bounded semaphore
# from threading import *
# s = BoundedSemaphore(2)
# s.acquire()
# s.acquire()
# s.release()
# s.release()
# s.release()
# print("end")




# import os, re, threading

# class ip_check(threading.Thread):
#    def __init__ (self,ip):
#       threading.Thread.__init__(self)
#       self.ip = ip
#       self.__successful_pings = -1
#    def run(self):
#       ping_out = os.popen("ping -q -c2 "+self.ip,"r")
#       while True:
#         line = ping_out.readline()
#         if not line: break
#         n_received = re.findall(received_packages,line)
#         if n_received:
#            self.__successful_pings = int(n_received[0])
#    def status(self):
#       if self.__successful_pings == 0:
#          return "no response"
#       elif self.__successful_pings == 1:
#          return "alive, but 50 % package loss"
#       elif self.__successful_pings == 2:
#          return "alive"
#       else:
#          return "shouldn't occur"
# received_packages = re.compile(r"(\d) received")

# check_results = []
# for suffix in range(20,70):
#    ip = "192.168.178."+str(suffix)
#    current = ip_check(ip)
#    check_results.append(current)
#    current.start()

# for el in check_results:
#    el.join()
#    print ("Status from ", el.ip,"is",el.status())