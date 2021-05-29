"""Flashcards

   A program for running through flashcards. Card data is stored in csv files
   from the data/[flash]cards directory.

   Instructions
   ============

   Setup
   -----
   1. Create a folder data/flashcards if it doesn't exist
   2. Make flashcard csv files
      [ ] In the data/flashcards directory manually make file called ending in .csv
      [ ] Each line should be one card with the format: "text for front, text for back".
      Here is my "paths.csv" example:

      front, back
      import the Path class, from pathlib import Path
      check if Path object path exists, path.exists()
      check if Path object path is a file, path.is_file()
      check if Path object path is a directory, path.is_dir()

   Exercise
   --------
   1. Start your flashcards.py file
      [ ] write a main() function, and in it print something, then call it

   2. Write a load_csv() function

      This function should take one argument, a Path object to a csv
      file. Eventually it will return a list where each item is a dict with
      "front" and "back" keys, one for each row in the file except the header.

      * part 1: start the function and call it from main()
      load_csv():
      [ ] write a load_csv() function that takes one argument, "path"
      [ ] check to make sure the csv file exists, if not, print a message
          including the path then return
      [ ] print "loading file: {path}"

      in main():
      [ ] make a Path object to your csv file
      [ ] call your load_csv() function, passing it your path object as the
          argument, and assign the returned value to a variable named cards

      * part 2: read each line of the csv file
      in load_csv():
      [ ] open the csv file in read mode using the `open()` function
      [ ] use `fp.readlines()` to iterate through each line in the file
      [ ] print each line

      * part 3: parse the cards from the csv file
      in load_csv(), before the readlines() loop:
      [ ] make an empty list assigned to a variable named cards

      in load_csv(), in the readlines() loop:
      [ ] make an empty dict assigned to a variable named card
      [ ] split each line on the "," using the `.split()` method and assign
          the result to a variable named row
      [ ] check that there are two items in the row using the len() function,
          if not print an error message and return
      [ ] card["front"] to the first item in the row, and card["back"] to the
          second
      [ ] append the card dict to the cards list using the .append() method

      after the end of the loop:
      [ ] return the cards list

      in main():
      [ ] if the cards is falsy, return
      [ ] otherwise, print the cards list

      * part 4: remove extra whitespace
      in load_csv():
      [ ] use the .strip() method to remove leading and trailing whitespace
          (including the "\n" at the end of each line) from card["front"] and
          card["back"]

      * part 5: skip the header
      in load_csv(), in the readlines() loop, before append:
      [ ] check if card["front"] is "front" and card["back"] is "back", if so,
          continue before appending to the cards list

   2. Write a play() function

      This function should take one argument, the list of cards.
      Eventually it will contain the user interface for running through each
      card, getting the answers from the user, and printing the score.

      * part 1: start the play() function
          [ ] write a play() function that takes one argument: cards
          [ ] print something from it

          in main():
          [ ] call play() passing it the list of cards

       * part 2: in random order, go through each card
           at the top of your file:
               [ ] import the random module
           in play():
               [ ] make a while loop where the condition is: cards
           in the loop:
               [ ] use random.choice() to get a random item from the cards
                   list and assign it to a variable named card
               [ ] remove the selected card from the list by calling .remove
                   on cards passing it the argument card
               [ ] print card

       * part 3: basic flashcards interface
           in play(), above the loop:
               [ ] assign the length of cards to a variable total
               [ ] make a num variable set to 1
               [ ] make a score variable set to 0
           in play(), in the loop:
               [ ] print card x of y followed by the card["front"]
               [ ] prompt the user for their answer using the input() function
                   and assign the result to a variable named answer
               [ ] check if the answer is the same as card["back"]
                   [ ] if so, increment score by one and print "CORRECT"
                   [ ] if not, print "INCORRECT", then cards["back"]
               [ ] increment num by 1
               [ ] call input() asking if the user wants to continue
           in play(), after the loop:
               [ ] print "{score} of {total}"

       * part 4: prettify flashcards
           [ ] get rid of any debug print() statements
           at the top of your file:
               [ ] make a global variable WIDTH and set it to around 75
           in play():
               [ ] add a line to the beginning and end of each card
               [ ] print the "card x of y" message on its own line
               [ ] add some extra lines around various elements
               [ ] center any string by calling the .center() method on it and
                   pass the argument WIDTH
               [ ] right align any string by calling the .rjust() method on it
                   and passing the argument WIDTH
               [ ] add the score of total to the end of each card

   Bonus ideas
   -----------
   [ ] keep a log with dates and scores
   [ ] make extra flashcard files, then add a menu to allow the user to select
       which topic(s) they would like to be quizzed on
   [ ] add an optional limit argument to limit the number of cards to go
       through at a time
   [ ] add extra columns to flashcards files to keep track of each time you get
       the answer right and wrong, use this to generate reports
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
