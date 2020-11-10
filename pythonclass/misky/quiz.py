#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pop Quiz"""

# ## Global Variables ########################################################

QUESTIONS = [
    "Make a new script for your answers to this exercise.",
    "Ask the user for their name, then say hello to them.",
    "Add two plus two then print the result.",
    "Ask the user for a number, then multiply it by a random number and print the results.",
    "Write a function that multiplies two numbers, then call it and print the result",
    "Make a grocery list then print out each item on one line.",
    "Make a dictionary of your favorite color, food, and season. Print a sentence to tell us of your favorites.",
    """Using the python shell, find out how to put a list of words in alphabetical order.
   Use this to sort your list of groceries before you print them.""",
    'Ask the user to pick a number. If the number is one of a list of "lucky" numbers give them a prize.',
    "Keep printing random numbers until the random number over 100."
]


def main():
    """Print the questions and prompt to continue"""
    for question in QUESTIONS:
        print("\n  ", question, "\n")
        input("[Enter to continue.]")


if __name__ == "__main__":
    main()
