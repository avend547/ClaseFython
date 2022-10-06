pos_integer = int(input("Enter a positive integer: "))
aux = pos_integer-1
record = 1
while aux > 1:
    if pos_integer%aux==0:
        record+=aux
    aux-=1

if record==pos_integer:
    print(f"{pos_integer} is a perfect number")
else:
    print(f"{pos_integer} is not a perfect number")