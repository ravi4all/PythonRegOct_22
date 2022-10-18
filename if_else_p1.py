age = int(input("Enter your age : "))

if age > 18:
    print("You are eligible...")
else:
    print("You are not eligible...")

if age > 18:print("You are eligible...")
else:print("You are not eligible...")

print("Eligible" if age > 18 else "Not Eligible")
