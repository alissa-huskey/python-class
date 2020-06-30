#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A module for relaying messages to and from the user"""

import sys

# the max width of the screen
WIDTH = 55

# what command always means quit
QUIT_COMMAND = "q"


def exit_if_quit(response):
    """Exit the game if response is the quit command"""
    if response == QUIT_COMMAND:
        sys.exit()


def header(text):
    print("\n"+text)
    line("=")


def line(char="-"):
    """Print a line"""
    print(char * WIDTH)


def cols(left_text, right_text, rcol_width):
    """Print text in two columns, the right column right-aligned"""
    lcol_width = WIDTH - rcol_width - 1
    left = left_text.ljust(lcol_width)
    right = right_text.rjust(rcol_width)
    print(left, right)


def center(text, char=" ", padding=1):
    """Print text centered on the screen"""
    print(text.center(WIDTH, char), padding*"\n")


def info(*args):
    """Print text to the user formatted as info (indented)"""
    args = map(str, args)
    print("  ", " ".join(args))


def ask(prompt=""):
    """Ask the user for input using padded prompt. Exit for quit command or
       return response."""

    # Add a space to the end of the prompt if one is passed and it does not
    # already have one
    if len(prompt) > 0 and not prompt.endswith(" "):
        prompt += " "

    response = input(prompt)
    exit_if_quit(response)
    return response
