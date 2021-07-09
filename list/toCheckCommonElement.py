def common_ele(l1,l2):
    count=0
    for x in l1:
        if x in l2:
          count+=1
    if count>=1:
            print("true")
    else:
            print("Not at least one element same")
    return count
print(common_ele([1,2,32,50],[3,4,5,6,78]))
