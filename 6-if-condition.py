# Checking the Voter ID Eligibility using If-Elif-Else Condition

name = input("Enter your name: ")
year = int(input("Enter your year of birth: "))
age = 2025-year

if age>=18 and age<100:
    print(f"Hello {name}, Congratzz. You are eligible for Voting!")

elif age<0:
    print("Plz enter the year less than 2025")

else:
    print(f"Hello {name}, You are NOT eligible for Voting!")
