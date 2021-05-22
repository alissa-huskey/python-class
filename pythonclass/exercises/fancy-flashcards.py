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

PRIZES   = (
    (100,  cli.symbols.hundred   ) ,      # 💯
    ( 95,  cli.symbols.trophy    ) ,      # 🏆
    ( 90,  cli.symbols.medal     ) ,      # 🏅
    ( 85,  cli.symbols.sparkles  ) ,      # ✨
    ( 80,  cli.symbols.start3    ) ,      # 💫
    ( 75,  cli.symbols.start2    ) ,      # 🌟
    ( 70,  cli.symbols.star      ) ,      # ⭐
    ( 65,  cli.symbols.rock      ) ,      # 🤘
    ( 60,  cli.symbols.clap      ) ,      # 👏
    ( 55,  cli.symbols.thumbsup  ) ,      # 👍
    ( 50,  cli.symbols.ok        ) ,      # 👌
)

MESSAGES   = (
    ( 95,  "Amazing!"                            ) ,
    ( 90,  "Fantastic!"                          ) ,
    ( 85,  "Supurb"                              ) ,
    ( 80,  "WOW"                                 ) ,
    ( 75,  "Great job!"                          ) ,
    ( 70,  "Astounding!"                         ) ,
    ( 65,  "Impressive work"                     ) ,
    ( 60,  "Excellent"                           ) ,
    ( 55,  "Wowzers",                            ) ,
    ( 50,  "Your hard work is paying off!"       ) ,
    ( 40,  "Nice work today!"                    ) ,
    ( 30,  "Great practice!"                     ) ,
    ( 20,  "Done for the day!"                   ) ,
    ( 10,  "Mark coding practice off your list!" ) ,
    (  0,  "Good for you!"                       ) ,
)


def prize(score: int):
    """Return a symbol and message for a 0-100 score"""
    symbol = ""

    for level, s in PRIZES:
        print(level, s)
        if score >= level:
            symbol = s
            break

    for level, m in MESSAGES:
        if score >= level:
            message = m
            break

    return (message, symbol)

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
            if lineno == 0 and line.startswith("front"):
                continue

            card = {}
            card["front"], card["back"] = [ text.strip() for text in line.split(",") ]
            cards.append(card)

    return cards

def play(cards, category):
    """Run through flashcards, return (score, total)"""
    score, count, total = 0, 1, len(cards)

    while cards:
        cli.clear()

        card = random.choice(cards)
        cards.remove(card)

        cli.output(category, end="")
        cli.output(f"{count} of {total}",
                   align="right",
                   width=WIDTH-len(category))

        cli.goto_middle()
        cli.output(card["front"], align="center")

        cli.goto_bottom(5)
        with cli.goback():
            answer = input("> ")

            if answer == card["back"]:
                feedback = cli.symbols.right
                score += 1
            else:
                feedback = cli.symbols.wrong

        cli.output(feedback)

        cli.goto_middle(3)
        cli.output(f"{card['back']}",
                   align="center",
                   width=WIDTH - 1,
                   color="green_reverse")
        cli.goto_bottom(2)

        if count == total:
            message = "[done]"
        else:
            message = "[next]"

        cli.output(message, color="cyan", align="center")

        cli.await_keypress()

        count += 1

    return score, total

def endgame(score, total):
    """Print the score"""
    percent = int((score / total) * 100)
    message, symbol = prize(percent)

    cli.clear()
    cli.goto_middle()
    cli.output(f"{percent}% - {score} of {total}", align="center")

    cli.goto_middle(2)
    cli.output(f"{symbol:<2}{message}", align="center")
    cli.goto_bottom()

def main():
    path = CARDS_DIR / "paths.csv"
    cards = load_cards(path)
    score, total = play(cards, path.stem)
    endgame(score, total)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
    except (cli.GracefulExit, cli.FatalError) as e:
        if e.message:
            out = stderr if e.code else stdout
            print(f"{e.prefix}{e.message}", file=out)
        exit(e.code)
