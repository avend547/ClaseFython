pos_integer = input("write a positive integer: ")
dig = [int(x) for x in pos_integer]
dig_root=sum(dig)
if dig_root > 9:
    while dig_root > 9:
        cycle = sum([int(i) for i in str(dig_root)])
        dig_root = cycle
        print(cycle)
else:
    print(dig_root)

"""
if dig_root > 9:
    cycle = sum([int(i) for i in str(dig_root)])
    print(cycle)
else:
    print(dig_root)
"""