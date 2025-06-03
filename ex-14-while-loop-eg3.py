
num = int(input("Enter a number b/w 1 - 100: "))

while num < 1 or num > 100:
    print(f"{num} is not valid")
    num = int(input("Enter a number b/w 1 - 100: "))

print(f"Your number is {num}") 
   