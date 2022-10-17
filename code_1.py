#print("Hello World")

a = 12
b = 29
c = a + b
d = b / a
print(c)
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {2} is {0}".format(c,a,b))

print("Div of {} and {} is {:.3f}".format(b,a,d))

# f-strings - format strings
print(f"Sum of {a} and {b} is {c}")











