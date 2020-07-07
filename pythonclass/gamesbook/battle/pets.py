#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pets Data"""

# a hash of pet pics
# species: pic
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

# nested list of pets
#   each element of the list is dictionary
#
#   Below is is the same as:
#
#   FLUFO = {...}
#   SCALEY = {...}
#   PETS = [ FLUFO, SCALEY ]
#
#   You can access an element the way you normally would, so we could get the
#     details for a pet with the syntax `variable[index]`:
#
#     pet = PETS[3]
#     print(pet['name'], "says hello!")
#
#   You can access also access nested elements from a list by adding the `[]`
#     reference straight to the end of the previous `[]` with the syntax
#     `variable[index][key]`.
#
#     print(PETS[3]['name'], "says hello!")
#

PETS = [
    {'name': "Flufosourus", 'species': "cat"},
    {'name': "Scaley", 'species': "fish"},
    {'name': "Count Chocula", 'species': "bat"},
    {'name': "Curious George", 'species': "monkey"},
]
