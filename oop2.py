#instead of directly assigning values to
#variables, use init to work with different values

class Person:
    def __init__(self, name, age, gender):
#values that are to be assigned to the variables name, age and gender should go to their respective variables
        self.name = name
        self.age = age
        self.gender = gender

    def movement(self):
        print("Person is walking")
    def standing(self):
        print("Person is standing")

#creating an object from the class
a = Person("Joe", 34, "Male")
print(a.name)
print(a.age)
b = Person("Mary", 21, "Female")
print(b.name)
c = Person("John", 45, "Male")
print(c.name)
print(c.gender)
