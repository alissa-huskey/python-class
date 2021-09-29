"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html
"""

def do_shop():
    """List the items for sale."""
    print("\nItems for sale.\n")

    for key, item in ITEMS.items():
        print(f'{item["name"]:<13}', item["description"])

    print()

def do_quit():
    """Exit the game."""
    print("Ok, goodbye.")
    quit()

def do_go(args):
    """Move to a different place"""
    print(f"Trying to go: {args}")

def main():
    print("Welcome!")
    while True:
        reply = input("> ").strip()
        args = reply.split()

        if not args:
            continue

        command = args.pop(0)

        if command in ["q", "quit", "exit"]:
            do_quit()

        elif command in ["shop"]:
            do_shop()

        elif command in ["g", "go"]:
            do_go(args)

        else:
            print("No such command.")
            continue

        print()

if __name__ == "__main__":
    main()

