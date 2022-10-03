pos_integer = int(input("write a positive integer: "))
aux = 1
triangle = 1
while aux <= pos_integer:
    aux2 = triangle
    while aux2 >= 1:
        if aux2 == 1:
            print(aux2)
        else:
            print(aux2, end=" ")
        aux2-=2
    aux +=1
    triangle += 2