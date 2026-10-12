try:
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    result=num1+num2
    print(result)

except ValueError:
    print("Your input is not a number. Please type in a number")