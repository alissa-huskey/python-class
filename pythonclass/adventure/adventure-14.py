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

Part 14: Dragons

"""

import random
import textwrap
from string import Template

from console import fg, fx

WIDTH = 45

MARGIN = 2

DEBUG = True

# ## Game World Data #########################################################

COLORS = ("red", "black", "silver")

MOODS = [
    {
        "mood": "cheerful",
        "treasure": (3, 15),
        "message": "thinks you're adorable! He gives you $gems gems!"
    },
    {
        "mood": "grumpy",
        "damage": (-15, -3),
        "message": (
            "wants to be left alone. The heat from his mighty sigh "
            "singes your hair, costing you $damage in health."
        ),
    },
    {
        "mood": "lonely",
        "treasure": (8, 25),
        "damage": (-25, -8),
        "message": (
            "is just SO happy to see you! He gives you a whopping "
            "$amount gems! Then he hugs you, squeezes you, and calls "
            "you George... costing you $damage in health."
        )
    },
]

# placeholder -- maps colors to dragons
DRAGONS = {}

PLAYER = {
    "place": "home",
    "inventory": {"gems": 50},
    "health": 100,
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
        "east": "woods",
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
        "items": ["elixr", "dagger"],
        "can": ["shop", "buy"],
        "description": (
            "A tidy store with shelves full of goods to buy. A wooden hand "
            "painted menu hangs on the wall."
        ),
    },
    "woods": {
        "key": "woods",
        "name": "The Woods",
        "east": "hill",
        "west": "town-square",
        "description": (
            "A dirt road meanders under a canopy of autumn leaves in brilliant "
            "hues of gold and crimson.",

            "You hear a stream burbling somewhere out of sight. Leaves crunch "
            "under your feet on the sun dappled forest floor.",

            "You see an ancient moss-covered hollow tree, its gnarled and twisted "
            "branches looming over you. On the opposite side, a fallen log juts "
            "partway into the road.",
        ),
        "items": [],
    },
    "hill": {
        "key": "hill",
        "name": "A grassy hill",
        "west": "woods",
        "south": "cave",
        "description": (
            "A winding path leads up the slope of a grassy hill. The air is "
            "warm here.",
            "At the top of the hill, you see that the path continues to the "
            "down to the south. In that direction you can make out a cave by "
            "the shore of a lake."
        ),
        "items": [],
    },
    "cave": {
        "key": "cave",
        "name": "A cave",
        "north": "hill",
        "description": (
            "Your footsteps echo as you step into the vast cavern.",
            "Shafts of sunlight slice through the gloom, playing against the "
            "landscape of glittering treasure.",
            "Resting atop a mound of gold, a collosal dragon rests curled up snugly. "
            "Its three enormous heads snore softly, each in turn.",
        ),
        "items": [],
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
        "title": (
            "The book is open to a page that reads:"
        ),
        "message": (
            "At the edge of the woods is a cave that is home to a three "
            "headed dragon, each with a different temperament. ",

            "Legend says that if you happen upon the dragon sleeping, the "
            "brave may pet one of its three heads. ",

            "Choose the right head and you will be rewarded with great "
            "fortunes. ",

            "But beware, choose poorly and it will surely mean your doom!",
        ),
    },
    "gems": {
        "key": "gems",
        "name": "gems",
        "description": (
            "A pile of sparkling gems."
        ),
    },
}

# ## Message functions #######################################################


def header(title):
    """Print a header"""
    print()
    write(fx.bold(title))
    print()


def wrap(text, indent=1):
    """Print wrapped and indented text."""

    # calculate the indentation
    margin = (MARGIN * " ") * indent

    # if a string was passed, turn it into a single item tuple
    if isinstance(text, str):
        text = (text,)

    # make an empty list for the wrapped blocks
    blocks = []

    # iterate over items
    for stanza in text:

        # wrap the text
        paragraph = textwrap.fill(
            stanza,
            WIDTH,
            initial_indent=margin,
            subsequent_indent=margin,
        )

        blocks.append(paragraph)

    # print the wrapped text
    print(*blocks, sep="\n\n")


def write(text, indent=1):
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


def health_change(amount):
    """Add the following (positive or negative) amount to health, but limit to 0-100"""
    PLAYER["health"] += amount

    # don't let health go below zero
    if PLAYER["health"] < 0:
        PLAYER["health"] = 0

    # cap health at 100
    if PLAYER["health"] > 100:
        PLAYER["health"] = 100


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


def place_can(action):
    """Return True if the current place supports a particular action."""
    place = get_place()
    return action in place.get("can", [])


def is_for_sale(item):
    """Return True if item is for sale (has a price)."""
    return "price" in item


# ## Action functions ########################################################


def do_shop():
    """List the items for sale."""

    if not place_can("shop"):
        error("Sorry, you can't shop here.")
        return

    place = get_place()

    header("Items for sale.")

    for key in place.get("items", []):
        item = get_item(key)
        if not is_for_sale(item):
            continue

        write(
            f'{item["name"]:<13}  {item["description"]:<45}  '
            f'{abs(item["price"]):>2} gems'
        )

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

    # print the price if we're in the market
    if place_can("shop") and place_has(name) and is_for_sale(item):
        write(f"{abs(item['price'])} gems".rjust(WIDTH - MARGIN))
        print()

    # print the quantity if the item is from inventory
    elif player_has(name):
        write(f"(x{PLAYER['inventory'][name]})".rjust(WIDTH - MARGIN))
        print()

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


def do_buy(args):
    """Purchase an item."""

    debug(f"Trying to buy: {args}.")

    if not place_can("buy"):
        error("Sorry, you can't buy things here.")
        return

    # make sure the player typed an item
    if not args:
        error("What do you want to buy?")
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

    if not is_for_sale(item):
        error(f"Sorry, {item['name']} is not for sale.")
        return

    price = abs(item["price"])
    if not player_has("gems", price):
        gems = PLAYER["inventory"].get("gems", 0)
        error(
            f"Sorry, you can't afford {item['name']} "
            f"because it costs {price} and you only have {gems}."
        )
        return

    # remove gems from inventory
    inventory_change("gems", -price)

    # add item to inventory
    inventory_change(name)

    # remove item from place
    place_remove(name)

    wrap(f"You bought {item['name']}.")


def do_read(args):
    """Read an item with a message."""

    debug(f"Trying to read: {args}")

    # make sure the player said what they want to read
    if not args:
        error("What do you want to read?")
        return

    # get the item entered by the user and make it lowercase
    name = args[0].lower()

    # make sure the item is in this place or in the players inventory
    if not (place_has(name) or player_has(name)):
        error(f"Sorry, I don't know what this is: {name!r}.")
        return

    # get the item dictionary
    item = get_item(name)

    # make sure it is an item you can read
    if "message" not in item:
        error(f"Sorry, I can't read {name!r}.")
        return

    # print the item header
    title = item.get("title", "It reads...")
    header(title)

    # print the item message
    wrap(item["message"], indent=3)


def do_pet(args):
    """Pet dragons"""

    debug(f"Trying to pet: {args}")

    # make sure they are somewhere they can pet dragons
    if not place_can("pet"):
        error("You can't do that here.")

    # remove the expected words from args
    for word in ["dragon", "head"]:
        if word in args:
            args.remove(word)

    # make sure the player said what they want to pet
    if not args:
        error("What do you want to pet?")
        return

    color = args[0].lower()

    # make sure they typed in a real color
    if color not in COLORS:
        error("I don't see a dragon that looks like that.")
        return

    # generate the DRAGONS dict and randomly assign each color to a dragon
    global DRAGONS
    if not DRAGONS:
        random.shuffle(COLORS)
        DRAGONS = dict(zip(COLORS, MOODS))

    # get the dragon info for this color
    dragon = DRAGONS[color]
    dragon["color"] = color

    # calculate the treasure
    possible_treasure = dragon.get("treasure", (0, 0))
    dragon["gems"] = random.randint(*possible_treasure)

    # calculate the damage
    possible_damage = dragon.get("damage", (0, 0))
    dragon["damage"] = random.randint(*possible_damage)

    # add the treasure to the players inventory
    if dragon["gems"]:
        inventory_change("gems", dragon["gems"])

    # remove health
    if dragon["damage"]:
        health_change(dragon["damage"])

    # generate the message
    tpl = Template(f'The $mood $color dragon {dragon["message"]}')
    text = tpl.safe_substitute(dragon)
    write(text)

    # reset the DRAGONS dict
    DRAGONS = {}


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

        elif command in ("r", "read"):
            do_read(args)

        elif command == "drop":
            do_drop(args)

        elif command == "buy":
            do_buy(args)

        else:
            error("No such command.")
            continue

        # print a blank line no matter what
        print()

        # exit the game if player has no health
        if not PLAYER["health"]:
            write("Game over.\n")
            quit()


if __name__ == "__main__":
    main()
