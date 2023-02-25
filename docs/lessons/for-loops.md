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

For Loops
=========

A `while` loop continues for as long as a condition is met, a `for` loop on the
other hand repeats for every element in an iterable.

```{contents} Table of Contents
:backlinks: entry
:local:
:depth: 2
```

Part 1: Syntax
--------------

The syntax for a for loop is:

{{ leftcol | replace("col", "col-5") }}

```{include} ../templates/syntax/for.md
```

{{ rightcol | replace("col", "col-7") }}

```{include} ../templates/desc/for.md
```

{{ endcols }}

Here's a simple example that iterates over a `list` of strings.

```{literalinclude} ../templates/examples/for.py
:caption: "`for` loop example"
:linenos:
```

### Part 1.1: Exercise

```{exercise} Movies
:label: movies-exercise

Iterate over a `list` of `movies` and print each one out using a `for` loop.
```

`````{solution} movies-exercise
:class: dropdown

```{code-block} python
:caption: Movies Exercise
:linenos:

movies = [
  "Treasure Planet",
  "Finding Nemo",
  "Kung Fu Panda",
  "Wall-E",
  "Lilo & Stitch",
]

for name in movies:
  print(movie)
```

`````

Part 2: Iterables and iterators
-------------------------------

Some objects in Python are {term}`iterable`--that is, an object that can be
itereated over. For example, `list`, `tuple` and `range` objects are all
iterable.

All iterables can be converted to an {term}`iterator`, which is an object that
will keep returning elements until there are no more left.

To demonstrate this we'll create a `colors` `list` then convert the it to a
`colors_iterator` using the `iter()` function.

```{code-cell} python
colors = ["red", "green", "blue"]
colors_iterator = iter(colors)
```

Then we'll keep requesting items using the `next()` function, until we
encounter a `StopIteration` exception.

```{code-cell} python
next(colors_iterator)
```

```{code-cell} python
next(colors_iterator)
```

```{code-cell} python
next(colors_iterator)
```

```{code-cell} python
:tags: [raises-exception]
next(colors_iterator)
```

### Part 2.1: Exercise

```{exercise} Iterators
:label: iterator-exercise

1. Create a list containing the letters in your name assigned to the variable `letters`.
2. Convert the list to an iterator using the `iter()` function and assign it to the variable `letters_iterator`.
3. Keep calling `next()` with the argument `letters_iterator` until you encounter a `StopIteration` exception.
```

`````{solution} iterator-exercise
:class: dropdown

```{code-block} python
:caption:  Iterators Exercise

>>> letters = list("alissa")
>>> letters_iterator = iter(letters)
>>> next(letters_iterator)
'a'

>>> next(letters_iterator)
'l'

>>> next(letters_iterator)
'i'

>>> next(letters_iterator)
's'

>>> next(letters_iterator)
's'

>>> next(letters_iterator)
'a'

>>> next(letters_iterator)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-51-15be8840759d> in <module>
----> 1 next(letters_iterator)

```
`````

Part 3: Under the hood
----------------------

Now that you know what iterables and iterators are, we demystify for loops.

Lets look at the syntax again.

```{include} ../templates/syntax/for.md
```

Here's what's happening behind the scenes:

1. `ITERABLE` is converted to an iterator object using `iter()`, or rather its {term}`magic method`
2. Each iteration, `next()` is called, and the results are assigned to `VAR`
3. The `BODY` statements are executed
3. When `next()` results in a `StopIteration` exception it is discarded and the loop ends


Lets revisit our `for` loop example, and see if we can deconstruct the behavior
of a `for` loop. First we'll create a `houses` list, and convert it to a
`houses_iter` using the `iter()` function.

```{code-cell} python
# create iterable
houses = [
  "Arryn",
  "Baratheon",
  "Greyjoy",
  "Lannister",
  "Martell",
  "Stark",
  "Targaryen",
  "Tully",
  "Tyrell",
]

# create iterator
houses_iter = iter(houses)
```

