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

Lists
=====

This page contains brief code snippets for `list` related operations. It is
intended as a resource for quickly looking up the syntax for a particular task,
most likely to jog a students memory.

While you may well learn something here, it is not written as a lesson.

:::{tip}

You can modify and execute any of the code on this page.

1. ![launch][] just click this icon at the top of the page
1. ![live][] followed by this one

:::

[launch]: ../assets/rocket-icon.png
[live]: ../assets/live-icon.png

```{contents} Table of Contents
:backlinks: top
:local:
```

Creating
--------

### Bracket syntax

Create an empty list using `[` `]`:

```{code-cell} python
a_list  = []
print(a_list)
```

Create a list of `3` `None` elements:

```{code-cell} python
b_list  = [None] * 3
print(b_list)
```

Create a list with initial elements:

```{code-cell} python
:tags: [thebe-init]
numbers = [0, 1, 2, 3, 4, 5]
print(numbers)
```

### list constructor

Create an empty list using the `list()` constructor:

```{code-cell} python
c_list  = list()
print(c_list)
```

Create a list from another iterable:

```{code-cell} python
:tags: [thebe-init]
letters = list("abcdefghijklmnopqrstuvwxyz")
print(letters)
```

Selecting Elements
------------------

Elements are accessed via {term}`subscription` with the syntax: {samp}`{COLLECTION}[{SELECTOR}]`.

The `SELECTOR` can be:

* {term}`index number`
* {term}`negative index number`
* {term}`slice`

### Via index number

First element:

```{code-cell} python
print(letters[0])
```

Second element:

```{code-cell} python
print(letters[1])
```

Last element:

```{code-cell} python
print(letters[-1])
```

### Via slice

Or the `SELECTOR` can be a {term}`slice`.

The synax is either of the following.

* {samp}`{COLLECTION}[{START}:{STOP}]`
* {samp}`{COLLECTION}[{START}:{STOP}:{STEP}]`

From `numbers[1]` to before `numbers[3]`:

```{code-cell} python
print(numbers[1:3])
```

All but the first element:

```{code-cell} python
print(numbers[1:])
```

All but the last element:

```{code-cell} python
print(numbers[:-1])
```

Every other element from `numbers[3]` to before `numbers[15]`:

```{code-cell} python
print(numbers[3:15:2])
```

Elements in reversed order with a negative `STEP` number and a `START` that is
greater than `STOP`.

```{code-cell} python
print(numbers[2::-1])
print(numbers[-1:-3:-1])
```

Entire list:

```{code-cell} python
print(numbers[:])
```

### Exceptions

An `IndexError` exception will be raised for any selectors using using
non-existant index numbers.

```{code-cell} python
:tags: [raises-exception]
value = numbers[10]
print(value)
```

```{code-cell} python
:tags: [raises-exception]
value = numbers[-10]
print(value)
```

Suppress errors with a try except block:

```{code-cell} python
try:
  value = numbers[10]
except IndexError:
  value = None

print(value)
```

Modification
------------

### Change

#### By index

```{code-cell} python
numbers[1] = 100
print(numbers)
```

#### By slice

```{code-cell} python
numbers[3:5] = [300, 400]
print(numbers)
```

### Add

```{code-cell} python
:tags: [thebe-init]
animals = ["bear", "chimpanzee", "elephant"]
print(animals)
```

#### To end

```{code-cell} python
animals.append("hedgehog")
print(animals)
```

#### At a specific position

```{code-cell} python
animals.insert(2, "dolphin")
print(animals)
```

```{code-cell} python
animals.insert(0, "antelope")
print(animals)
```

#### From iterable

##### Using `.extend()`

```{code-cell} python
from pprint import pprint

animals.extend(["lynx", "ocelot", "puma"])
pprint(animals)
```

##### With concatonation

```{code-cell} python
animals = animals + ["skink", "turtle", "viper"]
pprint(animals)
```

Or using the `+=` operator:

```{code-cell} python
animals += ["wolf", "zebra"]
pprint(animals)
```

##### Repeteadly with multiplication

```{code-cell} python
steps = ["rinse", "repeat"]
print(steps)

steps = (steps * 3)
print(steps)
```

Or using the `*=` operator:

```{code-cell} python
steps = ["rinse", "repeat"]
print(steps)

steps *= 3
print(steps)
```

### Remove

```{code-cell} python
chars = list("Hello world")

del chars[4]
print(chars)
```

#### By index

```{code-cell} python
chars = list("Hello world")

del chars[4]
print(chars)
```

#### By value

Remove first occurance of value using the `.remove() method`:

```{code-cell} python
chars = list("Hello world")

chars.remove("l")
print(chars)
```

#### By slice

Using the `del` keyword:

```{code-cell} python
chars = list("Hello world")

del chars[2:9]
print(chars)
```

