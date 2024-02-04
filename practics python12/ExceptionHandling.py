try:
    x=int(input("Enter the  number:"))
    y=int(input("Enter secound number:"))
    print(x/y)
    print(x+y)
except ZeroDivisionError:
    print("This is valid number")

