a,b,c = 12,43,23

if a > b and a > c:
    print("A is greatest...")
elif b > a and b > c:
    print("B is greatest...")
else:
    print("C is greatest...")

res = "A" if a > b and a > c else "B" if b > a and b > c else "C"
print(res,"is greatest...")
