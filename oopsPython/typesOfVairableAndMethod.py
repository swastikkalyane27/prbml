'''
1)instance varaible :-a)the varaible which are declaired by using self
b)the value of instance variable varies from object to object ,c) for every object saperate instatnce variable
copy is created
2)static variable :-also khown as class level variable ,b) for all object only one static variable copy
which sheared to every objrct ,c) id of static variable for all object is same
3)local variable :-declaire inside the method for temporary requirement ,b) scope of local variable is only
 up to method
# '''
# class Employ:
#     ecompony='IBM'  #static variable
#     def __init__(self,eno,ename,esal):
#         count=0            #local variable
#         self.eno=eno       #instance variable
#         self.ename=ename    #instance variable
#         self.esal=esal      #instance variable
#     def info(self):
#         a=10    #local variable
#         print('employ name:',self.ename)
# e1=Employ(100,"swastik",100000)
# e2=Employ(200,"raj",200000)
# e1.info()
# e2.info()
# print(Employ.ecompony)
#


'''
METHOD:
1) instatce method :-related to object only; b)access instance variable ; c)(self) argument must be require; 
d)call it by OBJECT ref. only
2) class method  :-class related data; b)for every class one class method is there ;c) we can create class method 
    by using decorator @classmethod and (cls) argument ;d) we should call class method only by class name 
    e.g. classname.classmethodname  ;
3)static method  :-just utility method we can create by using decorator @staticmethod no need to implicit argument
 we can call it by using clasname as well as  object ref; f)never going to use any instance or static variable
 '''


class student:
    cname="msbidve"
    def __init__(self,sno,sname,smark):
        self.sno=sno
        self.sname=sname
        self.smark=smark
    def info(self):                          #instatnce method
        print("student name;",self.sname)
        print("student no:",self.sno)
        print("student mark :",self.smark)

    @classmethod
    def getclg(cls):              #class method
        print(cls.cname)
    @staticmethod         # staticmethod;# by removin decorator we should call this fun by class name
    def fun(x,y):
         print("avrage:-",(x+y)/2)

s1=student(1,'swastik',95)
s2=student(2,"raj",98)
s1.info()            #instance method call by object ref.
s2.info()              #instance method call by object ref.
student.getclg()         #class method call by class name only
s1.fun(10,20)            #static method we can call by classs name as well as object ref.
student.fun(14,12)