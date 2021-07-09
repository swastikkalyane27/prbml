# o/p
# 1 2 3 4 0
# 1 2 3  1
# 1 2  2
# 1   3

n=int(input("enter no"))
for i in range(n):
    for j in range(n-i):
        print((j+1),end=" ")
    print("")