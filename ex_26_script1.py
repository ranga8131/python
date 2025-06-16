# This program is demonstrate the use of || if __name__ == '__main__' || --> This statement
# make the python file to execute only if the condition is met.
# This program should be used with "ex_26_script2.py" to see how this program's data has been 
# imported but not executing the whole program

def fav_foods(food):
    print(f"Your favourite food is {food}")

def main():
    print("Hi Rangaraj!")    
    fav_foods("Briyani")
    print("Good Bye!")

if __name__ == '__main__':
    main() 


