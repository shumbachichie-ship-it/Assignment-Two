# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method in the base class
    def description(self):
        return f"This is a vehicle: {self.brand} {self.model}"


# Subclass Car
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)   # Call base constructor
        self.doors = doors

    # Overriding the method
    def description(self):
        return f"This is a car: {self.brand} {self.model} with {self.doors} doors."


# Subclass Bike
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    # Overriding the method
    def description(self):
        return f"This is a {self.bike_type} bike: {self.brand} {self.model}."


# Example usage
v = Vehicle("GenericBrand", "X1")
c = Car("Toyota", "Corolla", 4)
b = Bike("Yamaha", "R15", "Sport")

print(v.description())  # Uses base class method
print(c.description())  # Uses overridden method in Car
print(b.description())  # Uses overridden method in Bike

