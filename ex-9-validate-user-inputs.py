# Validate User input: 

#   1) User input must not be more than 12
name = input("Enter your name: ")
length = len(name)

if length > 12:
    print("Enter the characters less than 12")

else:
    print("Your character is valid")   


#   2) User input must not contain spaces
name = input("Enter your name: ")
is_space = name.find(" ")

if is_space != -1:
    print("Username must not contain spaces")

elif is_space == -1:
    print("Your character is valid")  


#   3) User name must not contain digits
name = input("Enter your name: ")
is_alpha = name.isalpha()

if is_alpha:
    print("Your character is valid")

else:
    print("Username must not contain digits")