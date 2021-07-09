# '''in py oops there is no overloding concept ,
# if it happend then it will simply overwrite first one and it
#     will conssider leatest contructor'''
class Test:
    def __init__(self):
        print("no arg")
    def __init__(self):
        print("one arg two")
    def m1(self):
        print("method")
    def m1(self):
        print("methon one two ")
t1=Test()
t1.m1()