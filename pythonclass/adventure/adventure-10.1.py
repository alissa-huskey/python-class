"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html

+--------------------------------------------------------+
|                                                        |
| =========                                              |
| World Map                                              |
| =========                                              |
|                                                        |
|                                                        |
|           market                                       |
|             |                                          |
| home -- town square -- woods -- hill                   |
|             |                    |                     |
|           bakery                cave                   |
|                                                        |
+--------------------------------------------------------+

Part 10.1: Add market and market items

"""

import re
import textwrap

from console import fg, bg, fx

WIDTH = 45

MARGIN = 2

DEBUG = True

# ## Game World Data #########################################################

PLAYER = {
    "place": "home",
    "inventory": {},
}


PLACES = {
    "home": {
        "key": "home",
        "name": "Your Cottage",
        "east": "town-square",
        "description": "A cozy stone cottage with a desk and a neatly made bed.",
        "items": ["desk", "book"],
    },
    "town-square": {
        "key": "town-square",
        "name": "The Town Square",
        "west": "home",
        "north": "market",
        "description": (
            "A large open space surrounded by buildings with a burbling "
            "fountain in the center."
        ),
    },
    "market": {
        "key": "market",
        "name": "The Market",
        "south": "town-square",
        "items": ["elixir", "dagger"],
        "description": (
            "A tidy store with shelves full of goods to buy. A wooden hand "
            "painted menu hangs on the wall."
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
        "can_take": True,
        "name": "a book",
        "description": (
            "A hefty leather-bound tome open to an interesting passage."
        ),
    },

}

# ## Message functions #######################################################

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
    print(MARGIN*" ", text, sep="")

def error(message):
    """Print an error message."""
    print(f"{fg.red('! Error')} {message}\n")

def debug(message):
    """Print a debug message if in debug mode."""
    if not DEBUG:
        return
    print(fg.lightblack(f"# {message}"))

def abort(message):
    """Print a fatal error message then exit the game."""
    error(message)
    exit(1)

# ## Data functions ##########################################################

def get_place(key=None):
    """Return the place information from the PLACES dictionary, either
       associated with key, or if none is passed, where the user is
       currently at. """
    # get the current player's place if key is not passed
    if not key:
        key = PLAYER["place"]

    # get the place info
    place = PLACES.get(key)

    # this should never happen if we write the code correctly
    # but just in case there is no key in PLACES matching
    # the new name, print an error
    if not place:
        abort(f"Woops! The information about {key!r} seems to be missing.")

    return place

def get_item(key):
    """Return item information from ITEMS dictionary associated with key. If no
       item is found, print an error message and return None."""
    item = ITEMS.get(key)

    if not item:
        abort(f"Woops! The information about {key!r} seems to be missing.")

    return item


def inventory_change(key, quantity=1):
    """Add item to player inventory."""
    PLAYER["inventory"].setdefault(key, 0)
    PLAYER["inventory"][key] += quantity

    # remove from inventory dictionary if quantity is zero
    if not PLAYER["inventory"][key]:
        PLAYER["inventory"].pop(key)

def place_add(key):
    """Add an item to the current place."""
    # get the current place
    place = get_place()

    # add the item key to the place items list
    place.setdefault("items", [])
    if key not in place["items"]:
        place["items"].append(key)

def place_remove(key):
    """Remove an item from the current place."""
    # get the current place
    place = get_place()

    # remove from place
    if key in place.get("items", []):
        place["items"].remove(key)

# ## Validation functions ####################################################

def player_has(key, qty=1):
    """Return True if the player has at least qty item(s) associated with key in
       their inventory."""
    return key in PLAYER["inventory"] and PLAYER["inventory"][key] >= qty

def place_has(item):
    """Return True if current place has a particular item."""
    place = get_place()
    return item in place.get("items", [])

def is_for_sale(item):
    """Return True if item is for sale (has a price)."""
    return "price" in item

# ## Action functions ########################################################

def do_shop():
    """List the items for sale."""

    place = get_place()

    header("Items for sale.")

    for key in place.get("items", []):
        item = get_item(key)
        if not is_for_sale(item):
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
    place = get_place()

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
            item = get_item(key)
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

        destination = get_place(name)
        write(f"To the {direction} is {destination['name']}.")

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

    # make sure the item is in this place or in the players inventory
    if not (place_has(name) or player_has(name)):
        error(f"Sorry, I don't know what this is: {name!r}.")
        return

    # get the item dictionary
    item = get_item(name)

    # print the item information
    header(item["name"].title())

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
    old_place = get_place()

    # look up what is in that direction from here
    new_name = old_place.get(direction)

    # print an error if there is nothing in that direction
    if not new_name:
        error(f"Sorry, you can't go {direction} from here.")
        return

    # look up the place information
    new_place = get_place(new_name)

    # move the player to the new place
    PLAYER["place"] = new_name

    # print information about the new place
    header(f"{new_place['name']}")
    wrap(new_place["description"])

def do_take(args):
    """Pick up an item and add it to inventory."""
    debug(f"Trying to take: {args}")

    # make sure the player typed an item
    if not args:
        error("What do you want to take?")
        return

    # get the item name from arguments
    # and make it lowercase
    name = args[0].lower()

    # make sure the item is in this place
    if not place_has(name):
        error(f"Sorry, I don't see a {name!r} here.")
        return

    # get the item information
    item = get_item(name)

    if not item.get("can_take"):
        error(f"You try to pick up {name!r}, but you find you aren't able to lift it.")
        return

    # add to inventory
    inventory_change(name)

    # remove from place
    place_remove(name)

    wrap(f"You pick up {item['name']} and put it in your pack.")

def do_inventory():
    """Show the players inventory"""

    debug("Trying to show inventory.")

    header("Inventory")

    if not PLAYER["inventory"]:
        write("Empty.")
        return

    for name, qty in PLAYER["inventory"].items():
        item = get_item(name)
        write(f"(x{qty:>2})  {item['name']}")

    print()

def do_drop(args):
    """Remove an item from inventory"""

    debug(f"Trying to drop: {args}.")

    # make sure the player typed an item
    if not args:
        error("What do you want to drop?")
        return

    # get the item name from arguments
    # and make it lowercase
    name = args[0].lower()

    # make sure the item is in inventory
    if not player_has(name):
        error(f"You don't have any {name!r}.")
        return

    # get the amount currently in inventory
    qty = PLAYER["inventory"][name]

    # remove from player inventory
    inventory_change(name, -qty)

    # add to place items
    place_add(name)

    # print a message
    wrap(f"You set down the {name}.")


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

        if command in ("q", "quit", "exit"):
            do_quit()

        elif command in ("shop"):
            do_shop()

        elif command in ("g", "go"):
            do_go(args)

        elif command in ("x", "exam", "examine"):
            do_examine(args)

        elif command in ("l", "look"):
            do_look()

        elif command in ("t", "take", "grab"):
            do_take(args)

        elif command in ("i", "inventory"):
            do_inventory()

        elif command == "drop":
            do_drop(args)

        else:
            error("No such command.")
            continue

        # print a blank line no matter what
        print()

if __name__ == "__main__":
    main()

