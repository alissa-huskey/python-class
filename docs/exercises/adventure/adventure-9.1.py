"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html

  =========               N
  World Map             W-+-E
  =========               S



  home -- town square -- woods -- hill
                                   |
                                  cave

"""

import re
import textwrap

from console import fg, bg, fx

WIDTH = 45

MARGIN = 2

DEBUG = True

PLAYER = {
    "place": "home",
    "inventory": {},
}

PLACES = {
    "home": {
        "name": "your cottage",
        "east": "town-square",
        "items": ["note", "desk", "walking-stick", "note"],
        "description": "A cozy stone cottage with a desk and a neatly made bed.",
        "details": (
            "The furniture in your one room stone cottage is made up of dark "
            "wood. A circular rug covers much of the cold stone floor and heat "
            "from a cast iron stove in the corner drives away the chill.",

            "Light streams in through the window against the north wall, "
            "around which a counter and shelves hold kitchen supplies. Against "
            "the opposite wall is a desk with a high backed chair. Built into "
            "a nook behind you is your bed, the bedding is slightly rumpled.",

            "Before you is the arched wooden front door, facing east.",
        )
    },
    "town-square": {
        "name": "the town square",
        "west": "home",
        "east": "woods",
        "items": ["fountain", "coin"],
        "description": (
            "A large open space surrounded by buildings with a burbling "
            "fountain in the center."
        ),
    },
    "woods": {
        "name": "the woods",
        "west": "town-square",
        "east": "hill",
        "description": (
            "A spooky forest."
        ),
    },
    "hill": {
        "name": "a grassy hill",
        "west": "woods",
        "south": "cave",
        "description": (
            "A dirt path meanders up a grassy hill."
        ),
    },
    "cave": {
        "name": "a gloomy cave",
        "north": "hill",
        "items": ["dragon"],
        "actions": ["pet"],
        "description": (
            "A vast cavern."
        ),
        "details": (
            "Your footsteps echo as you step into the vast cavern.",

            "Shafts of sunlight slice through the gloom, playing against the "
            "landscape of glittering treasure.",

            "Resting atop a mound of gold, a collosal dragon rests curled up "
            "snugly. Its three enormous heads snore softly, each in turn.",
        )
    },
}

ITEMS = {
    "elixr": {
        "name": "healing elixr",
        "description": "a magical elixr that will heal what ails ya",
        "price": -10,
    },
    "dagger": {
        "name": "a dagger",
        "description": "a 14 inch dagger with a double-edged blade",
        "price": -25,
    },
    "desk": {
        "name": "a desk",
        "items": ["book"],
        "description": (
            "A wooden desk with a large leather-bound book open on "
            "its surface."
        ),
    },
    "note": {
        "can_take": True,
        "name": "a note",
        "aliases": ["scroll", "note"],
        "description": (
            "A note scrawled hastily on a scroll."
        ),
        "do_read": (
            "The worn and creased scroll reads:",
            (
                "Beware the Jabberwock, my son!",
                "The jaws that bite, the claws that catch!",
                "Beware the Jubjub bird, and shun",
                "The frumious Bandersnatch!",
            ),
        ),
    },
    "book": {
        "can_take": True,
        "name": "a book",
        "description": (
            "A hefty leather-bound tome open to an interesting passage."
        ),
        "do_read": (
            "The hefty leather bound tome is open to a page that reads:",
            (
                "At the edge of the woods is a cave that is home to a three "
                "headed dragon, each with a different temperament.",

                "Legend says that if you happen upon the dragon sleeping, the "
                "brave may pet one of its three heads.",

                "Choose the right head and you will be rewarded with great "
                "fortunes.",

                "But beware, choose poorly and it will surely mean your doom!",
            ),
        ),
    },
    "walking-stick": {
        "aliases": ("stick", "walking stick"),
        "can_take": True,
        "name": "a walking stick",
        "description": (
            "A gnarled walking stick made of wood."
        ),
    },
    "dragon": {
        "name": "a three-headed dragon",
        "description": (
            "A fearsome three-headed dragon."
        ),
    },
    "coin": {
        "name": "a silver coin",
        "can_take": True,
        "description": "A shiny silver coin.",
    },
    "fountain": {
        "name": "a fountain",
        "description": (
            "A merrily bubbling fountain."
        ),
    },
}

# item alias (str) -> item key (str)
ITEM_ALIASES = {}

# place (str) -> item keys (list[str])
PLACE_ITEMS = {}

# action (str) -> item key (str)
ACTION_ITEMS = {}

# action (str) -> place keys (list[str])
ACTION_PLACES = {}

def header(title):
    """Print a header"""
    write(fx.bold(title), before=1, after=1)

def nl(times=1):
    print("\n"*times, end="")

def wrap(text, before=0, after=0, indent=MARGIN * " "):
    """Print wrapped and indented text."""
    # wrap the text
    paragraph = textwrap.fill(
        text,
        WIDTH,
        initial_indent=indent,
        subsequent_indent=indent,
    )

    # print the wrapped text
    nl(before)
    print(paragraph)
    nl(after)

def write(text, before=0, after=0, indent=MARGIN * " "):
    """Print an indented line of game text."""
    nl(before)
    print(indent, text, sep="")
    nl(after)

def error(message):
    """Print an error message."""
    print(f"{fg.red('! Error')} {message}\n")

def debug(message):
    """Print a debug message if in debug mode."""
    if not DEBUG:
        return
    print(fg.lightblack(f"# {message}"))

def has(item):
    """Return True if item is in inventory"""
    if not item:
        return False

    key = item["key"]
    return item and key in PLAYER["inventory"] and PLAYER["inventory"][key]

def is_present(item):
    """Return True if item is in current place"""
    if not item:
        return False

    place = get_place()
    return item["key"] in PLACE_ITEMS.get(place["key"], [])

def is_available(item):
    """Return True if the item is in the current place or inventory"""
    return has(item) or is_present(item)

def get_item(key):
    """Return the item from ITEMS associated with key."""
    return ITEM_ALIASES.get(key, {})

def get_place(key=None, default=None):
    """Return the place from PLACES associated with key or current place if key is not
    present."""
    if not key:
        key = PLAYER["place"]
    return PLACES.get(key, default)

def do_shop():
    """List the items for sale."""

    header("Items for sale.")

    for item in ITEMS.values():
        if "price" not in item:
            continue
        write(f'{item["name"]:<13}  {item["description"]}')

    nl()

def do_quit():
    """Exit the game."""
    write("Ok, goodbye.\n")
    quit()

def do_look(verbose=False):
    """Look at the current place"""

    debug("Trying to look around.")

    # look up where the player is now
    place = get_place()

    # print information about the current place
    header(f"{place['name'].title()}")

    if "details" in place and (verbose or not place.get("visited")):
        for paragraph in place.get("details", []):
            wrap(paragraph, after=1)
    else:
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
        wrap(f"You see {text}.", before=1, after=1)

    # print what is in each direction from here
    for direction in ("north", "east", "south", "west"):
        name = place.get(direction)
        if not name:
            continue

        destination = get_place(name)
        write(f"To the {direction} is {destination['name']}.", after=1)

def do_examine(args):
    """Look at an item in the current place."""

    debug(f"Trying to examine: {args}")

    # make sure the player said what they want to examine
    if not args:
        error("What do you want to examine?")
        return

    # get the item entered by the user and make it lowercase
    name = " ".join(args).lower()
    item = get_item(name)

    # make sure the item is in this place or in the players inventory
    if not is_available(item):
        error(f"Sorry, I don't know what this is: {name!r}.")
        return

    # print the item information
    header(item["name"].title())
    wrap(item["description"])

    # get the items in the room
    children = item.get("items", [])

    if children:
        # for each of the place items
        # get the info from the ITEMS dictionary
        # and make a list of item names
        names = []
        for key in children:
            child = get_item(key)
            names.append(child["name"])

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
        wrap(f"You see {text}.", before=1, after=1)


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

    # this should never happen if we write the code correctly
    # but just in case there is no key in PLACES matching
    # the new name, print an error
    if not new_place:
        error(f"Woops! The information about {new_name} seems to be missing.")
        return

    # move the player to the new place
    PLAYER["place"] = new_name

    # print information about the new place
    do_look()

    # mark the place as visited
    new_place["visited"] = True

def do_take(args):
    """Pick up an item and add it to inventory."""
    debug(f"Trying to take: {args}")

    # make sure the player typed an item
    if not args:
        error("What do you want to take?")
        return

    # get the item name from arguments
    # and make it lowercase
    name = " ".join(args).lower()

    # get the item information
    item = get_item(name)

    # make sure the item is in this place
    if not is_present(item):
        error(f"Sorry, I don't see a {name!r} here.")
        return

    if not item.get("can_take"):
        wrap(
            f"You try to pick up {item['name']} but you find you aren't able "
            "to lift it.",
            before=1
        )
        return

    PLAYER["inventory"].setdefault(name, 0)
    PLAYER["inventory"][name] += 1
    unplace_item(item)

    wrap(f"You pick up {item['name']} and put it in your pack.", before=1)

def do_inventory():
    """Show the players inventory"""

    debug("Trying to show inventory.")

    header("Inventory")

    if not PLAYER["inventory"]:
        write("Empty.")

    for name, qty in PLAYER["inventory"].items():
        item = get_item(name)
        write(f"(x{qty:>2})  {item['name']}")

    nl()

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

    item = get_item(name)

    # make sure the item is in inventory
    if not has(item):
        error(f"You don't have any {name!r}.")
        return

    # remove from inventory
    PLAYER["inventory"][name] -= 1
    if not PLAYER["inventory"][name]:
        PLAYER["inventory"].pop(name)

    # look up where the player is now
    place = get_place()

    place_item(place, item)

    wrap(
        f"You remove {item['name']} from your pack and leave it on the ground.",
        before=1,
    )

def do_read(args):
    """Read an item"""
    name = " ".join(args)
    item = get_item(name)

    if not is_available(item):
        error(f"Sorry, I don't see {name!r}.")
        return

    if not item.get("do_read"):
        error(f"Sorry, I don't know how to read {name!r}.")
        return

    intro, paragraphs = item.get("do_read")

    header(item["name"].title())
    wrap(intro, after=1)

    for text in paragraphs:
        wrap(text, after=1, indent=MARGIN*2+" ")

def unplace_item(item):
    if not item:
        error(f"Failed to unplace: {item!r}")
        exit(1)

    key = item["key"]

    parent = item["parent"]
    place = item["place"]

    item["parent"] = {}

    if place and key in place["items"]:
        place["items"].remove(key)

    if parent and key in parent["items"]:
        parent["items"].remove(key)

    if key in PLACE_ITEMS[place["key"]]:
        PLACE_ITEMS[place["key"]].remove(key)

    item["place"] = {}

def place_item(place, item, parent=None):
    if not item:
        error(f"Failed to place: {item!r} @ {place_key!r}")
        exit(1)

    place["items"].append(item["key"])

    PLACE_ITEMS[place["key"]].append(item["key"])

    item["place"] = place
    item["parent"] = parent

    for key in item.get("items", []):
        child = get_item(key)
        place_item(place, child, item)

def init():
    """Initialize game."""
    # set up PLACES
    for key, place in PLACES.items():
        place["key"] = key
        place.setdefault("items", [])
        place.setdefault("details", [])
        place.setdefault("actions", [])

    # set up ITEMS
    for key, item in ITEMS.items():
        item["key"] = key
        item.setdefault("parent", {})
        item.setdefault("items", [])
        item.setdefault("aliases", [])
        item.setdefault("actions", [])
        item.setdefault("can_take", False)

    # set up ITEM_ALIASES, ACTION_ITEMS
    for key, item in ITEMS.items():
        ITEM_ALIASES[key] = item

        for action in item["actions"]:
            ACTION_ITEMS[action].append(item["key"])

        for alias in item["aliases"]:
            ITEM_ALIASES[alias] = item

    # set up ACTION_PLACES, PLACE_ITEMS
    for key, place in PLACES.items():
        PLACE_ITEMS.setdefault(key, [])
        for item_key in place["items"]:
            item = get_item(item_key)
            place_item(place, item)

        for action in place["actions"]:
            ACTION_PLACES.setdefault(action, [])
            ACTION_PLACES[action].append(key)

def main():
    init()
    header("Welcome!")
    do_look()
    place = get_place()
    place["visited"] = True

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
            do_look(verbose=True)

        elif command in ("t", "take", "grab"):
            do_take(args)

        elif command in ("i", "inventory"):
            do_inventory()

        elif command in ("read"):
            do_read(args)

        elif command == "drop":
            do_drop(args)

        else:
            error("No such command.")
            continue

        nl()

if __name__ == "__main__":
    main()

