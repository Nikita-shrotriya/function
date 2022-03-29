def function():
    weight=int(input("enter the weight"))
    height=int(input("enter the height"))
    bmi=weight/height
    if bmi<=18.5:
        print("underweight")
    if bmi>=18.5 and bmi<=25.0:
        print("normal")
    if bmi>=25.0 and bmi<=30.0:
        print("overweight")
    if bmi>=30:
        print("obese")
function()    
