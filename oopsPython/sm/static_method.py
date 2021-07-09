## Static Method
# class Test:
#     def __init__(self):
#         self.a = 5
#         self.b = "shubham"

#     def operations(x,y):
#         print('the sum',x+y)
#         print('the product',x*y)

# t = Test()
# t.operations(10,2)
# Test.operations(10,2)


# class Test:
#     def m1():
#         print('some method')

# t = Test()
# t.m1()


# class Test:
#     def m1():
#         print('some method')

# Test.m1()


# class Test:
#     @classmethod
#     def m1(cls):
#         print('some method')

# # t = Test()
# # t.m1()
# Test.m1()

# class Test:
#     def m1(x):
#         print('some method',x)

# t = Test()
# t.m1(10)




## prob
def add(c,k):
    c.test=c.test+1
    print(c)
    k=k+1
    print("add k",k)

class A:
    def __init__(self):
        self.test = 0
def main():
    Count=A()
    print(Count)
    k=0
 
    for i in range(0,25):
        add(Count,k)
    print("Count.test=", Count.test)
    print("k =", k)
main()

# a) Exception is thrown
# b) Count.test=25
#    k=25
# c) Count.test=25
#    k=0
# d) Count.test=0
#    k=0

# class Employee:
#     def __init__(self):
#         print("object creatation")

#     def __del__(self):
#         print("destructive method called")

# obj = Employee()
# del obj