By assigning to an empty list:

```{code-cell} python
chars = list("Hello world")

chars[0:3] = []
print(chars)
```

#### All elements

```{code-cell} python
chars = list("Hello world")

chars.clear()
print(chars)
```

#### Remove and return

##### The last element

```{code-cell} python
chars = list("Hello world")

removed = chars.pop()

print("removed:", repr(removed), "\n")
print(chars)
```

##### A specific element by position

```{code-cell} python
chars = list("Hello world")

removed = chars.pop(2)

print("removed:", repr(removed), "\n")
print(chars)
```

Membership
----------

```{code-cell} python
:tags: [thebe-init]
chars = list("Mississippi")
words = ['Welcome', 'to', 'Python', 'Class']
```

### Contains

Check if list contains value using the `in` operator:

```{code-cell} python
"Class" in words
```

Check if list does not contains value using the `not in` operator:

```{code-cell} python
"Class" not in words
```

### Count

Number of times value occurs in list:

```{code-cell} python
chars.count("i")
```

### Index

To look up the index number of a particular value, use the `.index()` method.

Get the first index number of value:

```{code-cell} python
chars.index("s")
```

Same, but look in `chars[3:]`:

```{code-cell} python
chars.index("s", 3)
```

Same, but look in `chars[5:9]`:

```{code-cell} python
chars.index("i", 5, 9)
```

Iteration
---------

### for loop

Iterate over each element:

```{code-cell} python
colors = ["red", "blue", "green"]
for item in colors:
  print(item)
```

#### enumerate

Iterate over each index number and element:

```{code-cell} python
meals = ["breakfast", "lunch", "dinner"]
for i, item in enumerate(meals):
  print(i, item)
```

Iterate over each index number and element value, starting `i` at `1`:

```{code-cell} python
drinks = ["water", "tea", "coffee"]
for i, item in enumerate(drinks, 1):
  print(i, item)
```

Aggregation
-----------

Functions that provide information about the container as a whole.

### Length

```{code-cell} python
len([0, 1, 2, 3])
```

### Maximum value

```{code-cell} python
max([0, 1, 2, 3])
```

### Minimum value

```{code-cell} python
min([0, 1, 2, 3])
```

### Sum of values

```{code-cell} python
sum([0, 1, 2, 3])
```

### any

Return `True` if any elements are truthy:

```{code-cell} python
any([0, False, ""])
```

```{code-cell} python
any([0, 1, 2, 3])
```

### all

Return `True` if all elements are truthy:

```{code-cell} python
all([0, 1, 2, 3])
```

```{code-cell} python
all([True, 1, "hello"])
```

Copying
-------

```{code-cell} python
:tags: [thebe-init]
DEFAULTS = [
  {
    'name': "Joe Smith",
    'email': 'joe.smith@gmail.com',
  },
  {
    'name': "Jane Doe",
    'email': "jane.doe@gmail.com"
  }
]
```

### Alias

A {term}`reference` or {term}`alias` creates a new variable that points to the
same object.

```{code-cell} python
authors = DEFAULTS

authors is DEFAULTS
```

### Shallow copy

A {term}`shallow copy` creates a new container object then adds references to elements.

Using `.copy()`:

```{code-cell} python
authors = DEFAULTS.copy()

print(authors is DEFAULTS)
print(authors[0] is DEFAULTS[0])
```

Using `copy.copy()`:

```{code-cell} python
import copy

authors = copy.copy(DEFAULTS)

print(authors is DEFAULTS)
print(authors[0] is DEFAULTS[0])
```

Using a slice:

```{code-cell} python
authors = DEFAULTS[:]

print(authors is DEFAULTS)
print(authors[0] is DEFAULTS[0])
```

### Deep copy

A {term}`deep copy` creates a new container object then recursively adds the copies of nested elements.

```{code-cell} python
import copy
authors = copy.deepcopy(DEFAULTS)

print(authors is DEFAULTS)
print(authors[0] is DEFAULTS[0])
```

Sorting
-------

```{code-cell} python
:tags: [remove-input, thebe-init]
"""setup for sorting section"""

from pprint import pformat

def pprint(obj):
  """pretty print obj if defined, otherwise print an equal number of lines"""
  if obj:
    print(pformat(obj, width=40))
  else:
    print("-" + ("\n"*(len(FRUIT)-1)) + repr(obj))
```

```{code-cell} python
:tags: [thebe-init]
"""setup for sorting section"""

# define global FRUIT list
FRUIT = ["cherry", "apple", "date", "bananna", "elderberry"]
```


### Returned sorting

The following functions return a sorted version of the collection and leave
original collection unmodified.

```{code-cell} python
:tags: [thebe-init]
# copy fruit list
fruit = FRUIT[:]
pprint(fruit)
```

#### Ascending order

```{code-cell} python
result = sorted(fruit)
pprint(result)
```

