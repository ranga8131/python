# Python Number Guessing Game

import random

lowest_value = 1
highest_value = 100

answer = random.randint(lowest_value, highest_value)

guesses = 0

is_running = True
print("Python Number Guessing Game")
print(f"Select any number between {lowest_value} and {highest_value}")

while is_running:
    guess = input("Enter a number: ")
    
    if guess.isdigit():
        guess = int(guess)
        if answer < guess < highest_value or lowest_value < guess < answer:
            if guess < answer:
                print(f"The {guess} is too low!")
                print(f"Please select any number between {lowest_value} and {highest_value}")
                guesses += 1
            elif guess > answer:
                print(f"The {guess} is too high!")
                print(f"Please select any number between {lowest_value} and {highest_value}")
                guesses += 1   

        elif guess > highest_value:
            print("The number is out of the specified range")
            print(f"Please select any number between {lowest_value} and {highest_value}")
        elif guess < lowest_value:
            print("The number is out of the specified range")
            print(f"Please select any number between {lowest_value} and {highest_value}") 
        else:
            print("CORRECT!")
            print(f"Your total guesses are {guesses}")
            is_running = False       

    else:
        print("Invalid guess!")
        print(f"Please select any number between {lowest_value} and {highest_value}")