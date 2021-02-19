"""An example script for of the Testing lesson
   Part 5.1: Keep your interface separate
   https://alissa-huskey.github.io/python-class/lessons/testing.html#part-5-1-keep-your-interface-separate
"""

def is_palindrome(text):
    """Return True if text is the same forward and backwards."""

    return text == "".join(reversed(text))

def message(isit, text):
    if isit:
        msg = f'Yes, "{text}" is a palindrome.'
    else:
        msg = f'No, "{text}" is not a palindrome.'

    return msg


def main():
    """Ask the user for text, then print a message telling the user if it is
       an palindrome or not."""

    text = input("Enter a word to determine if it's an palindrome: ")
    word_is_palindrome = is_palindrome(text)
    output = message(word_is_palindrome, text)
    print(output)

if __name__ == "__main__":
    main()
