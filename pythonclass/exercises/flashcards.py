"""Flashcards

   A program for running through flashcards. Card data is stored in csv files
   from the data/[flash]cards directory.
"""

import csv
from pathlib import Path
import random
import textwrap
from sys import stderr
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

    with open(path) as fp:
        # iterate through each line of file
        for lineno, row in enumerate(csv.reader(
            fp,
            quotechar="'",
            skipinitialspace=True,
            escapechar="\\"
        )):
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

def main():
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

    play(cards)

def parse_line(line: str):
    quotes, backslash, comma = ("'", '"'), "\\", ","

    cells, start, stop, quote = [], None, None, ""

    for i, char in enumerate(line):
        last = line[i-1]

        # the cell hasn't started
        if start is None:

            # the cell starts with a quote,
            # so set start and quote
            if char in quotes:
                start = i + 1
                quote = line[i]
                #  say("found start quote", start=start, quote=quote)

            elif start == i:
                continue

            # disregard whitespace outside of cells
            elif char.isspace() or char == comma:
                continue

            # the first nonspace, non-quote character
            # is the beginning of the cell
            else:
                start = i
                # say("found first non-whitespace char", start=start, quote=quote)


        # this cell started with a quote
        elif quote:

            # this cell ends with the same quote, non-escaped
            if char == quote and last != backslash:
                stop = i
                # say("matched quote", start=start, quote=quote, char=char, stop=stop)

        # this cell didn't start with a quote
        else:

            # the cell ends at the next comma
            if char == comma and last != backslash:
                stop = i
                # say("found end comma", start=start, quote=quote, stop=stop)


        # if we've found the end of the cell
        # append it to cells and reset variables
        if stop:
            cells.append(line[start:stop])
            start, stop, quote = None, None, ""

    # append the last item
    if start and not stop:
        cells.append(line[start:])

    return cells

# only call main() if the script is being run, not imported
if __name__ == "__main__":
    try:
        main()

    # suppress errors when the user hits CTRL+C
    except KeyboardInterrupt:
        print()
