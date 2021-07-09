class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('name:-',self.name)
        print('age:-',self.age)

class B(A):
    def __init__(self,name,age,rollno,marks):
        self.name = name
        self.age = age
        # super().__init__(name,age)      #(we can write for line 8 and 9 also)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print('name:-',self.name)
        print('age:-',self.age)
        # super().display()           #(17 and 18)
        print('marks:-',self.marks)
        print('rollno:-',self.rollno)
class C(B):
    def __init__(self,name,age,sal,subject):
        self.name=name
        self.age=age
        # super().__init__(name,age,)      # (15 and 16)
        self.sal=sal
        self.subject=subject
    def display(self):
        print('name:-',self.name)
        print('age:-',self.age)
        # super().display()         #(30 and 31)
        print('sallary:-',self.sal)
        print('subject:-',self.subject)
a=A('raj',45)
b=B('ravi',28,)
b.display()


# MULTI LEVEL
class A:
    def m1(self):
        print('method of A')
    def m2(self):
        print("method2 of A")
class B(A):
    def m1(self):
        print("method of B")
    def m3(self):
        print("method3 of B")
class C(B):
    def m1(self):
        print("method of C")
class D(C):
    def m1(self):
        print('method of D')
class E(D):
    def m1(self):
        print("method of E")
        # super(C,self).m2()     #we caan call any parent class by using super
e=E()
e.m1()
e.m2()
e.m3()

