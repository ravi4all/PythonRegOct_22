a = 12
b = 21
# walrus operator - :=
# variable initialization + print
#print("Sum is",c := a + b)

print(f"""
Sum is {(c := a + b)}
Sub is {(d := a - b)}
Div is {(e := a / b)}
Mul is {(f := a * b)}
""")