Now we'll call `next()` in a `while` loop, and assign the results to `name`.

```{code-cell} python
:tags: [raises-exception]
# loop forever
while True:
    # assign VAR to the results of next()
    name = next(houses_iter)

    # BODY statements
    print(f"House {name}")
```

This is close, but we're still seeing that `StopIteration` exception. To
supress it we'll need a try-except block.

```{code-cell} python
:tags: [raises-exception]

# create iterator
houses_iter = iter(houses)

# loop forever
while True:

    # any code that may raise an exception goes under the try header
    try:

        # assign VAR to the results of next()
        name = next(houses_iter)

    # the type of exception that we want to catch
    # instead of raising it, the body statements will be executed
    except StopIteration:

        # StopIteration means there are no more elements, so exit the loop
        break

    # BODY statements
    print(f"House {name}")
```

Now we have a `while` loop that replicates the behavior of a `for` loop. Here they are side by side.

<div class="row"><div class="col">

```{code-block-hl} python
houses = [
  "Arryn",
  "Baratheon",
  "Greyjoy",
  "Lannister",
  "Martell",
  "Stark",
  "Targaryen",
  "Tully",
  "Tyrell",
]

houses_iter = iter(!!!houses!!!)

while True:
    try:
      !!!name!!! = next(houses_iter)
    except StopIteration:
      break

    print(f"House {name}")

```

</div><div class="col">

```{code-block-hl} python
houses = [
  "Arryn",
  "Baratheon",
  "Greyjoy",
  "Lannister",
  "Martell",
  "Stark",
  "Targaryen",
  "Tully",
  "Tyrell",
]

for !!!name!!! in !!!houses!!!:
  print(f"House {name}")

```
</div></div>

### Part 3.1: Exercise

```{exercise} Game Characters
:label: characters-exercise

1. Make a `list` of game character `roles`.
1. write a `while` loop
   1. Convert the `list` to an `roles_iter` iterator using the `iter()` function
   1. Make a `while` loop with the condition `True`
   1. Get each `role` element from the `roles_iter` by calling `next()`
   1. Print the `role`
   1. Suppress the error with a try-except block
2. write a `for` loop
   1. Make a `for` loop with the variable name `role` and the iterable `roles`
   1. Print the `role`

```

`````{solution} characters-exercise
:class: dropdown

```{code-block} python
:caption: Characters Exercise
:linenos:

WIDTH = 30
roles = ["mage", "thief", "warrior"]

print("WHILE LOOP ".ljust(WIDTH, "#"))
roles_iterator = iter(roles)
while True:
    try:
      role = next(roles_iterator)
    except StopIteration:
        break
    print(role)


print("FOR LOOP ".ljust(WIDTH, "#"))
for role in roles:
  print(role)

```

`````

Part 4: Multiple assignment
---------------------------

Depending on the type passed to it, `next()` may sometimes return more than one
value. The classic example of this is {samp}`{dict}.items()`.

```{code-cell} python
suites = {
  "heart": "red",
  "diamond": "red",
  "club": "black",
  "spade": "black",
}
suites_iterator = iter(suites.items())
```

```{code-cell} python
next(suites_iterator)
```

You can see that `next()` returns a `tuple` that contains two items. We can
assign this to a single variable, which will then contain the entire `tuple.`

```{code-cell} python
item = next(suites_iterator)
item
```

Or we could use {term}`multiple assignment` to assign each item in the `tuple`
to a cooresponding variable. There must be the same number of variables to the
left of the `=` as there are items in the `tuple` seperated by `,`.

```{code-cell} python
suit, color = next(suites_iterator)
```

```{code-cell} python
suit
```

```{code-cell} python
color
```

Lets put this assignment fanciness in a `while` loop.

```{code-cell} python
suites_iterator = iter(suites.items())

while True:
    try:
      suit, color = next(suites_iterator)
    except StopIteration:
      break

    print(f"The {suit} suit is {color}.")
```

And lets see how it looks in a `for` loop.

