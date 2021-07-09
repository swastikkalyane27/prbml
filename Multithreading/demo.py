
#Thread identification Number(ident):




# from threading import *
# def info():
# 	print("child Thread")
# t = Thread(target=info)
# t.start()

# print("Main Thread identification number:",current_thread().ident)
# print("Child Thread identification number:",t.ident)     






#---------------------------------------------------------------------------------------------------------




# active_count()


# from threading import *
# import time

# def info():
# 	print(current_thread().name,"started....")
# 	time.sleep(4)
# 	print(current_thread().name,"ended...")
# print("Current active count:",active_count())
# t1 = Thread(target=info,name="child thread 1")
# t2 = Thread(target=info,name="child thread 2")
# t3 = Thread(target=info,name="child thread 3")
# t1.start()
# t2.start()
# t3.start()
# print("Current active count:",active_count())
# time.sleep(1)	
# print("Current active count:",active_count())







#---------------------------------------------------------------------------------------------------------






#enumerate() function:

# from threading import *
# import time
# def info():
# 	print(current_thread().name,"started....")
# 	time.sleep(4)
# 	print(current_thread().name,"ended...")
# t1=Thread(target=info,name="child thread 1")
# t2=Thread(target=info,name="child thread 2")
# t3=Thread(target=info,name="child thread 3")
# t1.start()
# t2.start()
# t3.start()
# time.sleep(4)
# l=enumerate()
# print(l)
# for t in l:
#   	print("name",t.name)
# l=enumerate()
# print(l)
# for t in l:
#   	print("name",t.name)    
# time.sleep(10)
# l=enumerate()
# for t in l:
#   	print("name",t.name)






#---------------------------------------------------------------------------------------------------------





# isAlive():


# from threading import *
# import time
# def info():
# 	print(current_thread().name,"started....")
# 	time.sleep(4)
# 	print(current_thread().name,"ended...")
# t1=Thread(target=info,name="child thread 1")
# t2=Thread(target=info,name="child thread 2")
# t3=Thread(target=info,name="child thread 3")
# t1.start()
# t2.start()
# t3.start()
# print(t1.name,'isAlive:',t1.isAlive())
# print(t2.name,'isAlive:',t2.isAlive())
# print(t3.name,'isAlive:',t3.isAlive())













# from threading import *
# import time
# def info():
# 	print(current_thread().name,"started....")
# 	time.sleep(4)
# 	print(current_thread().name,"ended...")
# t1=Thread(target=info,name="child thread 1")
# t2=Thread(target=info,name="child thread 2")
# t3=Thread(target=info,name="child thread 3")
# t1.start()
# t2.start()
# t3.start()
# print(t1.name,'is Alive:',t1.is_alive)
# print(t2.name,'is Alive:',t2.is_alive)
# print(t3.name,'is Alive:',t3.is_alive)
# time.sleep(6)
# print(t1.name,'is Alive:',t1.is_alive)
# print(t2.name,'is Alive:',t2.is_alive)
# print(t3.name,'is Alive:',t3.is_alive)




#-------------------------------------------------------------------------------------




# join() method:




# from threading import *
# import time
# def info():
#   for i in range(3):
#     print(" A Thread")
#     #time.sleep(2)
# def info2():
#   for i in range(5):
#     print(" B Thread")
#     #time.sleep(2)

# t=Thread(target=info)
# t1=Thread(target=info2)
# t.start()
# t.join()
# t1.start()
# t1.join()

# for i in range(3):
#   print(" B Thread coming ")





#-------------------------------------------------------------------------------------




# Deamon Threads:


# from threading import *
# print(current_thread().isDaemon())
# current_thread().setDaemon(True)
# print(current_thread().isDaemon())




#--------------------------------------------------------------------------------------------------------




# Default nature:



# from threading import *
# import time
# def job():
#   print("child thread")

# t=Thread(target=job)  # main thread is parent and t child  
# print(t.daemon)

# t.start()
# t.setDaemon(True)
# print(t.daemon)





