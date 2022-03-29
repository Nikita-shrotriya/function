def unique():
    n=[1,2,3,3,3,3,4,5]
    m=[]
    i=0
    while i<len(n):
        if n[i]not in m:
            m.append(n[i])
        i=i+1
    print(m)
unique()            
