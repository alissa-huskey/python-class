"""
2023-07-08 Object Oriented Programming
https://alissa-huskey.github.io/python-class/lessons/in-depth/oop.html

Side note:
https://docs.python.org/3/tutorial/index.html
"""

val = None

while True:
    if input("> ")  == "yes":
        val = 0

    if val != None:
        val = val + 10
        print("val is:", val)
    else:
        print("you need to set val")

quit()

cat = {
    'name': "Flufosourus",
    'weight': 7,
    'is_hungry': True,
    'pic': "(=^o.o^=)__",
}

fish = {
    'name': "Scaley",
    'weight': 0.5,
    'is_hungry': False,
    'pic': "<`)))><",
}

def feed(pet):
    if pet["is_hungry"]:
        print("Feeding: " + pet["name"])
        pet["is_hungry"] = False
        pet["weight"] = pet["weight"] + 1
    else:
        print(pet["name"] + " is not hungry, thanks anyway.")

def main():
    feed(cat)
    feed(fish)

class Car():
    def __init__(self, make=None, model=None, color=None, year=None, is_clean=False):
        self.make = make
        self.model = model
        self.year = year


class Animal():
    def __init__(self, name, pic, weight, is_hungry=True):
        self.name = name
        self.pic = pic
        self.weight = weight
        self.is_hungry = is_hungry

    def feed(self):
        if self.is_hungry:
            print("Feeding: " + self.name)
            self.is_hungry = False
            self.weight += 1
        else:
            print(self.name + " is not hungry, thanks anyway.")





do_thing([])
do_thing([1, 2, 3])

val = "x"



if bool(val) == True:        # this is the same as
    print("truthy")

if val:                      # this ^
    print("truthy")

if not val:                  # and this is the same as
    print("falsy")

if bool(val) == False:       # this ^
    print("also falsy")

snake = Animal(
    name="Snuggles",
    weight=50,
    pic=r'_/\__/\_/--{ :>~',
)


car = Car(
    model="Honda",
    make="Accord",
    year=2010,
    color="Black",
)

car.color = "Red"

truck = Car()
truck.model = "Ford"
truck.make = "F150"
truck.year = 2015
truck.color = "Silver"

print(truck.color, truck.make, truck.model, truck.year)
print(car.color, car.make, car.model, car.year)

print(snake.name, snake.pic, snake.weight, snake.is_hungry)

print("-"*40)

print(snake.name, "is hungry:", snake.is_hungry, "weight:", snake.weight)
snake.feed()
print(snake.name, "is hungry:", snake.is_hungry, "weight:", snake.weight)
