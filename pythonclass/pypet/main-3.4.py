"""
Pypet Game

    From the tutorial found at:

    https://alissa-huskey.github.io/python-class/lessons/tutorial.html
"""

# print to the screen by calling the print() function
print("Welcome to PyPet!")

# dictionary
cat = {
    "name": "Fluffy",
    "age": 5,
    "weight": 9.5,
    "hungry": True,
    "color": "white",
    "pic": "(=^o.o^=)__",
}

# use the name variable to form a new message
# by concatenating two strings, then print it
print("Hello " + cat["name"])

# print the pet picture
print(cat["pic"])
