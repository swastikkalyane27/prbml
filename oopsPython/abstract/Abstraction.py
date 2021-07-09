# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon():

    @abstractmethod
    def sides(self):
        print("abstract method")

class Triangle(Polygon):


	def sides(self):
		print("I have 3 sides")

class Pentagon(Polygon):


	def sides(self):
		print("I have 5 sides")

class Hexagon(Polygon):


	def sides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):


	def sides(self):
		print("I have 4 sides")


R = Triangle()
R.sides()

K = Quadrilateral()
K.sides()

R = Pentagon()
R.sides()

K = Hexagon()
K.sides()

obj=Polygon()
obj.sides()
