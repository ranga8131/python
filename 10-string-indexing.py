# Indexing - Accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9123-4567"

# print(credit_number[0])
# print(credit_number[:4]) --> python assumes start index automatically although mentioned
# print(credit_number[5:9])
# print(credit_number[-1]) --> If indexing is in negative, python reads from last string
# print(credit_number[: :2]) --> prints every second index if step is given as 2

# example: write a program to print only the last 4 digits of the credit card number
last_digit = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digit}")

# example: write a program to reverse the credit card number
reverse = credit_number[::-1] # reverses the credit card number
print(reverse)