#### Descending order

```{code-cell} python
result = sorted(fruit, reverse=True)
pprint(result)
```

#### Reverse order

```{code-cell} python
result = list(reversed(fruit))
pprint(result)
```

#### Order by callable key

Using function:

```{code-cell} python
def order_by_length(text):
    return len(text)

result = sorted(fruit, key=order_by_length)
pprint(result)
```

Using lambda:

```{code-cell} python
result = sorted(fruit, key=lambda v: len(v))
pprint(result)
```

### In-place sorting

The following methods and functions change the order of the original collection
and return `None`.

#### Ascending order

```{code-cell} python
# reset fruit list
fruit = FRUIT[:]
pprint(fruit)
print("--------------")

fruit.sort()
pprint(fruit)
```

#### Descending order

```{code-cell} python
# reset fruit list
fruit = FRUIT[:]
pprint(fruit)
print("--------------")

fruit.sort(reverse=True)
pprint(fruit)
```

#### Reverse order

```{code-cell} python
# reset fruit list
fruit = FRUIT[:]
pprint(fruit)
print("--------------")

fruit.reverse()
pprint(fruit)
```

#### Order by callable key function

Using function:

```{code-cell} python
# reset fruit list
fruit = FRUIT[:]
pprint(fruit)
print("--------------")

def order_by_length(text):
    return len(text)

fruit.sort(key=order_by_length)
pprint(fruit)
```

Using lambda:

```{code-cell} python
# reset fruit list
fruit = FRUIT[:]
pprint(fruit)
print("--------------")

fruit.sort(key=lambda v:len(v))
pprint(fruit)
```

#### Random order

```{code-cell} python
# reset fruit list
fruit = FRUIT[:]
pprint(fruit)
print("--------------")

from random import shuffle
shuffle(fruit)
pprint(fruit)
```

Transformation
--------------

Generate a modified collection.

### Mapping

Produce a new collection containing the results from applying a function to
each element in a collection.

```{code-cell} python
:tags: [thebe-init]
"""Setup for the Mapping section"""

# the collection to base mappings on
birth_years = [1954, 1956, 1984, 1986]

# used in relative_age()
REL_YEAR = 1994

# the function to apply
def relative_age(year):
  return REL_YEAR - year
```

#### Using a for loop

```{code-cell} python
# initialize a list the same size as birth_years filled with None values
ages = [None] * len(birth_years)

# iterate over birth years and map the cooresponding element in ages to
# the results from applying the function to that element
for i, year in enumerate(birth_years):
  ages[i] = relative_age(year)

# print the ages list
print(ages)
```

#### Using list comprehension

```{code-cell} python
:tags: [thebe-init]
ages = [relative_age(year) for year in birth_years]

print(ages)
```

#### Using map

```{code-cell} python
ages = list(map(relative_age, birth_years))

print(ages)
```

### Filtering

Produce a new collection containing only elements which, when a applying a
function, return a truthy value.

```{code-cell} python
:tags: [thebe-init]
"""Setup for the Filtering section"""

# the function to apply
def is_adult(age):
  return age >= 18

# print the previously created ages collection to base the filterings on
print(ages)
```

#### Using a for loop

```{code-cell} python
# initialze an empty list
adults = []

# iterate over ages and append elements that results in True
# when applying the filtering function
for age in ages:
  if is_adult(age):
    adults.append(age)

# print the adults list
print(adults)
```

#### Using list comprehension

```{code-cell} python
adults = [ age for age in ages if is_adult(age) ]

print(adults)
```

#### Using filter

```{code-cell} python
adults = list(filter(is_adult, ages))

print(adults)
```

Typecasting
-----------

### str to list

#### individual characters

```{code-cell} python
list("abc")
```

#### split on whitespace

```{code-cell} python
"list info search".split()
```

#### split on delimiter

```{code-cell} python
"555-555-5555".split("-")
```

#### split on newlines

```{code-cell} python
"a\nb\nc\n".splitlines()
```

#### split on pattern

```{code-cell} python
import re
re.split(r"[./]", "github.com/git")
```

### dict to list

```{code-cell} python
:tags: [thebe-init]
fruit_sizes = {'cherry': 6, 'bananna': 7, 'date': 4, 'elderberry': 10, 'apple': 5}
```

#### keys

```{code-cell} python
list(fruit_sizes)
```

```{code-cell} python
list(fruit_sizes.keys())
```

#### values

```{code-cell} python
list(fruit_sizes.values())
```

### list to string

```{code-cell} python
"".join(["a", "b", "c"])
```

### list to dict

```{code-cell} python
dict([["a", 1], ["b", 2]])
```

```{code-cell} python
dict(zip(["a", "b"], [1, 2]))
```

----

% TODO
% - [ ] nested lists
% - [ ] comparisons
