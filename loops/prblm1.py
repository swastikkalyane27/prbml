'''''i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
while loop using continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
print(i)
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
'''

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
'''

for x in range(6):
  if x == 3:break
  print(x)

else:
     print("Finally finished!")


