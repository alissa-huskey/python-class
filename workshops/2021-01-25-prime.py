def is_prime(number):
  """Return True if the number is a prime. Takes a positive whole number and returns True or False.

  Examples
  --------
  >>> is_prime(3)
  True

  >>> is_prime(4)
  False
  """

  if number == 0:
    return True

  # iterate through each number less than the input number, starting at 2
  for i in range(2, number):

    # divide the numbers
    quotient = number/i

    # if the number is whole, return False
    return int(quotient) != quotient



def test_is_prime():

  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(0), "Zero should be prime"
  assert is_prime

test_is_prime
