#!/usr/bin/env python3
"""
This is used for testing python.
"""
# Comment
# First part modules come first
# When file executed, the sys module will create a list of arguments used
import sys

# empty line between first party module and third party module
# Imports a third party module named requests (handles http request)
# Install with "pip3 install requests"
import requests


a_string = "Djibril"
an_integer = 5
a_float = 3.14
# First index is always 0, so below is three items long with indexes 0, 1, 2
a_list = ["Hi", 4, 2.7]  # A List can contain any type
a_boolean = True  # True or False
no_type = None  # No data, no value

# Keywords: def, return, for, while, if, ...


# print(a_string + " is cool")
# print(an_integer + 5)

# print("Hello " + a_string)
# print("Hello " + "Giuliano")


def greet(name: str):
    # print("Hello " + name + "!" + "You, Sir " + name + " are awesome!")
    print(f"Hello {name}! You, Sir {name} are awesome!")


# greet("Djibril")
# greet("Giuliano")

# Read as "Function get_website takes a string as argument and returns a string"
def get_website(url: str) -> str:
    """Get website via GET request and print it.
    
    :param url:     URL to a website
    :return:        The content of the website as string
    """
    req = requests.get(url)
    req.raise_for_status()
    print(req.text)


# If the file is executed
# If internal name of this file is __main__ (Execute via command line) than call function get_website
if __name__ == "__main__":
# sys.argv is a list of command line arguments
# sys.argv[0] is the name of the script. E.g. session_1.py
# sys.argv is a list that looks in this example like:
# ["session_1.py", "https://raw.githubusercontent.com/GiulianoCTRL/PillarCandy/main/README.md"]
    get_website(sys.argv[1])
