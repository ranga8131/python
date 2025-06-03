# arbitrary arguments
# *args    - allows us to pass multiple non-key arguments
# **kwargs - allows us to pass multiple knyword arguments
#               * unpacking operator
#                     1. Positional, 2. Default, 3. Keyword, 4. Arbitrary


# -----------------------*args--------------------------------------------
def greetings(*args):
    for arg in args:
       print(arg, end=" ")

greetings("Hello!", "Mr.", "Rangaraj", "Nandhagopal")


def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5))  

# -----------------------**kwargs--------------------------------------------

def address(**kwargs):
    for keys,values in kwargs.items():
        print(f"{keys}:{values}")

address(flat_no="02",
        street="Lingappan Street",
        city="Kanchipuram",
        pincode="631502")
