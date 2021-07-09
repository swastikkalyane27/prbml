## Abstract method
from abc import *
# class Vehicle:
#     @abstractmethod
#     def get_no_of_wheels(self):
#         pass
#
# Abstract class
# hierarchical
# class Vehicle(ABC):
#     @abstractmethod
#     def get_no_of_wheels(self):
#         pass
#
# class Bus(Vehicle):
#     def get_no_of_wheels(self):
#         return 7
#
# class Auto(Vehicle):
#     def get_no_of_wheels(self):
#         return 3
#
# b = Bus()
# a = Auto()
# print(b.get_no_of_wheels())
# print(a.get_no_of_wheels())
#

# multilevel
# class P(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#
#     @abstractmethod
#     def m2(self):
#         pass
#
# class C(P):
#     def m1(self):
#         print("m1 implementation")
#
# class CC(C):
#     def m2(self):
#         print("m2 implementation")
#
# a = CC()
# a.m1()
# a.m2()


# class P(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#
#     def m2(self):
#         print("m2 normal method")
#
# class C(P):
#     def m1(self):
#         print("m1 implementation")
#
# c = C()
# c.m1()
# c.m2()



# from abc import *
# class Shape():
#    @abstractmethod
#    def area(self):
#       pass
#
# class Rectangle(Shape):
#    def __init__(self, x,y):
#       self.l = x
#       self.b=y
#
#    def area(self):
#       return self.l*self.b
#
# r = Rectangle(10,20)
# print ('area: ',r.area())







# import abc
# from abc import ABC, abstractmethod
#
#
# class parent(ABC):
#     @abc.abstractproperty
#     def geeks(self):
#         return "parent class"
#
#
# class child(parent):
#
#     @property
#     def geeks(self):
#         return "child class"
#
#
# try:
#     r = parent()
#     print(r.geeks)
# except Exception as err:
#     print(err)
#
# r = child()
# print(r.geeks)



## Interface
# from abc import *
# class DBinterface(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
# class Oracle(DBinterface):
#     def connect(self):
#         print("connecting to oracle database")
#
#     def disconnect(self):
#         print("disconnecting from oracle database")
#
# class Mysql(DBinterface):
#     def connect(self):
#         print("connecting to Mysql database")
#
#     def disconnect(self):
#         print("disconnecting from Mysql database")
#
# o1 = Oracle()
# o1.connect()
# o1.disconnect()
#
# o2 = Mysql()
# o2.connect()
# o2.disconnect()
