"""
Lessons about filesystems and files.
"""
# Note: Add function and keyword examples to basics

# r = read, w = write, a = append
# w will overwrite what's in the file -> Will create file if not existing
# a will append what is already existing

# Open a file / return a "TextObject"
lorem = open("lorem_ipsum.txt", "r")

# Read the content of the file
# text = lorem.read()



line_num = 0
for line in lorem:
    # Below is short way of writing
    # line_num = line_num + 1
    line_num += 1
    # .strip() method on strings removes any whitespace to the left or right of the string
    print(line_num, line.strip())

# Always close file
lorem.close()