```{code-cell} python
for suit, color in suites.items():
    print(f"The {suit} suit is {color}.")
```

Here they are side by side.

<div class="row"><div class="col">

```{code-block-hl} python
:linenos:

suites = {
  "heart": "red",
  "diamond": "red",
  "club": "black",
  "spade": "black",
}

suites_iterator = iter(!!!suites.items()!!!)

while True:
    try:
      !!!suit, color!!! = next(suites_iterator)
    except StopIteration:
      break

    print(f"The {suit} suit is {color}.")
```
</div><div class="col">

```{code-block-hl} python
:linenos:

suites = {
  "heart": "red",
  "diamond": "red",
  "club": "black",
  "spade": "black",
}

for !!!suit, color!!! in !!!suites.items()!!!:
    print(f"The {suit} suit is {color}.")

```

</div></div>

### Part 4.1: Exercise

```{exercise} Game Tools
:label: toolss-exercise

1. Make a `dict` of game character `tools`, where the key is the `role` and the value is a `tool`.
1. write a `while` loop
   1. Convert `tools.items()` to an `tools_iter` iterator using the `iter()` function
   1. Make a `while` loop with the condition `True`
   1. Get each `role` and `tool` element from the `tools_iter` by calling `next()`
   1. Print the {samp}`"A {role}s favorite tool is their trusty: {tool}."`
   1. Suppress the error with a try-except block
2. write a `for` loop
   1. Make a `for` loop with the variable name `tool` and the iterable `tools`
   1. Print the `tool`

```

`````{solution} skills-exercise
:class: dropdown

```{code-block} python
:caption: Skills Exercise
:linenos:

WIDTH = 30
tools = {
  "mage": "wand",
  "thief": "lockpick set",
  "warrior": "sword",
}
tools_iter = iter(tools.items())

print("WHILE LOOP ".ljust(WIDTH, "#"))
while True:
  try:
    role, tool = next(tools_iter)
  except StopIteration:
    break
  print(f"A {role}s favorite tool is their trusty: {tool}.")

print("FOR LOOP ".ljust(WIDTH, "#"))
for role, tool in tools.items():
  print(f"A {role}s favorite tool is their trusty: {tool}.")

```

`````

Part 5: Incrementing
--------------------

Sometimes we need to keep track of the number associated with each item in an
iterable. One way to do this would be to increment a number each iteration.

```{code-cell} python
i = 0
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for color in rainbow:
  print(i, color)
  i += 1
```

An easier way to do this is to use the `enumerate()` function which returns an
iterator. Each iteration it yields a tuple containing the count and the next
item.

Lets take a look at what happens when we pass the `rainbow` list to
`enumerate()`. (Notice that we convert the iterator to a list so we can see its
contents.)

```{code-cell} python
list(enumerate(rainbow))
```

To use this in a `for` loop, we'll call `enumerate()` on the `ITERABLE`. Then
we'll change `VAR` so that it assigns both `i` and `color`.

```{code-cell} python
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i, color in enumerate(rainbow):
  print(i, color)
```

We can change the number that `emumerate()` starts at by passing an optional
second argument.

```{code-cell} python
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i, color in enumerate(rainbow, 1):
  print(i, color)
```

But what happens if you want to enumerate an iterable that yields multiple
items per iteration? Is it possible to assign the number and the other items to
their respective variable names?

Lets take a look at what happens when we pass a {samp}`{dict}.items()` iteratable to
`enumerate()`.

```{code-cell} python

suites = {
  "heart": "red",
  "diamond": "red",
  "club": "black",
  "spade": "black",
}

list(enumerate(suites.items()))
```

The iterable now yields a tuple containing a the count, and each item is a
tuple containing the key and value like so: {samp}`({COUNT}, ({KEY}, {VALUE}))`

To use this in a for loop, simply encose the key-value tuple in parenthesis.

```{code-cell} python

suites = {
  "heart": "red",
  "diamond": "red",
  "club": "black",
  "spade": "black",
}

for i, (suit, color) in enumerate(suites.items(), 1):
    print(f"{i}. The {suit} suit is {color}.")
```


