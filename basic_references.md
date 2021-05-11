# Python quick references

### Basic types
```python
integer = 1                     # Whole numbers
string = "String"               # String with double quotes
alternative_string = 'String'   # String with single quotes (same function)
this_is_a_float = 4.5           # Floating point numbers / decimals
boolean = True                  # Either True or False
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