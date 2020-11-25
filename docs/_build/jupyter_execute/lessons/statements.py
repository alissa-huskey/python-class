#!/usr/bin/env python
# coding: utf-8

#  # Fundamentals: Statements
#  A *statement* is a valid unit of code that serve as an instruction to Python.
# 
#  When a statement is run, it is called *executing* the code.
#  ## Simple Statements
#  Most statements are a single line of code.
# 
#  For example:

# In[1]:



name = "Alissa"
print("Hello", name)
import random
colors = ["red", "green", "blue"]


#  You can break up part of a statement that is inside of parentheses, square
#  brackets or curly braces after delimiters (seperator symbols) or operators.
#  This is called *implicit line continuation*.
#  > Even though these examples are broken up into multiple lines, the
#  > `address =` lines make up a single statement and the `print()` lines
#  > make up another single statement.

# In[2]:



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


#  Where implicit continuation won't work, you can break up a statement into
#  multiple lines by adding a `\` to the end of each line. This is called
#  *explicit line continuation*.
#  > Even though this example is broken up into multiple lines it is still a
#  single statement

# In[3]:



a = 1 + 2 + 3 +     4 + 5 + 6 +     7 + 8 + 9


#  You can also put multiple statements on one line by putting a `;` between
#  each statement. (Though it's not recommended in your saved code, it's
#  sometimes handy in the Python shell.)
#  > Even though this example is on one line there are two statements.

#  ## Compound Statements
#  There are some cases where a number of statements are grouped together to be
#  executed as a single unit. This is called a *compound statement*.
#  A compound statement always has at least one *header* line that that ends in
#  a `:` and controls one or more *body* statement lines that are at the same
#  indentation level.
#  <header>:
#    <body>
#  One example is a function definition.

# In[4]:



def print_debug(text):
    print("DEBUG:", text)


#  Another example is an if-statatement.
#  > An if-statement can include multiple headers, but it is still all one statement.

# In[5]:



if answer < 0:
    print("Answer must be a positive number")
elif answer > 5:
    print("Answer must be less than five.")
else:
    print("Your answer was:", answer)


#  ## Self-Quiz
#  1. How many statements are in the following:

# In[ ]:



favs = {
    'color': "purple",
    'season': "Fall",
    'food': "cheese"
}
print("My favorite color is:", favs['color'])


#  2. What is wrong with the following:

# In[5]:



import random
num = random.randint(0, 10)
if num > 5:
    print(num)


#  3. What is wrong with the following:

# In[14]:



def print_header(title):
    print(title)
    print("============================================")

print_header("section")


#  4. How many statements are in the following:

# In[ ]:



name = "Jack" ; age = 24 ; print(name, "is", age, "years old")


# # Today we learned
#  * **statement**: is a valid unit of code that serve as an instruction to Python
#  * **execute**: when Python runs a piece of code
#  * **simple-statement**: a statement that can be written on a single line by itself, even if it is not actually written that way
#  * **compound-statement**: a number of statements grouped together as a single unit
#  * **implicit line continuation**: when a simple statement is broken into multiple lines inside of `(` `)`, `[` `]` or `{` `}` after operators.
#  * **explicit line continuation**: when a simple statement is broken into multiple lines by appending a `\` to the end of each line
