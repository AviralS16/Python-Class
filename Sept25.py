# lists - ordered sequence of data
# can contain mixed types of data
# are mutable

sample_list = [2, "a", 4, [100, 200]]
print(len(sample_list))
print(sample_list[0] + 1) # adds 1 to 2
print(sample_list[3][0])
print(sample_list[2])


sample_list[2] = 5
print(sample_list)

for element in sample_list:
    print(element) # prints each element on a new line


# appending to a list
sample_list.append("hello")
print(sample_list)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# removing elements
list3.remove(5)
print(list3)

del(list3[1])
print(list3)

del(list3[1]) # del(list_name[index] will be removed)
print(list3)

list3.pop() # removes last element
print(list3)

message = "i <3 cs"
message_to_list = list(message)
print(message_to_list) # makes string into list

list_to_string=  "".join(message_to_list)
print(list_to_string)

blob = [43, 432, 9873, 12, 43234, 7647]
blob.sort() # list in least to greatest
print(blob)

blob.reverse() # prints list backwards
print(blob)

# Tuples
# Ordered sequence of elements, multiple types
numTuple = (1, 2, 3)
# also define tuples without the "()".
numberTuple = 1, 2, 3
# tuples are immutable, whereas lists are 
# recommend tuple uasge if you just want to iterate over

print(numTuple, type(numTuple))

# can print these out like list
print(numTuple[0])

# you cannot modify a tuple
# numTuple[1] = 0       : you will get an error
# you also cannot do .append(), .remove(), .pop()

# converting lists to tuples, vice versa
randomList = [3, "orange", 39]
print(tuple(randomList)) # converts into tuple

randomTuple = ("apple", 3231, "Ocean")
print(list(randomTuple)) # converts into list

# list of tuples
report = [("Aviral", 4.0), ("Ronak", 4.0), ("Kate", 4.0), ("Aadi", 4.0)]

for student in report:
    for gpa in student:
        print(gpa)

# tuple of tuples
tupleSquared = (("x, y, z"), ("X, Y, Z"))
print("This is a tuple of tuples: " +  str(tupleSquared))

# "modifying" a tuple
anotherTuple = (34, "a", 432423, [88, 89])

# we can change the value of mutable elements in a tuple
# in this case, our list is mutable
# tupleName[IndexOfListInTuple][index to modify]
anotherTuple[3][0] = 4343434
anotherTuple[3][1] = "almond"

print("This is our tuple after modifying" + str(anotherTuple))

# dictionaries 
# key : value
# dictioanries do not have an order
# dictionaries must have a key and a value, where lists just have values

# define a balnk dictionary
blank_dictionary = {}

# define a dictionary with numeric keys
num_dictionary = {1: "soccer", 
                  2: "baseball"}


# dictionaries can support mixed data types

mix_dictionary = {"class": "python", 
                  "students" : [0, 1, 2, 3] }
print(mix_dictionary)

# iterating through dictionary
directory = {"Student Name" : "Barry",
             "Subject": "Biology",
             "Classroom" : 213}

for keys in directory:
    print(keys)


# printing out keys and values
print("{Keys}:{Values}")
for keys, value in directory.items():
    print(str(keys) + ": " + str(value))

# add to dictionary
# dictionaryName[Key] = Value
directory["Hallway"] = "J"
print(directory)

# removing from dictionary
# dictionaryName.pop
directory.pop("Hallway")
print(directory)

# removes random element
directory.popitem

# deletes all items
directory.clear
print(directory)

# eliminating the dictionary object
# del dictionaryName
del directory
# print(directory) - error, directory is deleted at this point
