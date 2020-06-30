#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dragon Realm - A game where the player decides between two caves, which hold
  either treasure or certain doom.
  Inspired by: http://inventwithpython.com/invent4thed/chapter5.html
"""

WIDTH = 58
CAVES = ["right", "left"]


def valid_cave(response):
    """Return True if response is in the list of valid CAVES"""
    return response in CAVES


def intro():
    """Display the introduction description to the player"""
    print("""You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.\n""")


def choose():
    """Prompt the player to choose "right" or "left" then return response."""
    cave = ""
    while not valid_cave(cave):
        print("Do you enter the cave on the right or left?")
        cave = input("(right, left): ").lower()

        if cave in ["q", "quit", "exit"]:
            exit()

        if not valid_cave(cave):
            print('Type "right" or "left". \n')

    print()
    return cave


def main():
    """Keep playing the game until the user doesn't say yes"""
    print("Welcome to Dragon Realm!")
    again = "yes"
    while again.lower() in ["y", "yes"]:
        print("-" * WIDTH, "\n")
        intro()
        cave = choose()
        again = input("Play again? ")


# this means that if this script is executed, then
# the main() function will be called
if __name__ == '__main__':
    main()
