#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A module for relaying messages to and from the player."""

import sys

# the max width of the screen
WIDTH = 48

# what command always means quit
QUIT_COMMAND = "q"


def line(char="-"):
    """Print a line"""
    print(char * WIDTH)


def center(text):
    """Print text centered on the screen"""
    print(text.center(WIDTH), "\n")


def info(text):
    """Print text to the user formatted as info"""
    print("  ", text)


def exit_if_quit(response):
    """Exit the game if response is the quit command"""
    if response == QUIT_COMMAND:
        sys.exit()
