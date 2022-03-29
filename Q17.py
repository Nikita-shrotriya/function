def upper():
    str=input("enter")
    upper=0
    lower=0
    i=0
    while i<len(str):
        if str[i]>"A" and str[i]<"Z":
            upper=upper+1
        if str[i]>"a" and str[i]<"z":
            lower=lower+1
        i=i+1    
    print("upper case=",upper)
    print("lower case=",lower)
upper()            

