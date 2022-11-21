# lambda - anonymous

# def even(n):return n % 2 == 0

# lambda n : n % 2 == 0
nums = [4,3,2,1,5,6,7,6,5,8,9,8,12,21,55]
e = list(filter(lambda n : n % 2 == 0, nums))
print(e)
