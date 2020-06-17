#!/usr/bin/env python3
"""
cards.py - Deal a hand of cards to 4 players.
Inspired by: https://realpython.com/python-type-checking/
Wherein I mess around a bit with function annotations and OOP.
"""

import random

RANKS = list(range(2, 11)) + list("JQKA")
SUITS = [
    "♠",  # \U2660 BLACK SPADE SUIT
    "♡",  # \U2661 WHITE HEART SUIT
    "♢",  # \U2662 WHITE DIAMOND SUIT
    "♣",  # \U2663 BLACK CLUB SUIT
    #  "♤",  # \U2664 WHITE SPADE SUIT
    #  "♥",  # \U2665 BLACK HEART SUIT
    #  "♦",  # \U2666 BLACK DIAMOND SUIT
    #  "♧",  # \U2667 WHITE CLUB SUIT
]


class Screen:
    """Class for display related functionality"""
    PREFIX = '\x1b'
    CLEAR = f'{PREFIX}[H{PREFIX}[2J'
    INVERT = f'{PREFIX}[7m'
    NORMAL = f'{PREFIX}[0m'
    GREEN = f'{PREFIX}[32m'
    GRAY = f'{PREFIX}[48;5;8m'

    @classmethod
    def invert(cls, text: str) -> str:
        """Return text surrounded with control sequences to invert fg/bg
        colors"""
        return f"{cls.INVERT}{text}{cls.NORMAL}"

    @classmethod
    def clear(cls) -> str:
        """Return control sequences to clear the screen"""
        return cls.CLEAR

    @classmethod
    def green(cls, text: str) -> str:
        """Return control sequences to turn text green"""
        return f"{cls.GREEN}{text}{cls.NORMAL}"

    @classmethod
    def gray(cls, text: str) -> str:
        """Return control sequences to turn text gray"""
        return f"{cls.GRAY}{text}{cls.NORMAL}"


def create_deck(shuffle: bool = False) -> list:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal(deck: list, players: int, size: int = None) -> dict:
    """Deal the cards in the deck into hands for all players
    deck: [(suite, rank), ...]
    players: number of players
    size: of hand
    return: {"P{number}": [(suite, rank),...]}
    if no size, dealt an even(ish) number of cards
    """
    if size is None:
        return {f"P{p+1}": deck[p::players] for p in range(players)}

    return {f"P{p+1}": [deck.pop() for _ in range(size)]
            for p in range(players)}


#  def draw(deck: list, hand: dict, num: int):
#      """x"""


def show(cards: list) -> str:
    """Return a string representation of the card list.
    cards: [ (suite, rank), ...]"""
    return "  ".join(Screen.invert(f"{s}{str(r).rjust(2)}")
                     for (s, r) in cards)


def setup(players: int, per_hand: int) -> dict:
    """Deal cards to all players then show all hands."""
    deck = create_deck(shuffle=True)
    hands = deal(deck, players, per_hand)
    return hands


def table(hands: dict, active: str = "P1"):
    """Draw the card table"""
    for name, cards in hands.items():
        if name == active:
            player = Screen.green(name)
        else:
            player = name

        print(f"{player}: {show(cards)}\n")


def play(players: int, per_hand: int):
    """Play the game"""
    hands = setup(players, per_hand)
    for name in hands.keys():
        print(Screen.clear())
        table(hands, name)
        action = input(f"\n{name}: [d]iscard, or [p]lay > ")
        print(action)


if __name__ == "__main__":
    play(players=4, per_hand=6)
