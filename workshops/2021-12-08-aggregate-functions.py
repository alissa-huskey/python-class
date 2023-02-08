"""
2021-12-08 Data & In-Depth -- Aggregate builtin functions

Attendees
---------
- Fiona
- Brian

Exercises
---------

1. Assign your name (capitalized) to the variable text and find out what the "minimum" letter is.
2. Find out the maximum length of a list of strings.
   ie: ["title", "author", "year"]
3. Make an list of three randomly selected numbers between 0 and 1. If they are
   all truthy print "jackpot!" otherwise print "better luck next time."
   - make an empty list things
   - use a for loop to iterate over a range up to 3
   - append a random number to things between 0 and 1

4. Write a function valid_row that checks if no fields in a csv row are blank.
   - valid_row should take one argument, line, a string
   - in the function:
    * split line on the comma delimiter
    * if all of the values are truthy, print "Valid" and return True
    * otherwise print "Error" and return False
   - test with the following arguments:
    * "a,b,c"
    * "x,,z"

"""

from random import randint
from pathlib import Path

# word_list = Path("data/Oxford English Dictionary.txt").read_text()

"""

"""

numbers = [randint(0, 1) for _ in range(3)]

print(numbers)

# [ ] max()
# [ ] min()
# [ ] sum()

print(min(numbers))
print(min(numbers))
print(sum(numbers))

# [ ] all()
# [ ] any()

things = ["", "", None, 0, 0.0]

if any(things):
    print("yes")
else:
    print("no")


stuff = [" ", 1.0, -100, 0.25, -0]

if all(stuff):
    print("all(): yes")
else:
    print("all(): no")



# [ ] zip()

# [ ] sort()
# [ ] reverse()

##################


words = ["apple", "bear", "carrot"]

revised = [len(x) for x in words]        # [5, ...]
revised = (map(something, words)               # <map()>

revised = []

for word in words:
    new_word = word.upper()
    new_word = word.strip()

    revised.append(word.upper())

for word in words:
    new_letters = []
    for char in word:
        new_letters.append(char.upper())

    new_word = "".join(new_letters)
    revised.append(new_letters)

revised = [x.upper() for x in words]
revised_two = [x.strip() for x in words]


