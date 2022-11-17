def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

print("""
1. Addition
2. Subtraction
3. Division
4. Multiplication
""")

ch = int(input("Enter your choice : "))
x = int(input("Enter first num : "))
y = int(input("Enter second num : "))

# operations = [add, sub, div, mul]
# operations[ch - 1](x, y)

operations = {
    1 : add,
    2 : sub,
    3 : div,
    4 : mul
}
operations.get(ch)(x,y)


# if ch == "1":
#     add(x,y)
# elif ch == "2":
#     sub(x,y)
