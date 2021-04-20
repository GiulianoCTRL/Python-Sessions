"""
Short introducing while and for loops.
"""
numbers = [1, 2, 3, 4, 5, 6, 7]

# A for loop is finite and will stop iterating when the end of our iterator
# (Our list in this case) is reached.
for number in numbers:
    print(number)

# We could use a for loop to create a list containing the caracters of a string.
characters = []
for char in "This is a short.":
    characters.append(char)

# It is possible to write the above shorter and into one single line.
# The could be read as "Add a character for each character in this string to a list
# named 'characters'."
characters = [char for char in "This is a shortcut."]


# While loops are defined with the while keyword and followed by a condition.
# A condition is something that evaluates to True of False, similar to if statements.
# One example could be 1+1 == 2, so our instead of writing 'if 1 + 1 == 2' we write
# 'while 1 + 1 == 2'
# A while loop repeats as long as the condition is true, it is therefore to crucial
# to implement a condition to stop it.

# In the below example we want to stop the loop when the point in the string
# is reached. Remember, a string can be seen as a list of characters (in this case).
# [a, 2, 8, 9, ..., i, u]
long_string = "a2890523y89fhisgbksiu38y45.hufhsfbuihgbeiu"
# Symbol is the first (index 0) symbol in our string, so 'a'
symbol = long_string[0]


# We need to ensure to progress through the string, therefore we need to somehow
# increase the index we access.
index = 1  # This is named count in the short, but makes more sense being named index
while symbol != ".": # While the symbol is not a .
    print(symbol)
    symbol = long_string[index]  # Now we access index 1 and update the symbol variable
    index += 1  # We increase the index variable by 1, so that the next symbol we be the
                # character at index 2, then 3, 4 etc.

# As we defined index outside the loop, we can still use it. We can therefore print
# how many symbols we needed to print until we reached a '.'
print(f"{index} symbols have been printed until a '.' has been reached.")
