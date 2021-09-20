
ANIMALS = {
    2000: "Dragon",
    2001: "Snake",
    2002: "Horse",
    2003: "Sheep",
    2004: "Monkey",
    2005: "Rooster",
    2006: "Dog",
    2007: "Pig",
    2008: "Rat",
    2009: "Ox",
    2010: "Tiger",
    2011: "Hare",
}
MIN, MAX = 2000, 2011

def birth_animal(birth_year):
    """Return the animal for a given year
    >>> birth_animal(2005)
    'Rooster'
    >>> birth_animal(1999)
    'Hare'
    >>> birth_animal(2012)
    'Dragon'
    >>> birth_animal(2039)
    'Sheep'
    >>> birth_animal(1965)
    'Snake'
    """
    if birth_year < MIN:
        diff = (MAX - birth_year) - 1
    elif birth_year > MAX:
        diff = (birth_year - MAX) - 1
    else:
        diff = (birth_year - MIN)

    breakpoint()

    if diff > 12:
        diff = diff % 12

    year = MIN + diff

    return ANIMALS.get(year)

# birth_animal(1999)
