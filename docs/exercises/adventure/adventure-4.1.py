"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html
"""

import re
import textwrap

from console import fg, bg, fx

WIDTH = 45

MARGIN = "  "

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
            "A wooden desk with a large leather-bound book open on "
            " its surface."
        ),
    },
    "book": {
        "key": "book",
        "name": "A book",
        "description": (
            "A hefty leather-bound tome open to an interesting passage."
        ),
    },
}

def header(title):
    """Print a header"""
    print()
    write(fx.bold(title))
    print()

def wrap(text):
    """Print wrapped and indented text."""
    # wrap the text
    paragraph = textwrap.fill(
        text,
        WIDTH,
        initial_indent=MARGIN,
        subsequent_indent=MARGIN,
    )

    # print the wrapped text
    print(paragraph)


def write(text):
    """Print an indented line of game text."""
    print(MARGIN, text, sep="")

def error(message):
    """Print an error message."""
    print(f"{fg.red('! Error')} {message}\n")

def debug(message):
    """Print a debug message if in debug mode."""
    if not DEBUG:
        return
    print(fg.lightblack(f"# {message}"))

def do_shop():
    """List the items for sale."""

    header("Items for sale.")

    for item in ITEMS.values():
        if "price" not in item:
            continue
        write(f'{item["name"]:<13}  {item["description"]}')

    print()

def do_quit():
    """Exit the game."""
    write("Ok, goodbye.\n")
    quit()

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
    old_name = PLAYER["place"]
    old_place = PLACES[old_name]

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
    wrap(new_place["description"])

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

        else:
            error("No such command.")
            continue

        print()

if __name__ == "__main__":
    main()

