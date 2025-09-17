# Function that uses polymorphism
def process_sound(sound_object):
    # It doesn't care what type of object it is,
    # as long as it has a make_sound method
    print(sound_object.make_sound())


# Dog class
class Dog:
    def make_sound(self):
        return "Woof! Woof!"


# Cat class
class Cat:
    def make_sound(self):
        return "Meow~"


# Example usage
dog = Dog()
cat = Cat()

process_sound(dog)  # Output: Woof! Woof!
process_sound(cat)  # Output: Meow~
