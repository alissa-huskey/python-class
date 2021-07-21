"""
Demo of an input function that will timeout

Uses the blessed module:
https://blessed.readthedocs.io/en/latest/intro.html

Install with pip:
pip install blessed

or poetry:
poetry install blessed
"""

from blessed.terminal import Terminal

TERM = Terminal()

def timed_input(limit=3):
    """Return the user input, but timeout after limit seconds"""
    key, timeout = "", 0

    # enter cbreak mode, where every keypress is sent to our program
    with TERM.cbreak():

        # keep going as long as we haven't reached the timeout
        # and no key has been pressed
        while not key and timeout < limit:
            # assign the key variable to whatever key was pressed
            key = TERM.inkey(timeout=1)

            # increment timeout
            timeout += 1

    if not key:
        print("\nOut of time!")
        return
    else:
        return key + input(key)

def main():
    print("say something: ")
    answer = timed_input()
    if answer:
        print(f"\nYou answered: {answer}")




main()
