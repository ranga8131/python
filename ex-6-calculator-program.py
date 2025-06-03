# Writing the Calcuator Program

operator = input("Which operator do you like to work? (+ or - or * or /): ")
if operator == "+" or operator == "-" or operator == "*" or operator == "/":
    print("Enter value for A and B:")
    A = float(input("A: "))
    B = float(input("B: "))

    if operator == "+":
        result = A + B
        print(f"Result is {result}")

    elif operator == "-":
        result = A - B
        print(f"Result is {result}")

    elif operator == "*":
        result = A * B
        print(f"Result is {result}")       

    elif operator == "/":
        result = A / B
        print(f"Result is {result}")
else:
    print("Plz enter the valid operator!")