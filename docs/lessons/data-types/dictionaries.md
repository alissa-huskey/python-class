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

Dictionaries
============

{{ leftcol | replace("col", "col-8")  }}

A collection of *key: value* pairs.

```{contents} Table of Contents
:backlinks: top
:local:
```

{{ rightcol | replace("col", "col-4 text-right") }}

:::{fieldlist}

:Type:        `dict`
:Synatx:      {samp}`\{{item},...\}`
:Bases:       Mapping
:State:       Mutable
:Position:    Ordered
:Composition: Heterogeneous
:Diversity:   Repeatable
:Access:      Subscriptable
:Value:       Not hashable

:::

{{ endcols }}

Basics
------

A dictionary is a collection of key value pairs. Each key is connected to a
value, which makes them a handy way to look up a particular value.

### Creating

To create a dictionary, enclose comma-seperated key value pairs in curly braces
`{` `}` with a `:` between each key and value.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

book = {
  "title": "Last Chance to See",
  "author": "Douglas Adams",
  "year": 1990,
}
```

`````{exercise} Shapes Dictionary
:label: shapes-dict-exercise

Create a dictionary assigned to the variable `shapes` that has a shape name
(like `"square"` or `"triangle"`) for each key and the number of sides (`4` and
`3`) for the value.

Print the dictionary.
`````

`````{solution} shapes-dict-exercise
:class: dropdown

```{code-block} python
:caption: Shapes Dictionary Exercise
:class: full-width
:linenos:

from pprint import pprint

shapes = {
    "square": 4,
    "triangle": 3,
    "circle": 0,
    "rectangle": 4,
    "octogon": 8,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
}

pprint(shapes, sort_dicts=False)
```

`````

### Accessing

Items are accessed via {term}`subscription`, using `[` `]` after the object to
enclose the key.

```{code-cell} python
:class: full-width
print("Title:", book["title"])
print("Author:", book["author"])
print("Published:", book["year"])
```

If you try to access a key that does not exist, you will encounter a
`KeyError`.

```{code-cell} python
:class: full-width
:tags: [raises-exception]

print("Series:", book["series"])
```

However, you can avoid this using the `.get()` method, which takes two
arguments: the key, and an optional default value.

```{code-cell} python
:class: full-width
:tags: [raises-exception]

series = book.get("series", "NA")
print("Series:", series)
```

`````{exercise} Lookup Sides
:label: shapes-sides-exercise

Print {samp}`"A {name} has {number} sides."` for a `square` and `rectangle`.
```{code-block} text
:caption: output
A triangle has 3 sides.
A square has 4 sides.
```

`````

`````{solution} shapes-sides-exercise
:class: dropdown

```{code-block} python
:caption: Shapes Exercise
:class: full-width
:linenos:
:emphasize-lines: "16-17"

from pprint import pprint

shapes = {
    "square": 4,
    "triangle": 3,
    "circle": 0,
    "rectangle": 4,
    "octogon": 8,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
}

pprint(shapes, sort_dicts=False)

print("A triangle has", shapes["triangle"], "sides.")
print("A square has", shapes["square"], "sides.")
```

`````

`````{exercise} Lookup Side with Fallback
:label: shapes-sides-fallback-exercise

Prompt the user for the shape name, then look up the number of sides in `shapes` using the `.get()` method.

If the shape is not in the dictionary print: {samp}`"Sorry, I don't know the shape: {name}"`

Otherwise print: {samp}`"A {name} has {number} sides."`

```{admonition} Need a hint?
   :class: "dropdown hint"
   1. Use the `input()` function to prompt the user for a shape name and
      assign the returned value to the variable `name`.

   2. Look up the number of sides: Call the
      `.get()` method on `shapes` with the argument `name` and the optional
      second argument `None` (the value that will be returned if `name` is
      not a key in `shapes`). Assign to the variable `sides`.

   3. Use an if statement with the condition that `sides` is equal to `None`.

      In the body print the message:
      {samp}`"Sorry, I don't know the shape: {name}"`

      Use an `else` clause. In the body print the message:
      {samp}`"A {name} has {number} sides."`
```

```{code-block} text
:caption: output
shape > rectangle
A rectangle has 4 sides.

shape > heart
Sorry, I don't know the shape: heart
```

`````

`````{solution} shapes-sides-fallback-exercise
:class: dropdown

```{code-block} python
:caption: Shapes Exercise
:class: full-width
:linenos:
:emphasize-lines: "19-25"

from pprint import pprint

shapes = {
    "square": 4,
    "triangle": 3,
    "circle": 0,
    "rectangle": 4,
    "octogon": 8,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
}

pprint(shapes, sort_dicts=False)

print("A triangle has", shapes["triangle"], "sides.")
print("A square has", shapes["square"], "sides.")

name = input("shape > ")
sides = shapes.get(name, None)

if sides == None:
    print("Sorry, I don't know the shape:", name)
else:
    print("A", name, "has", sides, "sides.")
```

