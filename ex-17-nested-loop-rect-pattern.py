# This program is to print symbols in rectangular pattern using nested loops

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter the symbol which you would like to print pattern: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()       