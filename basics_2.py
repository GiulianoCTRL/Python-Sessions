"""
Writing our own functions
"""


# Function are defined with the def keyword
def function_name():
    return 5


# Functions can take arguments
def add_two_numbers(number1, number2):
    """Function docstring describing what the function does.

    :param number1:     Describe what number1 is and does
    :param number2:     Same for number2
    :return:            What does the function return?
    """
    return number1 + number2


# A better way to write a function
# Read this as function add_example takes an integer num1 and an integer num2
# and returns an integer
def add_example(num1: int, num2: int) -> int:
    """Add two numbers and return the result.

    :param num1:        First number to be added
    :param num2:        Second number to be added
    :return:            The result of num1 + num2
    """
    return num1 + num2


def greet(name: str) -> None:
    """Greet a person with name.

    :param name:    A name
    :return:        None
    """
    # If a function  does not use the return keyword, it will return None
    print("Hello " + name)
    # print(f"Hello {name}")