valid=False
while not valid:
    try:
        num=int(input("Type in a number"))
        while num%2==0:
            print("nice")
            num=int(input("Type in a number"))
            valid=True
    except ValueError:
        print("Please type in a NUMBER")