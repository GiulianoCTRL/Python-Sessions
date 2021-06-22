# Challenge 1
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
# solution('hello my name is franz walter', '1 hello my name is franz walter')


def endswith(string: str, ending: str) -> bool:
    """Return whether string ends with specific ending.
    
    :param string:      Full string that should be checked
    :param ending:      Ending to be checked against string
    :return:            Whether string ends in ending
    """
    return string.endswith(ending)


# Challenge 2
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_words(text: str) -> str:
    """Return each word in sentence reversed while keeping the sentence's order.

    :param text:      Sentence to reverse
    :return:          Semi-reversed string
    """
    # 1. Split sentence into list of words.
    # 2. Reverse each word.
    # 3. Join words into new sentence.
    pass


