def positive():
    list=[2,-7,5,-64,-14]
    i=0
    count=0
    count1=0
    while i<len(list):
        if list[i]>0:
            count=count+1
        else:
            count1=count1+1
        i=i+1
    print(count,"posetive")
    print(count1,"negative") 
positive()                              
