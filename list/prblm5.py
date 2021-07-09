'''Write a Python program to count the number of
 strings where the string length is 2 or more and
the first and last character are same from a given list of strings.'''

'''def match(item):
    count=0
    for x in item:
        if len(x)>1 and x[0]==x[-1]:


            count+=1

    return count
print(match(["swas","swastiks","raj","kamlesh"]))'''



def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
