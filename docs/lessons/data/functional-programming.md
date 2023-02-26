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
Functional Programming
======================

```{include} ../../toc.md
```

Introduction
------------

The code we have written so far in this class has either been
{term}`procedural <procedural programming>` or
{term}`object oriented <object oriented programming>`. Today we're going to
learn about another programming paradigm: functional programming.

{term}`Functional programming <functional programming>` is an approach to
programming that focuses computations via {term}`modular`, {term}`stateless`,
{term}`deterministic`, {term}`goal oriented <declarative>` functions.

Procedural code is comprised of statements describing the exact steps to solve
a particular problem and usually involve making modifications to global or
external values along the way. In functional programming on the other hand, you
rely on tools built into the language to decide how to go about solving the
problem, which you provide with functions that describe the desired result.
These tend to be more expression, and ideally return the processed data without
changing the external {term}`state`.

Functional programming is a concise and a powerful tool for data processing.
The results are often less error prone and (once you get the hang of it) more
readable than the procedural equivalent.

In this lesson you'll learn the functional programming features provided by
Python.

Part 1: Mapping
---------------

Generating a new collection by applying the same transformation to every item
in a container is called {term}`mapping <map>`.

### Part 1.1: Procedural

The procedural way to map an iterable is via the old standby, the `for` loop.

{{ leftcol }}

In this example we append to a list `converted` which contains all elements of
the `date` list with `str()` applied.

Appending to `converted` is an example of what is meant when we say that the
shared state has been changed.

{{ rightcol }}

```{code-cell} python
date = ["Wednesday", "Nov", 4, 2021]

converted = []

for elm in date:
    converted.append(str(elm))

print(converted)
```

{{ endcols }}

### Part 1.2: `map()`

Python provides a built in `map()` function which does the same thing in a
single function call.

:::{hint}

`map()` returns a {term}`iterator` object which is displayed as something like
`<map at 0x10f174b80>`. Convert it to a `list` to see the contents.

:::

{{ leftcol }}

`map()` takes two arguments: the function to apply then the iterator.

{{ rightcol }}

```{code-cell} python
date = ["Wednesday", "Nov", 4, 2021]
converted = map(str, date)

list(converted)
```

{{ newrow }}

You can use any {term}`callable`, such as {term}`lambda`...

{{ rightcol }}

```{code-cell} python
days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

list(map(lambda x: x[:3], days))
```

{{ newrow }}

...a user defined function...

{{ rightcol }}

```{code-cell} python
from fractions import Fraction

def to_dec(val):
    num = Fraction(str(val))
    return round(num.numerator / num.denominator, 2)

measurements = ["1/4", "2/5", "5/64"]
list(map(to_dec, measurements))
```

{{ newrow }}

...or a type.

{{ rightcol }}

```{code-cell} python
from pathlib import Path

files = [
    "README.md",
    "pyproject.toml",
    "bin/build",
]

list(map(Path, files))
```

{{ newrow }}

You can even use type methods.

{{ rightcol }}

```{code-cell} python
words = [
   'clarify',
   'whereby',
   'above',
   'strong',
   'able',
]

list(map(str.capitalize, words))
```

{{ endcols }}

### Part 1.2: Exercise

`````{exercise} Map
:label: map-exercise

Write a function `normalize()` that takes one argument `text` and returns a
lowercased version with leading and trailing whitespace removed and spaces
replace with underscores.

Map the following list of `files` list using both a `for` loop and `map()`.

```python
files = [
  "Oxford English Dictionary.txt",
  "ColorFAQ.txt",
  "custom.css",
  "weather.json",
]
```

`````

`````{solution} map-exercise
:class: dropdown

```{code-block} python
:caption: "Map Exercise"
:class: full-width
:linenos:

def normalize(text):
    return text.strip().lower().replace(" ", "_")

files = [
  "Oxford English Dictionary.txt",
  "ColorFAQ.txt",
  "custom.css",
  "weather.json",
]

transformed = []

for x in files:
    transformed.append(normalize(x))

