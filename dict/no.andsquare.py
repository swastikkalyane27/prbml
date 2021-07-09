#Write a Python script to print a dictionary
# where the keys are numbers between 1 and 15 (both included) and the values are square of keys
'''dict={x:x*x for x in range(1,16)}
print(dict)'''


def fun(a):
    z="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d={}
    for x in range(a):
      d[z[x]]=x*x
    return d
print(fun(27))


'''d = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
     print(color_key, 'corresponds to ', value) '''
