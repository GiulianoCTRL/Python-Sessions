# Python quick references

## Basic types
```python
integer = 1                     # Whole numbers
string = "String"               # String with double quotes
alternative_string = 'String'   # String with single quotes (same function)
this_is_a_float = 4.5           # Floating point numbers / decimals
boolean = True                  # Either True or False
```

## Arithmic operators
```python
# Addition
a = 4 + 4   # 8
b = a + 5   # 8 + 5 = 13
a = a + 10  # 8 + 10 = 18
# a += 10-*-* == a = a + 10
a += 10     # 18 + 10 = 28
>>> a
28

# Same for substraction
c = 3 - 4   # -1
c -= 4      # -4
>>> c
-4

# Multiplication
d = 4 * 5   # 20
d *= 5      # 100
>>> d
100

# Division
e = 40 / 8  # 5
e /= 2      # 2.5
>>> e
2.5

# Power of
f = 2 ** 2  # 4
f **= 2     # 16
>>> f
16

# Modulo
# Return the rest of an even division
>>> 6 % 3
0
>>> 7 % 3
1
>>> 8 % 3
2
>>> 9 % 3
0


```

### Strings
Strings have different features to format them easily:
```python
# Alternative 1: Simple addition
string1 = "Hello" 
string2 = "John"
>>> string1 + " " + string2 + "."
"Hello John."

# Alternative 2: format function
# Curly brackets as place holders for variables
# string1 is inserted into first curly brackets position, string2 into the second
>>> "{} {}.".format(string1, string2)

# Alternative 3: f(ormat) strings
# This alternativ is clearer and shorter than alternative 2
f"{string1} {string2}"
```

## Advanced types
### Lists
```python
# List is intialized/marked by square brackets []
# Lists and there content are changeable (this is called mutable)
# A list of integers
numbers = [7537, 234, 128, 234, 383, 422, 335]
# A list of strings
names = ["Alfonso", "Wellington", "Waluigi", "Gian-Giuseppe"]
# Variables can be in a list, too
string_list = [string1, string2]

some_name = "Chad"
# A list is not resitricted by a single type
mixed_list = [some_name, "Mountain top", 145, 77.774, True]
# This means we can also have a list of lists (nested)
all_lists = [numbers, [names, string_list], mixed_list, some_name, True]

# List content is accessed via index (starting from 0)
>>> numbers[0]
7537
>>> numbers[4]
383
>>> numbers[12]
# Accessing item outside of list causes error
IndexError: list index out of range
# Get last item of list
>>> numbers[-1]
335
>>> numbers[-2]
422

# Add objects to a list
names.append("Georgina")
>>> names
["Alfonso", "Wellington", "Waluigi", "Gian-Giuseppe", "Georgina"]
# Arithmic operators also useable
numbers += [777, 666]
>>> numbers
[7537, 234, 128, 234, 383, 422, 335, 777, 666]

# insert
names.insert(3, "Yoda")
>>> names
["Alfonso", "Wellington", "Waluigi", "Yoda", "Gian-Giuseppe", "Georgina"]

# remove item by value
names.remove("Gian-Giuseppe")
>>> names
["Alfonso", "Wellington", "Waluigi", "Yoda", "Georgina"]

# delete by index
del names[1]
>>> names
["Alfonso", "Waluigi", "Yoda", "Georgina"]
```
### Tuple
```python
# Tuples is intialized/marked by brackets ()
# Tuples are not changeable (this is called immutable)

# A tuple of integers
numbers_tuple = (7537, 234, 128, 234, 383, 422, 335)
# A list of strings
names_tuple = ("Alfonso", "Wellington", "Waluigi", "Gian-Giuseppe")
# Variables can be in a list, too
string_tuple = (string1, string2)

# A list is not resitricted by a single type
mixed_tuple = (some_name, "Mountain top", 145, 77.774, True)
# This means we can also have a list of lists (nested)
all_lists = (numbers, (names, string_tuple), mixed_tuple, some_name, True)

# All the above stuff on lists does not work here
```