# def out():
#     x=2
#     def inn():
#         y=2
#         result=x+y
#         return result
#     return inn()
# print(out())             # if paranthisis {out()}is not given then it will give the memory location of out function
# # we can call fun as argument>>
# def fun1():
#     print('hello am fun1')
# def fun2(fun):
#     print("hello am fun2 , callin fun1")
#     fun()
# # fun1()
# fun2(fun1)
def upper_str(fun):
    def inner():
        str1=fun()
        return str1.upper()
    return inner
def split_str(fun):
    def fun4():
        str2=fun()
        return str2.split()
    return fun4
@ split_str
@ upper_str
def print_str():
    return "good morning"

print(print_str())
# d=upper_str(print_str)
# print(d)


# def dec_div(fun):
#     def inner(x,y):
#         if y==0:
#             return 'give proper inpute'
#         return fun(x,y)
#     return inner
# @dec_div
# def div(a,b):
#     return a/b
# print(div(4,2))
# d=dec_div(div)
# print(d(10,5))
