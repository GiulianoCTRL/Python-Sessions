"""References for lists and dictionaries."""

# List basics
x_coordinates = [1.1, 2.2, 7.7, 9.9, 5.5]
y_coordinates = [-4.1, -7.1, -11.1, 13.1, 18.1]

# print items in list
for i in x_coordinates:
    print(i)
# 1.1 \n 2.2 \n 7.7 \n 9.9 \n 5.5

# print specific item
print(y_coordinates[3])
# 13.1

# All three examples below do the same
y = 0  # y is persistent thorughout loop iterations
for x in x_coordinates:  # x is a temporary variable that will be overwritten each iteration
    y += x

z = 0
z += x_coordinates[0]
z += x_coordinates[1]
z += x_coordinates[2]
z += x_coordinates[3]
z += x_coordinates[4]

total = sum(x_coordinates)  # Sum calculates the sum of the iterables (list, dicts, tuple, etc.) and returns it
print(y, z, total)
# 26.4 26.4 26.4

# Adding
x_coordinates.append(11.11)  # Adds to the end of the list
y_coordinates.insert(3, -23.1)  # Inserts at given index (moves previous item at that index to the right (index +1))

# Replace value
# Counting starts from 0 in both directions
x_coordinates[0] = 3.3  # Replace first item (index 0) with 3.3
y_coordinates[-1] = -5.1  # Replace last item (-1) with -5.1

# Remove value
x_coordinates.remove(11.11)  # raises ValueError if value does not exist, only removes first occurence if more than one of the same value exist
del y_coordinates[3]  # Delete specific index, IndexError if index not exist

# Filtering
# filter functions should return bool (True|False)
# Usual function
def filter_two(number: int) -> bool:
    """Return False if number is two, and True if it isn't."""
    return number != 2

# Lambda function
# No def or brackets needed, simple expressions
filter_three = lambda number: number != 3 # Returns False if number is three

to_be_filtered = [2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 6]

# Filter function takes function (with one argument) and iterable as input.
no_twos = filter(filter_two, to_be_filtered)
no_threes = filter(filter_three, to_be_filtered)
no_fives = filter(lambda n: n != 5, to_be_filtered)

print(list(no_twos))
print(list(no_threes))
print(list(no_fives))


# TODO GiulianoCTRL: sort, dict from list, tuples, adding two lists
