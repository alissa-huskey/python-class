"""
2021-12-20 Fundamentals

Agenda
------
* Expression Exercise
* Strings
    * Splitting and Joining Review
    * Character encoding
        - ascii, unicode, hebrew
        - chr() and ord()
"""

##################################
# Expression Exercise
##################################

# order of operation rules
#
# - replace variables with values
# - inside to outside
# - left to right
# - */ before +-

text = "Polly want a cracker?"
text.replace("P", "M")[:-1] + "!"
# "Polly want a cracker?".replace("P", "M")[:-1] + "!"
# "Molly want a cracker?"[:-1] + "!"
# "Molly want a cracker" + "!"
# "Molly want a cracker!"

##################################
# Splitting and Joining Review
##################################

# - converting a string to a list of words

text = "the quick red fox does something or other with the sleepy brown dog"
words = text.split()

# - converting a string to a list of characters

text = "easy!"
characters = list(text)

# - converting a string to a list by another delimiter

rhyme = """
Eeny, meeny, miny, moe,
Catch a tiger by the toe.
If he hollers, let him go,
Eeny, meeny, miny, moe.
"""

# the result should look like:
#
# lines = [
#     "",
#     "Eeny, meeny, miny, moe,",
#     "Catch a tiger by the toe.",
#     "If he hollers, let him go,",
#     "Eeny, meeny, miny, moe.",
#     "",
# ]

lines = rhyme.strip().split(sep="\n")

# - converting an iterable to a string

characters = ["s", "t", "u", "f", "f"]
text = "".join(characters)

# - converting an iterable to a string joined by another delimiter

flavors = ["vanilla", "chocolate", "strawberry"]
text = "the flavors are " + ", ".join(flavors)

##################################
# Character Encoding
##################################

# 65 = A
# ...
# 90 = Z
#
# 97 = a
# ...
# 122 = z


decimals = [128013, 32, 105, 115, 32, 103, 114, 101, 97, 116, 33]
characters = []
for number in decimals:
    char = chr(number)
    characters.append(char)

text = "".join(characters)
print(text)