transformed = list(map(normalize, files))

```

`````


### Part 1.3: Multiple Args

For a transformation callable that takes multiple arguments, you can provide
multiple iterables to `map()`.

{{ leftcol }}

One value from each iterable will be passed as an argument each iteration.

{{ rightcol }}

```{code-cell} python
from operator import add

list(map(add, "abc", "123"))
```

{{ endcols }}

### Part 1.3: Exercise

`````{exercise} Mapping Multiple Args
:label: map-multiple-exercise

Using `map()` apply the function `operator.mul` to multiply each of the
following `prices` keys by their exchange rate value.

```python
rates = {
    "USD": 1,
    "EUR": .86,
    "CAD": 1.24,
    "GBP": 0.73,
    "MXN": 20.83,
}

prices = {
  141: rates["EUR"],
  45: rates["USD"],
  47: rates["GBP"],
  155: rates["CAD"]
}
```

`````

`````{solution} map-multiple-exercise
:class: dropdown

```{code-block} python
:caption: "Mapping Multiple Args Exercise"
:class: full-width
:linenos:

from operator import mul

rates = {
    "USD": 1,
    "EUR": .86,
    "CAD": 1.24,
    "GBP": 0.73,
    "MXN": 20.83,
}

prices = {
  141: rates["EUR"],
  45: rates["USD"],
  47: rates["GBP"],
  155: rates["CAD"]
}

list(map(mul, prices.keys(), prices.values()))

```

`````

Part 2: Filter
--------------

Generating a new collection containing only items that match a certain condition
is called {term}`filtering <filter>`.

### Part 2.1: Procedural

{{ leftcol }}

Here is how you would filter the old fashioned way, via a `for` loop.

{{ rightcol }}

```{code-cell} python
numbers = [13, 88, 80, 58, 23, 33, 31, 28]

even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

even
```

{{ endcols }}

### Part 2.2: `filter()`

Python provides a built in `filter()` function.

{{ leftcol }}

`filter()` takes two arguments: a boolean function that serves as the filtering
condition followed by the iterable to filter.

{{ rightcol }}

```{code-cell} python
def is_even(num):
    return num % 2 == 0

numbers = [13, 88, 80, 58, 23, 33, 31, 28]

list(filter(is_even, numbers))
```

{{ newrow }}

As with `map()` you can use any kind of callable as the filtering function.

{{ rightcol }}

```{code-cell} python
animals = ["ox", "Tiger", "rabbit", "Dragon"]

list(filter(str.istitle, animals))
```

{{ newrow }}

Keep in mind, the result is evaluated in a boolean context, meaning that
{term}`falsy` values will be filtered out.

{{ rightcol }}

```{code-cell} python
numbers = [55, 38, 168, 71, 123, 31, 118, 15]

list(filter(lambda x: x//100, numbers))
```

{{ endcols }}

### Part 2.3: Truthy filtering

Often you just want to filter a list for non-empty or {term}`truthy` values.

{{ leftcol }}

If you pass `None` as the first argument to `filter()`, it will return only
{term}`truthy` values. In this example, all blank lines will be filtered out.

{{ rightcol }}

```{code-cell} python
poem = """
"The sun was shining on the sea,
      Shining with all his might:

He did his very best to make
      The billows smooth and bright —

And this was odd, because it was
      The middle of the night.
"""

list(filter(None, poem.splitlines()))
```

{{ endcols }}

Part 3: Reducing
----------------

{term}`Aggregation <aggregation>` operations, or those that apply the same
operation, cumulatively, to each element in a collection to arrive at a single
value is called {term}`reducing <reduce>`.

### Part 3.1: Procedural

{{ leftcol }}

Here's an example of how you would reduce via a `for` loop.

In this example, we add each number in the `numbers` list to the previous total
to arrive at the sum of all numbers in the sequence.

{{ rightcol }}

```{code-cell} python
numbers = [9, 7, 5, 1, 1]

total = 0

for num in numbers:
    total = total + num

print(total)
```

{{ endcols }}

