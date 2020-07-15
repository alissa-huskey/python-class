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

import random
import time
from pets import PICS, PETS

# ## Global Variables ########################################################

# the range of damage each player can do
#
#   this is a data type called a tuple
#   it is just like a list, except it is
#   immutable, meaning it cannot be changed

POWER = (10, 30)

# the number of seconds to pause for dramatic effect
DELAY = 1

# the max width of the screen
WIDTH = 56

MAX_HEALTH = 100

# a list attacks
FIGHTIN_WORDS = (
    "nips at",
    "takes a swipe at",
    "glares sternly at",
    "ferociously smacks",
    "savagely boofs",
    "is awfully mean to",
    "can't even believe",
    "throws mad shade at",
)


# ## Functions ###############################################################

# ### pet functions ###
#

def setup(pets):
    """Takes a list of pets and sets initial attributes"""
    for pet in pets:
        pet['health'] = MAX_HEALTH
        pet['pic'] = PICS[pet['species']]


def show(pet):
    """Takes a pet and prints health and details about them"""
    name_display = f"{pet['name']} {pet['pic']}"
    health_display = f"{pet['health']} of {MAX_HEALTH}"
    rcol_width = WIDTH - len(name_display) - 1
    print(name_display, health_display.rjust(rcol_width))


# ### game event functions ###
#

def attack(foe):
    """Inflict a random amount of damage is inflicted on foe, then return the
       damage and attack used"""
    # choose an attack
    act = random.choice(FIGHTIN_WORDS)

    # randomly set damage
    damage = random.randint(POWER[0], POWER[1])

    # inflict damage
    foe['health'] -= damage

    # return the amount of damage attack and description
    return damage, act


# ### top-level game functions ###
#

def lotto():
    """Return two randomly chosen PETs"""
    # randomly reorder the PETS list
    random.shuffle(PETS)

    # return the first two items in the PETS list
    return [PETS[0], PETS[1]]


def intro(fighters):
    """Takes a list of two PETs (fighters) and prints their details"""

    print("\n  Tonight...\n")
    time.sleep(DELAY)

    # announce the fighters
    header = f"*** {fighters[0]['name']} -vs- {fighters[1]['name']} ***"
    print(header.center(WIDTH, " "), "\n\n")

    # pause for input
    input("ARE YOU READY TO RUMBLE?!")
    print("." * WIDTH, "\n")


def fight(fighters):
    """Repeat rounds of the fight until one wins then
       Take a list of two PETs and return the winning PET"""

    # winning fighter
    winner = None

    # the index in the fighters list of the attacker in each round
    current = 0

    # ### rounds of the fight
    #
    while winner is None:
        # set the roles for this round
        #
        # `not <value>` is a handy way to switch 0 and 1
        #   it is the same as `<value> == False`
        attacker = fighters[current]
        rival = fighters[not current]

        # pause for input
        input(f"\n{attacker['name']} FIGHT>")

        # the attack
        damage, act = attack(rival)

        # pause for effect, then print attack details
        time.sleep(DELAY)
        print(f"\n  {attacker['name']} {act} {rival['name']}...\n")

        # pause for effect, then print damage
        time.sleep(DELAY)
        print(f"-{damage} {rival['name']}".center(WIDTH), "\n")

        # one more pause before the round ends
        time.sleep(DELAY)

        # check for a loser (placeholder)
        winner = random.choice(fighters)

        # print updated fighter health
        print()
        for combatant in fighters:
            show(combatant)

        # print a line at the end of every round
        print("-" * WIDTH, "\n")

        # flip current to the other fighter for the next round
        current = not current

    #
    # ### end of fighting rounds

    # return the winner
    return winner


def endgame(winner):
    """Takes a PET (winner) and announce that they won the fight"""


# The main() function should be at the last function defined
#

def main():
    """PyPet Battle Game"""
    print("\nWelcome to the THUNDERDOME!")

    fighters = lotto()
    setup(fighters)

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
