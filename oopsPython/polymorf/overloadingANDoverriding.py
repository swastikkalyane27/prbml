# method overloading
# class Add():
#     def sum1(self,a,b,c):
#         s = a + b + c
#         print(s)
#     def sum1(self,a,b):
#         s = a + b
#         print(s)
#     def sum1(self):
#         print('no argument')
#
# o = Add()
# o.sum1(10,20,3)



#
# class Myclass:
#     def sum(self, a=None, b=None, c=None):
#         if a != None and b != None and c != None:
#             s = a + b + c
#         elif a != None and b != None:
#             s = a + b
#         else:
#             s = 'Provide at least Two Numbers'
#         return s
#
#
# obj = Myclass()
# print(obj.sum())

# method overiding

# class Add():
#     def sum1(self,**a):
#         s = 0
#         for x in a.values():
#             s += x
#         print(s)
# b = Add()
# b.sum1(b=10,c=20,d=30,e=40)


# class Add:
#     def result(self, a, b):
#         print('Addition:', a + b)
#
#
# class Multi(Add):
#     def result(self, a, b):
#         print('Multiplication:', a * b)
# #
# #
# m = Multi()
# m.result(10, 20)

# m = Add()
# m.result(10, 20)


class Add:
    def result(self, a, b):
        print('Addition:', a + b)


class Multi(Add):
    def result(self, a, b):
        super().result(a, b)  # Calling Parent Class's Method
        print('Multiplication:', a * b)


m = Multi()
m.result(10, 20)