### Part 3.2: `reduce()`

Python provides the `reduce()` function from the `functools` module.

{{ leftcol }}

It takes two arguments: the function to apply followed by the iterable to apply
it to.

In this example, we use the `operator.add` function to calculate the sum of all
`numbers`.

{{ rightcol }}

```{code-cell} python
from functools import reduce
from operator import add

numbers = [9, 7, 5, 1, 1]

total = reduce(add, numbers)

print(total)
```

{{ newrow }}

Any function used in `reduce()` must take two arguments:

* result -- the accumulated value of all previous operations
* current -- the current sequence element

It must return a single value which will be the result value for the next
iteration, or returned by `reduce()` after the last element.

{{ rightcol }}

```{code-cell} python
def func(res, cur):
    """Signature for `reduce()` functions."""
    # calculate value here
    value = ...
    # returned value will be the
    # next iterations res
    return value
```

{{ newrow }}

In this example we re-implement the `add()` function, using the parameter name
`running_total` for the result and `number` for the current element.

{{ rightcol }}

```{code-cell} python
def add(running_total, number):
    value = running_total + number
    return value

total = reduce(add, numbers)

print(total)
```

{{ endcols }}

### Part 3.2: Exercise

`````{exercise} Reduce
:label: reduce-exercise

Make a list assigned to the variable `letters` with all the letters in the
[word of the day](https://www.dictionary.com/e/word-of-the-day/).

Concatonate all letters using both a `for` loop and the `functools.reduce()`
function.

`````

`````{solution} reduce-exercise
:class: dropdown

```{code-block} python
:caption: "Reduce Exercise"
:class: full-width
:linenos:

from operator import add
from functools import reduce

letters = ['g', 'r', 'i', 's', 'l', 'y']

word = ""

for letter in letters:
    word += letter

print(word)

word = reduce(add, letters)

print(word)
```

`````

### Part 3.3: Initial value

`reduce()` determines the initial value of `res` by calling the type of the
first element of the iterable. For example, if your iterable is `[1, 2, 3]`,
the initial value of `res` will be `int()` or `0`.

If you need a different initial value, you can pass it as the optional third
argument.

{{ leftcol }}

In this example we are converting a tuple of integers into strings then
concatenating them.

`reduce()` would choose `0` as the initial value, but we can override that by
passing an empty string (`""`) as the third argument.

{{ rightcol }}

```{code-cell} python
numbers = [1, 2, 3]

reduce(
    lambda res, cur: res + str(cur),
    numbers,
    ""
)
```

{{ newrow }}

Here is a more complicated example that removes all punctuation characters from
a string by iterating over a string containing the punctuation characters, and
using the string to strip as the initial value.

{{ rightcol }}

```{code-cell} python
import string
from functools import reduce

filename = "hello_world.py"

reduce(
    lambda text, char: text.replace(char, ""),
    string.punctuation,
    filename
)
```

{{ endcols }}

### Part 3.3: Exercise

`````{exercise} Initializer
:label: reduce-initializer-exercise

Use `reduce()` to count the number of vowels in a string.

`````

`````{solution} reduce-initializer-exercise
:class: dropdown

```{code-block} python
:caption: "Initializer Exercise"
:class: full-width
:linenos:

def addifvowel(total, char):
   if char.lower() in "aeiou":
       return total + 1
   else:
       return total


text = "Einstein"
reduce(addifvowel, text, 0)

```

`````

Challenges
----------

This section contains a series of more challenging exercises using `map()`,
`filter()` or `range()`.

### Fibonacci sequence

`````{exercise} Fibonacci
:label: fibonacci-exercise

Use `reduce()` to generate a list containing the first `10` numbers of the
[fibonacci sequence][] in which each successive number is the result of adding
the preceeding two.

**Example output**

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

`````

`````{solution} fibonacci-exercise
:class: dropdown

```{code-block} python
:caption: "Fibonacci Exercise"
:class: full-width
reduce(lambda seq, _: seq + [sum(seq[-2:])], range(10), [0, 1])

