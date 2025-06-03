# We will see some built-in math functions in Python

x = 3.14
y = -4
z = 5
u = 4.28732587

# round() - Round off fn
t1 = round(x)
print(t1)
# round(<variable>, <round off up to>) 
t6 = round(u, 3)
print(t6)

# abs() - Absolute value fn
t2 = abs(y)
print(t2)

# pow() - Power fn (<base>, <power>)
t3 = pow(y, 3)
print(t3)

# max() - Shows a maximum value among the given no.
# min() - Shows a Minimum value among the given no.
t4 = max(x, y, z)
t5 = min(x, y, z)
print(f"maximum is {t4} and minimum is {t5}")

# Importing Math module
import math
a = 9.9
print(math.pi)
print(math.e)
print(math.sqrt(a))
print(math.ceil(a))
print(math.floor(a))