# Collection = Single 'variable' used to store multiple values
# There are 3 types of collections:
#          - List = [] ordered and changeable. Duplicates OK
#          - Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#          - Tuple = () ordered and immutable. Duplicates OK. FASTER


# ---------------------------------------------------------------------------------------------------------

# List = [] ordered and changeable. Duplicates OK

car_brands = ["Audi", "BMW", "Citreon", "Datsun", "BYD", "Mahindra"]

# print(len(car_brands))            --> counts how many elements in the list
# car_brands[3] = 'Toyota'          --> replaces an element at index 3 with 'Toyota'
# print('BMW' in car_brands)        --> if 'BMW' is in the 'car_brands' list, it prints True. If not, it prints False
# car_brands.sort()                 --> It sorts the 'car_brands' list in ascending order
# car_brands.append('Kia')          --> Adds 'kia' to the 'car_brands' list
# car_brands.insert(3,'Hyundai')    --> Inserts 'Hyundai' at index 3 of the 'car_brands' list
# car_brands.remove('Datsun')       --> Removes 'Datsun' from the 'car_brands' list
# car_brands.reverse()              --> Reverse the order in the 'car_brands' list
# print(car_brands.count('Datsun')) --> Counts how many 'Datsun' in the 'car_brands' list
# car_brands.clear()                --> Clears the entries in the 'car_brands' list
# print(car_brands.index("BYD"))    --> Prints the index of 'BYD'

#for car_brand in car_brands:  # 'car_brand' is counter                        
#   print(car_brand)          # 'car_brands' is collection variable

# ----------------------------------------------------------------------------------------------------------

# Set = {} unordered and immutable, but Add/Remove OK. No duplicates

bikes = {"Honda", "Royal Enfield", "TVS", "Jawa", "Triumph", "TVS" }
print(bikes)


# ----------------------------------------------------------------------------------------------------------

# Tuple - Ordered and immutable (read-only). Duplicates are allowed.
# point = (10, 20)
# x,y = point
# print(f"x:{x} and y:{y}")

# ---------------------------------------------------------------------------------------------------------
'''
Lists (Mutable, Ordered, Duplicates Allowed):

    Modification Methods:
            append(item): Adds an item to the end of the list.
            extend(iterable): Extends the list by appending elements from an iterable.
            insert(index, item): Inserts an item at a specific index.
            remove(item): Removes the first occurrence of a specified item.
            pop(index=-1): Removes and returns the item at a given index (defaults to the last item). 
            clear(): Removes all items from the list.
            sort(key=..., reverse=...): Sorts the list in place.
            reverse(): Reverses the order of the list in place.

        Accessing Methods:
            count(item): Returns the number of occurrences of an item.
            index(item, start=..., end=...): Returns the index of the first occurrence of an item.

        Copying:
            copy(): Returns a shallow copy of the list.
            len(list): returns the length of the list.

Sets (Mutable, Unordered, No Duplicates):

    Modification Methods:
        add(item): Adds an item to the set.
        update(iterable): Updates the set with elements from an iterable.
        remove(item): Removes a specified item (raises KeyError if not found).
        discard(item): Removes a specified item if it exists (no error if not found).
        pop(): Removes and returns an arbitrary item.
        clear(): Removes all items from the set.

    Set Operations:
        union(other_set, ...) or |: Returns the union of sets.
        intersection(other_set, ...) or &: Returns the intersection of sets.
        difference(other_set, ...) or -: Returns the difference of sets.
        symmetric_difference(other_set) or ^: Returns the symmetric difference of sets.
        isdisjoint(other_set): Returns True if sets have no common elements.
        issubset(other_set) or <=: Returns True if the set is a subset of another.
        issuperset(other_set) or >=: Returns True if the set is a superset of another.

    Copying:
        copy(): Returns a shallow copy of the set.
        len(set): returns the length of the set.

Tuples (Immutable, Ordered, Duplicates Allowed):

    Accessing Methods:
        count(item): Returns the number of occurrences of an item.
        index(item, start=..., end=...): Returns the index of the first occurrence of an item.
        len(tuple): returns the length of the tuple. 
        Important Note: Tuples do not have modification methods because they are immutable. 

'''
