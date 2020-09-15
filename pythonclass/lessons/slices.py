#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Slices Lesson"""

import string
import random
import textwrap
import os
import sys
from pprint import pprint
import shutil

# ===========================================================================
# script meta--ignore all this
# ===========================================================================
#


def print_info(msg, val):
    em = "\033[38;5;6m"
    clr = "\033[0m"
    lpad = (" "*26)
    msg = msg.rstrip(':')
    wrapper = textwrap.TextWrapper(
        width=WIDTH,
        initial_indent=lpad,
        subsequent_indent=lpad + "    "
    )
    lines = wrapper.wrap(repr(val))
    first = lines.pop(0)
    print(f"\n{em}{msg:>26}{clr}: ", end="")
    print(first[26:], *lines)


WIDTH, _ = shutil.get_terminal_size()


# ===========================================================================
# slices
# ===========================================================================
#
# convert the ascii_lowercase string to a list ------------------------------
#
print_info("alphabet string:", string.ascii_lowercase)
mylist = list(string.ascii_lowercase)
print_info("alphabet list:", mylist)

# access an indiviidual element from the list -------------------------------
#
print_info("a letter:", mylist[5])

# randomly select a element from the iist -----------------------------------
#
print_info("random letter:", random.choice(mylist))

# update a list element using the index address -----------------------------
#
mylist[5] = mylist[5].upper()
print_info("a changed letter:", mylist[5])
print_info("mylist, changed", mylist)

# access a section, or slice of the list ------------------------------------
#    the syntax is: <listname>[start-index:end-index+1]
#
print_info("a slice!", mylist[5:10])

# change all elements of a list slice ---------------------------------------
#
mylist[5:10] = ["x", "y", "z", 0, 1]
print_info("mylist, changed forever", mylist)

# delete elements from a list slice -----------------------------------------
#
del mylist[5:10]
print_info("mylist has lost something", mylist)

# copy a slice to a new list ------------------------------------------------
#
section = mylist[8:15]
print_info("section:", section)

# iterate over the new list, randomly swapping case -------------------------
#
for i, c in enumerate(section):
    if random.randint(0, 1):
        section[i] = section[i].swapcase()
print_info("section, transformed:", section)

# update mylist with the changes from section -------------------------------
#
mylist[8:15] = section
print_info("mylist, different:", mylist)

# ===========================================================================
# strings as lists
# ===========================================================================
#

# just your average string --------------------------------------------------
#
mystr = "hello world"
print_info("mystr:", mystr)

# and yet! characters can be accessed like a list ---------------------------
#   strings are really just lists of characters under the hood
#
print_info("a mystr character:", mystr[3])

# make a new list with the contents of mystr ---------------------------------
#
newstr = list(mystr)

# iterate over the characters of mysstr, without converting it to a list -----
#
for i, c in enumerate(mystr):
    if random.randint(0, 1):
        # change the newstr character at the same index as mystr -------------
        #
        newstr[i] = mystr[i].swapcase()

print_info("newstr:", "".join(newstr))


# ===========================================================================
# DND stats
# ===========================================================================
#
""" DND stats example """
# Jayson

# D&D Time
# lazy math
stat = "0" * 6

# set list
stats = list(stat)

print_info("stats", stats)


# variables
strength, wisdom, charisma, thing, thing, thing = stats
# strength = stats[1]

# wisdom = stats[2]

# charisma = stats[3]

# = stats[4]

# = stats[5]

# = stats[6]
# stats[1] = input("Enter the value of your char's STR")

stats = dict(
    strength=0,
    wisdom=0,
    charisma=0,
    humor=0,
    magic=0,
    pain_tollerance=0
)

for key, val in stats.items():
    print(f"Enter the value for your chars {key}", end="")
    default_val = random.randint(0, 100)
    stats[key] = input(f"[{default_val}]> ")
    if stats[key] == "":
        stats[key] = default_val

pprint(stats)
