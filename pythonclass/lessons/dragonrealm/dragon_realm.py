#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dragon Realm - A game where the player decides between two caves, which hold
  either treasure or certain doom.
  Inspired by: http://inventwithpython.com/invent4thed/chapter5.html
"""

import random
import time
import textwrap

CAVES = ["right", "left"]
DELAY = 1
WIDTH = 58
WRAP = 50
DEBUG = False

PREFIX = '\x1b'
YELLOW = f'{PREFIX}[33m'
NORMAL = f'{PREFIX}[0m'


def debug(*messages):
    """If DEBUG global variable is True, print one line for each element of
       messages list in debug style: indented, yellow"""
    if not DEBUG:
        return

    message = " ".join([str(m) for m in messages])
    print(" ", f"{PREFIX}{YELLOW}", message, f"{PREFIX}{NORMAL}")


def describe(message):
    """Prints string message in special description style, indented"""
    for line in textwrap.wrap(message, WRAP):
        print("  ", line)


def valid_cave(response):
    """Return cave matching response or first letter of response, or False"""
    response = str(response)
    for cave in CAVES:
        if response == cave or response == cave[0]:
            return cave

    return False


def is_friendly(dragon):
    """Return True if dragon is in the randomly chosen friendly one"""
    friendly = random.randint(0, 1)
    debug("Your dragon is", dragon)
    debug("The friendly dragon is:", friendly)
    debug("The friendly dragon is:", CAVES[friendly])
    return dragon == CAVES[friendly]


def dragon(is_friendly):
    """Print the dragon action for a friendly or unfriendly dragon"""
    actions = {
        # friendlyness: action
        True: "Gives you his treasure! 💰",
        False: "Gobbles you down in one bite! 💀",
    }
    print()
    describe(actions[is_friendly])
    print()


def intro():
    """Display the introduction description to the player"""

    describe("""You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.""")
    print()


def choose():
    """Prompt the player to choose "right" or "left" then return response."""
    cave = ""
    while not valid_cave(cave):
        print("Do you enter the cave on the right or left?")

        cave = input("(right, left): ").lower()
        if cave in ["q", "quit", "exit"]:
            exit()

        cave = valid_cave(cave)
        if not valid_cave(cave):
            print('Type "right" or "left". \n')

    print()
    return cave


def enter(cave):
    """Prints description of what happens when the user enters the cave based
      on value of cave: "right" or "left" """

    messages = [
        "You approach the cave...",
        "It is dark and spooky...",
        "A large dragon jumps out in front of you!",
        "He opens his jaws and...",
    ]

    for message in messages:
        describe(message)
        time.sleep(DELAY)

    nature = is_friendly(cave)
    dragon(nature)


def play():
    """Play the game"""
    intro()
    cave = choose()
    enter(cave)


def main():
    """Keep playing the game until the user doesn't say yes"""
    print("\nWelcome to Dragon Realm!")
    again = "yes"
    while again.lower() in ["y", "yes"]:
        print("-" * WIDTH, "\n")
        play()
        again = input("Play again? ")


# this means that if this script is executed, then
# the main() function will be called
if __name__ == '__main__':
    main()
