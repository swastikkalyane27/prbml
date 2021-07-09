'''def sum_lis(items):
    sum=0
    for x in items:
        sum+=x
    return sum

print(sum_lis([10,12,34]))'''

#multiplication of all items in list

def mult_list(numbers):
    mult=1
    for x in numbers:
        mult*=x
    return mult
if __name__ == "__main__":

   print(mult_list([20,3,12,34]))
