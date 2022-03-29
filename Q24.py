def perfact():
    m=1
    while m<=100:
        num=m
        i=1
        sum=0
        while i<m:
            if num%i==0:
                sum=sum+i
            i=i+1
        if sum==num:
            print(num,"perfact number")
        m=m+1
perfact()        
