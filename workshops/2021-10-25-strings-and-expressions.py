"""
10/25/2021 Fundamentals: Review of Strings Lesson--Part 1, Expressions exercises
https://alissa-huskey.github.io/python-class/lessons/data-types/strings.html
"""


movie = "LOTR"
print(movie)

things = """Things I like:
raindrops on roses,
whiskers on kittens
bright copper kettles"""
print(things)

other_things = "warm woolen mittens \nbrown paper packages\n"
print(other_things)

print("-" * (8+2))

print("one", "two", "three")
things = [
    "one",
    "two",
    "three",
]

# child_words = "My mother said "
# child_words = "My " "mother " "said "

child_words = (
    "My "
    "mother "
    "says "
    "to "
    "pick "
    "the "
)
print(child_words)

# three syntax rules that make the description below work
#
# 1. You can group an expression using parenthesis
# 2. You can split a single statement onto multiple lines when it is inside of: (), [], or {}
# 3. When you put two string literals next to each other, they are automatically concatonated

words = ["one", "two", "three"]
words = ("one", "two", "three")
print(words)

words = "onetwothree"
words = "one" "two" "three"
words = ("one" "two" "three")
print(words)

description = (
    "Your cottage is at the top of a hill with a winding path leading down "
    "to a burbling brook which in turn has fish and rocks and blah blah blah "
    "and stuff the end."
)

# description = """
#     Your cottage is at the top of a hill with a winding path leading down
#     to a burbling brook which in turn has fish and rocks and blah blah blah
#     and stuff the end.
# """

print("description is a:", type(description))
print(description)

text = r"This is text \ bilbo"
print(text)

print(f"hello there: {5*5}")

title = "Things"
line = "-" * (len(title) + 2)

# line = "-" * 6 + 2
# line = "-" * 8
# line = "--------"


print(title)
print(line)

x = 3 * 'un' + 'ium'
# x = 'ununun' + 'ium'
# x = 'unununium'
print(x)

# order of operation rules
#
# 1. replace variable name with values
# 2. inner-most to outer-most
# 3. left to right
# 4. * / before + -

s = 'supercalifragilisticexpialidocious'
x = (s[0:5] + str(len(s)) + "\n") * 3
# x = 'supercalifragilisticexpialidocious'[0:5] + str(len('supercalifragilisticexpialidocious')) + "\n" * 3
# x = 'supercalifragilisticexpialidocious'[0:5] + str(34) + "\n" * 3
# x = 'supercalifragilisticexpialidocious'[0:5] + str(34) + "\n\n\n"
# x = 'super' + str(34) + "\n\n\n"
# x = 'super' + '34' + "\n\n\n"
# x = 'super34\n\n\n"
print(x)


from pprint import pprint
from datetime import datetime
from dateutil.parser import parserinfo

days = parserinfo.WEEKDAYS
today = datetime.now()

x = "Have a happy " + days[today.weekday()][1]
# x = "Have a happy " + days[0][1]
# x = "Have a happy " + ('Mon', 'Monday')[1]
# x = "Have a happy " + 'Monday'
# x = "Have a happy Monday"
print(x)

score = .75
labels = {}
for i in range(0, 60):
    labels[i] = "loser"

for i in range(61, 79):
    labels[i] = "okay person"

for i in range(80, 100):
    labels[i] = "winner"



x = "Your score is: " + str(score*100) + "%, so you're a " + labels[int(score*100)].title()
# x = "Your score is: " + str(.75*100) + "%, so you're a " + labels[int(.75*100)].title()
# x = "Your score is: " + str(75.0) + "%, so you're a " + labels[int(75.0)].title()
# x = "Your score is: " + str(75.0) + "%, so you're a " + labels[75].title()
# x = "Your score is: " + str(75.0) + "%, so you're a " + "okay person".title()
# x = "Your score is: " + "75.0" + "%, so you're a " + "okay person".title()
# x = "Your score is: " + "75.0" + "%, so you're a " + "Okay Person"
# x = "Your score is: 75.0%, so you're a Okay Person"
print(x)


width = 45
times = {}
for i in range(0, 13):
    times[i] = "morning"
for i in range(13, 16):
    times[i] = "afternoon"
for i in range(16, 20):
    times[i] = "evening"
for i in range(20, 24):
    times[i] = "night"

x = ("Good " + times[today.hour]).rjust(width)
# x = ("Good " + {0: 'morning', ...}[today.hour]).rjust(45)
# x = ("Good " + {0: 'morning', ...}[18]).rjust(45)
# x = ("Good " + "evening").rjust(45)
# x = "Good evening".rjust(45)
# x = "                                 Good evening"
print(x)


levels = ("empty", "full")
print(levels[1])

# print(("empty", "full")[1])
# print("full")

gas = 0.25
x = "The gas tank is " + ("Empty", "Full")[gas > 1] + "."
# x = "The gas tank is " + ("Empty", "Full")[.25 > 1] + "."
# x = "The gas tank is " + ("Empty", "Full")[False] + "."
# x = "The gas tank is " + ("Empty", "Full")[0] + "."
# x = "The gas tank is " + "Empty" + "."
# x = "The gas tank is Empty."
print(x)
