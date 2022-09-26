number1 = input("Enter a number: ")
if number1.isnumeric():
    number1 = int(number1)
else:
    print("Must be a number")
##
if number1 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")