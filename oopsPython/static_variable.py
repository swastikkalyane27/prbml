class Test:
    cname="swastik"     #inside class but outside of any method directly we can declear
    def __init__(self):
        Test.b=20        #inside constructor method we can declear by class name
    def method(self):
        Test.c=30         #inside instance method we can declear by class name
    @classmethod
    def m2(cls):
        cls.d=40        #inside class method we can declear by using class name or cls variable
        Test.f=50
    @staticmethod
    def m2():
        Test.g=26       #inside static method we can declear by class name
a=Test()
Test.k=87       # outside the class also we declear by using class name
print(Test.__dict__)
''' by using classname.__dict__ we can check all static variable; and if we call other method
before this then only static variable  in that method wiil be print on terminal otherwise not'''


#how to access static variable and modify
class Test:
    x=10
    def __init__(self):
        print("constructor")
        print(Test.x)   #inside constructor :- by using classname or self
        print(self.x)
    def m1(self):
        print("m1")
        print(Test.x)     #inside instance method :- by using classname or self
        print(Test.x)
    @classmethod
    def m2(cls):
        print("cls method")
        print(Test.x)       #inside classmethod:- by using class name or cls variable
        print(cls.x)
    @staticmethod
    def m3():
        print("static")
        print(Test.x)    #inside statict:- by using class name only
t=Test()
print(Test.x)   #outside class :-by using class name only

