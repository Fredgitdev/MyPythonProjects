number = 2 #Integer
second = 56.78 # float
text = "Hello there" #String
isPythonInteresting = True #Boolean


print(number)
print(second)
print(text)
print(isPythonInteresting)

#Data Structures - Allow you to store multiple values in a single variable
cars = ["toyota", "nissan", "vw"] #List - Ordered and changable
fruits = ["banana", "orange", "apple"] #Tuple - Ordered but unchangable
countries = {"Kenya", "Tunisia", "Algeria"} #Set - Ordered, Unchangable(Immutable) uses curly braces - changes when run
student = {
    "first_name": "Mary",
    "last_name": "Njo",
    "age": 23, #number
    "course": "web-development",
    "nationality":"Kenyan"
}   #This is a dictionary with keys and values

print(cars)
print(fruits)
print(countries)


print(student["nationality"])

#Typecasting - converting from one data type to another

print(float(number))
print(int(second))