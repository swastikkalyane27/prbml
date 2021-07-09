# O/P
# A
# B B
# C C C
# D D D D
#nested for loop not required bcz in single row element is same
n=int(input("enter number\n"))
for i in range(n):#0,1,2,3
    print((chr(65+i)+" ")*(i+1))
