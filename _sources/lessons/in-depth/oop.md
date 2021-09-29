---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
Object Oriented Programming
===========================

```{contents} Table of Contents
:backlinks: top
:local:
```

Object oriented programming is a way to organize your code around objects, or
types, instead of functions or dictionaries.

It allows us to define our own types and give those types attributes and behaviors.

Part 1: Classes
---------------

Lets think back to our old pypet program. We had something like this:

```{code-block} python
:caption: old pypet.py
:class: full-width
:linenos:

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
        print(pet["name"] + "is not hungry, thanks anyway.")

def main():
  feed(cat)
  feed(fish)

if __name__ == "__main__":
  main()
```

There are a lot of similarites between each of our pets, aren't there? Each one
has a `name`, a `weight`, a `pic` and an `is_hungry` value.

In this lesson we'll rewrite that using object oriented programming, staring by
creating an `Animal` class.

### Part 1.1: Simple classes

{{ leftcol }}

Here is the simplest class.

{{ rightcol }}

```{code-cell} python
:class: full-width
class Animal:
    ...
```

{{ newrow }}

Now we can create a new animal instance like so:

{{ rightcol }}

```{code-cell} python
:class: full-width
cat = Animal()
type(cat)
```

{{ newrow }}

We could assign attributes to `cat` after it has been instantiated.

{{ rightcol }}

```{code-cell} python
:class: full-width
cat.name = "Flufosourus"
cat.weight = 7
cat.is_hungry = False
cat.pic = "(=^o.o^=)__"

print(cat.name)
print(cat.pic)
```

{{ endcols }}

### Part 1.1 Exercise

`````{exercise} Car class
:label: car-class-exercise

1. Create a `Car` class.
2. Make a new `Car` object and assign it to the variable `car`.
3. Add attributes for `make`, `model`, `color` and `year`.
3. Print those attributes `make`, `model`, `color` and `year`.

`````

`````{solution} car-class-exercise
:class: dropdown

```{code-block} python
:caption: Car Class Exercise
:class: full-width
:linenos:

class Car:
  ...

car = Car()
car.make = "Honda"
car.model = "Accord"
car.year = 2010
car.color = "Black"

print(car.color, car.make, car.model, car.year)

```

`````


### Part 1.2: Constructors

Usually when we create a class, we have an idea of what attributes it is going
to have. Instead of relying on the programmer to assign arbitrary attributes,
we often want the programmer to provide those values when the object is being
created.

This is where a constructor comes in.  A constructor is a {term}`dunder method`
that is used to create new instances of that class like when you call
`Animal()`.

{{ leftcol }}

To make a constructor we'll add the `__init__` method to the `Animal` class.
Class methods always take at least one argument `self`, which is a special
variable that refers to the object itself.

{{ rightcol }}

```{code-cell} python
:class: full-width

class Animal:
    def __init__(self):
        print("Here is a new animal.")
```

{{ newrow }}

Now lets see what happens when we create a new `Animal` object.

{{ rightcol }}

```{code-cell} python
:class: full-width
cat = Animal()
```

{{ endcols }}

To make this class more useful, lets have `__init__` take the arguments `name`,
`pic`, `weight` and `is_hungry`. Then we'll use `self` to assign each of these
values to their respective attribute on the object.

```{code-cell} python
:class: full-width

class Animal:
    def __init__(self, name, pic, weight, is_hungry):
        self.name = name
        self.pic = pic
        self.weight = weight
        self.is_hungry = is_hungry

        print(f"Here is your new animal: {self.name}.")
```

{{ br }}

{{ leftcol }}

Now we can pass in arguments when we instantiate the object.

{{ rightcol }}

```{code-cell} python
:class: full-width
cat = Animal(
  "Flufosourus",
  "(=^o.o^=)__",
  7,
  True
)
```

{{ newrow }}

And each of the attributes that we assigned on `self` will now be available
from `cat`.

{{ rightcol }}

```{code-cell} python
:class: full-width
print(cat.name)
print(cat.pic)
```

{{ endcols }}

### Part 1.2 Exercise

`````{exercise} Car Constructor
:label: car-constructor-exercise

1. Add an `__init__` method to your car class that takes the arguments `make`,
   `model`, `year`, and `color`.
2. When you create your `car` object, send those values as arguments to `Car`.

`````

`````{solution} car-constructor-exercise
:class: dropdown

```{code-block} python
:caption: Car Constructor Exercise
:class: full-width
:linenos:

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

car = Car(
  "Honda",
  "Accord",
  2010,
  "Black",
)

print(car.color, car.make, car.model, car.year)

```

`````


