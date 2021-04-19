"""
Playing around with lists. (For lists video.)
"""

names = ["John", "James", "Francis", "Wade"]

print(names[0])
# >>> "John"

names[0] = "Baptiste"

names[19]
# >>> Index out of range error

# Last item in list can be accessed with -1 if length is unknown
# Wade == Wade
bool(name[3] == name[-1])
name[-2] # Francis

# Length is 4 - 1 = 3
names[len(names) - 1]

names.append("Johan")
# List now looks like ["Baptiste", "James", "Francis", "Wade", "Johan"]
names.insert(2, "Max")


# Append in a for loop
characters = []
for char in "SuperLongString":
    characters.append(char)

# List comprehension 
characters = [char for char in "SuperLongString"]
