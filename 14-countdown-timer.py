# Countdown timer program
# This program introduces 'time' module and 'sleep' function to make the program for inactive 
# for certain duration and execute the code.

import time

timer = int(input("Enter the timer value: "))

time.sleep(timer) # In the 'sleep' function's parenthesis, any value (e.g. 3) is represented will be in seconds.

print("Time's UP!")