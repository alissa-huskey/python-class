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

{{ leftcol | replace("col", "col-8")  }}

An ordered collection of arbitrary objects accessed via index numbers.

```{contents} Table of Contents
:backlinks: top
:local:
```

{{ rightcol | replace("col", "col-4 text-right") }}

:::{fieldlist}

:Type:        `list`
:Synatx:      {samp}`[{item},...]`
:Bases:       Sequence, Iterable
:State:       Mutable
:Position:    Ordered
:Composition: Heterogeneous
:Diversity:   Repeatable
:Access:      Subscriptable
:Value:       Not hashable

:::

{{ endcols }}

```{code-cell} python
:tags: [remove-input, thebe-init]
"""setup pprint method"""

from pprint import pformat

def pprint(obj):
  """pretty print obj if defined, otherwise print an equal number of lines"""
  if obj:
    print(pformat(obj, width=40))
  else:
    print("-" + ("\n"*(len(GLOBAL)-1)) + repr(obj))
```

Basics
------

### Creating

There are several ways to create a new list. The simplest is to enclose the
elements, seperated by commas, in square brackets (`[` and `]`):

```{code-cell} python
:tags: [thebe-init]
cities = ["London", "Paris", "Berlin"]
```

```{code-cell} python
:tags: [thebe-init, remove-input]
# set global to cities list for pprint
GLOBAL = cities
```

Each element is assigned a successive {term}`index number`, starting at `0`.
Under the hood, the `cities` list looks like this:

```{kroki}
:type: ditaa
+----------------------------------------+
|                                        |
| cities (list)                          |
|                                        |
|   +----------+----------+----------+   |
|   |          |          |          |   |
|   | London   | Paris    | Berlin   |   |
|   |          |          |          |   |
|   +----------+----------+----------+   |
|   |    0 cCFF|    1 cCFF|    2 cCFF|   |
|   +----------+----------+----------+   |
|   |   -3 cCCF|   -2 cCCF|   -1 cCCF|   |
|   +----------+----------+----------+   |
|                                        |
+----------------------------------------+

  /----\               /----\
  |cCFF| index number  |cCCF| negative index
  \----/               \----/

```

### Accessing

Items are accessed via {term}`subscription`, using `[` `]` after the object
to enclose a selector expression. For example, use the index number to select
an individual item.

```{code-cell} python
print(cities[0])
```

You can use a negative index number to access elements starting at the end.

Negative index numbers are shorthand for
{samp}`{length of list} + {negative index value}`.

```{code-cell} python
print(cities[-1])
```

Subscription is also used to change list elements.

```{code-cell} python
cities[1] = "Amsterdam"
print(cities)
```

### Adding

To add an element to the end of a list, use the `.append()` method.

```{code-cell} python
:tags: [thebe-init]
cities.append("Dublin")
print(cities)
```

Or you can add an item at a specific position with the `.insert()` method.

```{code-cell} python
:tags: [thebe-init]
cities.insert(1, "Italy")
print(cities)
```

Or you can add all the items from another {term}`iterable` with the `.extend()`
method.

```{code-cell} python
:tags: [thebe-init]
cities.extend(["San Francisco", "Brooklyn", "Denver"])
pprint(cities)
```

### Removing

Use the `del` keyword to remove an element by index.

```{code-cell} python
:tags: [thebe-init]
del cities[1]
print(cities)
```

Or to remove an element by value, use the `.remove()` method.

```{code-cell} python
:tags: [thebe-init]
cities.remove("London")
print(cities)
```

### Membership

Check if list contains value using the `in` operator:

```{code-cell} python
"London" in cities
```

Check if list does not contains value using the `not in` operator:

```{code-cell} python
"London" not in cities
```

To look up the index number of a particular value, use the `.index()` method.

Get the first index number of value:

```{code-cell} python
cities.index("Dublin")
```

### Exercises

`````{exercise} Random Lotto Numbers
:label: lotto-numbers-exercise

Generate a list of six unique numbers between `1` and `49`, then print the list.

```{dropdown} Need help?
* import the `random` module
* make an empty list assigned to the variable `numbers`
* start a `while` loop with the condition that the length of `numbers` is less than `6`
* in the loop:
  * get a random number between `1` and `49` using the `random.randint()`
    method and assign it to the variable `num`
  * check if `num` is in the `numbers` list
    * if not, append `num` to `numbers`
* print the `numbers` list
```

**Example output**:

```python
[29, 19, 17, 49, 45, 4]
```

`````

`````{solution} lotto-numbers-exercise
:class: dropdown

```{code-block} python
:caption: Random Lotto Numbers Exercise
:class: full-width
:linenos:

import random

