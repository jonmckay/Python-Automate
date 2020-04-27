# Getting the index of an item in a list
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

# Adding an item to the end of a list
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

# Inserting an item at index 1
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

#Removing a specific item
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

# Deleting an item from a list at an index
del spam[0]
print(spam)

# Below is an example of sorting a list of numbers
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

# Below is an example of sorting ASCII-betically (capital before lowercase) strings
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# Another example showing sort() not sorting alphabetically but by ASCII
spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

# To sort in a true alphabetical order
spam.sort(key=str.lower)
print(spam)

