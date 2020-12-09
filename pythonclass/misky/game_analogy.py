#!/usr/bin/env python

potions = 5
coins = 30
pet = {
    'name': "Flufosourus",
    'pic': "(=^o.o^=)__",
    'health': 75,
}

def hide():
    print("You quickly jump behind a bush. Now nobody can see you!")


def heal(pet, potions):
    if potions < 1:
        print("You don't have enough magic potion preform the healing spell.'")
    else:
        pet['health'] = 100
        print(pet['name'], "is healed")


def pickpocket():
    amount = random.randint(0, 55)
    print("You lifted", amount, "coins.")
    return amount

