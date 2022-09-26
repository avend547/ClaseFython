prime_number = int(input("write an integer: "))
aux = prime_number-1
cont = 0
while aux > 1:
    if prime_number%aux == 0:
        cont+=1
        break
    aux-=1

if cont == 0:
    print('The number is prime')
else:
    print('The number is not prime')
