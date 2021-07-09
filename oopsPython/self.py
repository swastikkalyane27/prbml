class employee:
    '''doc string(discription about class)'''
    def __init__(self,eno,ename,esal,eadd):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eadd=eadd
    def info(self):
        # print("employee number:",eno)    '''normally we do this to acces but here not possible it raise error'''
        # print("employee name:",ename)    #bcz here we initilize by self which give reference
        # print("employee sallary:",esal)  #so we have to access by using self.argument only
        # print("employee add:",eadd)
        print("#"*10)
        print("employee number:", self.eno)
        print("employee name:", self.ename)
        print("employee sallary:", self.esal)
        print("employee add:", self.eadd)
        print(id(self))                         #line 18
e1=employee(100,"swastik",100000,"lATUE")
e2=employee(200,"raj",200000,"nanded")
e1.info()
e2.info()
print(employee.__doc__)       #'''to print doc string'''
print(employee.__dict__)
help(employee)
print(employee.__weakref__)
# sefl is pointing to current object( e1,e2) current==leatest
print(id(e1),id(e2)) #line 18
