"""Flashcards

   A program for running through flashcards. Card data is stored in csv files
   from the data/[flash]cards directory.
"""

import csv
from pathlib import Path
import random
import textwrap
from sys import stderr, argv
from os import _exit as exit

WIDTH = 75
MARGIN = 20
MAXWIDTH = WIDTH - MARGIN
DEBUG_MODE = False
CARDS_DIR = Path(__file__).parent.parent.parent / "data" / "cards"
TOPICS = []

def error(*args):
    """Print an error message"""
    print("Error", *args)
    exit(1)

def load_csv(path, errors):
    """Takes one argument, a Path object to a csv file. Return a list where
    each item is a dict with "front" and "back" keys, one for each row in the
    file except the header."""

    # initialize cards list
    cards = []

    if not path.is_file():
        errors.append("file does not exist: {path}")
        return

    if path.suffix.lower() != ".csv":
        errors.append(f"Not a csv file: {path}")
        return

    with open(path) as fh:
        reader = csv.reader(
            fh,
            quotechar="'",
            skipinitialspace=True,
            escapechar="\\",
        )

        # iterate through each line of file
        for lineno, row in enumerate(reader):
            if not row:
                continue

            # initialize card dict
            card = {}

            # ensure that there are 2 columns
            if len(row) != 2:
                errors.append(
                    f"{path.name}@{lineno + 1}: "
                    f"{len(row)} column(s)")
                continue

            # get the card data from the row
            card["front"] = row[0].strip()
            card["back"] = row[1].strip()

            # skip the header row
            if (card["front"].lower(), card["back"].lower()) == ("front", "back"):
                continue

            # add card to the list
            if card not in cards:
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
        print("=" * WIDTH)

        # print card x of y
        print(f"card {num} of {total}".rjust(WIDTH), "\n" * 2)

        # print the card front
        print("QUESTION".center(WIDTH))
        print("--------".center(WIDTH), "\n")

        # wrap long questions
        lines = textwrap.wrap(card['front'], MAXWIDTH)
        for line in lines:
            print(line.center(WIDTH))

        print("\n" * 2)

        if DEBUG_MODE:
            print(f"The answer is: {card['back']}")

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

        # exit for quit command
        if answer.lower() in ("q", "quit"):
            break

        # if the answer was wrong, print the right one
        if answer != card["back"]:
            print("CORRECT ANSWER".center(WIDTH))
            print("--------------".center(WIDTH), "\n")
            print(card["back"].center(WIDTH), "\n" * 2)

        # print the current score
        print(f"score: {score} of {num}".rjust(WIDTH))

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


def menu():
    """Print a menu of all topics, return list of selected Paths"""
    TOPICS = sorted(CARDS_DIR.iterdir())

    if not TOPICS:
        reldir = CARDS_DIR.relative_to(Path.cwd())
        error("No flashcard data found in directory: {reldir}.")

    print(f"[0] all")
    for i, path in enumerate(TOPICS, 1):
        print(f"[{i}] {path.stem}")

    choices = input("choose one or more topics: ")
    selection = []
    for num in choices.split():

        # special case for "all"
        if num == "0":
            return TOPICS

        try:
            num = int(num) - 1
        except ValueError:
            error(f"Not a valid selection: {num}")

        try:
            selection.append(TOPICS[num])
        except IndexError:
            error(f"Not a valid selection: {num}")

    return selection

def main(limit=None):
    paths = menu()
    cards, errors = [], []

    for path in paths:
        cards.extend( load_csv(path, errors) )

    if errors:
        print()
        messages = [f"    {e}\n" for e in errors]
        error("CSV file errors:\n\n", *messages)

    if not cards:
        return

    random.shuffle(cards)

    if limit:
        cards = cards[:limit]

    play(cards)

# only call main() if the script is being run, not imported
if __name__ == "__main__":
    # get the limit from command line arguments
    limit = None
    try:
        idx = argv.index("--limit")
    except ValueError:
        pass
    else:
        if len(argv) > idx+1:
            limit = int(argv[idx+1])

    try:
        main(limit)

    # suppress errors when the user hits CTRL+C
    except KeyboardInterrupt:
        print()
