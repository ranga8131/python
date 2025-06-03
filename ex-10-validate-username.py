# This program validates the username for all 3 conditions at one go
# Conditions:
#           1) User input must not be more than 12
#           2) User input must not contain spaces
#           3) User name must not contain digits

name = input("Enter your name: ")
length = len(name)
is_space = name.find(" ")
is_alpha = name.isalpha()

if length > 12 and is_space != -1 and not is_alpha:
    print("Username is invalid")
    print("username should not exceed 12")
    print("Username should not contain spaces") 
    print("Username should not contain digits")

elif length > 12 or is_space != -1 or not is_alpha:
    if length > 12:
        print("username should not exceed 12")
    elif is_space != -1:    
        print("Username should not contain spaces") 
    elif not is_alpha:
        print("Username should not contain digits")

else:
    print(f"Welcome {name}!") 