def even(n):
    a=[]
    i=0
    while i<len(n):
        if n[i]%2==0:
            a.append(n[i])
        i=i+1
    print(a)
even([1,2,3,4,5,6,7,8,9])        
