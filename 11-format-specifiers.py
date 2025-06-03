# format specifier - {value: flag} formats the value based on what flags are inserted

price1 = 232134.234213
price2 = -234.234
price3 = 324.2343423

# :.(number)f --> round to that many decimal places (fixed point)
# :(number) --> allocate that many spaces
# :0(number) --> allocate and zero pad that many spaces
# :< --> left justify
# :> --> right justify
# :^ --> center align
# :+ --> use '+' sign to indicate positive value
# := --> place sign to leftmost position
# :  --> insert space before positive numbers
# :, --> use comma separators for thousands

print(f"price1 is {price1:+,.2f} ")
print(f"price2 is {price2:+,.2f} ")
print(f"price3 is {price3:+,.2f} ")
