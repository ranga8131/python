menu = {"Chicken Briyani": 250,
        "Mutton Briyani": 300,
        "Chicken Fry": 250,
        "Mutton Chops": 300,
        "Mutton Liver": 200,
        "Chicken Kabab": 250,
        "Water Bottle": 20,
        "Soft Drinks": 20}

cart = {}

total = 0

print("---------Shivaji Military Hotel---------")

for key, value in menu.items():
    print(f"{key:20}: RS.{value:.2f}")
print("----------------------------------------")

while True:
    food_input = input("Enter a food item (q to quit): ").lower()
    if food_input == 'q':
        break
    elif food_input in menu:
        if food_input in cart:
            cart[food_input] += 1
        else:
            cart[food_input] = 1
    else:
        print("Sorry, that item is not on the menu.")

print("-----------YOUR ORDER-----------")
for item, quantity in cart.items():
    price = menu.get(item)
    item_total = price * quantity
    total += item_total
    print(f"{item} x {quantity:2} = RS.{item_total:.2f}")
print("----------------------------------------")
print(f"Your Total is RS.{total:.2f}")