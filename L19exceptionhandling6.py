try:
    age=int(input("How old are you?"))
    if age>=18:
        print("You are an adult")
    if age<18:
        print("You are not an adult")
except ValueError:
    print("Please type in your age with numerals")
    