### Part 5.1: Exercise

`````{exercise} Number Names
:label: number-names-exercise

Use the `enumerate` function to print the numerical values `1` through `5` next
to the names of those numbers (`"one"` through `"five"`).

```{dropdown} Need help?
1. Make a list assigned to the variable `numbers` containing the names of the
numbers `"one"` through `"five"`.
2. Write a `for` loop using the variable names `i` and `name` that iterates over
the value returned from calling `enumerate()` with the arguments `numbers`
and `1`. \
   In the for loop:
   * print `i` and `name`
```

**Example output**:

```{code-block} text
:caption: example output
1 one
2 two
3 three
4 four
5 five
```

`````

`````{solution} number-names-exercise
:class: dropdown

```{code-block} python
:caption: Number Names Exercise
:linenos:

numbers = ["one", "two", "three", "four", "five"]

for i, name in enumerate(numbers, 1):
  print(i, name)

```

`````

Part 6: Comparing loops
-----------------------

Lets do some side-by-side comparisons of the same code written as a `while` loop
and a `for` loop.

On the left will be the `while` loop code and on the right will be the `for` loop code.

### Part 6.1: list iteration with `next()`

In this example we'll iterate over a `colors` `list`.

On the left we will use a `while` loop to iterate over a `list` by converting
it using the `iter()` function, then calling `next()` on the resulting
iterator.

On the right the same code as a `for` loop, where the use of `iter()` and
`next()` happens behind the scenes.

<div class="row"><div class="col">

```{code-block-hl} python
:caption: "Iter example A-1: `list` iteration via `while` loop"
colors = ["red", "green", "blue"]
colors_iterator = iter(!!!colors!!!)
while True:
    try:
        !!!color!!! = next(colors_iterator)
    except StopIteration:
        break
    print(color)
```

</div><div class="col">

```{code-block-hl} python
:caption: "Iter example A-2: `list` iteration via `for` loop"
colors = ["red", "green", "blue"]
for !!!color!!! in !!!colors!!!:
  print(color)
```

</div></div>

### Part 6.2: range iteration with `next()`

Lets do the same comparison with a `range` object.

On the left we will use a `while` loop to iterate over a `range` by converting
it using the `iter()` function, then calling `next()` on the resulting
iterator.

On the right is the same code as a `for` loop.

<div class="row"><div class="col">

```{code-block-hl} python
:caption: "Iter example B-1: `range` iteration via `while` loop (error surpressed)"
numbers = range(1, 4)
numbers_iter = iter(!!!numbers!!!)
while True:
  try:
    !!!num!!! = next(numbers_iter)
  except StopIteration:
    break

  print(num)
```

</div><div class="col">

```{code-block-hl} python
:caption: "Iter example B-2: `range` iteration via `for` loop"
numbers = range(1, 4)
for !!!num!!! in !!!numbers!!!:
  print(num)
```

</div></div>

### Part 6.3: list iteration with subscription

In this example we'll iterate over the `colors` `list` as before, except now
we'll use an incrementing index number to get each element using
{term}`bracket notation` or {term}`subscription`.

While you can achieve similar results this way, subscription is not a perfect
mirror of an analogous `for` loop. It's not quite as accurate in terms of what
goes on under the hood and in fact not all iterable objects provide access via
bracket notation.

Even so, the this familiar pattern may help to shed some light on `for` loop
behavior.

<div class="row"><div class="col">

```{code-block-hl} python
:caption: "Bracket example C-1: `list` iteration via `while` loop"

colors = ["red", "green", "blue"]
idx = 0

while idx < len(!!!colors!!!):
    !!!color!!! = !!!colors!!![idx]
    print(color)
    idx += 1
```

</div><div class="col">

```{code-block-hl} python
:caption: "Subscript example C-2: `list` iteration via `for` loop"

colors = ["red", "green", "blue"]

for !!!color!!! in !!!colors!!!:
  print(color)
```

