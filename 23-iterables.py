# Iterables - An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

# List of Iterables:
# 1)    String
#       name = "ABCDEF"

# 2)    list
#       numbers = [1, 2, 3, 4, 5]

# 3)    tuples
#       numbers = (1, 2, 3, 4, 5)

# 4)    sets
#       numbers = {"A", "B", "C", "D", "E"}

# 5)    dictionaries
#       dict = {"Apple": 2, "Orange": 4, "Banana": 7}

numbers = {"A":1, "B":2, "C":3, "D":4, "E":5}

for key, value in numbers.items():
    print(f"{key}:{value}", end = " ")