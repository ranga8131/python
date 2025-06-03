# Timer program using functions and default arguments

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Time's Up!")   

z = int(input("Set your timer: "))
count(0, z) 