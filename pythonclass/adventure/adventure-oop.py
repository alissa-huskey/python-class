"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html

OOP Refactor (From Part 9.4)
"""

import re
import textwrap

from console import fg, bg, fx

WIDTH = 45

MARGIN = 2

DEBUG = True

class DuplicateKeyError(BaseException): ...
class MissingRequiredAttrError(BaseException): ...
class UnrecognizedAttrError(BaseException): ...

class Object():
    """Base class for all objects"""
    REQUIRED = []
    PARAMS = {}

    @classmethod
    def get(cls, key):
        val = cls.all.get(key)

        if not val:
            klass = self.__class__.__name__
            abort(f"Woops! The information about the {klass.lower()} {key!r} seems to be missing.")

        return val

    def __init__(self, **kwargs):
        """Set all attributes in PARAMS with their default values"""

        klass = self.__class__.__name__

        # add all kwargs as attrs, unless unrecognized
        for name, val in kwargs.items():
            if name in self.PARAMS:
                setattr(self, name, val)
            else:
                raise UnrecognizedAttrError(f"Unrecognized {klass} attr: {name}")

        # set defaults for missing attrs
        for name, default in self.PARAMS.items():
            if default and name not in self.__dict__:
                setattr(self, name, default())

        # raise for missing required attrs
        for name in self.REQUIRED:
            if name not in self.__dict__:
                raise MissingRequiredAttrError(
                    f"Missing required attribute: {name}")


    def __repr__(self):
        params = ("key", "name")
        attrs = [f"{x}={getattr(self, x)!r}" for x in params if hasattr(self, x)]
        text = ", ".join(attrs)
        return f"<{self.__class__.__name__} {text}>"

class Collectable(Object):
    """Base class objects with collections"""
    all = {}

    @classmethod
    def get(cls, key):
        return cls.all.get(key)

    def __init__(self, **kwargs):
        """Set all attributes in PARAMS with their default values"""

        klass = self.__class__.__name__

        super().__init__(**kwargs)

        # raise exception if key is duplicated
        if self.key in self.all:
            raise DuplicateKeyError(f"Duplicate {klass} Key: {self.key}")

        # add to collection
        self.__class__.all[self.key] = self


class Place(Collectable):
    all = {}

    def __str__(self):
        return self.name

    PARAMS = {
        "key": None,
        "name": None,
        "description": None,
        "north": lambda: None,
        "south": lambda: None,
        "east": lambda: None,
        "west": lambda: None,
        "items": list,
    }
    REQUIRED = ["key", "name", "description"]

    def has(self, item):
        """return True if place has a particular item"""
        return item in self.items

    def to_the(self, direction):
        key = self.__dict__.get(direction)
        return self.all.get(key)


class Item(Collectable):
    all = {}

    PARAMS = {
        "key": None,
        "name": None,
        "description": None,
        "price": lambda: None,
        "can_take": lambda: False,
    }
    REQUIRED = ["key", "name", "description"]

    def is_for_sale(self):
        """Return True if item is for sale."""
        return not self.price == None

class Player(Object):
    PARAMS = {
        "place": None,
        "inventory": dict,
    }

    def has(self, key, qty=1):
        """Return True if the player has at least qty item(s) associated with
        key in their inventory."""
        return key in self.inventory and self.inventory[key] >= qty

    @property
    def place(self):
        return self.__dict__["place"]

    @place.setter
    def place(self, place):
        if isinstance(place, str):
            place = Place.get(place)
        self.__dict__["place"] = place


# ## Game World Data #########################################################

Place(
    key="home",
    name="Your Cottage",
    east="town-square",
    description="A cozy stone cottage with a desk and a neatly made bed.",
    items=["desk", "book"],
)
Place(
    key="town-square",
    name="The Town Square",
    west="home",
    description=(
        "A large open space surrounded by buildings with a burbling "
        "fountain in the center."
    ),
)

Item(
    key="elixir",
    name="healing elixir",
    description="a magical elixir that will heal what ails ya",
    price=-10,
)
Item(
    key="dagger",
    name="a dagger",
    description="a 14 inch dagger with a double-edged blade",
    price=-25,
)
Item(
    key="desk",
    name="a desk",
    description=(
        "A wooden desk with a large leather-bound book open on "
        "its surface."
    ),
)
Item(
    key="book",
    can_take=True,
    name="a book",
    description=(
        "A hefty leather-bound tome open to an interesting passage."
    ),
)

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

# ## Action functions ########################################################


class Command(Object):
    def __str__(self):
        return self.name

    def __init__(self, game):
        self.game = game

    def __getattr__(self, name):
        """Get missing attrs from self.game"""
        if hasattr(self.game, name):
            return getattr(self.game, name)
        raise AttributeError(name)

    @property
    def name(self):
        if not self.aliases:
            return ""
        return self.aliases[0]

class Shop(Command):
    aliases = ("shop",)

    def do(self):
        """List the items for sale."""

        header("Items for sale.")

        for item in self.items:
            if not item.is_for_sale():
                continue

            write(f'{item.name:<13}  {item.description}')
        print()

class Quit(Command):
    aliases = ("quit", "q", "exit")

    def do(self):
        """Exit the game."""
        write("Ok, goodbye.\n")
        quit()

class Look(Command):
    aliases = ("look", "l")

    def do(self):
        """Look at the current place"""

        debug("Trying to look around.")

        # print information about the current place
        header(self.place.name)
        wrap(self.place.description)

        if self.place.items:

            # for each of the place items
            # get the info from the Item.all
            # and make a list of item names
            names = []
            for key in self.place.items:
                item = Item.get(key)
                names.append(item.name)

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
            destination = self.place.to_the(direction)
            if destination:
                write(f"To the {direction} is {destination.name}.")

class Examine(Command):
    aliases = ("examine", "x", "ex", "exam")

    def do(self, *args):
        """Look at an item in the current place."""

        debug(f"Trying to examine: {args}")

        # make sure the player said what they want to examine
        if not args:
            error("What do you want to examine?")
            return

        # get the item entered by the user and make it lowercase
        name = args[0].lower()

        # make sure the item is in this place or in the players inventory
        if not (self.place.has(name) or self.player.has(name)):
            error(f"Sorry, I don't know what this is: {name!r}.")
            return

        # get the item object
        item = self.items.get(name)

        # print the item information
        header(item.name.title())
        wrap(item.description)

class Go(Command):
    aliases = ("go", "g")

    def do(self, *args):
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

        # look up what is in that direction from here
        destination = self.place.to_the(direction)

        # print an error if there is nothing in that direction
        if not destination:
            error(f"Sorry, you can't go {direction} from here.")
            return

        # move the player to the new place
        self.place = destination

        # print information about the new place
        header(f"{destination.name}")
        wrap(destination.description)

class Take(Command):
    aliases = ("take", "t", "grab")

    def do(self, *args):
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
        if not self.place.has(name):
            error(f"Sorry, I don't see a {name!r} here.")
            return

        # get the item information
        item = Item.get(name)

        if not item.can_take:
            error(f"You try to pick up {name!r}, but you find you aren't able to lift it.")
            return

        # add to inventory
        self.player.inventory.setdefault(name, 0)
        self.player.inventory[name] += 1

        # remove from place
        self.place.items.remove(name)

        wrap(f"You pick up {item.name} and put it in your pack.")

class Inventory(Command):
    aliases = ("inventory", "i")

    def do(self):
        """Show the players inventory"""

        debug("Trying to show inventory.")

        header("Inventory")

        if not self.player.inventory:
            write("Empty.")
            return

        for name, qty in self.player.inventory.items():
            item = Item.get(name)
            write(f"(x{qty:>2})  {item.name}")

        print()

class Drop(Command):
    aliases = ("drop", "d")

    def do(self, *args):
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
        if not player.has(name):
            error(f"You don't have any {name!r}.")
            return

        # remove from inventory
        self.player.inventory[name] -= 1
        if not self.player.inventory[name]:
            self.player.inventory.pop(name)

        # add to place items
        self.place.items.append(name)


class Game():
    def __init__(self):
        self.player = Player(place="home")
        self.items = Item.all
        self.places = Place.all
        self.commands = {}
        self.history = []

        for klass in Command.__subclasses__():
            cmd = klass(self)
            for alias in cmd.aliases:
                self.commands[alias] = cmd

    def parse(self, text):
        """Parse user input."""
        self.history.append(text)
        self.command_text, self.command = None, None
        self.args = text.strip().split()

        if self.args:
            self.command = self.args.pop(0)

        debug(f"Command: {self.command}, args: {self.args}")

    @property
    def input(self):
        if self.history:
            return self.history[0]

    @property
    def command(self):
        return self.__dict__["command"]

    @command.setter
    def command(self, val):
        if isinstance(val, str):
            self.command_text = val
            val = self.commands.get(val)
        self.__dict__["command"] = val

    @property
    def place(self):
        return self.player.place


def main():
    header("Welcome!")

    game = Game()

    while True:
        debug(f"You are at: {game.place}")

        reply = input(fg.cyan("> ")).strip()
        game.parse(reply)

        if not reply:
            continue

        if game.command:
            game.command.do(*game.args)

        else:
            error("No such command.")
            continue

        # print a blank line no matter what
        print()

if __name__ == "__main__":
    main()

