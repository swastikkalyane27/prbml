class A:
    def __init__(self):
        print('constructror of class A')
    def m1(self):
        print("method 1 in class A")
class B:
    def __init__(self):
        self.obj_a=A()
        print("constructor of class B")
    def m1(self):
        self.obj_a=obj_a.m1()
        print("method 1 of class B")
obj_a=A()
obj_a.m1()
print("*"*10)
obj_b=B()
obj_b.m1()