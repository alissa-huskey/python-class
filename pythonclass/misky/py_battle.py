#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""PyPet Battle Game"""

import random
import time
import messenger

MAX_HEALTH = 100

PICS = {
    'cat': "=^..^=",
    'fish': "<`)))><",
    'owl': "{O,o}",
    'snake': "_/\\__/\\_/--{ :>~",
    'bat': "/|\\^..^/|\\",
    'monkey': "@('_')@",
    'pig': "^(*(oo)*)^",
    'mouse': "<:3 )~~~",
    'bird': ",(u°)>",
    'cthulhu': "^(;,;)^",
    'fox': "-^^,--,~",
}


# our list of pets
# this is a list, where each element of the list is a dictionary
PETS = [
    {
        'name': "Flufosourus",
        'species': "cat",
    },
    {
        'name': "Scaley",
        'species': "fish",
    },
    {
        'name': "Count Chocula",
        'species': "bat",
    },
    {
        'name': "George",
        'species': "monkey",
    },
]

# the range of damage each player can do
# this is a set -- just like a list, except it is immutable
POWER = (10, 30)

# the number of seconds to pause for dramatic effect
DELAY = 1

FIGHTIN_WORDS = [
    "nips at",
    "takes a swipe at",
    "glares sternly at",
    "ferociously boofs",
    "is awfully mean to",
    "can't even believe",
    "throws mad shade at",
]


def prep():
    """Set the health and pic of all pets"""
    for pet in PETS:
        pet["health"] = MAX_HEALTH
        pet["pic"] = PICS[pet["species"]]


def lotto():
    """Return two randomly chosen pets"""
    random.shuffle(PETS)

    # This is called a slice--we are removing the first two elements of the
    # list
    return PETS[0:2]


def attack(foe):
    """A random amount of damage is inflicted on foe"""
    damage = random.randint(POWER[0], POWER[1])
    foe["health"] -= damage
    return damage


def show(pet):
    """Print the details about a pet"""
    print("  ", pet["name"], pet["pic"], pet["health"], "of", MAX_HEALTH)


def main():
    """PyPet Fight Game"""
    print("\nWelcome to the THUNDERDOME!")
    messenger.line("=")

    prep()
    fighters = lotto()
    winner = None
    current = random.randint(0, 1)

    print("\n  Tonight...\n")
    time.sleep(DELAY)
    print(" ***", fighters[0]["name"], "the",
          fighters[0]["species"].capitalize(),
          "-vs-", fighters[1]["name"], "the",
          fighters[1]["species"].capitalize(), "***\n\n")
    response = input("ARE YOU READY TO RUMBLE?! ")
    messenger.exit_if_quit(response)

    messenger.line(".")
    print()

    while winner is None:
        attacker = fighters[current]
        rival = fighters[not current]

        response = input(f"\n{attacker['name']} FIGHT> ").lower()
        messenger.exit_if_quit(response)

        damage = attack(rival)
        act = random.choice(FIGHTIN_WORDS)

        time.sleep(DELAY)
        print()
        messenger.info(f"{attacker['name']} {act} {rival['name']}...\n")

        time.sleep(DELAY)
        messenger.center(f"-{damage} {rival['name']}")
        time.sleep(DELAY)

        if rival["health"] <= 0:
            rival["health"] = 0
            winner = not current

        print()
        for combatant in fighters:
            show(combatant)

        messenger.line()
        current = not current

    # print the winnner
    print()
    messenger.center(f"{fighters[winner]['name']} is Victorious!")
    messenger.center(fighters[winner]["pic"])
    messenger.line()


if __name__ == '__main__':
    main()
