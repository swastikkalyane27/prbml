#    D
#   D C
#  D C B
# D C B A


n=int(input("enter no"))
for i in range(n):
    print((' ')*(n-i-1),end='')
    for j in range(i+1):
        print((chr(64+n-j)+' '),end=' ')

    print()