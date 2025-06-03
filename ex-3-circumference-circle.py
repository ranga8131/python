# Calculate the Circumference of the circle
import math 

radius = float(input("Enter the radius of the circle: "))
circumference = (2*math.pi*radius)
print(f"The Circumference of the circle of given radius {radius} is: {round(circumference, 2)}")