## constructor overriding
# Example 1
# class P:
#     def __init__(self):
#         print("parent constructor")
#
# class C(P):
#     def __init__(self):
#         super().__init__()
#         print("child constructor")
#
# obj = C()




#Example 2
# class Parent(object):
#     def __init__(self, a, **b):
#         print ('a', a)
#         print ('b', b)
#         print(type(a))
# class Child(Parent):
#     def __init__(self, c, d, *args,**s):
#         print ('c', c)
#         print ('d', d)
#         super(Child, self).__init__(*args,**s)
#
# test = Child(1,2,3,s=3,e=5)