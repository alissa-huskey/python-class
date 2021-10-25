"""
Texr-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html
"""

import re
from sys import stderr
import textwrap

from console import fg, bg, fx

WIDTH = 45

DEBUG = False

PLAYER = {
    "place": "home",
}

PLACES = {
    "home": {
        "key": "home",
        "name": "Your Cottage",
        "east": "town-square",
        "description": "A cozy stone cottage with a desk and a neatly made bed.",
        "items": ["book", "desk"],
    },
    "town-square": {
        "key": "town-square",
        "name": "The Town Square",
        "west": "home",
        "description": (
            "A large open space surrounded by buildings with a burbling "
            "fountain in the center."
        ),
    },
}

ITEMS = {
    "elixr": {
        "key": "elixr",
        "name": "healing elixr",
        "description": "a magical elixr that will heal what ails ya",
        "price": -10,
    },
    "dagger": {
        "key": "dagger",
        "name": "a dagger",
        "description": "a 14 inch dagger with a double-edged blade",
        "price": -25,
    },
    "desk": {
        "key": "desk",
        "name": "Desk",
        "description": (
            "A heavy book sits open on a stand on the desk. You "
            "also see an ink pot, a cup of feather quilled "
            "pens, and a pocket watch."
        ),
    },
    "book": {
        "key": "book",
        "name": "A book",
        "description": (
            "A hefty leather-bound tome is open to a page that reads:",
            "> In a mysterious cave lives a dragon with three heads "
              "each with a different temperament.",
            "> Legend says that if you happen upon the dragon sleeping, the "
              "brave may pet one of its three heads.",
            "> Choose the right head, and you will be rewarded with great "
              "fortune!",
            "> But beware! Choose poorly and it will surely mean your doom.",
        ),
    },
}

def header(title):
    """Print a header"""
    print()
    put(fx.bold(title))
    print()

def narrative(text):
    """Print game narrative
    """
    if isinstance(text, str):
        wrap(text)
        return

    # tuple
    for para in text:
        narrative(para)
        print()

def wrap(text):
    """Print wrapped text"""
    indent = ""
    if text.startswith("> "):
        indent = "    "
        text = text[2:]

    lines = textwrap.wrap(
        text,
        WIDTH,
        initial_indent=indent,
        subsequent_indent=indent,
    )

    for line in lines:
        put(line)

def put(text):
    """Print a line of game output."""
    print("   ", text, sep="")

def error(message):
    """Print an error message."""
    print(f"{fg.red('! Error')} {message}\n", file=stderr)

def debug(message):
    """Print a debug message if in debug mode."""
    if not DEBUG:
        return
    print(fg.lightblack(f"# {message}"))

def get_place():
    """Return the place dictionary where the player is at now"""
    name = PLAYER["place"]
    return PLACES[name]

def do_shop():
    """List the items for sale."""

    header("Items for sale.")

    for item in ITEMS.values():
        if "price" not in item:
            continue
        put(f'{item["name"]:<13}', item["description"])

    print()

def do_quit():
    """Exit the game."""
    put("Ok, goodbye.")
    quit()

def do_examine(args):
    """Look at an item in the current place."""

    debug(f"Trying to examine: {args}")

    # make sure the player said what they want to examine
    if not args:
        error("What do you want to examine?")
        return

    # look up where the player is now
    place = get_place()

    # get the item entered by the user and make it lowercase
    name = args[0].lower()

    # make sure it is a thing that is in this place
    if name not in place.get("items", []):
        error(f"Sorry, I don't know what this is: {name!r}.")
        return

    # get the item dictionary
    item = ITEMS[name]

    # print the item information
    header(item["name"])
    narrative(item["description"])

def do_go(args):
    """Move to a different place"""
    debug(f"Trying to go: {args}")

    # make sure the player included a direction
    if not args:
        error("Which way do you want to go?")
        return

    # get the direction from arguments
    # and make it lowercase
    direction = args[0].lower()

    # make sure it's a valid direction
    if direction not in ('north', 'south', 'east', 'west'):
        error(f"Sorry, I don't know how to go: {direction}.")
        return

    # look up where the player is now
    old_place = get_place()

    # look up what is in that direction from here
    new_name = old_place.get(direction)

    # print an error if there is nothing in that direction
    if not new_name:
        error(f"Sorry, you can't go {direction} from here.")
        return

    # look up the place information
    new_place = PLACES.get(new_name)

    # this should never happen if we write the code correctly
    # but just in case there is no key in PLACES matching
    # the new name, print an error
    if not new_place:
        error(f"Woops! The information about {new_name} seems to be missing.")
        return

    # move the player to the new place
    PLAYER["place"] = new_name

    # print information about the new place
    header(f"{new_place['name']}")
    narrative(new_place["description"])

def main():
    header("Welcome!")

    while True:
        debug(f"You are at: {PLAYER['place']}")

        reply = input(fg.cyan("> ")).strip()
        args = reply.split()

        if not args:
            continue

        command = args.pop(0)
        debug(f"Command: {command!r}, args: {args!r}")

        if command in ["q", "quit", "exit"]:
            do_quit()

        elif command in ["shop"]:
            do_shop()

        elif command in ["g", "go"]:
            do_go(args)

        elif command in ["x", "exam", "examine"]:
            do_examine(args)

        else:
            error("No such command.")
            continue

        print()

if __name__ == "__main__":
    main()
