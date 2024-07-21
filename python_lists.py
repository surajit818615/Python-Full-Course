
    # Lists are ordered collection of data items.
    # They store multiple items in a single variable.
    # List items are separated by commas and enclosed within square brackets [].
    # Lists are changeable meaning we can alter them after creation.
list1 = [1,2,3,4,5,6,7,8,9]
list2 = ["Red","Green","Blue"]
print(list1)
print(list2)

#Ex -2
details =["Surajit",21,"ECE",8.35]
print(details)

#list indexes: -Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

#Ex -3
colors1 = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors1[2])
print(colors1[4])
print(colors1[0])

# Negative Indexing:

# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

# EX -4
colors2 = ["Red", "Violet", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors2[-3])
print(colors2[-4])
print(colors2[-1])

# Check whether an item in present in the list?

# We can check if a given item is present in the list. This is done using the in keyword.
#ex-5
colors3 = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors3:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

# Ex-6
colors4 = ["Red", "Green", "Blue", "Yellow", "Pink"]
if "Orange" in colors4:
    print("Orange is present.")
else:
    print("Orange is absent.")

# Range of Index:

# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

#EX-7
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes
print(animals[1:8:3])

# List Comprehension

# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings

# EX-8

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)