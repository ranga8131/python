# Write a program to print sequence of numbers using while loop

num = int(input("Enter a number upto which it should be printed: "))
res = 1

while res < num+1:
    print(res)
    res += 1

print("end")    