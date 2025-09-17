# Base class
class Shape:
    def __init__(self, name):
        self.name = name
        print(f"Initializing Shape: {self.name}")

    def calculate_area(self):
        print("Calculating area in Shape (generic placeholder).")
        return 0   # Base placeholder


# Derived class
class Rectangle(Shape):
    def __init__(self, width, height):
        # Call Shape's constructor using super()
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        # Call base class method (not constructor) with super()
        super().calculate_area()   # demonstrates use of super
        return self.width * self.height


# Example usage
rect = Rectangle(10, 5)
print(f"The area of the {rect.name} is: {rect.calculate_area()}")
