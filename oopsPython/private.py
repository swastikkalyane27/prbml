# class Com:
#     def __init__(self):
#         self.__maxprice=900
#     def m1(self):
#         print('price;-',self.__maxprice)
#     def setmaxprice(self,price):    #we can not set from outside bcz maxprice is private variable
#         self.__maxprice=price
# c=Com()
# c.m1()
# c.setmaxprice(1000)
# c.m1()

class A():
   def __init__(self):
        self.name = "Tony Stark"

class B():
   def __init__(self):
        self.name = "Steve Rogers"

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

c1=C()
print(c1.name)