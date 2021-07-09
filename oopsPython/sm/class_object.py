# class Mobile:
#   def __init__(self):
#     self.model = "samsung m21"
#     self.platform = "android"
#   def show_details(self):
#     print("Model:",self.model)
#     print("Platform:", self.platform)

# a = Mobile()
# b = Mobile()
# print(a)
# print(b)
# print(a.model)
# print(a.platform)
# a.show_details()

# class Mobile:
#   def __init__(self):
#     self.model = "samsung M21"
#     self.platform = "android"
#
#   def show(self):
#     print("Model:",self.model,"\nPlatform:",self.platform)
#
# a = Mobile()
# print(a.model)
# print(a.platform)
# a.show()
#
# a.model = "RealMe X"
# a.platform = "os"
# print(a.model)
# print(a.platform)
# a.show()

# class Mobile:
#   def __init__(self,m,pf):
#     self.model = m
#     self.platform = pf
#
#   def show(self,p):
#     price = p
#     print("Model:",self.model,"\nPlatform:",self.platform,"\nPrice:",price)
#
# a = Mobile("Samsung M21","android")
# a.show(16000)

# class Mobile:
#   def __init__(self,m,pf):
#     self.model = m
#     self.platform = pf
#
#   def show(self,p):
#     price = p
#     print("Model:",self.model,"\nPlatform:",self.platform,"\nPrice:",price)

# a = Mobile("Samsung M21","android")
# a.show(16000)
# print(id(a))
# print()

# b = Mobile("one plus","OS")
# b.show(50000)
# print(id(b))
# print()
#
# c = Mobile("Redmi","MIUI")
# c.show(18000)
# print(id(c))

# a1 = Mobile("Samsung M21","android")
# a1.show(16000)
# print(id(a1))

# def calc_sum(n):
#     if n ==1:
#         return 1
#     else:
#         return n*n + calc_sum(n-1)*calc_sum(n-1)
# sum = calc_sum(3)
# print(sum)

# class Demo:
#     def __init__(x,nm):
#         x.y = "alexa"
#         print("hello ",x.y)
# d = Demo(nm="siri")
