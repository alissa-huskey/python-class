---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'
  row: '{{ newrow | replace("col", "col-5") }}'
  label: '<div class="text-right">Syntax:</div>'

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
Syntax
======

In this section we'll learn the basic Python syntax.

```{contents} Table of Contents
:backlinks: top
:local:
```

Introduction
------------

Syntax is set of grammar and punctuation rules that define how to put words and
symbols together to properly form a particular language.

In the English language for example, we know a sentence is made up of a subject
and predicate, that the first letter should be capitalized, and that
it should end in a period, question mark, or exclamation point.

Python is a programming language, intended to read by a computer. In order to
write code that the computer can understand, we need to understand the syntax.

Structure
---------

A program is made up of a series of instructions which are read and executed in
order from top to bottom.

To get a better idea of what is involved, lets consider the following simple
example:

```{code-cell} python
:class: full-width
:linenos:
"""My first program"""

import time

width = 80
today = time.localtime()

greeting = "Hello"

if today.tm_hour < 11:
  greeting = "Good morning"  # before 12pm

# put together the message and make it centered
message = (greeting + " world!").center(width)

print(message)
```

### Docstrings

{{ left }}

When the first line of a program or function is enclosed in triple single
(`'''`) or triple double (`"""`) quotes, it is a special kind of string
intended for documentation called a {term}`docstring`.

{{ right }}

```{code-block} python
:class: full-width
:emphasize-lines: "1"
:linenos:

"""My first program"""
```

{{ endcols }}

### Comments

{{ left }}

You can leave notes for future reference starting with a `#`. This tells
Python to ignore everything that follows until the end of the line.

{{ right }}

```{literalinclude} ../templates/examples/syntax.py
:class: full-width
:emphasize-lines: 1
:lines: "14-15"
:linenos:
```

{{ row }}

A comment doesn't have to be at the start of the line.

{{ right }}

```{code-block-hl} python
:linenos:
:class: full-width
:lineno-start: 11

if today.tm_hour < 11:
  greeting = "Good morning"  !!!# before 12pm!!!
```

{{ endcols }}

### Keywords

{{ left }}

Keywords are reserved words that have a special meaning in Python. A keyword
cannot be used as a function or variable.

{{ right }}

```{code-block-hl} python
:class: full-width
:linenos:

!!!import !!!time
!!!import !!!shutil
```

```{code-block-hl} python
:class: full-width
:lineno-start: 11

!!!if!!! today.tm_hour < 11:
```

{{ row }}

A list of all keywords is available in the `keyword` module `kwlist`.

{{ right }}


:::{dropdown} Show Keywords
:title: +text-center
:container: +keywords-list

```{include} keywords.md
```

:::

{{ endcols }}

### Statements

{{ left }}

Code is made up of a series of instructions to the computer called
{term}`statements <statement>`.

{{ right }}

`````{dropdown} **...**
:title: +text-center

```{code-block-hl} python
:linenos:
:emphasize-lines: "3-10, 14-16"
:caption: all statements

"""My first program"""

import time

width = 80
today = time.localtime()

greeting = "Hello"

if today.tm_hour < 11:
  !!!greeting = "Good morning"!!!  # before 12pm

# put together the message and make it centered
message = (greeting + " world!").center(width)

print(message)
```

`````

{{ row }}

The {term}`simple <simple statement>` form is a single line of code, kind of
like a sentence that says what to do.

{{ right }}

```{code-block-hl} python
:linenos:
:class: full-width
:emphasize-lines: "3"
:caption: a simple statement

"""My first program"""

import time
```

`````{dropdown} See more
:title: +text-center

```{code-block-hl} python
:linenos:
:emphasize-lines: "1-4, 10-12"
:caption: all simple statements
:lineno-start: 4

width = 80
today = time.localtime()

greeting = "Hello"

if today.tm_hour < 11:
  !!!greeting = "Good morning"!!!  # before 12pm

# put together the message and make it centered
message = (greeting + " world!").center(width)

