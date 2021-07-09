n=int(input("enter no"))
for i in range(n):
    for j in range(i-1):
        print(" "*(n-1)+"#"*i)
    print("\n")