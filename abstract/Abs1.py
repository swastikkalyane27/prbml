# # Python program invoking a
# # method using super()
#
# import abc
# from abc import ABC, abstractmethod
#
# class R(ABC):
#
# 	def show(self):
# 		print("Abstract Base Class")
# 	@abstractmethod
# 	def m1(self):
# 	 pass
#
# class S(R):
# 	def show(self):
# 		super().show()
# 		print("subclass ")
#
# # Driver code
# r = S()
# r.show()
# Python program showing
# implementation of abstract
# class through subclassing

from abc import ABC,abstractmethod

class parent(ABC):
	@abstractmethod
	def geeks(self):
		pass

class child(parent):
	def geeks(self):
		print("child class")

# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))
