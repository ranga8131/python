# keyword arguments - An argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. Positional, 2. Default, 3. Keyword, 4. Arbitrary

def hello(hello, title, first_name, last_name):
    print(f"{hello} {title}{first_name} {last_name}")

hello("Hello", "Mr.", last_name="Nandhagopal", first_name="Rangaraj")