list('Hello')

name = 'Zophie'
name = [0]
print(name)

# Taking a section of a string
name[1:3]
print(name)

# Create a new string using slices
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

# References
spam = 42
cheese = spam
spam = 100
print(spam)

# When you assign a list to a variable, you assign a reference of the list to the variable
# The lists spam and cheese below are referencing the same list
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)

# Passing lists in function calls
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# For mutable data types such as lists. You are creating a reference to that list.

import copy

# Copy.deepcopy creates a separate list in memory. Modifying cheese doesn't modify spam
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)

 



