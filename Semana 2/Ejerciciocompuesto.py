pos_integer = int(input("Enter a positive integer: "))
aux = pos_integer-1
record = 0
while aux > 1:
    if pos_integer % aux == 0:
        record += 1
        break
    aux -= 1

if record != 0:
    print(f"{pos_integer} is a composite number")
else:
    print(f"{pos_integer} is not a composite number")