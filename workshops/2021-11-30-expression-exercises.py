"""2021-11-29 

Attendees
- Nila
- Sean

"""

#######################################################################
# Order of Operation Rules
#
# - replace variables with values
# - */ before +-
# - inside to outside
# - left to right (except before =)
#
# Expression - any piece of code that evaluates to a value
#
#######################################################################

ACTIONS = {
    "take": ["home", "cave", "market"],
    "pet": ["cave"],
    "shop": ["market"],
}

action = "shop"

ACTIONS[action].append("buy")
# ACTIONS["shop"].append("buy")
# ["market"].append("buy")
# None


###########

card = {}
row = ["What is the answer to life, the universe and everything?", "42 "]
card["back"] = row[1].strip()
# card["back"] = "42 ".strip()
# card["back"] = "42"

###########

WIDTH = 30
num, total = 2, 10

f"card {num} of {total}".rjust(WIDTH)
# f"card {2} of {10}".rjust(30)
# "card 2 of 10".rjust(30)
# "     card 2 of 10"

from pathlib import Path

filepath = Path("help.txt")
filepath.is_file()

text = "hello"
text.is_file()


# int, str, bool, float, list, dict
# 
# from pathlib import Path
# from random import randint, Random

# randint(1, 100)

###########

# 1. Make a list of seasons (lowercase). Print the first three characters of the 3rd season, title cased.
# 2. Make a dictionary where the key is the numbers 1-7 and the value is the days of the week: monday - sunday.
#    - Write a function that takes one argument, a number, and returns the day of the week associated with that number.
# 3. Make a dictionary named schedule where the key is a weekday and the value is another dictionary. 
#    - The inner dictionary should be the schedule for the day, where the key is the time in 24 hour format (ie: "14:30")
#      and the value is the thing scheduled
#    - Use a for loop to iterate over each day and print the day name,
#    - then use a nested for loop to iterate over the schedule and print the time and activity
#

###########


