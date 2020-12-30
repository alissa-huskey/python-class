#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Display information about a random beer from the PunkAPI

Exercise from the Data Introspection lesson:
    https://alissa-huskey.github.io/python-class/lessons/data-introspection.html
"""

import requests


def main():
    """Fetch a random beer and print the name, description, and ingredients"""
    response = requests.get("http://api.punkapi.com/v2/beers/random")
    data = response.json()

    beer = data[0]

    print()
    print(beer['name'])
    print("-" * len(beer['name']), "\n")

    print(beer['description'], "\n")

    ingredients = set()
    for malt in beer['ingredients']['malt']:
        ingredients.add(malt['name'] + " Malt")

    for hop in beer['ingredients']['hops']:
        ingredients.add(hop['name'] + " Hops")

    ingredients.add(beer['ingredients']['yeast'])

    for item in sorted(ingredients):
        print(f"  * {item}")

    print()


if __name__ == "__main__":
    main()
