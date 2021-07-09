#how to access member of one class to other
# class Employee:
#     def __init__(self,eno,esal,ename):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#     def display(self):
#         print('employee name :- ',self.ename)
#         print("employee no :- ",self.eno)
#         print('employee sal :- ',self.esal)
# class test:
#     def modify(emp):
#         emp.esal=emp.esal+1000
#         emp.display()
# e=Employee(123,10000,'swastik')
# test.modify(e)
#
#
#inner class
#
# class outer:
#     def __init__(self):
#         print('constructor of outer class')
#     class inner:
#         def __init__(self):
#             print("contructor of inner class")
#         def m1(self):
#             print('method1 of inner class')
#
# '''to call m1 we have to create two object one foe outer class and second one is for inner class by
# using outer class object'''
# o=outer()
# i=o.inner()
# i.m1()
# aslo we can call by this way
# o=outer().inner().m1()
#aslo we can call by this way
# o=outer().inner()
# o.m1()


class person:
    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        self.dob=self.DOB(dd,mm,yyyy)
    def display(self):
        print('name:- ',self.name)
        self.dob.display()
    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy

        def display(self):

            print('DOB :-{}\{}\{}'.format(self.dd,self.mm,self.yyyy))

p=person('swastik',27,5,1996)
p.display()
p.dob.display()