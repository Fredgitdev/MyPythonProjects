#Functions
#1. User-defined functions - users defines
#2. Built-in library defined

#Built-in Library functions
#max stores the max value in y
y = max(56,34,34,12,55)
print(y)

#min stores the min value in x
x = min(43,65,89,42,51)
print("The minimum value is", x)

z = pow(2, 3)
print("The result is",z)

#User-defined Functions
def greetings():
    print("Hello there!")
greetings()  #Calling a user-defined function


def multiply():
    num1 = 23
    num2 = 10
    print(num1 * num2)

multiply()

#Parameters/Variable and Arguments/Values

def add(a, b):
    print(a + b)

add(3,4)
add(45, 60)
add(15, 30)

def employee(fullname, age, position, status):
    print(fullname,age,position,status)


employee("Mark Joe", 45, "CEO", "Married")
employee("Mary Jane", 35, "HR", "Single")
employee("Job Harry", 27, "Clerk", "Married")








