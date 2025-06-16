# Banking Program

def show_balance(balance):
    print(f"Your balance is INR {balance:.2f}")

def deposit():
    amount = float(input("Please enter amount to deposit: "))
    if amount < 0:
        print("please enter a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Enter a valid amount")
        return 0
    else:
        return amount        

def main():
    balance = 10000
    is_running = True

    while is_running:
        print("Welcome to ABC Bank")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter an operation (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()
            show_balance(balance)

        elif choice == '3':
            balance -= withdraw(balance)
            show_balance(balance)

        elif choice == '4':
            print("Thank You for banking with us!")
            is_running = False

        else:
            print("Enter a valid operation")  

if __name__ == '__main__':
    main()            