# **kwargs - variable length keyword arguments
# def person(**details):
#     print(details)

# person(id = 101, name = "Ram")
# person(id = 102, name = "Shyam", salary = 45000)
# person(name = "Mohan", address = "Delhi", salary = 50000)

def person(*args, **kwargs):
    print(args)
    print(kwargs)

person(101, "Ram", address = "Delhi")
