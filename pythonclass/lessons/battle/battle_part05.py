#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyPet Battle Game:
* Two fighters are randomly chosen from a list of PETS, each starting with a
  health of 100
* Print out details about the chosen fighters
* Each fighter takes a turn attacking the other until one fighter wins.
    - Each attack will have a description and do randomly selected amount of
    damage between 10-30
    - Each attack will print out the description of the attack, the damage it
    did, and the health of each fighter at the end of the turn
    - Whoever reaches 0 first loses and the other player wins.
* At the end of the game, announce the winner
"""

# The convention is to name modules (Python files) using
# lower_case_with_underscore
#
# The code for a project should be in a directory named using lowernounderscore
#   for example:
#
#   myproject/
#       my_module.py
#       my_script.py

# ### Imports ################################################################

from pets import PICS, PETS

# ## Global Variables ########################################################


# ## Functions ###############################################################

# ### top-level game functions ###
#

def lotto():
    """Return two randomly chosen PETs"""
    return []


def intro(fighters):
    """Takes a list of two PETs (fighters) and prints their details"""


def fight(fighters):
    """Repeat rounds of the fight until one wins then
       Take a list of two PETs and return the winning PET"""
    return {}


def endgame(winner):
    """Takes a PET (winner) and announce that they won the fight"""


# The main() function should be at the last function defined
#

def main():
    """PyPet Battle Game"""
    print("Welcome to the THUNDERDOME!")

    fighters = lotto()
    intro(fighters)
    winner = fight(fighters)
    endgame(winner)


# ## Runner ##################################################################

# This calls the main() function if the script is being run directly
#   but not if it is being imported as a module

# This should always be at the very end of the script
#

if __name__ == "__main__":
    main()
