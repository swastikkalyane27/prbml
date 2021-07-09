# class Rectangle:
#     __length = 0
#     __breadth=0
#     def __init__(self): #constructor
#      self.__length = 5
#      self.__breadth = 3
#      print(self.__length)
#      print(self.__breadth)
#
#
# rec = Rectangle()
# print(rec.__length)
# print(rec.__breadth)



class Computer:

    def __init__(self):
        self.__maxprice = 900
        # self.__maxprice=1300

    def sell(self):
        print("Selling Price:",self.__maxprice)

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
# c.__maxprice=1000
# c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()