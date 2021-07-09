## Instance Method
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print('hi',self.name)
        print('your marks are',self.marks)
    def grade(self):
        if self.marks>=60:
            print('first grade')
        elif self.marks>=50:
            print('second grade')
        elif self.marks>=35:
            print('you got third grade')
        else:
            print('you are failed')
n = int(input("enter number of students: "))
for i in range(n):
    name = input('enter student name: ')
    marks = int(input('enter students marks: '))
    s = Student(name,marks)
    s.display()
    s.grade()
    print('*'*20)


## Setter & Getter Method
class Student:
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks = marks
    def getmarks(self):
        return self.marks

n = int(input("enter number of students: "))
for i in range(n):
    name = input('enter student name: ')
    marks = int(input('enter students marks: '))
    s = Student()
    s.setname(name)
    s.setmarks(marks)
    print('hi',s.getname())
    print('your marks is:',s.getmarks())
   
