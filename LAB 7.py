'''Question 1: Create a class Person with attributes name and age, and a method display() that prints the name and age. Then, create a subclass Student that inherits from Person and adds an attribute student_id. Write a method show_details() in Student to print all details, including student_id.
Question 2: Create a class Vehicle with a method info() that prints "This is a vehicle". Inherit Car from Vehicle and add a method car_info() to print "This is a car". Further, create another subclass ElectricCar that inherits from Car and adds a method battery_info() to print "This car has a battery." Demonstrate how multilevel inheritance works by calling all methods from an ElectricCar object.
Question 3: Create two classes Teacher and Author, each with their own description() method to describe the profession. Then, create a subclass TutorAuthor that inherits from both Teacher and Author. Use this subclass to call the description() method from each parent class. Use the super() function to resolve any conflicts if necessary.
Question 4: Create a class Animal with a method sound() that prints "Animals make sound". Then create two subclasses Dog and Cat, each with their own version of sound() method that prints "Dog barks" and "Cat meows" respectively. Demonstrate hierarchical inheritance by calling the sound() method from both Dog and Cat objects.

ANSWERS'''

# Question 1: Person and Student
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_details(self):
        self.display()
        print(f"Student ID: {self.student_id}")

# Question 2: Vehicle, Car, and ElectricCar
class Vehicle:
    def info(self):
        print("This is a vehicle")


class Car(Vehicle):
    def car_info(self):
        print("This is a car")


class ElectricCar(Car):
    def battery_info(self):
        print("This car has a battery.")

# Question 3: Teacher, Author, and TutorAuthor
class Teacher:
    def description(self):
        print("This is a teacher")


class Author:
    def description(self):
        print("This is an author")


class TutorAuthor(Teacher, Author):
    def description(self):
        super(Teacher, self).description()  # Explicitly call Author's method
        Teacher.description(self)          # Explicitly call Teacher's method

# Question 4: Animal, Dog, and Cat
class Animal:
    def sound(self):
        print("Animals make sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")