</div></div>

### Part 6.4: string iteration with subscription

In this example we'll iterate over each `letter` in the string `word` using
bracket notaton.

<div class="row"><div class="col">

```{code-block-hl} python
:caption: "Bracket example D-1: `str` iteration via `while` loop"

word = "flibbertigibbet"
idx = 0

while idx < len(!!!word!!!):
    !!!letter!!! = !!!word!!![idx]
    print(letter)
    idx += 1
```

</div><div class="col">

```{code-block-hl} python
:caption: "Bracket example D-2: `list` iteration via `for` loop"

word = "flibbertigibbet"

for !!!letter!!! in !!!word!!!:
  print(letter)
```

</div></div>

Part 7: Exercises
-----------------

### Part 7.1: Game Skills

```{exercise} Game Skills
:label: skills-exercise

1. Make a `list` of game character `skills`.
1. write a `while` loop
   1. Assign the `idx` var to `0`
   1. Make a `while` loop with the condition that `idx` is less than the length of `skills`
      1. Get each element from `skills` using bracket notation `idx` and assign it to `skill`
      1. Increment `idx`
      1. Print the `skill`
2. write a `for` loop
   1. Make a `for` loop with the variable name `skill` and the iterable `skills`
      1. Print the `skill`

```

`````{solution} skills-exercise
:class: dropdown

```{code-block} python
:caption: Skills Exercise
:linenos:

WIDTH = 30
skills = ["heal", "attack", "acquire"]
idx = 0

print("WHILE LOOP ".ljust(WIDTH, "#"))
while idx < len(skills):
  skill = skills[idx]
  print(skill)
  idx += 1

print("FOR LOOP ".ljust(WIDTH, "#"))
for skill in skills:
  print(skill)

```

`````

### Part 7.2: Weekdays

```{exercise} Weekdays
:label: label-exercise

Print the weekday names horizontally and seperated by `|`.

1. Make a `WEEKDAYS` `list` of names.
1. Use a `for` loop to iterated over each `day`.
1. Print each `day` centered to the same `size` (somewhere around `10` to `20`)
   with seperated by vertical bars (`|`). \
   *Hint: using the `.center()` method.*

Example output:

`|   Monday   |  Tuesday   | Wednesday  |  Thursday  |   Friday   |`


```

`````{solution} label-exercise
:class: dropdown

```{code-block} python
:caption: Weekdays Exercise
:linenos:

SIZE=10
SEP = " | "
WEEKDAYS = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
]

strings = [SEP]

for day in WEEKDAYS:
  title = day.center(SIZE)
  strings = strings + [title, SEP]

print(*strings, sep="")
```

`````

Reference
---------

### Glossary

```{glossary} for-loops

iterable
  An object that can be iterated over. One that provides the `.__iter__()`
  method used by the `iter()` function.

iterator
  An object that provides a `.__next__()` method, used by the built in function
  `next()`,  which, when called repeatedly, will keep returning elements until
  there are no more left.

multiple assignment
  Assigning the contents of an itrable to multiple variables on the same line
  with the same number of variables names to the left of the `=` as there are
  items in the iterable seperated by `,`. \
  For example: \
  `from, to = (1, 100)` \
  `first, last = "a", "b"`

```

### See also

```{seealso}

* [python.org > Iterator Types](https://docs.python.org/3/library/stdtypes.html#typeiter)
* [python.org > Expressions > Subscriptions](https://docs.python.org/3/reference/expressions.html#subscriptions)
* [Loop Better: a deeper look at iteration in Python](https://treyhunner.com/2019/06/loop-better-a-deeper-look-at-iteration-in-python/)
* [Python’s built-in container data types: categorisation and iteration](http://blog.wachowicz.eu/?p=132)

```

----

% TODO .....
% [ ] break and continue
% [ ] different types, converting using list()
% [ ] iterators are one way
% [ ] enumerate()
% [x] multiple assignment
% [x] exercises
% [x] fix old exercses
