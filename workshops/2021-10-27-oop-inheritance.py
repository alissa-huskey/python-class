"""
2021-10-27 In-Depth OOP Lesson: Inheritance

Exercise:

[ ] Rename the Car class to Vehicle
[ ] Create two subclasses Car and Truck
[ ] For each add class attributes for doors
[ ] In __init__ make an is_loaded attribute and set it to False
[ ] Add method `load()` on each class that takes one argument `stuff` and
    [ ] Vehicle: sets self.is_loaded to True
    [ ] Car: calls super() and prints: The {stuff} is in the trunk.
    [ ] Truck: calls super() and prints: The {stuff} is in the flatbed.
"""

class Animal:
    ears = 2

    def __init__(self, name, weight, pic=None, is_hungry=False, toys=None):
        self.name = name
        self.weight = weight
        self.is_hungry = is_hungry

        if pic:
            self.pic = pic

        if not toys:
            toys = []

        self.toys = toys

    def feed(self):
        if self.is_hungry:
            print("Feeding: " + self.name)
            self.is_hungry = False
            self.weight = self.weight + 1
        else:
            print(self.name + "is not hungry, thanks anyway.")

    def speak(self):
        self.spoken_recently = True
        print("oh hai")

class Snake(Animal):
    pic = r"_/\__/\_/--{ :>~"
    species = "reptile"

    def speak(self):
        super().speak()
        print("hisss")

class Cat(Animal):
    pic = "(=^o.o^=)__"
    species = "feline"

    def speak(self):
        super().speak()
        print("meow")

class Object():
    def print(self):
        for key, value in self.__dict__:
            print(f"{key}: {value}")

class Item(Object):
    ...

class Place(Object):
    ...

cat = Cat(
    "Flufosourus",
    7,
)

snake = Snake(
    "Medusa",
    2,
)

print(cat.pic)
cat.speak()

print(snake.pic)
snake.speak()
