# Currency converter

list_of_my_currency = input("Which currency do you have? (USD or INR or EUR or JPY): ")
my_amount = float(input("Enter the amount: "))
convert_currency = input("Which currency you want to convert to? (USD or INR or EUR or JPY): ")

if list_of_my_currency == "USD":
    if convert_currency == "INR":
        my_amount = my_amount * 86.00
    elif convert_currency == "EUR":
        my_amount = my_amount * 0.96
    elif convert_currency == "JPY":
        my_amount = my_amount * 148.67
    print(f"The amount equivalent to {list_of_my_currency} is {round(my_amount, 2)} {convert_currency}") 

elif list_of_my_currency == "INR":
    if convert_currency == "USD":
        my_amount = my_amount * 0.012
    elif convert_currency == "EUR":
        my_amount = my_amount * 0.011
    elif convert_currency == "JPY":
        my_amount = my_amount * 1.73
    print(f"The amount equivalent to {list_of_my_currency} is {round(my_amount, 2)} {convert_currency}")        

elif list_of_my_currency == "EUR":
    if convert_currency == "USD":
        my_amount = my_amount * 1.08
    elif convert_currency == "INR":
        my_amount = my_amount * 93.18
    elif convert_currency == "JPY":
        my_amount = my_amount * 161.02
    print(f"The amount equivalent to {list_of_my_currency} is {round(my_amount, 2)} {convert_currency}")        

elif list_of_my_currency == "JPY":
    if convert_currency == "USD":
        my_amount = my_amount * 0.0067
    elif convert_currency == "INR":
        my_amount = my_amount * 0.58
    elif convert_currency == "EUR":
        my_amount = my_amount * 0.0062
    print(f"The amount equivalent to {list_of_my_currency} is {round(my_amount, 2)} {convert_currency}")                                        