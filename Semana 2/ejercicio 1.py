pos_integer = int(input("write a positive integer: "))

for number_for in range(1, pos_integer+1, 2):
    if number_for+2 > pos_integer:
        print(number_for)
    else:
        print(number_for, end= ", ")
