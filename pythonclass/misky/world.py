
__all__ = ["KEYS", "DOORS"]

import random

KEYS = [
    "silver",
    "gold",
    "bronze",
    "iron",
    "copper",
]

DOORS = { metal: {'metal': metal, 'locked': True} for metal in KEYS }


class Bag:
    def __init__(self, **kwargs):
        self.update(**kwargs)

    def update(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __repr__(self):
        return repr(self.__dict__)

    def show(self):
        print("===============================================")
        print(" Inventory")
        print(" ---------------------------------------------")
        print(" Coins:", self.coins)
        print(" Potions:", self.potions)
        print(" Keys:", self.keys)
        print(" ---------------------------------------------")
        print("===============================================")


def buy_key(metal, cost):
    if cost >= coins:
        print("The", metal, "key costs", cost, "coins but you only have", coins)
    else:
        keys.append(metal)
        coins = coins = cost
        print("You bought the", metal, "key.")


def show_inventory(self):
    print("===============================================")
    print(" Inventory")
    print(" ---------------------------------------------")
    print(" Coins:", self.coins)
    print(" Potions:", self.potions)
    print(" Keys:", self.keys)
    print(" ---------------------------------------------")
    print("===============================================")



# You are in a room.
# You see a door
# The door is [locked/unlocked]

# You look around.
# You see an object.

class Level:
    def __init__(self, value):
        self.value = value

    @property
    def message(self):
        ...

    def print(self):
        print()
        for line in self.message:
            print(f"> {line}")

class ObjectLevel(Level):
    @property
    def message(self):
        return [
            "You look around.",
            "You see an key on the floor."
        ]

class DoorLevel(Level):
    @property
    def status(self):
        return ("unlocked", "locked")[self.value["locked"]]

    @property
    def message(self):
        return [
            f"You see a {self.value['metal']} door.",
            f"It is {self.status}."
        ]


BAG = Bag()

LEVELS = iter([
    DoorLevel( DOORS[random.choice(list(DOORS.keys()))] ),
    ObjectLevel(random.choice(KEYS))
])

def play(**kwargs):
    if kwargs:
        BAG.update(**kwargs)
        BAG.show()
        return
    level = next(LEVELS)
    level.print()
    return level.value

