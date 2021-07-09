def log_word(n,str):
    l1=[]
    txt=str.split(" ")
    for x in txt:
        if len(x)>n:
            l1.append(x)
    return l1
print(log_word(3,"hello , myself swastik , am software engineer"))


