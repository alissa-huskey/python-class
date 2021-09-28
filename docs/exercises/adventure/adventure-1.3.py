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

