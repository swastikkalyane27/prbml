## composition (HAS - A Relationship)
# example 1 by using class name
# class Engine:
#     a = 10
#     def __init__(self):
#         self.b = 20
    
#     def m1(self):
#         print("Engine Specific Functionality")

# class Car:
#     def __init__(self):
#         self.engine = Engine()
#     def m2(self):
#         print("class car using Engine class Functionality")
#         # print(self.engine.a)
#         # print(self.engine.b)
#         # self.engine.m1()
#         # print(Engine.a)
#         # print(Engine.b)
#         # Engine.m1(self.engine)

# c = Car()
# c.m2()


# example 2 by creating object
# class Car:
#     def __init__(self,name,model,colour):
#         self.name = name
#         self.model = model
#         self.colour = colour
#     def m1(self):
#         print("car name: {},model: {},colur: {}".format(self.name,self.model,self.colour))

# class Employee:
#     def __init__(self,ename,eno,car):
#         self.ename = ename
#         self.eno = eno
#         self.car = car
#     def disp(self):
#         print("employee name:",self.ename)
#         print("employee no:",self.eno)
#         self.car.m1()

# c = Car("Honda","Petrol","Black")
# e = Employee("shubham",1000,c)
# e.disp()


## example 3 
# class X:
#     a = 10
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         print("m1 method in X class")

# class Y:
#     c = 30 
#     def __init__(self):
#         self.d = 40
#     def m2(self):
#         print("m2 method of Y class")
#     def m3(self):
#         x1 = X()
#         print(x1.a)
#         print(x1.b)
#         x1.m1()
#         print(self.c)
#         print(self.d)
#         self.m2()
#         print("m3 method of Y class")

# y = Y()
# y.m3()


## Inheritance (IS - A Relationship)
# example 1
# class P:
#     a = 10 
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         print("parent class instyance method")

#     @classmethod
#     def m2(cls):
#         print("parent class method")

#     @staticmethod   
#     def m3():
#         print("parent class static method")

# class C(P):
#     pass

# c = C()
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()

# example 2
# class P:
#     a = 10
#     def __init__(self):
#         self.b = 20 

# class C(P):
#     c = 30 
#     def __init__(self):
#         super().__init__()
#         self.d = 40

# c = C()
# print(c.a,c.b,c.c,c.d)


# example 3
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def eat_n_drink(self):
#         print("eat biryani and drink beer")

# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno = eno
#         self.esal = esal

#     def work(self):
#         print("coding python")
    
#     def empinfo(self):
#         print("employee name:",self.name)
#         print("employee age:",self.age)
#         print("employee number:",self.eno)
#         print("employee salary:",self.esal)

# e = Employee("shubham",25,101,10000)
# e.eat_n_drink()
# e.work()
# e.empinfo()


## using both HAS-A and IS-A Relationship
# class Car:
#     def __init__(self,name,model,colour):
#         self.name = name
#         self.model = model
#         self.colour = colour
#     def getinfo(self):
#         print("\tcar name: {},car model: {},car colour: {}".format(self.name,self.model,self.colour))

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def eat_n_drink(self):
#         print("eat biryani and drink beer")

# class Employee(Person):
#     def __init__(self,name,age,eno,esal,car):
#         super().__init__(name,age)
#         self.eno = eno
#         self.esal = esal
#         self.car = car

#     def work(self):
#         print("coding python")
    
#     def empinfo(self):
#         print("employee name:",self.name)
#         print("employee age:",self.age)
#         print("employee number:",self.eno)
#         print("employee salary:",self.esal)
#         print("car info:")
#         self.car.getinfo()

# c = Car("hyundai","i20","black")
# e = Employee("shubham",25,101,10000,c)
# e.eat_n_drink()
# e.work()
# e.empinfo()







