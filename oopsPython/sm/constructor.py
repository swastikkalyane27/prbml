# class Student():
#     def __init__(self):
#         print("constructor is called")

# s = Student()
# s = Student()
# s = Student()

class Mobile():
    def __init__(self):
        print("first constructor is called")

    def __init__(self,x):
        print("second constructor is called")

a = Mobile()
a = Mobile("shubham")