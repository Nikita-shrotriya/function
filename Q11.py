def password():
    n=input("enter the password")
    if(len(n)==8):
        if n>"A" and n<"Z" or n>"a" and n<"z" and n>"0" and n<"9" or n>"@" and n<"#":
            print("strong password")
        else:
            print("week password")
    else:
        print("please enter 8 charecter")            
password()                        
                        


