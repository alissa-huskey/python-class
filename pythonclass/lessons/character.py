#!/usr/bin/env python

import random

name = "Gaz"
title = "Thief"
level = random.randint(1, 5)

print(name, "is at level", level)

print(name, "is a level", level, title + ".")

level = level + 1


# emphasize-lines
def character_info(character_name, character_title, character_level):
    print(character_name, "is a level", character_level, character_title)

character_info(name, title, level)


name = "Gandolf"
title = "Mage"
level = 2



character_info("Shay", "warrior", 7)
character_info("Quinn", "thief", 3)
character_info("Max", "mage", 5)
