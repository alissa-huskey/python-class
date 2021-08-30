---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'
  row: '{{ newrow | replace("col", "col-5") }}'

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

# My first Python program
print("Hello world!")
```

### Comments

{{ left }}

You can leave notes for your own reference starting with a `#`. This tells
Python to ignore everything that follows until the end of the line.

{{ right }}

```{code-block-hl} python
:linenos:
:class: full-width thebe-align
:emphasize-lines: "1"

# My first Python program
print("Hello world!")
```

{{ endcols }}

### Statements

{{ left }}

A statement is an instruction that Python can execute as a unit, analagous to a
sentence.  In its simplest form it's is a line of code that does something.

{{ right }}

```{code-block} python
:linenos:
:class: full-width thebe-align
:emphasize-lines: "2"

# My first Python program
print("Hello world!")
```

{{ endcols }}

### Expressions

{{ left }}

A statement may contain one or more expressions. An expression is any piece
of code that produces a value.

{{ right }}

```{code-block-hl} python
:class: full-width thebe-align
:linenos:

# My first Python program
print(!!!"Hello world!"!!!)
```

{{ endcols }}

{{ left }}

Parentheses can be used around part of an expression to change order of
operation.

{{ right }}

```{code-cell} python
:class: full-width
:linenos:

2 * 3 + 4
```

```{code-cell} python
:class: full-width
:linenos:

2 * (3 + 4)
```

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
the left of the equals sign as values on the right, seperated by commas.

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

### Types

Lets take a closer look at the standard built in types.

`````{list-table}
:widths: 15, 10, 35, 35
:header-rows: 1

* - Name
  - Type
  - Description
  - Examples

* - <label>Strings</label>
  - `str`
  - Text data enclosed in either single or double quotes.
  - ```python
    "Hello"
    'Goodbye'
    ```

* - <label>Integers</label>
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

* - <label>Boolean</label>
  - `bool`
  - Either `True` or `False` with the first letter capitalized.
  - ```python
    True
    False
    ```

* - <label>None</label>
  -
  - A single value `None` with the first letter capitalized. Used to indicate
    that the value has not been set.
  - ```python
    None
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

For a string that spans multiple lines, enclose it in tripple double (`"""`) or
tripple single (`'''`) quotes.

{{ right }}

```{code-cell}
rhyme = """Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""

print(rhyme)
```

{{ row }}

To break long text into multiple lines of code, put strings on concecutive
lines (without seperating commas) and enclose the whole expression in
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

Strings can be concatenated (joined together) by using the `+` operator.

String literals (i.e. the ones in quotes) next to each other are automatically
concatonated.

{{ right }}

```{code-cell} python
name = "coding class"
print("Welcome to " + name + ".")

text = "Today we're talking about" 'strings.'
print(text)
```

{{ row }}

Use an f-string for string interpoliation by prefixing the string with the
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

To create one, enclose comma-seperated values in square brackets \
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

To create one, enclose comma-seperated key value pairs in curly braces (`{` `}`) with
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

To create one, enclose comma-seperated values in parenthesis \
(`(` `)`), or an empty pair of parenthesis for an empty tuple.

{{ right }}

```{code-cell} python
:tabs: [thebe-init]
()
(1, 2, 3)
```

{{ row }}

A tuple can also be created using comma seperated values without the
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

To create one, enclose comma-seperated values in curly braces \
(`{` `}`).

{{ right }}

```{code-cell} python
{1, 2, 3, 3, 2, 1}
```

{{ row }}

Since curley braces are also used for dictionaries, use `set()` to create an
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

If statements always start with an `if` clause. The syntax is:

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

An if statement may contain zero or more `elif` clauses. The syntax is:

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

And an if statement may optionally end with an `else` clause. The syntax is:

{{ right }}

```{include} ../templates/syntax/else.md
```

```{include} ../templates/desc/else.md
```

<br>

{{ row }}

In this example, `"Hello."` is printed if all preceeding conditions evaluated to
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

{{ endcols}}

### Functions

A {term}`function` is a set of Python instructions or statements that can be
executed, or called, later.

{{ left }}

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

### Calls

{{ left }}

Call a function by adding a set of parenthesis after the name. \
Syntax: {samp}`{NAME}()`

{{ right }}

```{code-cell} python
:class: full-width

print()
```

{{ row }}

Put arguments inside the parenthesis. \
Syntax: {samp}`{NAME}({ARG})`

{{ right }}

```{code-cell} python
:class: full-width

print("Welcome!")
```

{{ row }}

Seperate multiple arguments with commas. \
Syntax: {samp}`{NAME}({ARG1}, {ARG2}...)`

{{ right }}

```{code-cell} python
:class: full-width

name = "Mario"
print("Welcome", name)
```

{{ endcols }}

Reference
---------

### Glossary

```{glossary} syntax

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
% [ ] docstrings
% [x] comments
% [x] parens for grouping, order of operation
% [ ] line splitting
% [.] types
%     [x] list
%     [.] dict
%     [x] str
%     [x] None
%     [ ] set
%     [ ] tuple
% [ ] flow control
%     [ ] if
%     [ ] while
%     [ ] for
%         [ ] break
%         [ ] continue
%     [.] functions
%         [ ] return
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
% [ ] keywords
% [ ] case sensitive

% https://jakevdp.github.io/WhirlwindTourOfPython/02-basic-python-syntax.html
% https://www.101computing.net/wp/wp-content/uploads/Python-Cheat-Sheet.pdf
% https://ddi.ifi.lmu.de/probestudium/2013/ws-i-3d-programmierung/tutorials/python-referenzkarte
% https://www.codecademy.com/learn/introduction-to-python-dvp/modules/python-syntax-dvp/cheatsheet
% https://pythonprinciples.com/reference/
% https://programmingwithmosh.com/python/python-3-cheat-sheet/