```

`````

[fibonacci sequence]: https://en.wikipedia.org/wiki/Fibonacci_number

### RGB to Hex Color Code

`````{exercise} RGB to Hex
:label: rgb-to-hex-exercise

Use `reduce()` to convert a iterable of three RGB color values from `0-255` to
a six character string containing the equivalant hex color code.
([More info][color-info].)

*Note: The solution is not a mathmatical equation.*

```{dropdown} Need a hint?
Use [string formatting][] to convert each number to its hex equivalant.
```

**Example**

{{ leftcol }}

```{rubric} Given
```

```python
RGB = (34, 34, 171)
```

{{ rightcol }}

```{rubric} Output
```

```python
'2222AB'
```

{{ endcols }}

`````

`````{solution} rgb-to-hex-exercise
:class: dropdown

```{code-block} python
:caption: "RGB to Hex Exercise"
:class: full-width
:linenos:

yellow = (255, 255, 0)

reduce(lambda hex, val: hex + f"{val:02x}", yellow, "")

```

`````

[string formatting]: https://alissa-huskey.github.io/python-class/lessons/string-formatting-part-1.html#presentations

### Hex to RGB Color Values

`````{exercise} Hex to RGB
:label: hex-to-rgb-exercise

Use `reduce()` to convert a six character hex color code to list of the
equivalant [RGB color values][] from `0-255`. ([More info][color-info].)

*Note: The solution is not a mathmatical equation.*

```{dropdown} Need a hint?
* Use the range() function and a slice to exract each two digit hex number from
  the six digit string.
* You can convert a hex number to a base `10` integer (the normal kind) using
  the `int()` {term}`constructor` by including the optional second argument.
```

**Example**

{{ leftcol }}

```{rubric} Given
```

```python
hex_code = "00ffff"
```

{{ rightcol }}

```{rubric} Output
```

```python
(0, 255, 255)
```

{{ endcols }}

`````

`````{solution} hex-to-rgb-exercise
:class: dropdown

```{code-block} python
:caption: "Hex to RGB Exercise"
:class: full-width
:linenos:

def to_rgb(hex_code, i):
    code = hex_code[i*2:i*2+2]
    return int(code, base=16)

reduce(lambda rgb, i: rgb + [to_rgb("ffff00", i)], range(3), [])

```

`````

[color-info]: https://mathstats.uncg.edu/sites/pauli/112/HTML/seccolors.html
[RGB color values]: https://en.wikipedia.org/wiki/RGB_color_model

### Get values for multiple keys

`````{exercise} Multiple Dictionary Keys
:label: reduce-dict-keys-exercise

Given a dictionary mapping `letters` to their unicode codepoint, use `reduce()`
go return a list containing the values for an iterable of `keys`.

**Example**

{{ leftcol }}

```{rubric} Given
```

```python
letters = {
  'a': 97,
  'b': 98,
  'c': 99,
  'd': 100,
  'e': 101,
 }

 keys = ['c', 'a', 't']
```

{{ rightcol }}

```{rubric} Output
```

```python
[99, 97, None]
```

{{ endcols }}

`````

`````{solution} reduce-dict-keys-exercise
:class: dropdown

```{code-block} python
:caption: "Multiple Dictionary Keys Exercise"
:class: full-width
:linenos:

letters = {
  'a': 97,
  'b': 98,
  'c': 99,
  'd': 100,
  'e': 101,
}

keys = ['c', 'a', 't']

reduce(lambda values, key: values + [alpha.get(key)], "aeiou", [])

```

`````


Reference
---------

### Glossary

