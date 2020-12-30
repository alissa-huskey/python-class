#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Display information about a random beer from the PunkAPI

Exercise from the Data Introspection lesson:
    https://alissa-huskey.github.io/python-class/lessons/data-introspection.html
"""

import requests
import colorful
import textwrap
from sys import stderr


def abort(*messages):
    """Print message to stderr and exit"""
    print(colorful.red("Error"), *messages, file=stderr)
    exit()


def main():
    """Fetch a random beer and print the name, description, and ingredients"""
    response = requests.get("http://api.punkapi.com/v2/beers/random")
    if not response.ok:
        abort("Request failed:", response.status_code, response.reason)

    data = response.json()
    beer = data[0]

    print()
    print(" ", beer['name'])
    print(" ", "-" * len(beer['name']), "\n")

    lines = textwrap.wrap(
        beer['description'],
        initial_indent = "  ",
        subsequent_indent="  ")

    for line in lines:
        print(line)

    print()

    ingredients = set()
    for malt in beer['ingredients']['malt']:
        name = malt['name']
        if "malt" not in name.lower():
            name += " Malt"
        ingredients.add(name)

    for hop in beer['ingredients']['hops']:
        name = hop['name']
        if "hops" not in name.lower():
            name += " Hops"
        ingredients.add(name)

    ingredients.add(beer['ingredients']['yeast'])

    for item in sorted(ingredients):
        print(f"    * {item}")

    print()


if __name__ == "__main__":
    main()
