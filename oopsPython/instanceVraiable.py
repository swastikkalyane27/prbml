class Test:
    def __init__(self):
         self.a=10      #instance variable
         self.b=20      #instance variable
         self.c=30     #instance variable
    def method(self):
        self.d=32     #instance variable(inside class we can use self )
t=Test()
print(t.__dict__)
t.f=23   #instance variable(outside of class we can use object ref.)
print(t.__dict__)
t.method()  #calling method
print(t.__dict__)    # by using objectref.__dict__ we can check all instance variable

# we can del instance variable
# inside class
#     del self.variablename
# outside class
#     del objectref.variablename

class A:
    def __init__(self):
         self.a=10
         self.b=20
         self.c=30
         del self.c     #inside class
    def method(self):
        self.d=32
        del self.a   #inside class

a=A()
a.method()
del a.d           #outside class
print(a.__dict__)   # by using objectref.__dict__ we can check all instance variable