```{glossary} functional-programming

callable
  Any object that can be called such as a function, method, or type.

map
  A functional programming function that applies a function to every element of
  an iterable and returns a collection of results.

  See also: [map](https://en.wikipedia.org/wiki/Map_(higher-order_function)).


filter
  A functional programming function that applies a predicate function to every
  element of an iterable and returns a collection that contains the elements for
  which the predicate evaluated to `True`.

  See also: [filter](https://en.wikipedia.org/wiki/Filter_(higher-order_function)).


reduce
  A functional programming function that applies a function to an every element
  of an iterable and returns a single cumulative value.

  See also: [reduce](https://en.wikipedia.org/wiki/Fold_(higher-order_function)).


predicate
  A function that returns a boolean value of some condition.

  See also: [predicate](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic)).


aggregation
  Grouping together multiple values to calculate a single summary value.


procedural programming
  Code comprised of a list of instructions to tell the computer what to do step
  by step. Code is organized into functions (proceedures).

  See also: [procedural programming](https://en.wikipedia.org/wiki/Procedural_programming).


object oriented programming
  An approach to programing focused on encapsulating data and behavior into
  objects. Code is organized into classes, objects and methods.

  See also: [object oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming).


functional programming
  An approach to programming that focuses computations via modular, isolated,
  deterministic, goal oriented functions.

  See also: [functional programming](https://en.wikipedia.org/wiki/Functional_programming).


deterministic
  When an algorithm, given particular input, will always produce the same
  output regardless of any external factors. In contrast to
  {term}`nondeterministic`.

  See also: [deterministic](https://en.wikipedia.org/wiki/Deterministic_algorithm).


nondeterministic
  When an algorithm may exhibit different behavior for the same input. In
  contrast to {term}`deterministic`.

  See also: [nondeterministic](https://en.wikipedia.org/wiki/Nondeterministic_algorithm).


modular
  A software design technique that emphasizes separating the functionality of a
  program into independent, interchangeable modules, such that each contains
  everything necessary to execute only one aspect of the desired functionality.

  See also: [modular](https://en.wikipedia.org/wiki/Modular_programming).


imperative
imperative programming
  An approach to programming that involves describing the exact steps the
  program should take via a series of statements that make updates to the
  shared state. In contrast to {term}`declarative programming`.

  See also: [imperative programming](https://en.wikipedia.org/wiki/Imperative_programming).


declarative
declarative programming
  An approach to programming that involves describing what the program should
  do via expressions and tools built into the language rather than describing
  how to do it via a series of statements. In contrast to
  {term}`imperative programming`.

  See also: [declarative programming](https://en.wikipedia.org/wiki/Declarative_programming).


state
  The information retained throughout a programs runtime--for example the data
  stored in variables or loaded in from a file.

  See also: [state](https://en.wikipedia.org/wiki/State_(computer_science)).


statefulness
stateful
  A term describing software, a software component (like a function), or a
  protocol that references information from previous operations and/or makes
  changes to the information available for future operations.
  In contrast to {term}`statelessness`.


statelessness
stateless
  A term describing software, a software component (like a function), or a
  protocol that does not reference information from previous operations nor
  have any [side effects][] such as saving state for future
  operations. Instead each operation starts from scratch based only on the
  input and the only thing effected is the returned output.
  In contrast to {term}`statefulness`.

```

[side effects]: https://en.wikipedia.org/wiki/Side_effect_(computer_science)

### See Also

```{seealso}

* [python.org > Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
* [Functional Programming in Python](https://realpython.com/python-functional-programming/)
* [python.org > Built-in Functions > map()](https://docs.python.org/3/library/functions.html#map)
* [python.org > Built-in Functions > filter()](https://docs.python.org/3/library/functions.html#filter)
* [python.org > Built-in Functions > reduce()](https://docs.python.org/3/library/functools.html?highlight=reduce#functools.reduce)
* [Python's map(): Processing Iterables Without a Loop](https://realpython.com/python-map-function/)
* [Understanding The Python Reduce Function With Examples](https://melvinkoh.me/understanding-the-python-reduce-function-with-examples-ck7mzz8l200na8ss1ogdvw5c5?guid=none&deviceId=fb7e31e2-51ab-45db-a5d8-d71705d2ec8c)

```

### Summary

* `map()` is used to transform elements
* `filter()` is used to select elements
* `reduce()` is used for aggregation

% TODO
% - x if c else y
% - c and x or y
