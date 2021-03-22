"""
Simple script to convert a serial number to a string without colons and lower case.
"""

import sys


def convert_serial(serial: str) -> str:
    """Convert serial to lower case and remove colons.
    
    :param serial:      Serial number to be converted
    :return:            A new converted string
    """

    # Replace returns string without colons, and lower() operates on that string,
    # converting it to lower case
    return serial.replace(":", "").lower()

# global variables are usually capitalized
# SERIAL = "bl:ah:"
# local variable in lower case, can't be used outside of function (their scope)

# Operators:
# == Equal
# != Not equal
# "not =="" is the same as "!="
if __name__ == "__main__":
    # For every argument in the argument list (example line 35) print the result
    # of our convert_serial function
    for argument in sys.argv[1:]:
        print(convert_serial(argument))

# excercises.py SERIAL 2 3
# -> argv = ["exercise_1.py", SERIAL, 2, 3, ffff]
