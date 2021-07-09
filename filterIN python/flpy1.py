# syntax:
#   filter(fun,sequence)


age=[19,18,10,30,9,20,10]
l1=[16,46,74,76,23,8,10]
l2=[19,15,65,43,54,35,66]
def func(n):
    if n>18:
        return True
    else:
        return False
x=filter(func,age)
y=filter(func,l1)
z=filter(func,l1)
print(list(x))  # o/p is object
print(list(y))  # o/p is object
print(list(z))  # o/p is object
# for i in (x):
#     print(i,end=",")
# print()
# for i in (y):
#     print(i,end=',')
# print()
# for i in (z):
#     print(i,end=',')
# print()
# for i in (x):
#     print(i,end=",")
