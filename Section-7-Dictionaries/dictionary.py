spam = {12345: 'Luggage combination', 42: 'The Answer'}

eggs = {'name' : 'Zophie', 'species': 'cat', 'age': 8}

# Trying to find a key that doesn't exist in a dictionary will resule in a KeyError
# print(eggs['color'])

# Use 'in' and 'not in' to search for values inside a dictionary
print('name' in eggs)

print('name' not in eggs)

# Methods that will return list like values of the dictionaries keys, values, or both keys and values
##print(list(eggs.keys()))
##
##print(list(eggs.values()))
##
##print(list(eggs.items()))

# For loops can be used with these methods
##for v in eggs.values():
##    print(v)

# Multiple assignment can be used with dictionary.items() method. The method returns tuples (key, value)
##for k, v in eggs.items():
##    print(k, v)

# 'in' and 'not in' ca be used with the above methods
print('cat' in eggs.values())

# To avoid crashing the program when searching for a value or key in a dictinoary, use the get() method
print(eggs.get('age', 0))   # Defaults to 0 if age isn't found in the dictionary

print(eggs.get('color', '')) # Default to blank string if key isn't found


# To set a default key value pair inside a dictionary if it doesn't exist already, use the setdefault() method
eggs.setdefault('color', 'black')

    
