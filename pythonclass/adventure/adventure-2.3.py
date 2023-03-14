"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html
"""

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
    }
}

def error(message):
    """Print an error message."""
    print(f"! Error: {message}\n")

def debug(message):
    """Print a debug message if in debug mode."""
    if not DEBUG:
        return
    print(f"# {message}")

def do_shop():
    """List the items for sale."""
    print("\nItems for sale.\n")

    for item in ITEMS.values():
        print(f'{item["name"]:<13}  {item["description"]}')

    print()

def do_quit():
    """Exit the game."""
    print("Ok, goodbye.\n")
    quit()

def do_go(args):
    """Move to a different place"""
    debug(f"Trying to go: {args}")

def main():
    print("Welcome!")

    while True:
        debug(f"You are at: {PLAYER['place']}")

        reply = input("> ").strip()
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

