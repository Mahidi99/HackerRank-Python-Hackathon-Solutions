from decimal import Decimal
def duplicateNo(x):
    numbers = set()

    for i in range(len(x)):

        if x[i] in numbers:
            return x[i]
        else:
            numbers.add(x[i])

x = [int(i) for i in input().split(",")]
Duplicate = duplicateNo(x) 
print (Decimal(Duplicate).normalize())