numbers = []
while len(numbers) < 6:
  num = random.randint(1, 49)
  if num not in numbers:
    numbers.append(num)

print(numbers)

`````

Slices
------

You often want to extract part of a list. This could be accomplished using a
`for` loop, for example:

```{code-cell} python
partial, start, stop = [], 2, 5

for i, item in enumerate(cities):
  if i >= start and i < stop:
    partial.append(item)

print(partial)
```

Python provides handy dandy slice functionality, which is also supported by
subscription.

The syntax is: {samp}`{COLLECTION}[{START}:{STOP}]`

Using this feature we can extract the same part of the list like so:

```{code-cell} python
cities[2:5]
```

A missing `STOP` value will default to the end of the list.

```{code-cell} python
cities[2:]
```

A missing `START` value will default to the beginning of the list.

```{code-cell} python
cities[:2]
```

If both are missing, the slice will be a copy of the whole list.

```{code-cell} python
cities[:]
```


Values
------

The `list` type is {term}`heterogeneous`, which means it can contain arbitrary
objects of any type. So far in this lesson our example list has contained all
`str` objects.  But in fact, we can mix and match.

```{code-cell} python
[None, True, 'two', 3.0, 4]
```

We can use {term}`multiple assignment` to easily assign assign all of the
values in a list to a series of variables.

```{code-cell} python
book = [5, "Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979]

rating, title, author, year = book

print(f"{title} ({year}) by {author}: {rating} stars")
```

Lists can also contain other lists.

```{code-cell} python
:tags: [thebe-init]
meals = [
  ["omelet", "turkey wrap", "tacos"],
  ["oatmeal", "turkey burger", "tamales"],
  ["yogurt", "chicken salad", "enchiladas"],
]
```

You can access items in the nested lists by using multiple indexing operations.

```{code-cell} python
print(f"Dinner tonight is: {meals[0][2]}.")
print(f"Tomorrow for breakfast we're having: {meals[1][0]}.")
```

Iteration
---------

Iterate over each element using a `for` loop.

```{code-cell} python
for item in cities:
  print(item)
```

To include the index number, use the `enumerate()` function.

```{code-cell} python
for i, item in enumerate(cities):
  print(i, item)
```

To iterate over a nested list, you'll need nested for loops. The `VAR` in the
first loop will point to the child list; the nested `VAR` will point to the
child list elements.

```{code-cell} python
table = [
  [1, 2, 3, 4],
  [2, 4, 6, 8],
  [3, 6, 9, 12],
  [4, 8, 12, 16],
]

# iterate over the table list and assign each child list to row
for row in table:

   # iterate over the child list and assign each element to product
   for product in row:

       # print the number, right aligned, followed by two spaces
       print(str(product).rjust(2), end="  ")

   # print a new line at the end of every row
   print()
```

If you are certain to have the same number of items in every row, you can use
multiple assignment in the for loop `VAR`.

```{code-cell} python
for breakfast, lunch, dinner in meals:
   print(f"Breakfast: {breakfast}")
   print(f"Lunch: {lunch}")
   print(f"Dinner: {dinner}")
   print()
```

You can even combine this technique with `enumerate()` elements by enclosing
the child element variable names in `(` `)`.


```{code-cell} python
for i, (breakfast, lunch, dinner) in enumerate(meals):
   if i == 0:
       day = "Today"
   elif i == 1:
       day = "Tomorrow"
   else:
       day = f"In {i} days"

   print(f"### {day}\n")
   print(f"Breakfast: {breakfast}")
   print(f"Lunch: {lunch}")
   print(f"Dinner: {dinner}")
   print()
```

Sorting
-------

There are two ways to sort a list

* {samp}`sorted({list})` -- returns a new sorted list
* {samp}`{list}.sort()` -- sorts the list in place

To demonstrate this, we'll use the `FRUIT` list.

```{code-cell} python
:tags: [thebe-init]
# define global FRUIT list
FRUIT = ["cherry", "apple", "date", "bananna", "elderberry"]
```
We'll make copies and sort using both methods side by side.

```{code-cell} python
:tags: [thebe-init, remove-input]
# set global to FRUIT list for pprint
GLOBAL = FRUIT
```

{{ leftcol }}

```{rubric} Returned sorting
```

```{code-cell} python
:tags: [thebe-init]
# make a fresh copy of FRUIT
fruit = FRUIT[:]
pprint(fruit)
```

```{code-cell} python
:tags: [thebe-init]
# sorted() returns a new list
result = sorted(fruit)
pprint(result)
```

```{code-cell} python
# and leaves fruit alone
pprint(fruit)
```

{{ rightcol }}

```{rubric} In-place sorting
```

```{code-cell} python
:tags: [thebe-init]
# make a fresh copy of FRUIT
fruit = FRUIT[:]
pprint(fruit)
```

```{code-cell} python
:tags: [thebe-init]
# .sort() returns None
result = fruit.sort()
pprint(result)
```

```{code-cell} python
# but fruit was modified in place
pprint(fruit)
```

{{ endcols }}

Exercises
---------

`````{exercise} Delete Alternate Items
:label: delete-alternates-exercise

1. Make a list of words and print it.
2. Iterate over the list using a `for` loop and the `enumerate` function, and delete every other item.
   *Hint: You can check if a number is even with `i % 2 == 0`*
3. Print the list again.

**Example output:**

```
Before: ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
After: ['Lorem', 'dolor', 'sit', 'consectetur', 'adipiscing']
```


`````

`````{solution} delete-alternates-exercise
:class: dropdown

```{code-block} python
:caption: Delete Alternate Items Exercise
:class: full-width
:linenos:

words = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]
print("Before:", words)
for i, elm in enumerate(words):
  if i % 2 != 0:
    del words[i]
print("After:", words)

`````


`````{exercise} Appointment Maker
:label: appointment-exercise

This exercise is to find the overlapping days that two people are available.

1. Make two lists `my_days` and `your_days`, which each contain a list of
   weekday names that each hypothetical person is available.
2. Make an empty list `shared_days`.
3. Add items to the `shared_days` list that are in both the `my_days` and
   `your_days` lists.
   ```{dropdown} Need help?
   Iterate over one of the lists, then use the `in` operator to check if that
   day is in the other list. If it is, then use the `.append()` method to add
   that day to `shared_days`.
   ```
4. If there are no items in `shared_days` print a message saying that there are
   no shared days available.
5. Otherwise, print a message that the following days will work, then print
   each day on a new line.
6. Bonus: Make a function called `find_shared_days()` that takes `my_days` and
   `your_days` as arguments and returns `shared_days`.

Example output:
```text
The following days will work:
* Monday
* Thursday
```

Or:
```text
No shared days available, sadface.
```

`````

`````{solution} appointment-exercise
:class: dropdown

```{code-block} python
:caption: Appointment Maker Exercise
:class: full-width
:linenos:

my_days = ["monday", "tuesday", "friday"]
your_days = ["monday", "wednesday", "thursday"]
shared_days = []

for day in my_days:
    if day in your_days:
        shared_days.append(day)

if not shared_days:
    print("No shared days available, sadface.")
else:
    print("The following days will work:")
    for day in shared_days:
        print("*", day.title())
`````

`````{exercise} Deck of Cards
:label: deck-of-cards-exercise

Write a function `make_deck()` to generate a list of `52` playing cards where
each card is a number or letter representing the rank, and a letter or number
representing the suit.

```{dropdown} Need help?
* make a list of `SUITS` that contains the suit letters
* make a list of `RANKS` including the ranks
* write a function make_deck() in the function:
  * make an empty `deck` list
  * use a `for` loop to iterate over each `SUIT` with the variable name `suit`
    * use a (nested) `for` loop to iterate over each `RANK` with the variable name `rank`
      * combine the `rank` and `suit` into one string and assign it to the variable `card`
      * append `card` to the `deck` list
  * return `deck`
```

Bonus: Add an optional argument `shuffled` that defaults to False, which
shuffles the deck using the `random.shuffle()` function.

{{ leftcol }}

**Ranks**

|         |               |
|---------|---------------|
| `2`-`9` | numeric value |
| `"T"`   | Ten           |
| `"J"`   | Jack          |
| `"Q"`   | Queen         |
| `"K"`   | King          |

{{ rightcol }}

**Suits**

|         |               |
|---------|---------------|
| `"C"`   | Clubs         |
| `"D"`   | Diamonds      |
| `"H"`   | Hearts        |
| `"S"`   | Spades        |

{{ endcols }}

**Example usage**:

```python
>>> deck = make_deck()
>>> len(deck)
52
>>> deck[:13]
['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC']
```

`````

`````{solution} deck-of-cards-exercise
:class: dropdown

```{literalinclude} ../../../pythonclass/exercises/cards.py
:caption: Deck of Cards Exercise
:class: full-width
:linenos:
:start-at: "from random import shuffle"
:end-at: "return deck"


`````
Reference
---------

```{glossary} lists

heterogeneous
  Elements in the collection may be of any type.

homogeneous
  All elements in the collection are of the same type.

```

```{seealso}

* [Lists Reference](../../reference/lists.md)

```

----

% TODO
% - [x] nesting
% - [ ] copying
% - [ ] exercises
% - [ ] glossary terms
% - [x] multiple assignment
