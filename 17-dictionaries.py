# Dictionaries = a collection of {key:value} pairs
#                   ordered and changeagle. No duplicates


capitals = {"India":"New Delhi", "USA":"Washington D.C.", "Germany": "Berlin", "China": "Beijing"}

#--------------------------------------------------------------
'''
get = This method gets the value for requested key from the dictionary

#Input:
print(capitals.get("India"))

#output:
New Delhi
'''
#--------------------------------------------------------------
'''
update = This method updates the dictionary

#Input:
capitals.update({"Russia":"Moscow"})
print(capitals)

#output:
{'India': 'New Delhi', 'USA': 'Washington D.C.', 'Germany': 'Berlin', 
'China': 'Beijing', 'Russia': 'Moscow'}
'''
#------------------------------------------------------------------
'''
pop = This method removes the specified key and its value from the dictionary

#Input:
capitals.pop("China")
print(capitals)

#output:
{'India': 'New Delhi', 'USA': 'Washington D.C.', 'Germany': 'Berlin'} 
NOTE: China has been removed from the capitial dictionary
'''
#------------------------------------------------------------------
'''
popitem = This method removes the latest key and its value from the dictionary

#Input:
capitals.popitem()
print(capitals)

#output:
{'India': 'New Delhi', 'USA': 'Washington D.C.', 'Germany': 'Berlin'} 
NOTE: China has been removed from the capitial dictionary 
as China is the latest item in the dictionary.
'''
#------------------------------------------------------------------
'''
clear = This method removes all the key:value pairs from the dictionary

#Input:
capitals.clear()
print(capitals)

#output:
{}
NOTE: Currently no items are there in the capitals dictionary
'''
#------------------------------------------------------------------
'''
keys() = This method considers only the key in the dictionary

#Input:
for key in capitals.keys():
    print(key)

#output:
India
USA
Germany
China
'''
#------------------------------------------------------------------
'''
values() = This method considers only the values in the dictionary

#Input:
for value in capitals.values():
    print(value)

#output:
New Delhi
Washington D.C.
Berlin
Beijing
'''
#------------------------------------------------------------------
'''
items() = This method considers both keys and values in the dictionary

#Input:
for key, value in capitals.items():
    print(f"The capital of {key} is {value}")

#output:
The capital of India is New Delhi
The capital of USA is Washington D.C.
The capital of Germany is Berlin
The capital of China is Beijing
'''