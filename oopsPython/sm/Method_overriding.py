## Method overriding
# Example 1

# class Parent():
#     def __init__(self):
#         self.value = "Inside Parent"
#
#     def show(self):
#         print(self.value)
#
# class Child(Parent):
#     def __init__(self):
#         self.value = "Inside Child"
#
#     def show(self):
#         print(self.value)
#
# obj1 = Parent()
# obj2 = Child()
# obj2.show()
# obj1.show()


# Example 2 using multiple inheritance

# class Parent1():
#     def show(self):
#         print("Inside Parent1")
#
# class Parent2():
#     def display(self):
#         print("Inside Parent2")
#
# class Child(Parent1, Parent2):
#     def show(self):
#         print("Inside Child")
#
# obj = Child()
#
# obj.show()
# obj.display()


# Example 3 using multilevel inheritance

# class Parent():
#     def display(self):
#         print("Inside Parent")
#
# class Child(Parent):
#     def show(self):
#         print("Inside Child")
#
# class GrandChild(Child):
#     def show(self):
#         print("Inside GrandChild")
#
# g = GrandChild()
# g.show()
# g.display()


# Example 4

# class Parent():
#
#     def show(self):
#         print("Inside Parent")
#
# class Child(Parent):
#
#     def show(self):
#         Parent.show(self)
#         print("Inside Child")
#
# obj = Child()
# obj.show()

# Example 5 using super

# class Parent():
#
#     def show(self):
#         print("Inside Parent")
#
# class Child(Parent):
#
#     def show(self):
#         super().show()
#         print("Inside Child")
#
# obj = Child()
# obj.show()


class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)

class GFG2(GFG1):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG2:', b)
        super().sub_GFG(b + 1)

class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)
gfg = GFG3()
gfg.sub_GFG(10)