def calc(x,y, opr):
    # if opr == "+":
    #     return x + y
    # elif opr == "-":
    #     return x - y
    # elif opr == "/":
    #     return x / y
    # elif opr == "*":
    #     return x * y
    expression = x + opr + y
    print(expression)
    result = eval(expression)
    return result


print("""
1. Addition
2. Subtraction
3. Division
4. Multiplication
""")

ch = int(input("Enter your choice : "))
x = input("Enter first num : ")
y = input("Enter second num : ")

operations = {
    1 : "+",
    2 : "-",
    3 : "/",
    4 : "*"
}

operator = operations.get(ch)
res = calc(x,y,operator)
print("Result is",res)