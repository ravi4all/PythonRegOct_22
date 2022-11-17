def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    # Packing
    return z1, z2, z3, z4

# output = calc(5,6)
# print(output)

a,b,c,d = calc(5,6)
# a,b,c = calc(4,6)
print("Sum is",a)
print("Sub is",b)
