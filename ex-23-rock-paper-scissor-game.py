# Python Rock-Paper-Scissors Game

import random

options = ('rock', 'paper', 'scissors')



playing = True

while playing:
    computer = random.choice(options)
    player = None
    while player not in options:
        player = input("Enter any input (Rock/Paper/Scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissor" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!")

    if not input("Play again (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing!")        


           
