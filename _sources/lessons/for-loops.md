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

% TODO
% [ ] break and continue
% [ ] different types, converting using list()
% [ ] iterators are one way
% [ ] enumerate()
% [-] multiple assignment
% [x] exercises
% [x] fix old exercses


Table of Contents
-----------------

* [Syntax](#syntax)
   * [Exercise](#exercise)
* [Iterables and iterators](#iterables-and-iterators)
   * [Exercise](#exercise-1)
* [Comparing loops](#comparing-loops)
   * [Example A: list iteration with next()](#example-a-list-iteration-with-next)
   * [Example B: range iteration with next()](#example-b-range-iteration-with-next)
   * [Example C: list iteration with subscription](#example-c-list-iteration-with-subscription)
   * [Example D: string iteration with subscription](#example-d-string-iteration-with-subscription)
   * [Exercises](#exercises)
* [Exercises](#exercises-1)
* [Reference](#reference)
   * [Glossary](#glossary)
   * [See also](#see-also)

Syntax
------

The syntax for a for loop is:

`````{parsed-literal}
{samp}`for {VAR} in {ITERABLE}:`
    {samp}`    {BODY}`
`````

* `for` and `in` are {term}`keywords <keyword>`
* {samp}`{VAR}` -- variable name (or comma-seperated list of names) for each item
* {samp}`{ITERABLE}` -- object to iterate over
* {samp}`{BODY}` -- statements to execute where {samp}`{VAR}` will be used

Under the hood, a for loop converts `ITERABLE` an iterator object, then
repeatedly assigns the results of `next()` to `VAR` until there are no more
left. (More on iterables and itrators later.)

Here's a simple example that iterates over a `list` of strings.

```{code-block} python
:caption: "`for` loop example"
:class: full-width
:linenos:

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

for name in houses:
  print(f"House {name}")
```

### Exercise

```{exercise} Movies
:label: movies-exercise

Iterate over a `list` of `movies` and print each one out using a `for` loop.
```

`````{solution} movies-exercise
:class: dropdown

```{code-block} python
:caption: Movies Exercise
:class: full-width
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

Iterables and iterators
-----------------------

Some objects in Python are {term}`iterable`--that is, an object that can be
itereated over. For example, `list`, `tuple` and `range` objects are all
iterable.

All iterables can be converted to an {term}`iterator`, which is an object that
will keep returning elements until there are no more left.

### List iterator

To demonstrate this we'll create a `colors` `list` then convert the it to a
`colors_iterator` using the `iter()` function.

```{code-cell} python
:class: full-width
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

#### Exercise

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
:class: full-width

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

### Multiple assignment

Depending on the type passed to it, `next()` may sometimes return more than one
value. The classic example of this is {samp}`{dict}.items()`.

```{code-cell} python
:class: full-width
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
suite, color = next(suites_iterator)
```

```{code-cell} python
suite
```

```{code-cell} python
color
```


Comparing loops
---------------

Lets do some side-by-side comparisons of the same code written as a `while` loop
and a `for` loop.

On the left will be the `while` loop code and on the right will be the `for` loop code.

### Example A: list iteration with `next()`

In this example we'll iterate over a `colors` `list`.

On the left we will use a `while` loop to iterate over a `list` by converting
it using the `iter()` function, then calling `next()` on the resulting
iterator.

On the right the same code as a `for` loop, where the use of `iter()` and
`next()` happens behind the scenes.

<div class="row"><div class="col">

```{code-block-hl} python
:caption: "Iter example A-1: `list` iteration via `while` loop (ends in error)"
:class: full-width
colors = ["red", "green", "blue"]
colors_iterator = iter(!!!colors!!!)
while True:
    !!!color!!! = next(colors_iterator)
    print(color)
```

This will raise the `StopIteration` exception. To suppress it, we can use a
`try-except` block.

```{code-block-hl} python
:caption: "Iter example A-2: `list` iteration via `while` loop (error surpressed)"
:class: full-width
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
:caption: "Iter example A-3: `list` iteration via `for` loop"
:class: full-width
colors = ["red", "green", "blue"]
for !!!color!!! in !!!colors!!!:
  print(color)
```

</div></div>

### Example B: range iteration with `next()`

Lets do the same comparison with a `range` object.

On the left we will use a `while` loop to iterate over a `range` by converting
it using the `iter()` function, then calling `next()` on the resulting
iterator.

On the right is the same code as a `for` loop.

<div class="row"><div class="col">

```{code-block-hl} python
:caption: "Iter example B-1: `range` iteration via `while` loop (error surpressed)"
:class: full-width
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
:class: full-width
numbers = range(1, 4)
for !!!num!!! in !!!numbers!!!:
  print(num)
```

</div></div>

### Example C: list iteration with subscription

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
:class: full-width

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
:class: full-width

colors = ["red", "green", "blue"]

for !!!color!!! in !!!colors!!!:
  print(color)
```

</div></div>

### Example D: string iteration with subscription

In this example we'll iterate over each `letter` in the string `word` using
bracket notaton.

<div class="row"><div class="col">

```{code-block-hl} python
:caption: "Bracket example D-1: `str` iteration via `while` loop"
:class: full-width

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
:class: full-width

word = "flibbertigibbet"

for !!!letter!!! in !!!word!!!:
  print(letter)
```

</div></div>

### Exercises

```{exercise} Game Characters
:label: characters-exercise

1. Make a `list` of game character `roles`.
1. write a `while` loop
   1. Convert the `list` to an `roles_iter` iterator using the `iter()` function
   1. Make a `while` loop with the condition `True`
   1. Get each `role` element from the `roles_iter` by calling `next()`
   1. Print the `role`
   1. Bonus: add a try-except block to suppress the error
2. write a `for` loop
   1. Make a `for` loop with the variable name `role` and the iterable `roles`
   1. Print the `role`

```

`````{solution} characters-exercise
:class: dropdown

```{code-block} python
:caption: Characters Exercise
:class: full-width
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
:class: full-width
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



Exercises
---------

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
:class: full-width
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

container
  A value that can hold other values, for example `list` objects.

iterable
  An object that can be iterated over. One that provides the `.__iter__()`
  method used by the `iter()` function.

iterator
  An object that provides a `.__next__()` method, used by the built in function
  `next()`,  which, when called repeatedly, will keep returning elements until
  there are no more left.

subscript
subscription
bracket notation
  Accessing an element from a collection object using `[` `]` after the object
  which enclose a selector expression. The expression may be an index number,
  key, or slice depending on its type. \
  The syntax is: {samp}`{COLLECTION}[{SELECTOR}]`.

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

