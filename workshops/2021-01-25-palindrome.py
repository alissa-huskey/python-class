
def reverse_text(text):
  """Return text reversed"""

  # make a new blank word
  reversed_text = ""

  # take first letter of word, and start a new word with it
  # take second letter of word and prepend it to previous step's result
  # repeat untill all the letters have been ehausted

  # iterate through the letters
  for x in text:

    # prepend the letter to the new text
    reversed_text = x + reversed_text

  return reversed_text



def is_palindrome(text):
  """Takes a given word and returns True if word is a palindrome"""

  # reverse the word
  new = reverse_text(text)

  # check if the reversed is the same as orig
  if new == text:
    return True
  else:
    return False

def test_is_palindrome():
  print("madam",  is_palindrome("madam"))
  print("racecar", is_palindrome("racecar"))
  print("sir", is_palindrome("sir"))

  assert is_palindrome("madam"), "madam is a palindrome"
  assert is_palindrome("racecar"), "racecar is not a palindrome"
  assert not is_palindrome("sir"), "sir is not a palindrome"

def test_reverse_text():
  assert reverse_text("rats") == "star"

test_reverse_text()
test_is_palindrome()
