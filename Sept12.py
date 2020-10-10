# if statemant - executes when condition is true
# if <condition>:
    # <expression>
# else: - executes when (if) is false
#   <expression>

# if/elif/else - if, else if, else:
    # <expression>

# else:
#    <expression>

# ask user if they are hungry
hungry = input("Are you hungry: ")

# if yes, go to store
if hungry.lower() == "yes":
    print("Go to the store")

    cost = float(input("What is the price of a chocolate bar? $"))
    
    if cost < 1.00:
        print("Buy 3 chocolate bars")
    else: 
        print("You can only afford 1.")

# else, do not not hungry
else:
    print("You are not hungry.")



game = input("Do you want to play a video game? ")

if game.title() == "Yes":
    print("GLHF")
elif game.title() == "No":
    print("Watch TV")
else:
    print("I dont understand")

# if var1 > var2
# if var1 >=var2
# if var1 <= var2
# if var1 < var2
# if var1 == var2
# if var1 != var2

# not, and, or
# status - true
# playing - true
# if not status - false
# if status - True
# if status and playing - True 
# if status or playing - True
# if status not playing - False



# while loops - while <condition> is true:
#                    <execution>
#                    stepper_variable += 1

counter = 0
name = input("Enter your name: ")
while counter < 10:
    print("Hello " + name + "!")
    print("We are on iternation " + str(counter) + "!")
    counter += 1
print("End")

total = 0 
number = int(input("Enter a number(Enter 0 to end): "))
while total != 0:
    total += number
    print ("the total is "  + str(total))
    print(number)
print("Total: " + str(total))

# for loop - for x in range(5)
# for loop - for x in range(5,7)
# for loop - for x in range(5, 17, 2)

mySum = 0
for counter in range(5, 11, 2):
    mySum += counter

    if mySum == 5:
        break
print(mySum)

n = 0
while n < 5:
    print(n)
    n += 1

for n in range(5):
    print(n)

# for loops
# know the number of iterations
# uses a counter
# can rewrite for loops using a while loop

# while loops
# unknown number of iterations
# can use a counter, but must initialize before loop
# requires increment of counter variable
# may not be able to rewrite while loop as for loop

# menu
done = False
while not done: 
    print("Welcome to the Menu!")
    print("I - Introductory Problem")
    print("Q - Quit")
    print("E - Print even numbers")

    option = input("Enter an option")
    if option.upper() == "I":
        print("We are doing the introductory problem")

        counter = 0
        name = input("What is your name: ")

        while counter < 5:
            print(name)
            counter += 1

    elif option.upper() == "E":
        print("Printing even numbers between 1 and 20.")
        
        for even in range(2, 11, 2):
            print(even)

    elif option.upper() == "Q":
        print("We are now exiting")
        print("Have a good day!")
        done = True

    else:
        print("I don't understand")

