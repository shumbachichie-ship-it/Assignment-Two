import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Function to calculate total area using polymorphism
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()  
    return total


# Example usage
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 7)
]

print("Total Area:", total_area(shapes))
