"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html
"""

import re
import textwrap

from console import fg, bg, fx

WIDTH = 45

MARGIN = 2

DEBUG = True

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
    "elixir": {
        "key": "elixir",
        "name": "healing elixir",
        "description": "a magical elixir that will heal what ails ya",
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
        "name": "a desk",
        "description": (
            "A wooden desk with a large leather-bound book open on "
            "its surface."
        ),
    },
    "book": {
        "key": "book",
        "name": "a book",
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
    margin = MARGIN * " "
    # wrap the text
    paragraph = textwrap.fill(
        text,
        WIDTH,
        initial_indent=margin,
        subsequent_indent=margin,
    )

    # print the wrapped text
    print(paragraph)


def write(text):
    """Print an indented line of game text."""
    print(MARGIN * " ", text, sep="")

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

def do_look():
    """Look at the current place"""

    debug("Trying to look around.")

    # look up where the player is now
    place_name = PLAYER["place"]
    place = PLACES[place_name]

    # print information about the current place
    header(f"{place['name']}")
    wrap(place["description"])

    # get the items in the room
    items = place.get("items", [])

    if items:
        # for each of the place items
        # get the info from the ITEMS dictionary
        # and make a list of item names
        names = []
        for key in items:
            item = ITEMS.get(key)
            names.append(item["name"])

        # remove the last name from the list
        last = names.pop()

        # construct a sentence that looks like one of:
        #   x, x and y
        #   x and y
        #   y
        text = ", ".join(names)
        if text:
            text += " and "
        text += last

        # print the list of items.
        print()
        wrap(f"You see {text}.\n")

    # add a blank line
    print()

    # print what is in each direction from here
    for direction in ("north", "east", "south", "west"):
        name = place.get(direction)
        if not name:
            continue

        destination = PLACES.get(name)
        write(f"To the {direction} is {destination['name']}.")

def do_examine(args):
    """Look at an item in the current place."""

    debug(f"Trying to examine: {args}")

    # make sure the player said what they want to examine
    if not args:
        error("What do you want to examine?")
        return

    # look up where the player is now
    place_name = PLAYER["place"]
    place = PLACES[place_name]

    # get the item entered by the user and make it lowercase
    name = args[0].lower()

    # make sure the item is in this place
    if name not in place.get("items", []):
        error(f"Sorry, I don't know what this is: {name!r}.")
        return

    # make sure the item is in the ITEMS dictionary
    if name not in ITEMS:
        error(f"Woops! The information about {name} seems to be missing.")
        return

    # get the item dictionary
    item = ITEMS[name]

    # print the item information
    header(item["name"])
    wrap(item["description"])

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

        elif command in ("shop"):
            do_shop()

        elif command in ("g", "go"):
            do_go(args)

        elif command in ("x", "exam", "examine"):
            do_examine(args)

        elif command in ("l", "look"):
            do_look()

        else:
            error("No such command.")
            continue

        print()

if __name__ == "__main__":
    main()

