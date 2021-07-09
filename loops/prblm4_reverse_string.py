'''x="1234abcd"[::-1]
print(x)'''


def my_fun(str):
    index=len(str)
    res=""
    while index > 0 :
        res+=str[index-1]
        index=index-1
    return res
print(my_fun("swastik is very tallended boy"))

