try:
    calc=input("Choose your calculation method;+,-,*,/")
    num1=int(input("Pick your first number"))
    num2=int(input("Pick your second number"))
    if calc==("+"):
        print(num1+num2)
    elif calc==("-"):
        print(num1-num2)
    elif calc==("*"):
        print(num1*num2)
    elif calc==("/"):
        print(num1/num2)
    else:
        print("Please choose 1 of the 4 provided options")
    

except ValueError:
    print("Please type in a number")