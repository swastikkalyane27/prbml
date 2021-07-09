import time
print("what shall i remind you BOUT")
txt= str(input())
print("in hpw many minutes?")
local_time=float(input())
local_time=local_time*60
time.sleep(local_time)
print(txt)