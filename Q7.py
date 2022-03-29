def number():
    n=int(input("enter the number"))
    i=0
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%5==0:
        print("Buzz")    
    elif n%3==0:
        print("Fizz") 
    else:
        print(n)
    i=i+1
number()              
