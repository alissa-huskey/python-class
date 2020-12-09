class Level():
    ...

def ItemLevel():
    def update(self):
        ITEM = random.choice(items)
        print("You notice a", item, "sitting on a table.")

def SnoozeLevel():
    def update(self):
        print("You see", ENEMY['name'], "dozing in the corner.")

def AttackLevel():
    def update(self):
        print(ENEMY['name'], "attacks!")

def look_around():
    level = random.randint(_levels)
    level.update()

_items = ["spell book", "silver key"]
_levels = [
    ItemLevel(),
    SnoozeLevel(),
    AttackLevel(),
]

ENEMY = {
    'name': "Count Chocula",
    'pic': "=^..^=",
    'health': 75,
}

ITEM = []

