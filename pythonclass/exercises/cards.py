from random import shuffle

SUITS = ["C", "D", "H", "S"]
RANKS = list(range(1, 10)) + ["J", "Q", "K", "A"]

def make_deck(shuffled=False):
    """Return a deck of 52 playing cards, a list where each element is a string
    of two characters, the first character representing the rank, and the
    second representing the suit. The suits are C, D, H, S and the rank letters
    are J, Q, K, A.

    >>> deck = make_deck()
    >>> len(deck)
    52
    >>> list(sorted(set(deck))) == sorted(deck)
    True
    >>> deck = sorted(deck, key=lambda c: c[1])
    >>> [deck[i] for i in (0, 13, 26, 39)]
    ['1C', '1D', '1H', '1S']
    """
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            card = f"{rank}{suit}"
            deck.append(card)

    if shuffled:
        shuffle(deck)

    return deck

def draw(deck, size=5):
    """Return a list of cards removed from deck

    >>> deck = make_deck(shuffled=True)
    >>> hand = draw(deck)
    >>> len(hand)
    5
    >>> len(hand[0])
    2
    >>> len(deck)
    47
    >>> hand[0] in deck
    False
    """
    cards = []
    for i in range(size):
        if not deck:
            break
        cards.append(deck.pop())

    return cards

