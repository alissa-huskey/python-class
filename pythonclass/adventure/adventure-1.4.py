"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html
"""

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

def do_quit():
    """Exit the game."""
    print("Ok, goodbye.")
    quit()

def main():
    print("Welcome!")
    while True:
        reply = input("> ")

        if reply in ["q", "quit", "exit"]:
            do_quit()

        else:
            print("No such command.")
            continue

        print()

if __name__ == "__main__":
    main()

