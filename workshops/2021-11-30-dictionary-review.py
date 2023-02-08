"""2021-11-30 Dictionary Review

Attendies
---------
- Nila
- Sean
- Fiona
"""

from pprint import pprint

things = {
    "mittens":{
        "qty" : 17 ,
        "color" : "yellow" ,
        "name": "Kitten Mitten"
    }
}

things["hat"] = {}
things["hat"]["qty"] = 21
things["hat"]["color"] = "Green"
things["hat"]["name"] = "Hoot"

print( things["mittens"]["color"] )

pprint(things, sort_dicts=False)

thing_name = input("Which thing? ")

# print(things[thing_name])
stuff = things.get(thing_name)
print("Here's your thing:", stuff)