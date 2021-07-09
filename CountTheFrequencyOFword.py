user_str=input("enter a string\n")
l=user_str.split()
d={}
for x in l:
    if x not in d:
      d[x]=0
    d[x]=d[x]+1
print(d)