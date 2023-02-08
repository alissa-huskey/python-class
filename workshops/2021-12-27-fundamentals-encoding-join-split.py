"""2021-12-27 Fundamentals

- More String Joining & Splitting
- Character Encoding
- Multiple assignment

Attendees
---------
- Nila

"""

# ===================================================================
# Exercise #1: convert this list to a string with spaces between
#              each word
# ===================================================================

words = [
    "Merry",
    "Christmas",
    "to",
    "all",
    "and",
    "to",
    "all",
    "a",
    "good",
    "night",
]

sentence = " ".join(words)
print(sentence)

# ===================================================================
# Exercise #2 -- change this string to a list of characters
# ===================================================================

password = "hello"
letters = list(password)
print(letters)

# ===================================================================
# Exercise #3 -- split this email address at the @ character
#                bonus: use multiple assignment to assign to two
#                       variables: name and domain
# ===================================================================

# review of multiple assignment

a = 1
b = 2
a, b = 1, 2

numbers = [1, 2, 3]
x, y, z = numbers


email = "bart-simpson@fake.com"
name, domain = email.split("@")
print(name, domain)


# ===================================================================
# Exercise #4 -- Get the unicode integer for a character
# ===================================================================

char = "H"
number = ord(char)
print(f"The character {char!r} is the integer {number} in unicode.")

# ===================================================================
# Exercise #5 -- Get the unicode character for a integer
# ===================================================================

number = 110
character = chr(number)
print(f"The integer {number} is the unicode character {character!r}.")

# ===================================================================
# Exercise #6 -- Strip non-letter characters from a string
# ===================================================================

# A = 65
# Z = 90
# a = 97
# z = 122

text = "Happy New Year!!"
letters = []
for c in text:
    x = ord(c)
    if (x <= 90 and x >= 65) or (x <= 122 and x >= 97):
        letters.append(c)
        # print(f'{c!r}: {x!r}')

new_text = "".join(letters)
print(new_text)
