import Modules_Oct31
import math
from math import e


# object oriented programming (OOP)

# OOP terms
# classes: giving shape to things (baking set molds)
# objects: the things from the molded shape (sandcastle from bucket)

# OOP principles
# abstraction: don't need to know logic, we just know it gets things done
# encapsulation: holding all properties of something
# polymorphism: the ability to take on many forms
# inheritance: acquiring traits from parent

# BookStore class
class BookStore:
    numOfBooks = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        BookStore.numOfBooks += 1

    # book info function
    def bookInfo(self):
        print("Book title:", self.title)
        print("Book author:", self.author)

# BookStore objects
# each instance goes through __init__ automatically
book1 = BookStore("Great Expectations", "Charles Dickens")
book2 = BookStore("War and Peace", "Leo Tolstoy")
book3 = BookStore("The Lightning Thief", "Rick Riordan")
book4 = BookStore("The Idiot", "Fyodor Dostoevsky")

# calling member function for each object
# bookInfo is a normal function, so we need to call it
book1.bookInfo()
book2.bookInfo()
book3.bookInfo()
book4.bookInfo()

# print number of books
print("BookStore.numOfBooks: ", BookStore.numOfBooks)
# B1 is our object (shape from mold)
# BookStore() is our class (cookie shaper mold)

# printing attributes
print(book1.title)
print(book1.author)


# student class
class Student:

    # constructor (automatic initializer for objects)
    def __init__(self, name, town):
        self.name = name
        self.town = town

    # hello function
    def hello(self):
        print("Hello function is now called")
        print("Hello", self.name)

# main function
def main():
    # creates a student instance named Aviral
    Aviral = Student("Aviral", "Frisco")

    # printing object's attributes
    print(Aviral.name)
    print(Aviral.town)

    # calling member function on object
    Aviral.hello()

main()

# inheritance
# parent class Vehicle

class Vehicle:

    # constructor __init__
    def __init__(self, model, capacity, variant):
        self.model = model
        self.capacity = capacity
        self.variant = variant
    
    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model
    
    def getCapacity(self):
        return self.capacity
    
    def setCapacity(self, capacity):
        self.capacity = capacity

    def getVariant(self):
        return self.variant

    def setVariant(self, variant):
        self.variant = variant

# child class
# pass name
class Taxi(Vehicle):

    # constructor __init__
    def __init__(self, model, capacity, variant, color):
        # calling parent's constructor to set model, capacity, variant, and color
        super().__init__(model, capacity, variant)
        self.color = color

    # taxi info member function
    def taxiInfo(self):
        return self.getModel() + " " + self.getVariant() + " in " + self.color + " with " + self.getCapacity() + " seats."


vehicle1 = Taxi("Fortuner", "7", "MT2755", "White")
print(vehicle1.taxiInfo())

# super() allows us to access inheritence functions

print(Modules_Oct31.add(4, 5.5))

print("The value of pi is: ", math.pi)

print("Thr value of e is: ", math.e)
