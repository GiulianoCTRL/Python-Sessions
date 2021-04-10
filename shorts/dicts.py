"""
Code that goes with the dicts video.
"""

# Dictionaries are defined by curly brackets and contain key: value pairs.
settings = {
    "SSH enabled": True,
    "Camera": 3,
    "IR cut": False,
    "supported_versions": ["0.1", "1", "2.1"],
}

# Similar to lists and indexes we use square brackets to find a key in a dictionary,
# however, we cannot use index numbers, but must use key names instead.
settings["lang"] = "en"
settings["SSH enabled"] = False
settings["Recording"] = "Intruder.mkv"

# If trying to print a key that doesn't exist e.g. print(settings["Nani?"]) your
# program will crash with a key error (Key does not exist). If we are unsure if a
# given key exists in a dictionary (often abbreviated as dict) we use the .get method
# of the dictionary type to search for the key and return it. If the key does not exist
# the function will return None without crashing your program

if settings.get("Recording"):
    print(f"Recording is called {settings['Recording']}.")
else:
    # The dict type has three useful methods to iterate over it:
    # .keys() which yields (returns one by one until empty) all keys in the dictionary
    # .values() which does the same for values and
    # .items() which will return a tuple (In short a list that cannot be changed) containing
    # the key and it's value (key, value)

    # For loops can initialize more than one variable. As we know we always have one key
    # and one value we can therefore intialize them every time with a for loop.
    for key, value in settings.items():
        print(key, value)
