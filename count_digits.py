#3. Count digits in a number
n = 23137
count = 0
while n != 0:
    n = n // 10
    count += 1
    print(n)

print(f"Count is {count}")
