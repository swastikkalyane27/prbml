def fact(number):
    if number==0:
      facto=1
    if number >0:
        facto=number*fact(number-1)
    return facto
print(fact(13))