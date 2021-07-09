def dec_div(fun):
    def inner_div(*arg):
        list1=[]
        list1=arg[1:]
        for i in list1:
            if i ==0:
                return "give proper inpute"
            else:
                return fun(*arg)
        return inner_div
@dec_div
def div1(a,b):
    return a/b
@dec_div
def div2(a,b,c):
    return a/b/c
print(div1(10,2))
print(div2(20,0,2))