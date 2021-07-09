'''def dict_of(a,b):
    n=len(a)
    m=len(b)
    if n==m and n>0 and m>0:
        dict1=dict(zip(a,b))
    return dict1
print(dict_of(["a","b","c"],[1,2,3]))'''


'''def fun(keys,values):
    d={}
    if len(keys)==len(values) :
      for i in range(len(keys)):
        d[keys[i]]=values[i]
      return d
    else:
      print("invalid inpute")
print(fun(['a','b','c','d'],[1,2,3,4]))'''


def dict1(keys,values):
    n=len(keys)
    m=len(values)
    d={}
    if n==m and n>0 and m>0:
        d[keys[0]]=values[0]
        dict1(keys[1::],values[1::])
    return d
print(dict1(zip((['a','b','c'],[1,2,3]))))