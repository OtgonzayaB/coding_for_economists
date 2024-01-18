# In this file we will look at lists, dictionaries, set, tuples, range.

# List
myList = [1, 2, 3, 4, 5]
print(myList)

print(type(myList)) #<class 'list'>

# Grab the first object in the list
print(myList[0]) # 1

# How many objects are in our list?
print(len(myList)) # 5
print("Our list object myList had {len(myList)} elements.")

# Nice thing about lists: they are flexible with respect to the data type
mixedList = [1, 'two', 3.0, [4, 'four'], 5]
print(mixedList)

# We can also add and remove objects from a list.
mixedList.append(6)
print(mixedList)

#Removing
mixedList.pop() #Without argument, removes last item
print(mixedList)

# How many times does the integer 1 appear?
print(mixedList.count(1)) # 1

# Reverse a list
mixedList.reverse()
print(mixedList)