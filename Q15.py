a=[1,342,75,23,98]
b=[75,23,98,12,78,10,1]
c=[]
i=0
while i<len(a):
    if a[i] in b:
        c.append(a[i])
    i=i+1
print(c)