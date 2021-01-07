# The following operations depict the possible methods for python's lists
# Subject to change frequently


# ***********************************************
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of the number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list
# ***********************************************


# ***********************************************
# Negative indexing in lists
my_list = ['p','r','o','b','e']

print(my_list[-1])

print(my_list[-5])

# Expect:
# e
# p




# ***********************************************
# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

# Expect:
# ['o', 'g', 'r']
# ['p', 'r', 'o', 'g']
# ['a', 'm', 'i', 'z']
# ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']



# ***********************************************
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)

# Expect:
# [1, 3, 5, 7]
# [1, 3, 5, 7, 9, 11, 13]


# ***********************************************
# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd)

odd[2:2] = [5, 7]

print(odd)

# Expect:
# [1, 3, 9]
# [1, 3, 5, 7, 9]

# ***********************************************
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list

# Error: List not defined
print(my_list)

# Expect:
# ['p', 'r', 'b', 'l', 'e', 'm']
# ['p', 'm']
# Traceback (most recent call last):
#   File "<string>", line 18, in <module>
# NameError: name 'my_list' is not defined
