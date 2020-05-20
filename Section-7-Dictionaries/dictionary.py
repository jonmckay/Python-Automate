spam = {12345: 'Luggage combination', 42: 'The Answer'}

eggs = {'name' : 'Zophie', 'species': 'cat', 'age': 8}

# Trying to find a key that doesn't exist in a dictionary will resule in a KeyError
# print(eggs['color'])

# Use 'in' and 'not in' to search for values inside a dictionary
print('name' in eggs)

print('name' not in eggs)

# Methods that will return list like values of the dictionaries keys, values, or both keys and values
print(list(eggs.keys()))

print(list(eggs.values()))

print(list(eggs.items()))

# For loops can be used with these methods
for v in eggs.values():
    print(v)

# Multiple assignment can be used with dictionary.items() method. The method returns tuples (key, value)
for k, v in eggs.items():
    print(k, v)




    
