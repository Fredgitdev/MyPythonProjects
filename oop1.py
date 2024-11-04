#CLASS SHOULD HAVE
#Behaviors - Methods - functions
#Properties - Variables

# Steps of creating a class
# 1. class Name
# 2. properties = "variables"
# 3. behaviours (functions)


class Student:
    #Properties/Variables/Characteristics/Attributes
    name = "Joe"
    age = 23

    #Behaviours/Methods/Functions
    def study(self):
        print("Student is studying")
    def graduating(self):
        print("Student is also graduating")

# Instanciating an object ie object creating from a class

student1 = Student() #Instantiating/ Creating object

student1.study()
print(student1.name)
print(student1.age)

student1.graduating()
