"""
File handling, manipulation and interacting with the filesystem
"""

# a powerful cross-platform library to handle all major operating systems
import pathlib


def read_file(filename: str) -> str:
    """Read from a file and return it's content.
    
    :param filename:    Name/path to file
    :return:            Content of file as string
    """
    file_path = pathlib.Path(filename)
    # Assert is a function that will raise an error should the assertion
    # evaluate to False
    assert(file_path.exists())
    return file_path.read_text()


# Pathlib also has various other functions

lorem = pathlib.Path("lorem_ipsum.txt")

# Get the absolute path (full path)
print(lorem.absolute())
print(lorem.resolve())