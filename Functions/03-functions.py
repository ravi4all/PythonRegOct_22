# *args - variable length arguments
def addition(*x):
    # print(x)
    sum = 0
    if len(x) > 1:
        for i in range(len(x)):
            sum += x[i]
        print("Sum is",sum)
    else:
        print("Not enough arguments...")

addition(5)
addition(2,5)
addition(5,6,7)
addition(4,7,3,9)
addition()
addition(11,2,5,7,3,2,6,7)

