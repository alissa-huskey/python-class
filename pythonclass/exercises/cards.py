from random import shuffle

SUITS = ["C", "D", "H", "S"]
RANKS = list(range(2, 10))
RANKS.extend(["T", "J", "Q", "K", "A"])

def make_deck(shuffled=False):
    """Return a deck of 52 playing cards, a list where each element is a string
    of two characters, the first character representing the rank, and the
    second representing the suit.
    The suit letters are C, D, H, and S.
    The rank letters are T, J, Q, K and A.

    >>> deck = make_deck()
    >>> len(deck)
    52
    >>> deck[:13]
    ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC']
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
        card = deck.pop()
        cards.append(card)

    return cards

