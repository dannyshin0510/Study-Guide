# The following operations depict the possible methods for python's lists
# Subject to change frequently

#Dictionaries

# ***********************************************
# clear()	Removes all items from the dictionary.
# copy()	Returns a shallow copy of the dictionary.
# fromkeys(seq[, v])	Returns a new dictionary with keys from seq and value equal to v (defaults to None).
# get(key[,d])	Returns the value of the key. If the key does not exist, returns d (defaults to None).
# items()	Return a new object of the dictionary's items in (key, value) format.
# keys()	Returns a new object of the dictionary's keys.
# pop(key[,d])	Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
# popitem()	Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
# setdefault(key[,d])	Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).
# update([other])	Updates the dictionary with the key/value pairs from other, overwriting existing keys.
# values()	Returns a new object of the dictionary's values
# ***********************************************


# ***********************************************
# Creating dictionaries
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])



# ***********************************************
# List slicing in Python

# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])

# Expect:
# Jack
# 26
# None
# Traceback (most recent call last):
#   File "<string>", line 15, in <module>
#     print(my_dict['address'])
# KeyError: 'address'



# ***********************************************
# Changing elements
# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

# Expect:
# {'name': 'Jack', 'age': 27}
# {'name': 'Jack', 'age': 27, 'address': 'Downtown'}


# ***********************************************
# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Expect:
# 16
# {1: 1, 2: 4, 3: 9, 5: 25}
# (5, 25)
# {1: 1, 2: 4, 3: 9}
# {}
# Traceback (most recent call last):
#   File "<string>", line 30, in <module>
#     print(squares)
# NameError: name 'squares' is not defined
