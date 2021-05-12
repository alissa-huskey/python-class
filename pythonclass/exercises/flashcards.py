"""Flashcards
    Setup
    -----
    1. Create a folder data/flashcards if it doesn't exist
    2. Make flashcard csv files

    Exercise
    --------
"""

from pathlib import Path
import random
import time

from blessed import Terminal

FLASHCARDS_DIR = Path(__file__).parent.parent.parent / "data" / "flashcards"
TERM = Terminal()

POSITIONS = {
    "top": 1,
    "midpoint": TERM.height // 2,
    "mid-bottom": (TERM.height // 2) + (TERM.height // 4),
    "input": TERM.height - 5,
    "bottom": TERM.height - 2,
}

def get_flashcards(path):
    """Return a list of flashcards for path"""
    cards = []
    with open(path) as fp:
        for line in fp.readlines():
            card = {}
            card["back"], card["front"] = line.strip().split(",")
            cards.append(card)

    return cards

def output(text):
    """print to screen without newline"""
    print(text, end="")

def goto(position, down=0):
    """Move to vertical position on screen"""
    lineno = POSITIONS[position] + down
    output(TERM.move_y(lineno))

def clear():
    """Clear the screen"""
    output(TERM.home + TERM.clear)

def run(cards, title):
    """Run through flashcards, return (score, total)"""
    score, count, total = 0, 1, len(cards)

    while cards:
        card = random.choice(cards)
        cards.remove(card)

        clear()
        output(title)
        output(TERM.rjust(f"{count} of {total}", width=TERM.width-len(title)))

        goto("midpoint")
        output(TERM.center(card["front"]))

        goto("input")
        answer = input("> ")

        if answer == card["back"]:
            feedback = TERM.green("\u2714")  # ✔
            score += 1
        else:
            feedback = TERM.red("\u2716")    # ✖

        goto("input", 1)
        output(feedback)

        goto("mid-bottom")
        output(TERM.black_on_green(TERM.center(f"{card['back']}",
                                               width=TERM.width - 1)))

        goto("bottom")
        if count == total:
            message = "[done]"
        else:
            message = "[next]"

        output(TERM.cyan(TERM.center(message)))

        with TERM.cbreak(), TERM.hidden_cursor():
            TERM.inkey()

        count += 1

    return score, total

def endgame(score, total):
    """Print the score"""
    percent = int((score / total) * 100)

    clear()
    goto("midpoint")
    output(TERM.center(f"{percent}% - {score} of {total}"))
    goto("bottom", -2)

def main():
    path = FLASHCARDS_DIR / "paths.csv"
    cards = get_flashcards(path)
    score, total = run(cards, path.stem)
    endgame(score, total)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        ...
