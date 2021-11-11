"""2021-11-09 Dictionary Review

Study Hall
----------
- Sean

Review:

* how to get an item from a dictionary: DICT_NAME[KEY]

    examples:

    FRUITS["pear"]

    name = "blueberry"
    FRUITS[name]

* how to get an item from a dictionary and avoid KeyErrors: DICT_NAME.get(KEY)

    examples:

    FRUITS.get("mango")

    name = "grape"
    FRUITS.get(name)

* how to get an item from a dictionary, avoid KeyErrors, and if it is missing
  get a specific value back

    examples:

    FRUITS.get("orange", "Empty")

* how to change the value in a dictionary: DICT_NAME[KEY] = VALUE

    examples:

    FRUITS["blueberry"] = 1

    FRUITS['apple'] = FRUITS['apple'] + 1

    FRUITS["apple"] += 1

* add a value to a dictionary: DICT_NAME[KEY] = VALUE

    examples:

    FRUITS["orange"] = 1

* how to check if a dictionary contains a key: KEY [not] in DICT_NAME | KEY [not] in DICT_NAME.keys()

    examples:

    "cherry" not in FRUITS
    "cherry" not in FRUITS.keys()

    "fig" in FRUITS
    "fig" in FRUITS.keys()

* how to iterate over the keys and values in a dictionary: for KEY, VALUE in DICT_NAME.items():

    examples:

    for name, qty in FRUITS.items():

"""

from pprint import pprint

PLAYER = {
    "place": "home",
    "inventory": {},
}

#
#               the wall
#                   |
#       school --  home
#         |         |
#  post office -- store
#
#

PLACES = {
    'home': {
        'name': "Denver Pad",
        'south': 'store',
        'north': 'the wall',
        'west': 'school',
    },
    'store': {
        'name': "Safeway",
        'north': 'home',
        'west': 'post office',
    },
    'the wall': {
        'name': "The Wall",
        'south': 'home',
    },
    'school': {
        'name': "Skool",
        'east': 'home',
        'south': 'post office',
    },
}

FRUITS = {"apple": 5, "pear": 3, "blueberry": 0}

def do_eat(name):
    """Eat the fruit that has the name."""
    qty = FRUITS.get(name, 0)
    print(f"FYI, you have {qty} {name}s.")

    if not qty:
        print(f"No {name} for you!\n")
        return

    FRUITS[name] = qty - 1
    print(f"You ate a delicions {name}!\n")

def main():
    name = None
    while True:
        for name, qty in FRUITS.items():
            if qty:
                print(f"You see {qty} {name}s.")

        print("\nWhich fruit do you want to eat?")
        name = input("> ").strip().lower()

        if name == "q":
            return

        if name:
            do_eat(name)

if __name__ == "__main__":
    main()
