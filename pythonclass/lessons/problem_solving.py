"""Reverse a string"""

def reverse(text):
    """return the a string that reverses the order of the characters in text"""
    text = str(text)

    # make an array for the reversed string
    output = []

    # get the length of the input text
    i = len(text) - 1

    # iterate through each character in the input text, starting at the end
    while i >= 0:
        #   append the character to the reversed string
        output.append(text[i])
        i -= 1

    # convert the list to a string
    return "".join(output)

def main():
  # ask the user for the text to reverse
  text = input("Text to reverse: ").strip()

  # reverse the text
  output = reverse(text)

  # print the reversed text
  print(output)

def test_reverse():
    """."""
    assert reverse("jello") == "ollej", "string"
    assert reverse("") == "", "empty string"
    assert reverse(123.4) == "4.321", "float"
    assert reverse(1234) == "4321", "int"


if __name__ == "__main__":
    main()
