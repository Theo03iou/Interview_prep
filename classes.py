# A class is a blueprint for creating objects, which represent entities with properties (attributes) and behaviours (methods).
# Classes let you bundle related data and functions into one organised structure


# 1. Defining a class
class Dog:
    pass


# 2. Creating an Object (Instance) of a Class
# Once a class is defined, you can create an instance (object) of the class.
# Each instance can hold its own data but shares the class structure

my_dog = Dog()


# 3. Adding Attributes and Methods
# You can add attributes to the class using the __init__ method, which is a special methods called the initialiser or constructor.
# This methods runs automatically when a new object is created

class Dog:
    # def init method to inisialise attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display a greeting
    def bark(self):
        return f"{self.name} says woof!"

    def desc(self):
        return f"{self.name} is {self.age} years old!"


my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(my_dog.desc())


# 4. Modifying Attributes
my_dog.age = 4
print(my_dog.age)


# 5. Inheritance: Creating Subclasses
# Inheritance allows you to create new class based on an existing class, inheriting all of its attributes and methods while...
# adding new ones or modifying existing ones.

class Animal:
    def __init__(self, species):
        self.species = species
        
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog") # Call the parent class's init
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says woof!"
    
my_dog = Dog("Buddy", 10)
print(my_dog.species)
print(my_dog.bark())


# EXERCISE - Creating a Car Class

# Define a Car class.
# Add an __init__ method that initializes make, model, and year attributes.
# Add a method start() that returns a string like "The car is starting".
# Create an instance of Car and call its start() method.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        return "The car is starting"
    
    def desc(self):
        return f"{self.make} {self.model}, {self.year} "
    
my_car = Car("Honda", "civic", 2007)

print(my_car.desc())