#having same method across all  classes
#but with different implementations

class Rectangle:
    def shape(self):
        print("Drawing a Rectangle")

class Parallelogram:
    def shape(self):
        print("Drawing a Parallelogram")

class Rhombus:
    def shape(self):
        print("Drawing a Rhombus")


#creating an object for each class
r = Rectangle()
r.shape()

p = Parallelogram()
p.shape()

rhom = Rhombus()
rhom.shape()



# Demonstrating polymorphism with same method across all classes, each with a unique implementation

class Rectangle:
    def shape(self):
        print("Drawing a Rectangle")  # Implementation specific to Rectangle

class Parallelogram:
    def shape(self):
        print("Drawing a Parallelogram")  # Implementation specific to Parallelogram

class Rhombus:
    def shape(self):
        print("Drawing a Rhombus")  # Implementation specific to Rhombus

# Creating a list of objects of different shapes
shapes = [Rectangle(), Parallelogram(), Rhombus()]

# Demonstrating polymorphism using a loop
# Each object calls its own version of shape() method, regardless of its class
for shape in shapes:
    shape.shape()  # Polymorphic behavior: calls the shape method specific to each class

