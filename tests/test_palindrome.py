"""An example script for of the Testing lesson
   Part 5.1: Keep your interface separate
   https://alissa-huskey.github.io/python-class/lessons/testing.html#part-5-1-keep-your-interface-separate
"""

from pythonclass.lessons.palindrome import is_palindrome, message

def test_is_palindrome_true():
    assert is_palindrome("radar"), \
        "should return True if text is the same forwards and backwards"


def test_is_palindrome_false():
    assert not is_palindrome("something"), \
        "should return False if text is not the same forwards and backwards"


def test_message_no():
    assert message(False, "nope") == 'No, "nope" is not a palindrome.', \
        "should return a message saying text is not a palindrome if isit is False"



def test_message_yes():
    assert message(True, "level") == 'Yes, "level" is a palindrome.', \
        "should return a message saying text is a palindrome if isit is True"
