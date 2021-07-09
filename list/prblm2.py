#Write a Python program to multiplies all the items in a list
def multiplication(items):

    mult=1
    for x in items :
        mult*=x
    return mult
print(multiplication([10,20,30]))
