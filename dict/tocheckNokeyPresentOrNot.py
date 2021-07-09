dict1={"ankush":200,"swastik":300,"raj":259}
user_ip=input("enter name to verified\n")
if user_ip in dict1.keys():
    print("Name present in dict:")
    print(dict1[user_ip])
else:
    print("not in dict1")