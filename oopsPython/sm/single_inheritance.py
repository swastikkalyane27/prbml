## single inheritance
class Parent:
    def __init__(self):
        self.a = 10
    def m1(self):
        print("parent method")
class Child(Parent):
    def __init__(self):
        print("hiiiii")
    def m2(self):
        print("child method")

c = Child()
c.m1()
c.m2()