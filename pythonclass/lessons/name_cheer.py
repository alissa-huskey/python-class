"""Print a cheerleader cheer for your name.

An exercise from the loops lesson:
https://alissa-huskey.github.io/python-class/lessons/loops.html
"""

import time

NAME = "Alissa"

def main():
    i = 0
    while i < len(NAME):
        print("Gimme a", NAME[i].upper() + "!")
        i += 1
        time.sleep(0.5)

    print("\nWhat does it spell?")
    print(NAME.upper() + "!")


main()
