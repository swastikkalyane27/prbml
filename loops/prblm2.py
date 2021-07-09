#fide the max value from three no by using function
'''
def max_two(x,y):
    if x>y:
        return x
    return y
def max_three(x,y,z):
    return max_two(x,max_two(y,z))
print("max of three:", max_three(19,21,12))'''


def small2(x,y):
    if x<y:
        return x
    return y
def small3(x,y,z):
    return small2(x,small2(y,z))
print(small3(10,12,5))


