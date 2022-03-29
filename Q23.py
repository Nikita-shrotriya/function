a=[2,4,6,7]
b=[6,8,4,5]
i=0
c=[]
while i<len(a):
    while i<len(b):
        d=a[i]+b[i]
        c.append(d)
        i=i+1
print(c)                      

