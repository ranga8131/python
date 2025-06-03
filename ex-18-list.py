# Shopping Cart Problem
# This program is to get inputs from user about the list of food and its price 
# and then generate a bill using list[] method

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy (press q to quit): ")        
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the amount of {food}: INR"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your total is {total}")       