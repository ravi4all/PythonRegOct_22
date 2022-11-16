# positional argument
# def greet(name):
#     # name = "Ram"
#     print("Hello",name)

# greet("Ram")
# greet("Shyam")

# positional argument
# def greet(firstName, lastName):
#     name = firstName + " " + lastName
#     print("Hello",name)

# Default arguments
def greet(firstName, lastName=""):
    name = firstName + " " + lastName
    print("Hello",name)
# greet("Ram")
greet("Ram","Sharma")
greet("Ram")

# Keyword arguments
greet(firstName="Ram", lastName="Sharma")
greet(lastName="Tyagi", firstName="Ravi")
greet(firstName="Shyam")
