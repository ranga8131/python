# write a program to get food name as input to display and 
# quits if they ordered enough using while condition



food_name = input("Enter a food name (x to quit): ")

while not food_name =="x":
    print(f"You like {food_name}")
    food_name = input("Enter a food name (x to quit): ")

print("Thanks for choosing our restaurant!")