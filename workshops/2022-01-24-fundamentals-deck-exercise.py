"""
2022-01-24 -- Fundamentals -- Exercises

Agenda
------

* Expression exercise
* Problem solving exercise
    - generate a deck of cards


Attendees
---------
- Nila
- Sean

"""

from workshops import section, div, stop, exercise

section("A", "Expression Exercises")

div("A.1", "Draw a card")

# Order of operation rules
#
# - replace variables with values
# - inside to outside
# - left to right
# - */ before +-
# - and before or

def draw(deck):
    """Remove the first card from the deck and return it."""
    return deck.pop(0)

deck = ["JD", "5H", "TS", "3S", "QC"]

card = draw(deck)[-1]
# "JD"[-1]
# "D"

# exercise('draw(deck)[-1]', True)

section("B", "Problem Solving Exercise")

div("B.1", "Create a deck of cards")

# Genrate a list of strings representing a deck of 52 playing cards
#    where the first character represents the face and the second represents the suit
#    For example: "3S" is the 3 of spades
#    Suits: D, H, C, and S
#    Faces: 2-9, T, J, Q, K and A

Suits = ["D", "H", "S", "C"]
Faces = ["2","3","4","5","6","7","8","9", "T", "J", "Q", "K", "A"]
Whole_Deck = []


def card_deck():
    for face in Faces:
        for suit in Suits:
            card = face + suit
            Whole_Deck.append(f"{card}")
    print(Whole_Deck)


card_deck()
