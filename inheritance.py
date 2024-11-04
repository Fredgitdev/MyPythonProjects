# A concept of borrowing properties and methods from a parent class using inheritance

# Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

# Child class inheriting from the Animal class
class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog is barking")

# Creating objects for each class
a = Animal()
b = Dog()

# Calling methods to demonstrate inheritance
a.speak()  # This calls the speak method from the Animal class
b.speak()  # Inherited method from the Animal class
b.bark()   # Method defined in the Dog class
