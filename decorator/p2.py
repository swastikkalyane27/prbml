def outer(exp):
    def upper(fun):
        def inner():

           str1=fun()
           a= str1.upper()
           return a + exp
        return inner
    return upper
@outer(" SWASTIK")
def str_fun():
    return "good morning"
print(str_fun())


# l1=[1,2,3,4,5]
# t1=(3,4,5,7,8)
# l1=l1+t1
# print(l1)
# def fun(num):
#     for i in range(num):
#         yield i
# values=fun(12)
# print(values)
# for i in values:
#     print(i)
# for k in range(values):
#     print(k)


# t1=(x for x in range(10))
# print(t1)
# for i in t1:
#     print(i)
# for k in t1:
#     print(k)