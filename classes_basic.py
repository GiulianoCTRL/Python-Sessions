"""
Classes are often used to create objects with specific functions, that
can also hold data. Additionally, the can be used to create own types/objects
or make use of inheritance.
"""


# Classes are defined with the class keyword and make use of UpperCamelCase
# instead of the usual snake_case
class Vehicle:
    """A class docstring works the same as a function docstring, it
    should describe the class and any eventual parameters that the class
    takes.

    :param colour:      The vehicles colour
    """

    # The __init__ function initializes the class, this will mean that
    # every instance of this class will start with the below values
    def __init__(self, colour: str):
        """Initialize the class with the values of speed and x_pos."""
        self.colour = colour
        self.speed = 0
        self.distance = 0

    # self is a keyword representing a specific instance of the class.
    # Each newly created instance has therefore it's own values
    def move(self, distance: int):
        """Increase the position of the vehicle instance by distance.

        :param distance:        Amount by which to increase the current distance
        :return:                None
        """
        # += is shorthand for writing self.distance = self.distance + 1
        self.distance += distance


# What is an instance?
ferrari = Vehicle("Red")
lamborghini = Vehicle("Orange")
# The above are two different instances of the same class. They both have are
# Vehicles, but have their own properties

# Let's change the value of speed
ferrari.speed = 177
lamborghini.speed = 201

# And call the method (a function in a class) move
ferrari.move(12000)
lamborghini.move(7000)

# The type function returns the type of an object
print(ferrari.speed, ferrari.distance, ferrari.colour, type(ferrari))
print(lamborghini.speed, lamborghini.distance, lamborghini.colour, type(lamborghini))


# Some vehicles might differntiate or have more properties, this is where inheritance
# comes into play

# class Plane inherits from vehicle
# Plane is called a child- or sub-class and Vehicle a parent- or super-class
class Plane(Vehicle):

    # We need a init function again
    def __init__(self, colour: str):
        # Use the init function of the super class with the super() function.
        super().__init__(colour)
        self.height = 0
        self.on_ground = True

    def land(self):
        if self.on_ground:
            print("Already landed")
        else:
            self.on_ground = True

    # Only one new line after class methods
    def take_off(self):
        if self.on_ground:
            self.on_ground = False
        else:
            print("Already in air")


boeing = Plane("white")
# We can still use the move method, as it is defined in the parent class
boeing.move(100)
# But we can also use the take_off method
# We do not need to pass self! self is already passed as we are calling this from
# a specific class instance.
boeing.take_off()
print(boeing.colour, boeing.on_ground, boeing.distance, type(boeing))

