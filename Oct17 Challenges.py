# First Challenge - Multiply 2 numbers without using "*"
print("This will multiply 2 numbers without using *")
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a second number: "))

answer = num_1

while num_2 > 1:
    answer += num_1
    num_2 -= 1


print("The answer is: " + str(answer))

# Second Challenge - Get three color codes for red, blue, and green, and add a specific number so each color = 255
print("This will get three color codes for red, blue, and green, and add a specific number so each color = 255")
Red = int(input("Enter your color code for red: "))
Blue = int(input("Enter your color code for blue: "))
Green = int(input("Enter your color code for green: "))

red_color_code = 255 - Red
blue_color_code = 255 - Blue
green_color_code = 255 - Green

print("The color code for red to equal 255 is: " + str(red_color_code))
print("The color code for blue to equal 255 is: " + str(blue_color_code))
print("The color code for green to equal 255 is: " + str(green_color_code))

# Third Challenge - Calculates speeding ticket
print("This calculates how many speeding tickets you have")
speed = int(input("How fast are you driving in mph?: "))
if_birthday = input("Is it your birthday? (Yes or no): ")
birthday = False

if if_birthday.title() == "Yes":
    birthday = True
elif if_birthday.title() == "No":
    birthday = False
else:
    print("I don't understand")


if birthday:
    if speed <= 65:
        print("You have 0 speeding tickets.")
    elif speed >= 66 and speed <= 85:
        print("You have one speeding ticket.")
    elif speed >= 86:
        print("You have 2 speeding tickets.")
elif birthday == False:
    if speed <= 60:
        print("You have 0 speeding tickets.")
    elif speed >= 61 and speed <= 80:
        print("You have one speeding ticket.")
    elif speed >= 81:
        print("You have 2 speeding tickets.")

# Fourth Challenge - Calculates when Alarm clock should ring
print("This calculates when your Alarm clock should ring")
print("Number for each day of the week: 1 = Sun, 2 = Mon, 3 = Tue, 4 = Wed, 5 = Thurs, 6 = Fri, 7 = Sat")

vacation = False
day_of_week = input("What day of the week is it using the numbers above?: ")
if_vacation = input("Are you on vacation? (Yes or No): ")

if if_vacation.title() == "Yes":
    vacation = True
elif if_vacation.title() == "No":
    vacation = False

if vacation == True and day_of_week == "2" or "3" or "4" or "5" or "6":
    print("Set your alarm clock to wake you up at 10:00 AM.")
elif vacation == True and day_of_week == "1" or "7":
    print("Turn your alarm clock off.")
else:
    print("I don't understand.")

if vacation == False and day_of_week == "2" or "3" or "4" or "5" or "6":
    print("Set your alarm clock to wake you up at 7:00 AM.")
elif vacation == False and day_of_week == "1" or "7":
    print("Set your alarm clock to wake you up at 10:00 AM.")
else:
    print("I don't understand.")
