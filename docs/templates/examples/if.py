import random

age = random.randint(1, 99)

if age >= 21:
  print("Would you like a beer?")
elif age >= 12:
  print("Would you like a soda?")
elif age >= 5:
  print("Would you like a juice?")
else:
  print("Hello.")

