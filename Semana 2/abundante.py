ab_number = int(input("write an integer: "))
aux = 1
suma = 0

while aux < ab_number:
    if ab_number%aux == 0:
        suma+=aux
    aux = aux + 1

if suma > ab_number:
    print("The number is abundant")
else:
    print("The number is not abundant")
