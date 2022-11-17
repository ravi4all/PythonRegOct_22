# Nested Function - Function inside Function
def calc():
    x = 45
    y = 7
    # add() is now local function of calc
    def add():
        print("Add Function Called...")
        z = x + y
        return z

    def sub():
        print("Sub Function Called...")
        z = x - y
        return z

    return add, sub

x,y = calc()
print(x())
print(y())