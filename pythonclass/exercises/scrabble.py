POINTS = {
    "A": 1,
    "E": 1,
    "I": 1,
    "L": 1,
    "N": 1,
    "O": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10,
}

def score(letters):
    """Return the scrabble score for a list of letters
    >>> score("blank")
    11
    >>> score("dirt")
    5
    >>> score("fajita")
    16
    """
    total = 0
    for char in letters:
        total += POINTS.get(char.upper(), 0)

    return total
