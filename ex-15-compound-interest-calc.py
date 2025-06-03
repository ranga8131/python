# This program is to calculate the total amount after being compounded for years

# Compound interest formula = P * pow((1+R/100),T)
# P =  Principal (INR)
# R = Rate (%)
# T = Time (Years)

P = 0
R = 0
T = 0

while P <= 0:
    P = float(input("Enter the Principal amount (in INR): "))
    if P<=0:
        print("Your Principal amount cannot be 0 or negative value")
        

while R <= 0:
    R = float(input("Enter the Interest rate (in %): "))  
    if R<=0:
        print("Your Interest Rate cannot be 0 or negative value")
          

while T <= 0:
    T = float(input("Enter the Time (in years): "))
    if T<=0:
        print("Your Time cannot be 0 or negative value")
           

Total = P * pow((1+R/100),T)

print(f"Your total amount is INR {Total:.2f}")


