# A unit test, test a small of code, a so called unit
import unittest


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
    return " ".join([w[::-1] for w in text.split()])


# Challenge 3
# The main idea is to count all the occurring characters 
# in a string. If you have a string like aba, then the 
# result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.
def count(string: str) -> dict:
    """Iterate through string and count character occurrences.
    
    :param string:  String to analyze
    :return:        Dictionary with counts
    """
    # 1. Iterate through string
    # 2. Set default value of 1 if character does not exist in counts dict
    # 3. If exists increase count for that  character by one
    # 4. return dictionary
    counts = {}
    for char in string:
        # One liner counter[char] = counter.get(char, 0) + 1
        # Same as writing if X is true:
        if counts.get(char):
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


class TestEndswithChallenge(unittest.TestCase):

    def test_count_empty_string(self):
        self.assertEqual(count(""), {})
        
    def test_count_words(self):
        self.assertEqual(count("aa"), {"a": 2})
        self.assertEqual(count("aba"), {"a": 2, "b": 1})
        self.assertEqual(count("panda"), {"p": 1, "a": 2, "n": 1, "d": 1})

    def test_counts_space(self):
        self.assertEqual(count(" "), {" ": 1})


class TestCountChallenge(unittest.TestCase):

    def test_endswith_one_character(self):
        self.assertEqual(endswith("aba", "a"), True)


if __name__ == "__main__":
    unittest.main()
