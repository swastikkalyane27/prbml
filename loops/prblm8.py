def my_fun(num):
    y=[]
    for x in num:
        if x not in y:
            y.append(x)
    print(y)
my_fun([20,30,30,40,23,20,45,45,50,30,20])
