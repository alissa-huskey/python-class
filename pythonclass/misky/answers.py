#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Quiz answers"""


# ### Imports ################################################################

import random

# ## Global Variables ########################################################


# ## Functions ###############################################################

def multiply(x, y):
    """multiply two numbers"""
    return x * y


# The main() function should be at the last function defined
#

def main():
    """."""
    name = input("What is your name? ")
    print("hello", name)

    print(2 + 2)

    num = input("Pick a number: ")
    print(int(num) * random.randint(0, 100))

    print(multiply(2, 4))

    groceries = ["milk", "eggs", "soup"]
    groceries.sort()
    for item in groceries:
        print(item)

    favs = {
        'color': "black",
        'season': "fall",
        'food': "strawberries"
    }

    print(f"""My favorite food is {favs['food']}, my favorite color is
          {favs['color']} and my favorite season is {favs['season']}""")

    num = input("Pick a number: ")
    if int(num) in [7, 42]:
        print("You get a prize!")

    num = 0

    while num < 100:
        num = random.randint(0, 200)
        print(num)


# ## Runner ##################################################################

# This calls the main() function if the script is being run directly
#   but not if it is being imported as a module

# This should always be at the very end of the script
#

if __name__ == "__main__":
    main()
