## hybrid inheritance
class A:
    def m1(self):
        print("A class method")
class B(A):pass
    # def m1(self):
    #     print("B class method")
class C(A):pass
    # def m1(self):
    #     print("C class method")
class D(B,C):pass
    # def m1(self):
    #     print("D class method")

d = D()
d.m1()




# class Class1: 
#     def m(self): 
#         print("In Class1") 

# class Class2(Class1): 
#     def m(self): 
#         print("In Class2") 
#         super().m() 

# class Class3(Class1): 
#     def m(self): 
#         print("In Class3") 
#         super().m() 

# class Class4(Class2, Class3): 
#     def m(self): 
#         print("In Class4")    
#         super().m() 

# obj = Class4() 
# obj.m()



# class Animal:
#   def __init__(self, Animal):
#     print(Animal, 'is an animal.')

# class Mammal(Animal):
#   def __init__(self, mammalName):
#     print(mammalName, 'is a warm-blooded animal.')
#     super().__init__(mammalName)
    
# class NonWingedMammal(Mammal):
#   def __init__(self, NonWingedMammal):
#     print(NonWingedMammal, "can't fly.")
#     super().__init__(NonWingedMammal)

# class NonMarineMammal(Mammal):
#   def __init__(self, NonMarineMammal):
#     print(NonMarineMammal, "can't swim.")
#     super().__init__(NonMarineMammal)

# class Dog(NonMarineMammal, NonWingedMammal):
#   def __init__(self):
#     print('Dog has 4 legs.')
#     super().__init__('Dog')
    
# d = Dog()
# print('')
# bat = NonMarineMammal('Bat')