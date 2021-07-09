''' Write a Python function that accepts
a string and calculate the number of upper case letters and lower case letters'''


def str(z):
    uc=0
    lc=0
    for x in z:
       if x.isupper():
           uc+=1
       elif x.islower():
           lc+=1

    print(uc)
    print(lc)

print(str("SwaStik"))
