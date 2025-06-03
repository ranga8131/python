# Logical Operators - Evaluate multiple conditions (and, or, not)
#                   - and = all the condition must be true
#                   - or = at least one condition must be true
#                   - not = inverts the condition (not False, not True)

temp = float(input("Enter the temperature (deg Celsius): "))
is_sunny = input("Is it sunny? (Y/N): ") 

if temp>28 and is_sunny =='Y':
    print("It is HOT outside")
    print("It is sunny")

elif 0 < temp <= 28 and is_sunny =='Y':
    print("It is WARM outside")
    print("It is sunny")

elif temp<=0 and is_sunny == 'Y':
    print("It is COLD outside")
    print("It us sunny")

elif temp>28 and is_sunny =='N':
    print("It is HOT outside")
    print("It is Cloudy")

elif 0 < temp <= 28 and is_sunny =='N':
    print("It is WARM outside")
    print("It is Cloudy")

elif temp<=0 and is_sunny == 'N':
    print("It is COLD outside")
    print("It us Cloudy")

