# Functions - A block of reusable code
#               place () after the function name to invoke it


def happy_birthday(name, age):      # function(par1, par2)
    print(f"Happy Birthday to you {name}")
    print(f"You are {age} Old!")
    print()


happy_birthday("Ranga", 28)     # function(arg1, arg2)
happy_birthday("Ganesh", 24)
happy_birthday("Antony", 29)

# return - a statement used to end the function and return its value to the caller

def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(sub(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


#3 

def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("rangaraj", "nandhagopal")

print(full_name)
