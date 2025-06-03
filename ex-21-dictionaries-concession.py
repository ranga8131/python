# Concession Stand Program

menu = {"chicken briyani": 250, 
        "mutton briyani": 300, 
        "chicken fry": 250, 
        "mutton chops": 300, 
        "mutton liver": 200, 
        "chicken kabab": 250,
        "water bottle": 20, 
        "soft drinks": 20}

cart = []

total = 0

print("---------Shivaji Military Hotel---------")

for key, value in menu.items():
    print(f"{key:20}: RS.{value:.2f}")
print("----------------------------------------") 

while True:
    food = input("Enter a food item (q to quit): ").lower()
    if food in menu:
        cart.append(food)
    elif food == 'q':
        break
    else:
        print("PlZ, Choose an item on the menu")

print("-----------YOUR ORDER-----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")  
print()
print(f"Your Total is RS.{total:.2f}")   