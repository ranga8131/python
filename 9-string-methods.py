name = input("Enter your full name: ")

# result = len(name) --> Length method = Gives the total length of the characters starting from 0.
#                        Space is also counted.

# result = name.find(" ") --> Find method = locates the specified character or space from the left to right.

# result = name.rfind("a") --> locates the specified character or space from the right to left. 

# result = name.capitalize() --> Capitalizes the first character of the string.

# result = name.upper() --> converts all characters of the string to the UPPER CASE.

# result = name.lower() --> converts all characters of the string to the lower case

# result = name.isdigit() --> Returns 'True' if the entered value is in all numbers without space
#                             and returns 'False' if the entered value has characters/space.

# result = name.isalpha() --> Returns 'True' if the entered value is in all characters without space
#                             and returns 'False' if the entered value have numbers/space.

# result = name.count("a") --> Count method = Counts how many 'a' in the given name value.

# result = name.replace("x", "y") --> Replaces "x" with "y" for the given name value

result = name.replace("Nandhagopal", "N")

print(result)
