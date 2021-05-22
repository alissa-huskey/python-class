"""Flashcards

   A program for running through flashcards. It will load csv files from the
   data/flashcards directory.  Each line of a csv file is one card--the text
   for the front of the card, a comma, then the text for the back.

   The program will then

    Setup
    -----
    1. Create a folder data/flashcards if it doesn't exist
    2. Make flashcard csv files
       [ ] In the data/flashcards directory manually make file called ending in .csv
       [ ] Each line should be one card with the format: "text for front, text for back".
       Here is my "paths.csv" example:

       import the Path class, from pathlib import Path
       check if Path object path exists, path.exists()
       check if Path object path is a file, path.is_file()
       check if Path object path is a directory, path.is_dir()

    Exercise
    --------
    1. Start your flashcards.py file
       [ ] write a main() function, and in it print something, then call it
    2. Write a load_csv() function
       [ ] open the csv file you made using the `open()` function
       [ ] use `fp.readlines()` to iterate through each line in the file
       [ ] use the `.split()` method on each

    TODO
    ----
    [ ] test in vscode web, figure out width/height issue
        [ ] test with env var $COLUMNS, $LINES
    [ ] write more instructions / description
"""

from pathlib import Path
import random
import time
from os import _exit as exit
from sys import stderr, stdout

from pythonclass.exercises import cli

from pythonclass.exercises.cli import (
    abort,
    quit,
    WIDTH,
)

CARDS_DIR = Path(__file__).parent.parent.parent / "data" / "cards"

def load_cards(path, cards=[]):
    """Return list of cards in a csv file at path
       Skips optional header row "front, back".

       Return
       ------
       a list of dicts, where each dict has keys "front" and "back"

       for example:
       [
          {
             'front': "life the universe and everything?",
             'back': "42"
          },
          {
            'front': "most famous classic blunder",
            'back': "never get involved in a land war in Asia"
          },
       ]

    """
    if not path.exists():
        abort(f"No file found: {path}")

    if path.suffix.lower() != ".csv":
        abort(f"Not a csv file: {path}")

    with open(path) as fp:
        for lineno, line in enumerate(fp.readlines()):
            # strip the newline from the end
            # plus any other leading and trailing whitespace
            line = line.strip()

            # skip the header row
            if lineno == 0 and line.replace(" ", "").lower() == "front,back":
                continue

            # make a cards dict
            card = {}

            # split the line at the "," delimiter
            card["front"], card["back"] = line.split(",")

            # strip trailing and leading whitespace
            card["front"] = card["front"].strip()
            card["back"] = card["back"].strip()

            # add to the cards list
            cards.append(card)

    return cards

def play(cards, category):
    """Run through flashcards, return (score, total)"""
    # initialize values
    score, count, total = 0, 1, len(cards)

    while cards:
        # clear the screen before printing each card
        cli.clear()

        # pick a random card and remove it from the deck
        card = random.choice(cards)
        cards.remove(card)

        # print x of y (right aligned)
        cli.output(f"{count} of {total}", align="right")
        cli.newline(3)

        # print the front of the card
        cli.output(card["front"], align="center")
        cli.newline(2)

        # ask the user for input, then return the cursor to the
        # beginning of the same line
        with cli.goback():
            answer = input("> ")

        # figure out if their answer was right or wrong
        # and set their score and feedback symbol appropriately
        if answer == card["back"]:
            feedback = cli.symbols.right
            score += 1
        else:
            feedback = cli.symbols.wrong

        # print the check mark or x over where the prompt was
        # then go down a few lines
        cli.output(feedback)
        cli.newline(3)


        # print the correct answer
        # then go down a bit
        cli.output(f"{card['back']}",
                   align="center",
                   width=WIDTH - 1,
                   color="green_reverse")
        cli.newline(2)

        # print something to let the user know
        # they're done with this card
        action = "[next]"
        if count == total:
            action = "[done]"
        cli.output(action, color="cyan", align="center")

        # wait for them to press any key before
        # moving onto the next card
        cli.await_keypress()

        # increment the counter
        count += 1

    return score, total

def endgame(score, total):
    """Print the score"""

    # calculate the percentage score
    percent = int((score / total) * 100)

    # clear the screen then go down a bit
    cli.clear()
    cli.newline(3)

    # print the score
    cli.output(f"{percent}% - {score} of {total}", align="center")
    cli.newline(3)

def main():
    path = CARDS_DIR / "paths.csv"
    cards = load_cards(path)
    score, total = play(cards, path.stem)
    endgame(score, total)

# only call main() if the script is being run, not imported
if __name__ == "__main__":
    try:
        main()

    # this suppresses errors when the user hits CTRL+C
    except KeyboardInterrupt:
        print()

    # this suppress traceback message for some normal exits
    except SystemExit:
        ...

    # suppress traceback messages for normal usage
    except (cli.GracefulExit, cli.FatalError) as e:

        # if there's a message, print it nicely
        if e.message:
            out = stderr if e.code else stdout
            print(f"{e.prefix}{e.message}", file=out)

        # exits 0 if no errors, nonzero otherwise
        exit(e.code)
