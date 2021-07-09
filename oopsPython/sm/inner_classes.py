## how to access members of one class inside another class
# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.eno = eno
#         self.ename = ename
#         self. esal = esal
#     def display(self):
#         print("enter employee no:",self.eno)
#         print("enter employee name:",self.ename)
#         print("enter employee salary:",self.esal)

# class Test:
#     def modify(emp):
#         emp.esal = emp.esal + 10000
#         emp.display()

# e = Employee(879320,"shubham",70000)
# Test.modify(e)

# class Outer:
#     def __init__(self):
#         print("outer class object creation....")
#     # def m2(self):
#     #     print("outer class method")
#     class Inner:
#         def __init__(self):
#             print("inner class object creation....")
#         def m1(self):
#             print("inner class method")
# o = Outer()
# i = o.Inner()
# i.m1()

# i = Outer().Inner()
# i.m1()

# Outer().Inner().m1()

# o = Outer()
# i = o.Inner()
# i.m1()
# i.m2()

## example

class Person:
    def __init__(self):
        self.name = "shubham" 
        self.dob = self.DOB()
    def display(self):
        print("name:",self.name)
        self.dob.display()

    class DOB():
        def __init__(self):
            self.dd = 14 
            self.mm = 11 
            self.yyyy = 1994
        def display(self):
            print("DOB: {}/{}/{}".format(self.dd,self.mm,self.yyyy))
p = Person()
p.display()


