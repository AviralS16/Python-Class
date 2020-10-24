# First Challenge - This will tell if you are old enough to drive
print("This program will tell if you are old enough to drive")
MIN_DRIVING_AGE = 16

user_age = int(input("How old are you?: "))

if user_age >= 16:
    print("You are old enough to drive")
elif user_age < 16:
    print("You are not old enough to drive yet")

# Second Challenge - Pluralizing a word if greater than 2 using a for loop
print("This program will pluralizing a word if greater than 2 using a for loop")

games_won = int(input("How many games have you won?: "))
games_list = 0

for game in range(games_won):
    games_list += 1

if games_list >= 2 or games_list <= 0:
    print("You have won " + str(games_list) + " games.")
elif games_list == 1:
    print("You have won " + str(games_list) + " game.")

# Third Challenge - Countdown from 100
print("This program will countdown from 100")

numbers = 101

for number in range(numbers):
    print(number)

# Fourth Challenge - Accept a list of digits and print the smallest number possible from those digits
print("This program will accept a list of digits and print the smallest number possible from those digits")

digits = input("Enter a list of digits without commas or spaces: ")

digits_list = list(digits)
final_num = []

for digit in digits_list:
    minimum = min(digits_list)
    final_num.append(minimum)
    digits_list.remove(minimum)

str(final_num)

print("The minimum number you can make out of those digits is: " + str(final_num))