`````

### Modifying

Adding or changing elements in the list is done the same way, also using subscription.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

from pprint import pprint

book["genre"] = "Nonfiction"
book["author"] = "Douglas Adams, Mark Carwardine"

pprint(book)
```

You can also change multiple elements at once using the `.update()`
method, which takes one argument, a dictionary. Any keys already present in the
original dictionary will be changed, and any not in the original dictionary
will be added. The remaining elements will be left as they are.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

book.update({"isbn": "0345371984", "genre": "Science", "pages": 256})

pprint(book)
```

`````{exercise} Add and Change a Shape
:label: change-shape-exercise

Use {term}`subscription` to:

* add the shape `"oval"` to `shapes` with `0` sides
* change `"square"` to `"four"` sides

`````

`````{solution} change-shape-exercise
:class: dropdown

```{code-block} python
:caption:  Add and Change a Shape Exercise
:class: full-width
:linenos:
:emphasize-lines: "14-15"

from pprint import pprint

shapes = {
    "square": 4,
    "triangle": 3,
    "circle": 0,
    "rectangle": 4,
    "octogon": 8,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
}

shapes["oval"] = 0
shapes["square"] = "four"

pprint(shapes, sort_dicts=False)

print("A triangle has", shapes["triangle"], "sides.")
print("A square has", shapes["square"], "sides.")

name = input("shape > ")
sides = shapes.get(name, None)

if sides == None:
    print("Sorry, I don't know the shape:", name)
else:
    print("A", name, "has", sides, "sides.")
```

`````

`````{exercise} Add and Change Multiple Shapes
:label: change-shapes-exercise

Use the `.update()` method to
* change `"triangle"` to `"three"` sides
* add `star` with `10` sides
* add `nonagon` with `9` sides
`````

`````{solution} change-shapes-exercise
:class: dropdown

```{code-block} python
:caption: Add and Change Multiple Shapes Exercise
:class: full-width
:linenos:
:emphasize-lines: "17-21"

from pprint import pprint

shapes = {
    "square": 4,
    "triangle": 3,
    "circle": 0,
    "rectangle": 4,
    "octogon": 8,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
}

shapes["oval"] = 0
shapes["square"] = "four"

shapes.update({
    "star": 10,
    "nonagon": 9,
    "triangle": "three",
})

pprint(shapes, sort_dicts=False)

print("A triangle has", shapes["triangle"], "sides.")
print("A square has", shapes["square"], "sides.")

name = input("shape > ")
sides = shapes.get(name, None)

if sides == None:
    print("Sorry, I don't know the shape:", name)
else:
    print("A", name, "has", sides, "sides.")
```

`````

### Removing

To remove elements you can use the `del` keyword.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

del book["pages"]

pprint(book)
```

You can also remove items using the `.pop()` method, which returns the deleted
element before removing it.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

isbn = book.pop("isbn")
print("The books ISBN is:", isbn)
pprint(book)
```

Just like when using subscription, `.pop()` will raise a `KeyError` if no value
with that key exists.

```{code-cell} python
:class: full-width
:tags: [thebe-init, raises-exception]

fmt = book.pop("format")
print("This books format is:", fmt)
pprint(book)
```

You can avoid this error by pass the optional second argument `default`, which is the
value to return if it is missing.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

year = book.pop("year", "Unknown")
print("The year is:", year)
pprint(book)

fmt = book.pop("format", "Unknown")
print("The format is:", fmt)
pprint(book)
```

`````{exercise} Remove a Shape
:label: remove-shape-exercise

Print `shapes` then remove the `"star"` shape using `del`. Print `shapes` again
to confirm it has been removed.

`````

`````{solution} remove-shape-exercise
:class: dropdown

```{code-block} python
:caption: Remove a Shape Exercise
:class: full-width
:linenos:
:emphasize-lines: "25-27"

from pprint import pprint

shapes = {
    "square": 4,
    "triangle": 3,
    "circle": 0,
    "rectangle": 4,
    "octogon": 8,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
}

shapes["oval"] = 0
shapes["square"] = "four"

shapes.update({
    "star": 10,
    "nonagon": 9,
    "triangle": "three",
})

pprint(shapes)

del shapes["star"]

pprint(shapes, sort_dicts=False)

print("A triangle has", shapes["triangle"], "sides.")
print("A square has", shapes["square"], "sides.")

name = input("shape > ")
sides = shapes.get(name, None)

if sides == None:
    print("Sorry, I don't know the shape:", name)
else:
    print("A", name, "has", sides, "sides.")
```

`````
### Exercises

`````{exercise} Word calculator
:label: word-calculator-exercise

Make a dictionary of numbers where the keyword is a word (like `"one"`) and the
value is an integer (like `1`). Assign it to the variable `numbers`.

Write an `add()` function that takes two string arguments, adds together the
value in the `numbers` dictionary associated with those keys, and returns the
result.

**Example Usage**

``` python
>>> add("one", "three")
4
```

**Solution template**

```python
def add(a, b):
  """Add the value of two number strings.

  >>> add("one", "three")
  4
  """
```

`````

