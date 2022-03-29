def palindrom():
    name=["m","o","m"]
    p=name[-1::-1]
    if name==p:
        print(name,"is a palindrom")
    else:
        print(name,"is a not palindrom")
palindrom()            
