'''Basically, the main purpose of using getters and setters in object-oriented
 programs is to ensure data encapsulation. Private variables in python are 
 not actually hidden fields like in other object oriented languages. Getters and Setters in 
 python are often used when:

1)We use getters & setters to add validation logic around getting and setting a value.
2)To avoid direct access of a class field i.e. private variables cannot be
   accessed directly or modified by external user.'''
# hidindig data behind method ===>> encapuslation
#  advantage ==>>security increase
#  disadvantage ==> lenth increase,readablility down, performance down


# syntax:
#  def setvariableName(self,variableName):
#      self.variableName = variableName
#  def getvariableName(self):
#      return self.variableName
#  e.g :
#  def msetNae(self,name):
#      self.name = name
#  def getname(self):
#     return name



# Using property() function to achieve getters and setters behaviour
'''
In Python property()is a built-in function that creates and returns a property object. A property object 
has three methods,getter(), setter(), and delete(). property() function in Python has
four arguments property(fget, fset, fdel, doc), fget is a function for retrieving 
an attribute value. fset is a function for setting an attribute value. fdel is a function
for deleting an attribute value. doc creates a docstring for attribute. 
A property object has three methods, getter(), setter(), and delete()
to specify fget, fset and fdel individually. For Example
'''

# Using @property decorators to achieve getters and setters behaviour

'''
In previous method we used property() function in order to achieve getters and setters behaviour.
However as mentioned earlier in this post getters and setters are also used for validating 
the getting and setting of attributes value. There is one more way to implement property function 
i.e. by using decorator. Python @property is one of the built-in decorators. The main purpose of any 
decorator is to change your class methods or attributes 
in such a way so that the user of your class no need to make any change in their code.
'''