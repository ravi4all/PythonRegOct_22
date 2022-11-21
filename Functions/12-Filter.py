def even(n):
    return n % 2 == 0

# print(even(6))
nums = [4,3,2,1,5,6,7,6,5,8,9,8,12,21,55]
# evenList = list(map(even, nums))
evenList = list(filter(even, nums))
print(evenList)
