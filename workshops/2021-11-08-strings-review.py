"""
2021-11-08 Lecture/Demo

Strings Lesson Part 2: Spitting and Joining
https://alissa-huskey.github.io/python-class/lessons/data-types/strings.html#part-2-splitting-and-joining

Fundamentals
------------
- Sean
"""

from pprint import pprint

text = "donkey   railroad   erica       tabs"

text = """
one and
    two and
    three and
    four!
"""

words = text.split()

text = "mon.tue.wed.thurs.fri.sat.sun"

words = text.split(".")
print(words)

text = "one and two and three and four"

words = text.split("and")
print("  NO spaces", words)

words = text.split(" and ")
print("WITH spaces", words)

text = "an AWFUL thing to do!?@"
characters = list(text)

pprint(characters)

letters = ["a", "b", "c"]

# string.join(iterable)

text = " and then he said ".join(letters)
print("WITH spaces:", text)

text = "and then he said".join(letters)
print("  NO spaces:", text)

letters = ("x", "y", "z")
text = ":".join(letters)

print(text)

letters = "123"
text = "-".join(letters)

print(text)