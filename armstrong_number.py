#Armstrong Number
num = int(input("Enter a number : "))
sum = 0
temp = num
while num != 0:
    rem = num % 10
    sum += rem ** 3
    num = num // 10

if temp == sum:
    print(f"{sum} is armstrong...")
else:
    print(f"{temp} is not armstrong")
