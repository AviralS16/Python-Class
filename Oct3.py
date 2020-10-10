# list problem/exercise/brain activity 1
# create a list named sales
# create a loop to enter store sale's for 7 days
# print the total amount of sales

sales = []
list1 = []

for day in range(7):
    day_sales = float(input("Enter the store's sales: $"))
    sales.append(day_sales)

totalSales = 0
for element in sales:
    totalSales += element

print("The total is: " + str(totalSales))


# list problem/exercise/brain activity 2
# create a list of 10 postive and negative numbers
# print the number of negative numbers
# print the number of positive numbers
# print the number of zeroes

numbersList = [123, 456, 789, 0, -123, -456, -789, 0, 100]

positive_numbers = 0
negative_numbers = 0
zeroes = 0


for elem in numbersList:
    if elem > 0:
        positive_numbers += 1
    elif elem < 0:
        negative_numbers +=1
    elif elem == 0:
        zeroes += 1

print("The number of positive numbers is: " + str(positive_numbers))
print("The number of negagtive numbers is: " + str(negative_numbers))
print("The number of zeroes is: " + str(zeroes))



# extended brain exercise for 2
# print average of positive numbers
# print average of negative numbers

positive_total = 0
negative_total = 0

for elem in numbersList:
    if elem > 0:
        positive_total += elem
    elif elem < 0:
        negative_total += elem
    else:
        continue

positive_average = (positive_total / positive_numbers)
negative_average = (negative_total / negative_numbers)
print("The average of the postive numbers is: " + str(positive_average))
print("The average of the negative numbers is: " + str(negative_average))

# tuples, like lists but are IMMUTABLE - you can't modify once declared

example_tuple = ("hello", 54678, 242, [1, 2], (234, 567))
# exampleTuple[0] = 234 will return an error, can't modify tuples

# can modify a tuple if that data structure is Mutable
print("Tuple before Modification: " +  str(example_tuple))

# modifying list at index 2
example_tuple[3][0] = "almond" # tupleName[listIndex][index to change]

print("Tuple after Modification: " + str(example_tuple))


# dictionary activity
# dictionaries - key : value

done = False
friends = {"Andrew" : "Plano", "Charlie" : "Fort Worth", "Daniel" : "Richardson"}

while not done:
    print("Welcome to the friend example!")
    print("S - Show friends and the city they live in")
    print("A - Add a friend and their city they live in")
    print("D - Deleting a friend and the city they live in")
    print("P - Print friends and the city they live in")
    print("Q - Quit")
    

    choice = input("Enter an option: ")

    # show key and values in dictionary
    if choice.upper() == "S":
        print("This option will list the friends and the city they live in.")
        for key in friends:
            print(key, "/", friends[key])

    elif choice.upper() == "A":
        # dictionaryName[key] = value -> syntax for adding to dictionary
        friends["Jake"] = "Denton"

    # deleting specific from dictionary
    elif choice.upper() == "D":
        # dictionaryName.pop(key)
        friends.pop("Andrew") 

    elif choice.upper() == "P":
        print(friends)

    # quit
    elif choice.upper() == "Q":
        print("Have a good day!")
        done = True
    
    # error checking
    else:
        print("I don't understand")