`````{solution} word-calculator-exercise
:class: dropdown

```{code-block} python
:caption: Word Calculator Exercise
:class: full-width
:linenos:

numbers = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "ten": 10,
}

def add(a, b):
  """Add the value of two number strings.

  >>> add("one", "three")
  4
  """
  return numbers[a] + numbers[b]
`````

`````{exercise} Scrabble Score
:label: scrabble-score-exercise

In this exercise you'll write a function that calculates the scrabble score for
a list of letters.

1. Make a dictionary assigned to the global variable `POINTS` where each key is
   a letter with a value of the cooresponding point, as listed below.
   | Points | Letters                         |
   |--------|---------------------------------|
   | 1      | A, E, I, L, N, O, R, S, T and U |
   | 2      | D and G                         |
   | 3      | B, C, M and P                   |
   | 4      | F, H, V, W and Y                |
2. Write a function `score()` that takes one argument, a string or list of
   `letters`. Use the `POINTS` dictionary to look up the value of each letter and
   add them together, then return the total.
   ```{dropdown} Need a hint?
   * set a variable `total` to `0`
   * iterate over each letter in the list
     - get the point value for each letter from the `POINTS` dictionary
     - add it to `total`
   * return `total`
   ```

**Example Usage**

``` python
>>> score("blank")
11
>>> score(["d", "i", "r", "t"])
5
```

**Solution template**

```python
def score(letters):
    """Return the scrabble score for a list of letters
    >>> score("blank")
    11
    >>> score("dirt")
    5
    >>> score("fajita")
    16
    """
```

`````

`````{solution} scrabble-score-exercise
:class: dropdown

```{literalinclude} ../../../pythonclass/exercises/scrabble.py
:caption: Scrabble Score Exercise
:class: full-width
:linenos:

`````

Membership
----------

### Keys and values

You can get a list of all of the keys in a dictionary using the `.keys()` method.

```{code-cell} python
:class: full-width

print(book.keys())
```

Similarly, you can get a list of all of the values in a dictionary using the `.values()` method.

```{code-cell} python
:class: full-width

print(book.values())
```

Both of these are {term}`iterables` which can be converted to a `list`.

```{code-cell} python
:class: full-width

keys = list(book.keys())
pprint(keys)

values = list(book.values())
pprint(values)
```

### Key types

The `book` dictionary uses strings for keys, but you can actually use nearly
any type as a key.

```{code-cell} python
:class: full-width

numbers = {
  10: "ten",
  20: "twenty",
  30: "thirty",
}

print(numbers[30])
```

You can mix and match the type of keys.

```{code-cell} python
:class: full-width

numbers = {
  10: "ten",
  20: "twenty",
  30: "thirty",
  0.5: "half",
  0.25: "a quarter",
  0.125: "one eighth",
}

print(numbers[0.5])
```

You can even use a `tuple` objects as keys.

```{code-cell} python
:class: full-width
times = {
  (12, 0): "noon",
  (8, 30): "half past eight",
  (24, 0): "midnight",
  (9, 45): "quarter to nine",
}

print(times[(8, 30)])
```

You just can't use {term}`mutable` objects as keys, like `dict` or `list` objects.

```{code-cell} python
:class: full-width
:tags: [raises-exception]

times = {
  [12, 0]: "noon",
}

```

### Conditions

You can check if a dictionary has a particular key using the `in` operator.

```{code-block} python
:class: full-width
>>> "title" in book
True
>>> "series" in book
False
```

To check if a dictionary has a particular value you'll also use the `in`
operator, but on the `.values()` method.

```{code-block} python
:class: full-width
>>> 1990 in book.values()
True
>>> "Orson Scott Card" in book.values()
False
```

### Nested values

Values can be anything you want, even other dictionaries or lists.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

favorites = {
  "jessica": {
    "color": "purple",
    "movie": "Pulp Fiction",
    "book": "The Lion, the Witch and the Wardrobe",
    "song": "Another One Bites the Dust",
  },
  "eric": {
    "color": "green",
    "movie": "Goodfellas",
    "book": "The Lion, the Witch and the Wardrobe",
    "song": "Good Vibrations",
  }
}
```
You can access items in the nested lists by using multiple subscription
operations, with brackets back to back.

```{code-cell} python
:class: full-width

print("Jessica's favorite book is:", favorites["jessica"]["book"])
```

Another way to do this is to retrieve each level and store it in a variable.

```{code-cell} python
:class: full-width

jessica = favorites["jessica"]
print("Jessica's favorite book is:", jessica["book"])
```

% Iteration
% ---------

% When used as a {term}`iterable`, dictionaries often act like a {term}`sequence`
% of keys.

% For


----

% TODO
% [ ] ordered version 3.7+
% [ ] no duplicate keys, but duplicate values
% [x] creating
% [x] accessing
%     [x] with key
%     [x] get
% [x] removing
%     [x] pop
%     [x] del
% [x] values
% [x] membership
%     [x] keys
%     [x] values
%     [x] values that can be used as keys
% [ ] iteration
% [ ] exercise
% [ ] under the hood
%     [ ] tuples

