def count():
    list=["abc","xyz","aba","1221"]
    c=0
    i=0
    while i<len(list):
        if list[i]==list[-i]:
            c=c+1
        i=i+1
    print(c)
count()            