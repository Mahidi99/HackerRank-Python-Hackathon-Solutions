def adding(a, b):
    while b != 0:
        add = a & b
        a = a ^ b
        b = add << 1
    return a
a, b = map(int, input().split()) 
print(adding(a, b))




