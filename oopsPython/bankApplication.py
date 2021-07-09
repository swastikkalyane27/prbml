import sys
class BankOp:
    '''coustemer releated operaion class'''
    Bname="swastikbank"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposite(self,amt):
        self.balance=self.balance+amt
        print("banl balance after deposite :-",self.balance)
    def withdraw(self,amt):
        self.balance=self.balance-amt
        print("bank balance after withdraw :-",self.balance)
    def ministatment(self):
        print("your bank balance is",self.balance)

print('welcome to ',BankOp.Bname)
name=input("enter your name\n")
balance=float(input('enter your current balance\n'))
b=BankOp(name,balance)
while True:
    print("chose your option\n d-for deposite\n w-for withdraw \n m-for to check account balance\n e-for exits")
    option=input('enter option\n:-')
    if option=='d' or option=='D':
        amt=float(input("how much ammount you want to deposite\n:-"))
        b.deposite(amt)
    elif option=='w' or option=='W':
        amt=float(input('how much ammount you want to withdraw\n:-'))
        b.withdraw(amt)
    elif option=="e" or option=="E":
        sys.exit()
    elif option=='m' or option=="M":
        b.ministatment()
    else:
        print('CHOOSE VALID OPTION')
