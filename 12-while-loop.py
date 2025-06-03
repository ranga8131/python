# while loop - executes some code WHILE some condition remains true 

name = input("Enter your name: ")

while name =="":
    print("You did not entered your name: ")
    name = input("Enter your name: ") # if this line is not there, while loop 
#                                       will trigger the infinite loops

print(f"Welcome {name}!")
