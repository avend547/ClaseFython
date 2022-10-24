pos_integer = input("Enter a positive integer: ")
input_integer = int(pos_integer)
aux = 0
count = 0
if pos_integer.isnumeric():
    while aux < input_integer:
        aux+=1
        count+=aux
        if count == input_integer:
            break
else:
    print("Please enter a valid integer")

if count == input_integer:
    print(f"The number {input_integer} is a triangular number")
else:
    print(f"The number {input_integer} is not a triangular number")