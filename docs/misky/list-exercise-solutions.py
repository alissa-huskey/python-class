#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Running Calculator
1. Make a list of numbers.
2. Iterate over the list. For each element:
    a. Add the element value to a balance variable.
    b. Print the value, and the balance.
OUTPUT
    + 8     =  8
    + 5     = 13


Randomly swap the case of characters in a String
1. Convert a string into a list of individual characters
2. Iterate over the list and randomly either switch the case of the character
   or leave it the way it is.
    Hints:
        - String case functions `str.islower()`, `str.isupper()`, `str.upper()`
          and `str.lower()`
        - Change list values with `varname[<index-number>] = <newval>`
3. Join the list back into a new string.
4. Print the original string and the case-swapped string.
OUTPUT
    number: nUmBeR
"""

import random

def header(title):
    print("\n", title)
    print("-"*50)

def calc():
    """Running calculator"""
    balance = 0
    for val in [ 8, 5, -5, 20 ]:
        balance+=val
        print(f"+ {val:>3}       = {balance:>3}")

def random_case_switch(start_str):
    """Randomly switch the case of characters in a string"""
    end_str = list(start_str)
    for i, c in enumerate(end_str):
        if random.randint(0, 1):
            end_str[i] = c.upper() if c.islower() else c.lower()
    return str("").join(end_str)

words = "magnetic storage pot box number solar tide closed shop".split()
width = max(map(len, words))

header("calc")
calc()

header("random_case_switch")
for w in words:
    print(f"{w:>{width}}: {random_case_switch(w)}")

def pw_convert(start_str):
    """Convert string to a (bad) password"""
    end_str = list(start_str.lower())
    for i, c in enumerate(list(end_str)):
        if   c == "a": end_str[i] = "@"
        elif c == "s": end_str[i] = "$"
        elif c == "l": end_str[i] = "1"
        elif c == "i": end_str[i] = "!"
        elif c == "e": end_str[i] = "3"
        elif c == "o": end_str[i] = "0"
        elif c == " ": end_str[i] = "_"
    return str("").join(end_str)