print(message)
```

`````

<br>

{{ row }}

Various kinds of {term}`compound statements <compound statement>` are used to
group together and control part of a program.

{{ label }}


{{ right }}

```{include} ../templates/syntax/compound-statement.md
```

```{include} ../templates/desc/compound-statement.md
```

{{ row }}

While the full {term}`header` syntax depends on the statement, they all begin
with a keyword and end with a colon (`:`).

{{ right }}

```{code-block-hl} python
:class: full-width
:lineno-start: 11
:caption: header line

!!!if!!! today.tm_hour < 11!!!:!!!
  greeting = "Good morning "  # before 12pm
```

<br>

{{ row }}

Its {term}`body` of statements are indented under the header.

{{ right }}

```{code-block-hl} python
:class: full-width
:lineno-start: 11
:caption: indented body line

if today.tm_hour < 11:
!!!  !!!greeting = "Good morning"  # before 12pm
```

<br>

{{ endcols }}

### Expressions

{{ left }}

A statement may contain one or more {term}`expressions <expression>`, which is
any piece of code that resolves to a value.

{{ right }}

```{code-block-hl} python
:class: full-width
:linenos:
:lineno-start: 9

greeting = !!!"Hello"!!!
```

:::{dropdown} See more
:title: +text-center

```{code-block-hl} python
:class: full-width
:linenos:
:caption: all expressions

!!!"""My first program"""!!!

import time
import shutil

width = !!!80!!!
today = !!!time.localtime()!!!

greeting = !!!"Hello"!!!

if !!!today.tm_hour < 11!!!:
  greeting = !!!"Good morning"!!!  # before 12pm

# put together the message and make it centered
message = !!!(greeting + "world!").center(width)!!!

print(!!!message!!!)
```

:::

<br>

{{ row }}

Parentheses can be used around part of an expression to control order of
operation or grouping.

{{ right }}

```{code-block-hl} python
:class: full-width
:linenos:
:lineno-start: 15

message = !!!(greeting + "world!")!!!.center(width)
```

<br>

{{ endcols }}

Values
------

Every value has a type and each type has its own syntax. Let's take a look at
the following example with a summary of the simple types and how variables are
saved.

```{code-cell} python
greeting = "Hello." # string         (str)
health = 100        # integer        (int)
delay = 0.1         # floating point (float)
verbose = True      # boolean        (bool)
winner = None       # NoneType

# list (list)
letters = ["a", "b", "c", "d", "e", "f"]

# dictionary (dict)
numbers = {
  "I": 1,
  "II": 2,
  "III": 3,
  "IV": 4,
  "V": 5,
}

print(greeting)
```

### Variables

{{ left }}

Save a value to be easily used later in the code by giving it a name.  To
create a variable simply {term}`assign` a value to it it using the equals sign
(`=`).

Syntax: {samp}`{NAME} = {VALUE}`

{{ right }}

```{code-block-hl} python
:linenos:

!!!greeting = "Hello."!!! # string         (str)
!!!health = 100!!!        # integer        (int)
!!!delay = 0.1!!!         # floating point (float)
!!!verbose = True!!!      # boolean        (bool)
!!!winner = None!!!       # NoneType
```

{{ row }}

To {term}`reference` a variable, or retrieve the data you stored, use the variable name.

{{ right }}

```{code-block-hl} python
:lineno-start: 7

print(!!!greeting!!!)
```

{{ row }}

Assign multiple variables at once by putting the same number of variables on
the left of the equals sign as values on the right, separated by commas.

Syntax: \
{samp}`NAME1, NAME2... = VAL1, VAL2...`

{{ right }}

```{code-block} python
red, green, blue = 0, 255, 125
```

{{ row }}

Or the same number of variables on the left of the equals sign as elements in a
sequence such as a list.

Syntax: {samp}`NAME1, NAME2... = SEQUENCE`

{{ right }}

```{code-block} python
x, y = [-10, 10]
```

{{ endcols }}

### Bracket notation

