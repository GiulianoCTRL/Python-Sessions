"""
Code that goes with the classes shorts and session from 2021-04-27.

Important terms:
Instance:   A unique part of a class. Each instance has their own information.
            An instance is referred to by the self variable in the class.
Initialize: When the instance is created e.g. car = Vehicle("brand", "name") it is
            populated with information about this particular instance. In
            the above example the car instance would contain the information about
            brand and name.
Property:   Variables of the class instance. E.g. car.brand (self.brand).
Method:     A function that only applies to the class e.g. car.move().
Attribute:  An attribute is either a method or a property of a class.
"""


# Class keyword to define a class, no use of brackets
class Vehicle:
    """Class defining vehicles."""

    # The __init__ function initializes an instance of a class
    # Self is used to refer to an instance itself
    # (Remember, an instance is a unique part of a class.)
    def __init__(self, brand: str, model: str):
        """Initialize Vehicle with brand and model."""
        self.brand = brand
        self.model = model
        # We can define new properties without needing to pass them to the
        # __init__ function.
        self.location = 0

    # A function of a class should use the self keyword to apply to a
    # particular instance of the class
    def move(self):
        """Move vehicle."""
        # If self.location was 0 it is now 1, the next time we use move()
        # it will be 2 and so on. The instance is always aware
        # of all the different poperties of a class.
        self.location += 1
        print(f"{self.brand} {self.model} moved to {self.location}.")

    def move_back(self):
        """Mmove car one step back."""
        self.location -= 1
        print(f"{self.brand} {self.model} moved back to {self.location}.")


# Initializing/Instantiating a new instance of the vehicle class
car1 = Vehicle("Toyota", "Yaris")
car2 = Vehicle("Fiat", "500")

plane1 = Vehicle("Boeing", "777")

# We move car2 and car1. As they both are unique instances of the Vehicle
# class their properties are kept separate. So calling .move() on car1 does not
# affect car2 in any way.
car2.move()
car1.move()
car2.move_back()
car2.move_back()
car1.move()
car1.move_back()
car1.move()
car1.move()
car1.move()
print("property:", "car1", "car2")
print("brand:", car1.brand, car2.brand)
print("model:", car1.model, car2.model)
print("location:", car1.location, car2.location)
