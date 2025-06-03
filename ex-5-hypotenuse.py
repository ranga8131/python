# Calculate the Hypotenuse side of the triangle
import math

side1 = float(input("Enter the side 1: "))
side2 = float(input("Enter the side 2: "))
c = pow(side1, 2) + pow(side2, 2)
hyp = math.sqrt(c)
print(f"The Hypotenuse side of the triangle is: {round(hyp, 2)}")