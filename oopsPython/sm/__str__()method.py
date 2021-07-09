# __str__() Method:

# class Student:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#
#     def __str__(self):
#         return "this is a Student with name {} and rollno {}".format(self.name,self.rollno)
#
#
# s1 = Student("shubham",101)
# s2 = Student("akshay",102)
# print(s1)
# print(s2)



# ## __str__() VS __repr__()
# import datetime
# #from datetime import datetime
# now = datetime.datetime.now()
# #now = datetime.now()
# a = now.__str__()
# b = now.__repr__()
# # c = eval(a)
# d = eval(b)
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))





class Account:
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,amount):
        self.balance =self.balance + amount

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
        else:
            print("Sorry, insufficient balance")

    def print_statement(self):
        print("Account balance:",self.balance)

class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = -1000 )

    def __str__(self):
        return "{}'s Current Account balance: {}".format(self.name,self.balance)

class Saving(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = 0 )

    def __str__(self):
        return "{}'s Saving Account balance: {}".format(self.name,self.balance)

c = Current("shubham",10000)
print(c)
c.deposit(10000)
print(c)
c.withdraw(20900)
print(c)

s = Saving("shubham",10000)
print(s)
s.deposit(5000)
print(s)
s.withdraw(16000)
print(s)





