"""
Pypet Game

From the tutorial found at:

https://alissa-huskey.github.io/python-class/lessons/tutorial.html
"""


print("Welcome to Pypet!")

cat = {
  "name": "Fluffy",
  "hungry": True,
  "weight": 9.5,
  "age": 5,
  "pic": "(=^o.o^=)_",
}

mouse = {
    "name": "Mouse",
    "age": 6,
    "weight": 1.5,
    "hungry": False,
    "pic": "<:3 )~~~~",
}

pets = [cat, mouse]


def feed(pet):
  if pet["hungry"] == True:
    pet["hungry"] = False
    pet["weight"] = pet["weight"] + 1
    print("omnomom!!")
  else:
    print("The Pypet is not hungry!")

for pet in pets:
    print()
    print("------------------------------")
    print("Hello " + pet["name"] + "!")
    print(pet["pic"])
    print("Weight: " + str(pet["weight"]))
    feed(pet)
    print("Weight: " + str(pet["weight"]))
    print("------------------------------")

