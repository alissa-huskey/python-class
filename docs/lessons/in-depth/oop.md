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

Object oriented programming is a way to organize your code around objects, or
types, instead of functions or dictionaries.

It allows us to define our own types and give those types properties and behaviors.

```{contents} Table of Contents
:backlinks: top
:local:
```

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

We could assign properties to `cat` after it has been instantiated.

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
3. Add properties for `make`, `model`, `color` and `year`.
3. Print those properties `make`, `model`, `color` and `year`.

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

Usually when we create a class, we have an idea of what properties it is going
to have. Instead of relying on the programmer to assign arbitrary properties,
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
values to their respective properties on the object.

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

And each of the properties that we assigned on `self` will now be available
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
2. Remove the lines where you set the properties on `car`.
3. Modify your code that creates the `car` object to send those values as
   arguments to `Car`.

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

### Part 1.3 Default and keyword arguments

Often you want to give an property a default value if the user does not
specify the value. You can do this in the method definition with
{samp}`{PARAM}={DEFAULT_VALUE}`.

Lets make `is_hungry` `False` by default.

```{code-cell} python
:class: full-width

class Animal:
    def __init__(self, name, pic, weight, is_hungry=False):
        self.name = name
        self.pic = pic
        self.weight = weight
        self.is_hungry = is_hungry

        print(f"Here is your new animal: {self.name}.")
```

{{ leftcol }}

Now when we create the `cat` object, we can choose to leave off the `is_hungry`
argument, and it will get set to `False`.

{{ rightcol }}

```{code-cell} python
:class: full-width
cat = Animal(
  "Flufosourus",
  "(=^o.o^=)__",
  7,
)

print(cat.is_hungry)
```

{{ newrow }}

If you have more than two arguments or if it isn't obvious what the arguments
are just by looking at it, it can make your code clearer to use
{term}`keyword arguments`.

To do this, just put {samp}`{NAME}={VALUE}` when calling the constructor.

{{ rightcol }}

```{code-cell} python
:class: full-width

cat = Animal(
  name="Flufosourus",
  pic="(=^o.o^=)__",
  weight=7,
)
```

{{ endcols }}

### Part 1.3 Exercises

`````{exercise} Car Keyword Arguments
:label: car-keyword-args-exercise

Modify where you create the car object to use keyword arguments.

`````

`````{solution} car-keyword-args-exercise
:class: dropdown

```{code-block} python
:caption: Car Keyword Arguments Exercise
:class: full-width
:linenos:

car = Car(
  make="Honda",
  model="Accord",
  year=2010,
  color="Black",
)

```

`````


`````{exercise} Car Default
:label: car-default-exercise

1. Add an `is_clean` argument to the `Car` constructor and set it to `False` by
   default.
2. In the constructor, set the `is_clean` property on `self` to the value of
   the `is_clean` argument.
3. After creating the `car` object, print the value of `car.is_clean`.
4. Make a second `Car` object named `truck` with different values for the
   `make`, `model` and so on. Pass `True` for `is_clean`.
5. Print the properties for `truck`, including `is_clean`.

`````

`````{solution} car-default-exercise
:class: dropdown

```{code-block} python
:caption: Car Default Exercise
:class: full-width
:linenos:

class Car:
    def __init__(self, make, model, year, color, is_clean=False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_clean = is_clean

car = Car(
  make="Honda",
  model="Accord",
  year=2010,
  color="Black",
)

truck = Car(
  make="Ford",
  model="F-150",
  year=2021,
  color="Red",
  is_clean=True,
)

print(car.is_clean)
print(truck.color, truck.year, truck.make, truck.model, truck.is_clean)

```

`````


### Part 1.4: Methods

A benfit to writing things in an object oriented way is that data and the
behavior associated with it are all packaged together. That means that an
objects methods already have access to its properties.

To demonstrate this, lets add a `feed()` method to the `Animal` class.

```{code-cell} python
:class: full-width

class Animal:
    def __init__(self, name, pic, weight, is_hungry=False):
        self.name = name
        self.pic = pic
        self.weight = weight
        self.is_hungry = is_hungry

        print(f"Here is your new animal: {self.name}.")

    def feed(self):
        if self.is_hungry:
            print("Feeding: " + self.name)
            self.is_hungry = False
            self.weight = self.weight + 1
        else:
            print(self.name + "is not hungry, thanks anyway.")

cat = Animal(
    "Flufosourus",
    "(=^o.o^=)__",
    7,
    True
)

print(cat.name)
print(cat.pic)
```

{{ br }}

{{ leftcol }}

Now we can call `cat.feed()`.

{{ rightcol }}

```{code-cell} python
:class: full-width

cat.feed()
```

{{ newrow }}

And we can see that `cat.weight` and `cat.is_hungry` have both been changed.

{{ rightcol }}

```{code-cell} python
:class: full-width

print(cat.weight)
print(cat.is_hungry)

```

{{ endcols }}

### Part 1.4 Exercise

`````{exercise} Car Method
:label: car-method-exercise

1. Add a `wash` method to your `Car` class that:

    * prints {samp}`washing the {YEAR} {MAKE} {MODEL}`
    * changes `is_clean` to `True`.
2. Call the `wash()` method on `car` and `truck` then print the `is_clean` property of each.

`````

`````{solution} car-method-exercise
:class: dropdown

```{code-block} python
:caption: Car Method Exercise
:class: full-width
:linenos:

class Car:
    def __init__(self, make, model, year, color, is_clean=False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_clean = is_clean

    def wash(self):
        print(f"Washing the {self.year} {self.make} {self.model}")
        self.is_clean = True

car = Car(
  make="Honda",
  model="Accord",
  year=2010,
  color="Black",
)

truck = Car(
  make="Ford",
  model="F-150",
  year=2021,
  color="Red",
  is_clean=True,
)

car.wash()
truck.wash()

print(car.is_clean)
print(truck.is_clean)

```

`````

----

% [ ] TODO
% [ ] properties
% [ ] inheritance
% [ ] super
