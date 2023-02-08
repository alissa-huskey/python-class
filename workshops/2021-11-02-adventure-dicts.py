
#                   store
#                      |
#        home  --- town square    --- x  --- x 
#                                            |
#                                          cave
#         

fruits = {
    "apple": 2,
    "strawberry": 5,
    "blueberry": 10,
}

PLAYER = {
    'place': 'home',
    'gems': 0,
    'inventory': {
        'knife': 1,
    }
}

ITEMS = {
    'knife': {
        "name": "A wicked blade",
#       ...
    },
}

PLACES = {
    'home': {
        'name': "Denver Pad",
        'south': 'store',
        'north': 'the wall',
        'west': 'school',
    },
    'store': {
        'name': "Safeway",
        'north': 'home',
        'west': 'post office',
    },
    'the wall': {
        'name': "The Wall",
        'south': 'home',
    },
    'school': {
        'name': "Skool",
        'east': 'home',
        'south': 'post office',
    },
}

def do_go(args):
    current_place_name = PLAYER['place']
    current_place = PLACES[current_place_name]
    print("You are at:", current_place_name, current_place['name'])

    if not args:
        print("no args for you!")
        return

    direction = args[0]
    
    print("Trying to go:", direction)

    new_name = current_place.get(direction)

    if not new_name:
        print(f"YOU'RE GOING THE WRONG WAY! ({direction})")
        return

    new_place = PLACES.get(new_name)
    
    if not new_place:
        print(f"You done messed up. No such place as: {new_name}")
        return

    print("You have gone to:", new_place["name"])



def main():
    while True:
        reply = input("> ")
        args = reply.split()

        if reply.startswith("eat"):
            fruit = args[-1]
            num_have = fruits.get(fruit)
            if not num_have:
                print(f"No {fruit} for you!")
                continue

            print(f"You are eating 1 of your {num_have} {fruit}s")
            fruits[fruit] = num_have - 1

        elif reply.startswith("go"):
            args.pop(0)
            do_go(args)

if __name__ == "__main__":
    main()