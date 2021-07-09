l1=[1,2,2,3,3,4,5,6,6,7,8,8,9]
l2=[]
for x in l1:

   if x not in l2:
      l2.append(x)
print(l2)
#using function

def duplicate(items):
    l1=[]
    for x in items:
        if x not in l1:
            l1.append(x)
    return l1
print(duplicate([1,2,2,3,4,5,5,6,6,6,7,78,8,9,99]))




