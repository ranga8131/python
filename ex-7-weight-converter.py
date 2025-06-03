# Weight Converter program

weight = float(input("Enter Your weight: "))
unit = input("Which unit? (KG or LBS): ")

if unit == "KG":
    weight = weight * 2.205
    unit = "LBS"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "LBS":
    weight = weight/2.205
    unit = "KG"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid")

