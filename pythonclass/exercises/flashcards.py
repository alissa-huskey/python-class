"""Flashcards

   A program for running through flashcards. Card data is stored in csv files
   from the data/[flash]cards directory.
"""

from pathlib import Path
import random
from sys import stderr

WIDTH = 75
CARDS_DIR = Path(__file__).parent.parent.parent / "data" / "cards"

def error(*args):
    """Print an error message"""
    print("Error", *args)

def load_csv(path):
    """Takes one argument, a Path object to a csv file. Return a list where
    each item is a dict with "front" and "back" keys, one for each row in the
    file except the header."""

    if not path.is_file():
        error("file does not exist: {path}")
        return

    if path.suffix.lower() != ".csv":
        error(f"Not a csv file: {path}")
        return

    # initialize cards list
    cards = []

    with open(path) as fp:
        # iterate through each line of file
        for line in fp.readlines():

            # initialize card dict
            card = {}

            # split the line at the "," delimiter
            row = line.split(",")

            # ensure that there are 2 columns
            if len(row) != 2:
                error(f"{path.name}:{lineno + 1}:",
                      f"wrong number of columns: {len(row)} --",
                      f"'{line.strip()}'")
                return

            # get the card data from the row
            card["front"] = row[0].strip()
            card["back"] = row[1].strip()

            # skip the header row
            if card["front"] == "front" and card["back"] == "back":
                continue

            # add card to the list
            cards.append(card)

    # return the list of cards
    return cards

def play(cards):
    """The user interface for running through each card, getting the answers
    from the user, and printing the score.  Takes one argument, the list of
    cards."""

    # initialize values
    hide_cursor, show_cursor  = "\x1b[?25l", "\x1b[?12;25h"
    score, num, total = 0, 1, len(cards)
    right_symbol = "\u2714"          # ✔
    wrong_symbol = "\u2716"          # ✖

    # continue until we're out of cards
    while cards:

        # select a random card then remove it
        card = random.choice(cards)
        cards.remove(card)

        # print a line at the top of every card
        print("\n")
        print("=" * 75)

        # print card x of y
        print(f"card {num} of {total}".rjust(WIDTH), "\n" * 2)

        # print the card front
        print("QUESTION".center(WIDTH))
        print("--------".center(WIDTH), "\n")
        print(f"{card['front']}".center(WIDTH), "\n" * 2)

        # get the user answer
        answer = input("> ")

        # figure out if their answer was right or wrong
        # and set their score and print feedback appropriately
        if answer == card["back"]:
            score += 1
            feedback = f"{right_symbol} RIGHT!"
        else:
            feedback = f"{wrong_symbol} INCORRECT"
        print(feedback, "\n" * 2)

        # if the answer was wrong, print the right one
        if answer != card["back"]:
            print("CORRECT ANSWER".center(WIDTH))
            print("--------------".center(WIDTH), "\n")
            print(card["back"].center(WIDTH), "\n" * 2)

        # print the current score
        print(f"score: {score} of {total}".rjust(WIDTH))

        # print a line at the end of the card
        print("=" * 75, "\n" * 2)

        # wait for them to press enter before
        # moving onto the next card
        input("[continue]".center(WIDTH) + hide_cursor)
        print(show_cursor, end="")

        # increment the counter
        num += 1


    # print the final score
    print("\n" * 3)
    title = "FINAL SCORE"
    line = ("*" * len(title)).center(WIDTH)

    print(title.center(WIDTH), "\n")
    print(line, "\n")
    print(f"{score} of {total}".center(WIDTH), "\n")
    print(line, "\n" * 3)


def main():
    csv = CARDS_DIR / "paths.csv"
    cards = load_csv(csv)
    if not cards:
        return
    play(cards)

# only call main() if the script is being run, not imported
if __name__ == "__main__":
    try:
        main()

    # suppress errors when the user hits CTRL+C
    except KeyboardInterrupt:
        print()