Many {term}`container` types (like lists and dictionaries) support the use of
{term}`subscription` or {term}`bracket notation` to select elements from the
collection. Add square brackets (`[` `]`) after a value enclosing a selector
expression.

Syntax: {samp}`{VALUE}[{EXPRESSION}]`

{{ left }}

Depending on the type, a selector expression may be a negative or positive {term}`index number`...

{{ right }}

```{code-block-hl} python
letters!!![0]!!!
letters!!![-1]!!!
```

{{ row }}

... a {term}`key`...

{{ right }}

```{code-block-hl} python
numbers!!!["IV"]!!!
```

{{ row }}

...or a {term}`slice`.

{{ right }}

```{code-block-hl} python
letters!!![2:4]!!!
```

{{ row }}

As with any expression, variables can be used in selector expressions.

{{ right }}

```{code-block-hl} python
idx = 2
letters!!![idx]!!!
letters!!![idx:]!!!
```

{{ row }}

Bracket notation is most often used on a variable, but in fact it can be used
on any expression that results in a type that supports it.

{{ right }}

```{code-block-hl} python
"hello"!!![2]!!!
list("abc")!!![-1]!!!
{"a": 1}!!!["a"]!!!
```

{{ endcols }}

### Dot notation

{{ left }}

Use {term}`dot notation` to access {term}`members` of a given value by adding a
period (`.`) after a value followed by the member name.

Syntax: {samp}`{VALUE}.{MEMBER}`

{{ right }}

```{code-block-hl} python
letters!!!.sort!!!()
```

{{ row }}

While dot notation is most often used on a variable, it can actually be used on
any expression.

{{ right }}

```{code-block-hl} python
"hello"!!!.upper!!!()
```

{{ row }}

This means it is possible to {term}`chain` or string together multiple
attribute references, as long as each concecutive member returns a value.

{{ right }}

```{code-block-hl} python
name = input("Full Name: ")!!!.title!!!()!!!.strip!!!()
```

{{ endcols }}

### Calls

{{ left }}

Call a function by adding a set of parenthesis after the name.

Syntax: {samp}`{NAME}()`

{{ right }}

```{code-cell} python
:class: full-width

print()
```

{{ row }}

Put arguments inside the parenthesis.

Syntax: {samp}`{NAME}({ARG})`

{{ right }}

```{code-cell} python
:class: full-width

print("Welcome!")
```

{{ row }}

Separate multiple {term}`arguments <argument>` with commas.

Syntax: {samp}`{NAME}({ARG1}, {ARG2}...)`

{{ right }}

```{code-cell} python
:class: full-width

name = "Mario"
print("Welcome", name)
```

{{ endcols }}

Types
-----

Lets take a closer look at the standard built in types.

`````{list-table}
:widths: 15, 10, 35, 35
:header-rows: 1

* - Name
  - Type
  - Description
  - Examples

* - <label>None</label>
  -
  - A single value `None` with the first letter capitalized. Used to indicate
    that the value has not been set.
  - ```python
    None
    ```

* - <label>Boolean</label>
  - `bool`
  - Either `True` or `False` with the first letter capitalized.
  - ```python
    True
    False
    ```

* - <label>Integer</label>
  - `int`
  - Whole numbers.
  - ```python
    10
    0
    -55
    ```

* - <label>Floating point</label>
  - `float`
  - Numbers with a decimal point.
  - ```python
    .1
    1.5
    -0.25
    ```

* - <label>String</label>
  - `str`
  - Text data enclosed in either single or double quotes.
  - ```python
    "Hello"
    'Goodbye'
    ```

* - <label>List</label>
  - `list`
  - An ordered collection of arbitrary objects seperated by commas and enclosed in square brackets (`[` `]`).
  - ```python
    []
    [1, 2, 3]
    ```

* - <label>Dictionary</label>
  - `dict`
  - A collection of {samp}`{key}: {value}` pairs seperated by commas and enclosed in curly braces (`{` `}`).
  - ```python
    {}
    {"a": 1, "b": 2, "c": 3}
    ```

* - <label>Tuple</label>
  - `tuple`
  - An ordered, immutable collection of arbitrary objects seperated by commas and enclosed in parenthesis (`(` `)`)
  - ```python
    ()
    (1,)
    (1, 2, 3)
    1, 2, 3
    ```

* - <label>Set</label>
  - `set`
  - An unordered collection of unique elements seperated by commas and enclosed in curly braces (`{` `}`).
  - ```python
    set()
    {1, 2, 3}
    ```
`````

