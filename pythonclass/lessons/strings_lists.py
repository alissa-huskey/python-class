#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Strings and Lists"""

import shutil
import random

def print_info(msg, val):
    em = "\033[38;5;6m"
    clr = "\033[0m"
    lpad = (" "*26)
    msg = msg.rstrip(':')
    print(f"{em}{msg:>26}{clr}: ", val)


WIDTH, _ = shutil.get_terminal_size()

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
# iterate over the characters of mysstr, without converting it to a list -----
#

a_string = "hello"                 # "hello"
a_list = list(a_string)            # [ "h", "e", "l", "l", "o" ]
# iterate over each character, with the index
for i, c in enumerate(a_list):
    # using a dict with get(key, default) to decide the character
    chars = {
        "l": "1",
        "e": "3",
    }
    # set the value of list at the current index
    replacement_c = chars.get(c, c)

    # or you could use a bunch of if-elif statements
    # if   c == "l" : replacement_c = "1"
    # elif c == "e" : replacement_c = "3"

    # set the value of list at the current index
    a_list[i] = replacement_c

# convert a list to a string
new_string = "".join(a_list)


# iterate over the characters of mysstr, without converting it to a list -----
#
newstr = list(mystr)

for i, c in enumerate(mystr):
    if random.randint(0, 1):
        # change the newstr character at the same index as mystr -------------
        #
        newstr[i] = mystr[i].swapcase()

newstr = "".join(newstr)
print_info("newstr:", newstr)
