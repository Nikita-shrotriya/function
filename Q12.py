def max():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=int(input("enter the number"))
    if a>b and a>c:
        print(a,"is max")
    elif b>a and b>c:
        print(b,"is max")
    elif c>a and c>b:
        print(c,"is max")
max()                