### Strings

{{ left }}

Strings store text data and can be enclosed in either single or double quotes.

{{ right }}

```{code-cell}
""
"Hello."
'Farewell.'
"It's a lovely day."
'"Well hello!", he said.'
```

{{ row }}

For a string that spans multiple lines, enclose it in triple double (`"""`) or
triple single (`'''`) quotes.

{{ right }}

```{code-cell}
rhyme = """Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""

print(rhyme)
```

{{ row }}

To break long text into multiple lines of code, put strings on consecutive
lines (without separating commas) and enclose the whole expression in
parentheses `(` `)`.

{{ right }}

```{code-cell}
text = (
  "Lorem ipsum dolor sit amet, consectetur "
  "adipiscing elit, sed do eiusmod tempor "
  "incididunt ut labore et dolore magna "
  "aliqua. Ut enim ad minim veniam, quis "
  "nostrud exercitation ullamco laboris "
  "nisi ut aliquip ex ea commodo consequat."
)

print(text)
```

{{ row }}

Backslashes (`\`) are used to escape quotes or to indicate special characters,
like `\n` for a new line.

{{ right }}

```{code-cell} python
print('It\'s a nice day.')
print("line one\nline two")
```

{{ row }}

For strings that contain backslashes use a double backslash (`\\`) or prefix
the string with the letter `r` for a raw string.

{{ right }}

```{code-cell} python
print('"\\n" is used to add a newline')
print(r"C:\Documents\nodes")
```

{{ row }}

Strings can be {term}`concatenated <concatenate>` (joined together) by using
the `+` operator.

String literals (the ones in quotes) next to each other are automatically
concatenated.

{{ right }}

```{code-cell} python
name = "coding class"
print("Welcome to " + name + ".")

text = "Today we're talking about" 'strings.'
print(text)
```

{{ row }}

Use an f-string for string {term}`interpolation` by prefixing the string with the
letter `f` then enclose the variable or other evaluated code curly braces (`{` `}`).

{{ right }}

```{code-cell} python
price = 1.25
count = 5

print(f"I am buying {count} apples for ${price} each.")
print(f"The total is ${price*count}.")
```

{{ endcols }}

### Lists

A list is an ordered collection of arbitrary objects.

{{ left }}

To create one, enclose comma-separated values in square brackets \
(`[` `]`), or an empty pair of square brackets for an empty list.

{{ right }}

```{code-cell} python
[]
[1, 2, 3]
```

{{ row }}

Long lists can be split onto multiple lines after the commas.

{{ right }}

```{code-cell} python
:tabs: [thebe-init]
rainbow = [
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "indigo",
  "purple",
]
```

{{ row }}

List elements are primarily accessed, changed, or removed using
{term}`subscription` via either index numbers or slices.

{{ right }}

```{code-cell} python
:tabs: [thebe-init]

# changing
rainbow[-1] = "violet"

# removing
del rainbow[-2]

# accessing
print(rainbow[0])
print(rainbow[-1])
print(rainbow[0:3])
```

{{ endcols }}

### Dictionaries

A dictionary is a collection of key value pairs.

{{ left }}

To create one, enclose comma-separated key value pairs in curly braces (`{` `}`) with
a colon (`:`) between each key and value. Or use an empty pair of curly brackets
to make an empty dictionary.

{{ right }}

```{code-cell} python
:tags: [thebe-init]

pet = {}

garfield = {"name": "garfield", "kind": "cat", "color": "orange"}
```

{{ row }}

Long dictionaries can be split onto multiple lines after the commas.

{{ right }}

```{code-cell} python
:tags: [thebe-init]

toothless = {
  "name": "Toothless",
  "kind": "dragon",
  "color": "black",
  "pic": "/|\\{O_O}/|\\",
  "age": 24,
}
```

{{ row }}

List elements are primarily accessed, added, changed, or removed using
{term}`subscription` via keys.

{{ right }}

```{code-cell} python

# changing
garfield["name"] = "Garfield"

# adding
garfield["pic"] = "(=^o.o^=)__"

# removing
del toothless["age"]

# accessing
print(toothless["name"], ":", toothless["pic"])
print(garfield["name"], ":", garfield["pic"])
```

{{ endcols }}

### Tuples

A tuple is an immutable collection of arbitrary objects.

{{ left }}

To create one, enclose comma-separated values in parenthesis \
(`(` `)`), or an empty pair of parenthesis for an empty tuple.

{{ right }}

```{code-cell} python
:tabs: [thebe-init]
()
(1, 2, 3)
```

{{ row }}

A tuple can also be created using comma separated values without the
parenthesis.

{{ right }}

```{code-cell} python
:tabs: [thebe-init]
1, 2, 3
```

{{ row }}

Though parenthesis are required when splitting tuples onto multiple lines.

{{ right }}

```{code-cell} python
words = (
  "target",
  "specify",
  "incline",
  "college",
  "forget",
  "recent",
)
```

{{ row }}

Creating a tuple with only one item is a bit tricky, since parenthesis are
used for both expression grouping and tuples.

Use a trailing comma to create a tuple with one item.

{{ right }}

```{code-cell} python
# parens are interpreted as grouping
# so this is an int instead of a tuple
(1)
```

```{code-cell} python
# use a trailing comma to create a tuple
# with one item
nums = (1,)
print(nums)

# with or without the parenthesis
nums = 1,
print(nums)
```

{{ row }}

Tuple elements are accessed using {term}`subscription` via index numbers or
slices.

{{ right }}

```{code-cell} python

print(words[0])
print(words[-1])
print(words[0:3])
```

{{ endcols }}

Tuples are immutable, so items cannot be modified or removed.

### Sets

A set is an unordered collection with no duplicate elements.

{{ left }}

To create one, enclose comma-separated values in curly braces \
(`{` `}`).

{{ right }}

```{code-cell} python
{1, 2, 3, 3, 2, 1}
```

{{ row }}

Since curly braces are also used for dictionaries, use `set()` to create an
empty set.

{{ right }}

```{code-cell} python
set()
```

{{ endcols }}

Sets are unordered, so {term}`subscription` is not supported.

Flow Control
------------

### if statements

{term}`If statements <if statement>` are used to only execute code under
certain conditions.

{{ left }}

If statements always start with an `if` {term}`clause`.

{{ label }}

{{ right }}

```{include} ../templates/syntax/if.md
```

```{include} ../templates/desc/if.md
```

<br>

{{ row }}

In this example, `"Would you like a beer?"` will only be printed if `age >= 21`.

{{ right }}

```{literalinclude} ../templates/examples/if.py
:class: full-width
:linenos:
:emphasize-lines: "5-6"
```

<br>

{{ row }}

An if statement may contain zero or more `elif` clauses.

{{ label }}

{{ right }}

```{include} ../templates/syntax/elif.md
```

```{include} ../templates/desc/elif.md
```

<br>

{{ row }}

This example contains two `elif` clauses.

{{ right }}

```{literalinclude} ../templates/examples/if.py
:class: full-width
:linenos:
:emphasize-lines: "7-10"
```

<br>

{{ row }}

And an if statement may optionally end with an `else` clause. These body
statements will be executed if none of the previous conditions are met.

{{ label }}

{{ right }}

```{include} ../templates/syntax/else.md
```

```{include} ../templates/desc/else.md
```

<br>

{{ row }}

In this example, `"Hello."` is printed if all preceding conditions evaluated to
`False`.

{{ right }}

```{literalinclude} ../templates/examples/if.py
:class: full-width
:linenos:
:emphasize-lines: "11-12"
```

{{ endcols }}


### for loops


{{ left }}

For loops are used to iterate over every element in a sequence and repeat a
block of code each time.

{{ label }}

{{ right }}

```{include} ../templates/syntax/for.md
```

```{include} ../templates/desc/for.md
```

{{ row }}

{{ right }}

```{literalinclude} ../templates/examples/for.py
:linenos:
```

{{ endcols }}

### while loops

{{ left }}

A `while` loop is used to repeat a block of code as long as an
expression evaluates to `True`.

{{ label }}

{{ right }}

```{include} ../templates/syntax/while.md
```

```{include} ../templates/desc/while.md
```

<br>

{{ row }}

{{ right }}

```{literalinclude} ../templates/examples/while.py
:linenos:
```

{{ endcols }}

### Functions

{{ left }}

A {term}`function` is a set of Python instructions or statements that can be
executed, or called, later.

{{ label }}

{{ right }}

```{include} ../templates/syntax/def.md
```

```{include} ../templates/desc/def.md
```

<br>

{{ row }}

{{ right }}

```{literalinclude} ../templates/examples/def.py
:linenos:
```

{{ endcols }}

Reference
---------

### Glossary

```{glossary} syntax

chaining
method chaining
  Stringing together multiple {term}`dot notation` attribute references.

comment
  Parts in a source-code file which are ignored when the program is run. In
  Python add a `#` to the beginning a line to indicate that it is a comment.
  You can also comment out only part of a line by adding `#` followed by the
  comment text to the end of an expression. It is recommended to follow the `#`
  by a single space before the text of the comment.

keyword
  Reserved words that have special meanings in a programming language so that
  they cannot be used as an identifier. Some examples of keywords in Python are
  `for`, `if`, and `def`.

syntax
  A set of rules that determine how a programming language is understood by the
  computer. Grammar, but for code.

assign
  A {term}`statement` that sets the {term}`value` of a variable name.

identifier
  The name that refers to a some programming element, such as a variable,
  class, function or module.

variable
  A name given to a value.

```

### See also

:::{seealso}

* [Learn X in Y Minutes: Python](https://learnxinyminutes.com/docs/python/)
* [A Quick Tour of Python Language Syntax](https://jakevdp.github.io/WhirlwindTourOfPython/02-basic-python-syntax.html)
* [Python Programming Reference Sheet](https://pythonprinciples.com/reference/)

:::


----

% TODO
% [x] docstrings
% [x] comments
% [x] parens for grouping, order of operation
% [ ] line splitting
% [x] subscription
% [ ] dot notation
% [ ] case sensitive
% [ ] operators
% [ ] delimiters
% [x] types
%     [x] list
%     [.] dict
%     [x] str
%     [x] None
%     [x] set
%     [x] tuple
% [x] flow control
%     [x] if
%     [x] while
%     [x] for
%     [x] functions
% [ ] confusing
%     [ ] nested function calls
%     [ ] subscription and dot notation on values
%     [ ] expressions inside functions
% [ ] gotchas
%     [ ] parenthesis: tuples, precedence, functions
%     [ ] sets and dicts use `{}`
%     [ ] `x + 1` vs `x = x + 1`
%     [ ] `if function`
%     [ ] missing commas from list means concatonation
%
% [x] keywords

% https://www.101computing.net/wp/wp-content/uploads/Python-Cheat-Sheet.pdf
% https://ddi.ifi.lmu.de/probestudium/2013/ws-i-3d-programmierung/tutorials/python-referenzkarte
% https://www.codecademy.com/learn/introduction-to-python-dvp/modules/python-syntax-dvp/cheatsheet
% https://pythonprinciples.com/reference/
% https://programmingwithmosh.com/python/python-3-cheat-sheet/
