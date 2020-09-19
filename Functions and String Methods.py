def GCD(num1, num2):
    min = num2 if num1 > num2 else num1
    factor = 1

    for icount in range(1, min + 1):
        if num1 % icount == 0 and num2 % icount == 0:
            factor = icount

    return factor

# get numbers from input
def get_int():
    return int(input("Enter a number: "))

# main function

def main():
    val1 = get_int()
    val2 = get_int()
    print("The GCD of " + str(val1) + " and " + str(val2) + " is " + str(GCD(val1, val2)))

main()

# scopes

x = 10

def main():
    x = 10 # local variable
    print(x) # prints 10 because we are inside main, so local

main()
print(x) # prints 25 because we are outside main, so global


# g function
def g(x):
    def h():
        # h function
        x = "abc"
        print("Inside of H, x =", x)
    x += 1
    print("Inside of G, x =", x)
    h()
    return x

x = 3
z = g(x)

print("Outside of G and H. x =", x)
               
# string methods                   

name = "Aviral"

print(len(name))
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])

string = "abcdefgh"
print(string[3:6]) # starts at index 3, go till 5
print(string[3:6:2]) # starts at index 3, go till 5, increments by 2
print(string[::]) # prints the whole string
print(string[::-1]) # whole string backwards
# string[0] = "y" - gives an error, can't modify strings
message = "Quality, not Quantity"

for scount in range(len(message)):
    if message[scount] == "i" or message[scount] == "w":
        print("There is an i or w")

# Another better way to write loop then what's written above
for character in message:
    if character == "i" or character == "w":
        print("There is an i or w")


# python function that accepts a string
# calculates number of lower-case and upper-case letters
def calculate(phrase):
    numLower = 0
    numUpper = 0
    if character.isupper():
        numUpper += 1
    elif character.islower():
        numLower += 1
    else:
        print("Error reading string")
     
    print("Number of lower-case letters:", numLower)
    print("Number of upper-case letters:", numUpper)

print(calculate("The quick Brown Fox"))


                                                        