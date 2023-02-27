#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyPet Battle Game:

[ ] Two fighters are randomly chosen from a list of PETS, each starting with a
    health of 100
[ ] Print out details about the chosen fighters
[ ] Each fighter takes a turn attacking the other until one fighter wins.
    - Each attack will have a description and do randomly selected amount of
      damage between 10-30
    - Each attack will print out the description of the attack, the damage it
      did, and the health of each fighter at the end of the turn
    - Whoever reaches 0 first loses and the other player wins.
[ ] At the end of the game, announce the winner
"""

# ### Imports ################################################################

import random
import time
import messenger
from pets import PICS, PETS

# ## Global Variables ########################################################

MAX_HEALTH = 100

# the range of damage each player can do
#
#   this is a data type called a tuple
#   it is just like a list, except it is
#   immutable, meaning it cannot be changed

POWER = (10, 30)

# the number of seconds to pause for dramatic effect
DELAY = 1

# a list attacks
FIGHTIN_WORDS = [
    "nips at",
    "takes a swipe at",
    "glares sternly at",
    "ferociously smacks",
    "savagely boofs",
    "is awfully mean to",
    "can't even believe",
    "throws mad shade at",
]


# ## Functions ###############################################################

# ### pet functions ###
#

def init(pets):
    """Set attributes for each of list of pets"""
    for pet in pets:
        pet['health'] = MAX_HEALTH
        pet['pic'] = PICS[pet['species']]
        pet['title'] = f"{pet['name']} the {pet['species'].capitalize()}"


def show(pet):
    """Print the details about a pet"""
    messenger.cols(
        f"{pet['name']} {pet['pic']}",
        f"{pet['health']} of {MAX_HEALTH}",
        rcol_width=len("100 of 100")
    )


# ### game event functions ###
#

def attack(foe):
    """Inflict a random amount of damage is inflicted on foe, then return the
       damage and attack used"""
    # choose an attack
    act = random.choice(FIGHTIN_WORDS)

    # randomly set damage
    damage = random.randint(POWER[0], POWER[1])

    # the -= operator is the same as:
    # foe['health'] = foe['health'] - damage
    foe['health'] -= damage

    # return the amount of damage taken
    return damage, act


# ### top-level game functions ###
#

def lotto():
    """Return two randomly chosen PETs"""
    # randomly reorder the PETS list
    random.shuffle(PETS)

    # This is called a slice
    # it gets items 0 to (but not including) 2
    return PETS[0:2]


def intro(fighters):
    """Print the game header and announce the fighters"""
    messenger.header("Welcome to the THUNDERDOME!")

    # announce fighters
    print("\n  Tonight...\n")
    time.sleep(DELAY)
    messenger.center(
        f"*** {fighters[0]['title']} -vs- {fighters[1]['title']} ***",
        padding=2
    )

    # pause for input
    messenger.ask("ARE YOU READY TO RUMBLE?!")
    messenger.line(".")
    print()


def fight(fighters):
    """Repeat rounds of the fight until one wins then return the winning PET"""

    # ### set variables to initial values ###
    #

    # winning fighter
    #
    #   None is a special data type that means a variable is set, but it is
    #   set to nothing
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
        messenger.ask(f"\n{attacker['name']} FIGHT>")

        # the attack
        damage, act = attack(rival)

        # pause for effect, then print attack details
        time.sleep(DELAY)
        print()
        messenger.info(f"{attacker['name']} {act} {rival['name']}...\n")

        # pause for effect, then print damage
        time.sleep(DELAY)
        messenger.center(f"-{damage} {rival['name']}")

        # one more pause before the round ends
        time.sleep(DELAY)

        # check for a loser
        if rival['health'] <= 0:
            # don't let health drop below zero
            rival['health'] = 0
            # set the winner, this is now the last round
            winner = attacker

        # print updated fighter health
        print()
        for combatant in fighters:
            show(combatant)

        # print a line at the end of every round
        messenger.line()

        # flip current to the other fighter for the next round
        current = not current

    #
    # ### end of fighting rounds

    # return the winner
    return winner


def endgame(winner):
    """Announce the winner"""
    print()
    messenger.center(f"{winner['name']} is Victorious!")
    messenger.center(winner['pic'])
    messenger.line()


def main():
    """PyPet Fight Game"""

    fighters = lotto()
    init(fighters)

    intro(fighters)
    winner = fight(fighters)
    endgame(winner)


# ## Runner ##################################################################

if __name__ == '__main__':
    main()
