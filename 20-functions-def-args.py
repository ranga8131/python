# default arguments - A default value for certain parameters
#                     default is used when arg when argument is omitted
#                     make your function more flexible, reduces # of arguments
#                     1. Positional, 2. Default, 3. Keyword, 4. Arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(1000)) # only one argument is passed. Other values are taken from parameters 
#                           (Where discount and tax are dafault arg)

print(net_price(1000, 0.1, 0)) # These 2 arg passed here will override the default arg in the definition. 
#                                   This is why the default arg is more flexible