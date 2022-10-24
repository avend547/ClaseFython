pos_integer = input("Enter a positive integer: ")
input_integer = int(pos_integer)
aux = 0
count = 0
if pos_integer.isnumeric():
    while aux < input_integer:
        if (2**(2**aux))+1 == input_integer:
            count += 1
            break
        aux+=1
else:
    print("Please enter a valid integer")

if count != 0:
    print(f"The number {input_integer} is a Fermat's Prime")
else:
    print(f"The number {input_integer} is not a Fermat's Prime")