# t1=(10,20,30)
# print(id(t1))
# t1=t1+(40,)
# print(t1)
# print(id(t1))
# t1=t1[0:2]+(50,)+t1[2:]
# print(t1)
t1=10,20,30,40,50,60
# n1,n2,*n3,n4,n5 = t1
# print(n1,n2,n3,n4,n5)
# a,b=10,11
# z=a,b
# print(z)
# l1=list(t1)
# l1.append(90)
# l1.insert(12,12)
# print(l1)
# l1.remove(20)
# l1.pop()
# l1.pop(3)
# print(l1)
# t1=tuple(l1)
# print(t1)
# t1=([10,20],"hello",{1,2,3,4},{"a":10,"b":20},12.3,True)
# print(t1)
# print(type(t1))
# t1[0].append(50)
# print(t1)
# from copy import deepcopy
t1=[10,[],20,]
# t2=deepcopy(t1)
# t2[1].append(20)
# print(t1)
# print(t2)
t3=[40,50,60]
t3=t1.copy()
t3[1].append(50)
print(t3)
print(t1)










