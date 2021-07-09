
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("hi",self.name)
#         print("your markd is",self.marks)
# s=Student('swastik',100)
# print(s.name)
# s.display()

class Student:
    def setname(self,name):     # used only for single variable
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        '''we can write some validation code'''          # in constructor we can not write validation code
        return self.marks
    def display(self):
        print('hi',)
n=int(input('enter no of student :- '))
for i in range(n):
    name=input('enter name:- ')
    marks=int(input('enter marks :-'))
    s=Student()
    print(id(s))
    s.setname(name)
    s.setmarks(marks)
    print('hi',s.getname())
    print('your marks is:- ',s.getmarks())
    print("*"*10)

# # exaple 3:

# class Test:
#     def __init__(self):
#         self.var = 10
#         self._var1 = 11
#         self.__var2 = 12
#     def setter__var2(self,num):
#         self.__var2 = num
#     def get__var2(self):
#         return self.__var2
#     def fun1(self):
#         print(self.var)
#         print(self._var1)
#         print(self.__var2)
#     def __fun2(self):      # we can access private methid in same class only , not in child class also
#         print(self.var)
#         print(self._var1)
#         print(self.__var2)

# t=Test()
# t.setter__var2(19)
# t.fun1()

#
# # example :
# 'Using property() function to achieve getters and setters behaviour'''
#
#
# # Python program showing a
# # use of property() function
#
# class Test:
#     def __init__(self):
#         self.__age = 0       # we can do this for protected variable also
#
#
#     # function to get value of _age
#     def get__age(self):
#         print("getter method called")
#         return self.__age
#
#     # function to set value of _age
#     def set__age(self, a):
#         print("setter method called")
#         self.__age = a
#
#     # function to delete _age attribute
#     def del__age(self):
#         print('DEL METHOD C')
#         del self.__age
#
#     num = property(get__age, set__age, del__age)   # age as num we should call any action with num regarding age
#
#
# mark = Test()
#
# mark.num = 10
#
# print(mark.num)
# del mark.num

#
# # Using @property decorators to achieve getters and setters behaviour
#
# # Python program showing the use of
# # @property
#
# class Test:
#     def __init__(self):
#         self._age = 0
#
#     # using property decorator
#     # a getter function
#     @property
#     def get1(self):
#         print("getter method called")
#         return self._age
#
#     # a setter function
#     @get1.setter       # to take decorater name as @getterMethodName.setter  for setter
#     def set1(self, a):
#         if (a < 18):
#             raise ValueError("Sorry you age is below eligibility criteria")      #validation code
#         print("setter method called")
#         self._age = a
# mark = Test()
# mark.set1 = 19
# print(mark.get1)
