## Nested Class
# class Human:
#     def __init__(self):
#         self.name = "shubham"
#         self.head = self.Head()
    
#     def display(self):
#         print("name:",self.name)
#         self.head.talk()
#         self.head.brain.think()

#     class Head:
#         def __init__(self):
#             self.brain = self.Brain()
        
#         def talk(self):
#             print("talking....")
        
#         class Brain:
#             def think(self):
#                 print("thinking.....")
    
# h = Human()
# h.display()


## Nested Method
class Test:
    def m1(self):
        def op(a,b):
            print("first argument",a)
            print("second argument",b)
            print("the sum:",a+b)
            print("the product:",a*b)
            print("*"*20)
        op(10,2)
        op(10,20)
        op(10,200)

t = Test()
t.m1()