#Taking Input
name = input("Enter your name : ")
print("Welcome",name)

'''
valid variable names
firstnum
first_num
firstNum

invalid variable names
first num
first-num
first@num
12first
'''

# by default python return input in string type of data
# so we have to type cast input() into some other data type
fnum = int(input("Enter first num : ")) # type casting input() into int
snum = int(input("Enter second num : ")) # type casting input() into int
res = fnum + snum
print("Sum is",res)










