# %% [markdown]

# # Fundamentals: Statements

# A *statement* is a valid unit of code that serve as an instruction to Python.
#
# When a statement is run, it is called *executing* the code.

# ## Simple Statements

# Most statements are a single line of code.
#
# For example:

# %%

name = "Alissa"
print("Hello", name)
import random
colors = ["red", "green", "blue"]

# %% [markdown]

# You can break up part of a statement that is inside of parentheses, square
# brackets or curly braces after delimiters (seperator symbols) or operators.
# This is called *implicit line continuation*.

# > Even though these examples are broken up into multiple lines, the
# > `address =` lines make up a single statement and the `print()` lines
# > make up another single statement.

# %%

address = {
    'street': "1600 Pennsylvania Ave NW",
    'city': "Washington",
    'state': "DC",
    'zip': "20500-0003",
    'country': "United States",
}

print(
    "The White House: " +
    address['street'] +
    ", " +
    address['city'] +
     ", " +
    address['state'] +
     ", " +
    address['zip']
)

# %% [markdown]

# Where implicit continuation won't work, you can break up a statement into
# multiple lines by adding a `\` to the end of each line. This is called
# *explicit line continuation*.

# > Even though this example is broken up into multiple lines it is still a
# single statement

# %%

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

# %% [markdown]

# You can also put multiple statements on one line by putting a `;` between
# each statement. (Though it's not recommended in your saved code, it's
# sometimes handy in the Python shell.)

# > Even though this example is on one line there are two statements.


# %% [markdown]

# ## Compound Statements

# There are some cases where a number of statements are grouped together to be
# executed as a single unit. This is called a *compound statement*.

# A compound statement always has at least one *header* line that that ends in
# a `:` and controls one or more *body* statement lines that are at the same
# indentation level.

# <header>:
#   <body>

# One example is a function definition.


# %%

def print_debug(text):
    print("DEBUG:", text)

# %% [markdown]

# Another example is an if-statatement.

# > An if-statement can include multiple headers, but it is still all one statement.


# %%

if answer < 0:
    print("Answer must be a positive number")
elif answer > 5:
    print("Answer must be less than five.")
else:
    print("Your answer was:", answer)


# %% [markdown]

# ## Self-Quiz

# 1. How many statements are in the following:

# %%

favs = {
    'color': "purple",
    'season': "Fall",
    'food': "cheese"
}
print("My favorite color is:", favs['color'])

# %% [markdown]

# 2. What is wrong with the following:

# %%

import random
num = random.randint(0, 10)
if num > 5:
print(num)

# %% [markdown]

# 3. What is wrong with the following:

# %%

def print_header(title)
    print(title)
    print("============================================")


# %% [markdown]

# 4. How many statements are in the following:

# %%

name = "Jack" ; age = 24 ; print(name, "is", age, "years old")

# %% [markdown]

## Today we learned

# * **statement**: is a valid unit of code that serve as an instruction to Python
# * **execute**: when Python runs a piece of code
# * **simple-statement**: a statement that can be written on a single line by itself, even if it is not actually written that way
# * **compound-statement**: a number of statements grouped together as a single unit
# * **implicit line continuation**: when a simple statement is broken into multiple lines inside of `(` `)`, `[` `]` or `{` `}` after operators.
# * **explicit line continuation**: when a simple statement is broken into multiple lines by appending a `\` to the end of each line
