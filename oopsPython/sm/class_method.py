## class method
# class Animal:
#     legs = 4
#     @classmethod
#     def walk(cls,name):
#         print('{} walks with {} legs'.format(name,cls.legs))

# Animal.walk('dog')
# Animal.walk('cat')

## to track the no of object created in class
class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count + 1
    
    @classmethod
    def getnoofobject(cls):
        print('no of object created:',cls.count)

t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
Test.getnoofobject()