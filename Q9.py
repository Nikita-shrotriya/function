def sum():
   a= num_1+num_2
   print(a)   
def sub():
    b=num_1-num_2
    print(b)   
def multi():
    c=num_1*num_2
    print(c)   
def divide():
    d=num_1/num_2
    print(d)  
def calculator(): 
    if operation=="+":
        sum()
    elif operation=="-":
        sub()
    elif operation=="*":
        multi()
    else:
        divide()
num_1=int(input("enter the num"))
num_2=int(input("enter the num"))
operation=input("enter operation")        
calculator()


