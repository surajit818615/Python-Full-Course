# list.sort()

# This method sorts the list in ascending order. The original list is updated
colors1 = ["voilet", "indigo", "blue", "green"]
colors1.sort()
print(colors1)

num1 = [4,2,5,3,6,1,2,1,2,8,9,7]
num1.sort()
print(num1)
#ex-2
colors2 = ["voilet", "indigo", "blue", "green"]
colors2.sort(reverse=True)
print(colors2)

num2 = [4,2,5,3,6,1,2,1,2,8,9,7]
num2.sort(reverse=True)
print(num2)

# reverse()

# This method reverses the order of the list.
colors3 = ["voilet", "indigo", "blue", "green"]
colors3.reverse()
print(colors3)

num3 = [4,2,5,3,6,1,2,1,2,8,9,7]
num3.reverse()
print(num3)

# index()

# This method returns the index of the first occurrence of the list item.
colors4 = ["voilet", "green", "indigo", "blue", "green"]
print(colors4.index("green"))

num4 = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num4.index(3))

# count()

# Returns the count of the number of items with the given value.

colors5 = ["voilet", "green", "indigo", "blue", "green","green"]
print(colors5.count("green"))

num5 = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num5.count(3))

# copy()

# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

colors6 = ["voilet", "green", "indigo", "blue"]
newlist = colors6.copy()
newlist[0] = 0 
print(colors6)
print(newlist)

# append():

# This method appends items to the end of the existing list.

colors7 = ["voilet", "indigo", "blue"]
print(colors7)
colors7.append("green")
print(colors7)

# insert():

# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

colors8 = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors8.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors8)

# extend():

# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

#add a list to a list
colors9 = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors9.extend(rainbow)
print(colors9)

# Concatenating two lists:

# You can simply concatenate two lists to join two lists.
colors10 = ["voilet", "indigo", "blue", "green"]
colors11 = ["yellow", "orange", "red"]
print(colors10 + colors11)