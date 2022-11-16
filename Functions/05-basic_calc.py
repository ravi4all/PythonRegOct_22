def add():
    pass

def sub():
    pass

print("""
1. Addition
2. Subtraction
3. Division
4. Multiplication
""")

ch = input("Enter your choice : ")
x = int(input("Enter first num : "))
y = int(input("Enter second num : "))

if ch == "1":
    add(x,y)
elif ch == "2":
    sub(x,y)
