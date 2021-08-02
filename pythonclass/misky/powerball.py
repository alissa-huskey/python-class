"""Powerball matching """
from typing import NamedTuple, TypeVar, Any
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from random import choice, choices, randint
import json
from pathlib import Path
from os import _exit as exit
from sys import stderr
import pytz

from console import fg, bg, fx

WEEK, MONTH = 604811, 2592060
UTC = pytz.utc
WHITE_BALLS = tuple(range(1, 70))
RED_BALLS = tuple(range(1, 27))
POWER_PLAY = (True, False)
WINS = {}

STYLES = {
    "white": (
        fg.black + bg.white,
        fg.black + bg.lightwhite,
    ),
    "red": (
        fg.white + bg.red,
        fg.lightwhite + bg.lightred,
    )
}

SYMBOLS = [(fg.red, "✘"), (fg.green, "✔")]

PowerPlay = TypeVar("PowerPlay", bool, int)

def symbol(number, matches):
    """Return a styled symbol depending on if number is in matches"""
    color, char = SYMBOLS[number in matches]
    return color(char.center(2))

class Picks(NamedTuple):
    white: tuple
    red: int
    powerplay: PowerPlay
    other: Any = None
    label: str = ""
    date: datetime = datetime.today()

    def print(self):
        """Print styled label, date, balls, and powerplay; if self.other is
           present also print the check or x marks of matches."""

        if self.other:
            self.other.print()
        tpl = "{: >2d}"

        output = [f"{self.label: >10}:", str(self.date.date())]

        for num in self.white:
            style = STYLES["white"][num in self.matches[0]]
            output.append(style(tpl.format(num)))

        style = STYLES["red"][self.red in self.matches[1]]
        output.append(style(tpl.format(self.red)))

        if type(self.powerplay) == int:
            output.append(f"x{self.powerplay}")
        elif self.powerplay:
            output.append("✧")


        print(*output, sep="  ")
        print()

        if not self.other:
            return

        output = [symbol(num, self.matches[0]) for num in self.white]
        output.append(symbol(self.red, self.matches[1]))
        output.insert(0, " ".ljust(23))

        print(*output, sep="  ")
        print()

        if self.prize:
            print("{:>11}".format("Prize:"), f"${self.prize:.2f}", "\n")


    @property
    def guessed(self):
        """Return a tuple containing the number of correctly guessed (white, red)

        >>> one = Picks(list(range(1, 6)), 5, 2)
        >>> two = Picks(list(range(3, 7)), 1, False, one)
        >>> two.guessed
        (3, 0)
        >>> one = Picks(list(range(1, 6)), 5, 2)
        >>> two = Picks(list(range(5, 10)), 5, False, one)
        >>> two.guessed
        (1, 1)
        """
        return tuple(map(len, self.matches))

    @property
    def prize(self):
        """
        >>> winner = Picks((1, 21, 22, 34, 47), 4, 2)
        >>> mine = Picks(range(100, 106), 8, False, winner)
        >>> mine.prize
        0
        >>> mine = Picks(range(1, 6), 4, False, winner)
        >>> mine.prize
        4
        >>> mine = Picks((1, 21, 22, 34, 47), 8, True, winner)
        >>> mine.prize
        2000000
        >>> mine = Picks((1, 21, 22, 34, 47), 4, True, winner)
        >>> mine.prize
        199000000
        """
        if not self.other:
            raise ValueError("Cannot calculat prize without self.other")

        possible = PRIZES.get(self.guessed, loss)

        if callable(possible):
            return possible()

        amount, func = possible

        if self.powerplay:
            amount = func(amount, self.other.powerplay)

        return amount

    @property
    def matches(self):
        """Return a tuple of the intersection between self and other white and
           red respectively

        >>> one = Picks(list(range(1, 6)), 5, 2)
        >>> two = Picks(list(range(3, 7)), 1, False, one)
        >>> two.matches
        ({3, 4, 5}, set())
        >>> one = Picks(list(range(1, 6)), 5, 2)
        >>> two = Picks(list(range(5, 10)), 5, False, one)
        >>> two.matches
        ({5}, {5})
        """

        if not self.other:
            return (set(), set())

        return (
            set(self.white).intersection(self.other.white),
            set((self.red,)).intersection((self.other.red,))
        )


def request_recent_wins():
    """."""
    # from pythonclass.lessons.private import RAPIDAPI_KEY
    # t.astimezone(pytz.timezone('US/Eastern'))
    # "x-ratelimit-basic-remaining": "49",
    # "x-ratelimit-basic-reset": "2678383",

    # rl = "https://powerball.p.rapidapi.com/Latest10"
    # headers = {
    #     'x-rapidapi-key': RAPIDAPI_KEY,
    #     'x-rapidapi-host': "powerball.p.rapidapi.com"
    #     }
    # response = requests.request("GET", url, headers=headers)

def abort(*args):
    """Print error message and exit"""
    print(*args, file=stderr)
    exit(1)

def loss():
    """Prize callback, returns zero"""
    return 0

def jackpot():
    """Prize callback, returns the current jackpot amount"""
    return 199_000_000

def multiplied(amount, multiplier):
    """Powerplay callback, returns the prize times the powerplay multiplier"""
    return amount * multiplier

def doubled(amount, multiplier):
    """Powerplay callback returns the prize times two"""
    return amount * 2

PRIZES = {
    (0,1): (4, multiplied),
    (1,1): (4, multiplied),
    (2,2): (7, multiplied),
    (3,0): (7, multiplied),
    (3,1): (100, multiplied),
    (4,0): (100, multiplied),
    (4,1): (50_000, multiplied),
    (5,0): (1_000_000, doubled),
    (5,1): jackpot,
}

def load_wins(filepath, wins={}):
    """Load recent winning numbers from json file"""
    with open(filepath) as fp:
        data = json.load(fp)

    for win in reversed(data.get("data", [])):
        win.pop("NumberSet")
        drew = parse(win.pop("DrawingDate"))
        powerball, multiplier = win.pop("PowerBall"), win.pop("Multiplier")

        wins[drew] = Picks(win.values(), powerball, multiplier, date=drew, label="Winner")

def generate():
    """Randomly generate a ticket between a week and month ago"""
    date = datetime.utcnow() - relativedelta(seconds=randint(WEEK, MONTH))
    pick = (
        choices(WHITE_BALLS, k=5),
        choice(RED_BALLS),
        choice(POWER_PLAY),
    )
    return date.astimezone(UTC), pick

def main():
    """Randomly generate a ticket, find the winning numbers associated, and
       print the comparison and prize"""

    path = Path(__file__).parent.parent.parent / "data" / "powerball.json"
    load_wins(path, WINS)

    picked, data = generate()
    for drew, selection in WINS.items():
        if drew > picked:
            win = selection
            break

    if not win:
        abort("Error: No ticket found for ticket purchased")

    pick = Picks(*data, other=win, label="Yours", date=picked)
    pick.print()


if __name__ == "__main__":
    main()
