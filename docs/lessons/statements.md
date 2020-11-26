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
Fundamentals: Statements
========================

A *statement* is an instruction that Python can run or *execute* as a unit.

Like grammar in prose, statements follow syntax rules telling Python where they
begin and end as well as how they should be handled. 

Python's syntax rules define statements as either a single logical line of
code:

```python
debug_mode = True
```

Or a block of code grouping multiple statements together:

```python
if result < 0:
  print("Positive number required, try again.")
  ```

Simple Statements
-----------------

A *simple statement* is a single instruction, one that does not group together
other statements. In comprison to prose a simple statement is like a sentence.
While there are exceptions, a simple statements is essentially a line of code.

To be more accurate, a simple statement is a single instruction that could be
written on one line by itself, even if it is actually written differently.
This is referred to as a *logical line*.


### Single line statements

Most of the time simple statements are written one per line. The newline
character tells Python that the statement is complete.

```{code-block} python
---
caption: examles of simple statements, each on one physical line
---
name = "Alissa"
print("Hello", name)
import random
colors = ["red", "green", "blue"]
```

### Multi-line statements

A statement can be broken into multiple lines after operators or delimiters
(seperator symbols), as long as they are inside of parentheses, square brackets
or curly braces.

This is called *implicit line continuation*.

```{code-block} python
---
linenos:
caption: the same simple statement, shown on single and multiple physical lines
---
colors = ["red", "green", "blue"]
colors = [
  "red",
  "green",
  "blue",
]
```

```{code-block} python
---
linenos:
caption: two simple statements split via implicit line continuation
---
address = {
    'street': "1600 Pennsylvania Ave NW",
    'city': "Washington",
    'state': "DC",
    'zip': "20500-0003",
    'country': "United States",
}

print("The White House: " +
      address['street']   + ", " +
      address['city']     + ", " +
      address['state']    + ", " +
      address['zip'])
```

If the operators or delimiters are not within braces or parenthesis you can
still can break up a statement into multiple lines by adding a `\` to the end
of each line.

This is called *explicit line continuation*.

```{code-block} python
---
linenos:
caption: a single assignment statement, split via explicit line continuation
---
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
```

### Multi-statement lines

You can put multiple statements on one line by putting a `;` between each
statement.
```{code-block} python
---
linenos:
caption: two statements on one physical line
---
name = "Steve" ; print("Welcome", name)
```

> While this is considered poor practice, it's fine for the Python shell and
> can be a a handy shortcut.

Compound Statements
-------------------

There are some cases where a number of statements are grouped together to be
executed as a single unit. This is called a *compound statement*.

If a simple statement like a sentence, a compound statement is like a paragraph
in its simplest form.

A compound statement always has at least one *header* line that that ends in
a `:` and controls one or more *body* statement lines that are at the same
indentation level.

```
<header>:
  <body>
```

One example is a function definition.


```python
def print_debug(text):
    print("DEBUG:", text)
```

Another example is an if-statatement.

```{code-block} python
---
linenos:
caption: this is a single if-statement though it contains three headers (the `if`, `elif`, and `else` lines)
---
if answer < 0:
    print("Answer must be a positive number")
elif answer > 5:
    print("Answer must be less than five.")
else:
    print("Your answer was:", answer)
```


% Compound statements contain other compound statements.

% Statements vs. Expressions
% --------------------------

% Expressions can be statements.

% Statements may contain expressions, but expressions can't contain statements
% that are not also expressions.

% Expressions are evaluated, statements are executed.


Self-Quiz
---------

1\. How many statements are in the following:

```{code-cell} python
:tags: ["hide-output"]
favs = {
    'color': "purple",
    'season': "Fall",
    'food': "cheese"
}
print("My favorite color is:", favs['color'])
```

2\. What is wrong with the following:

```{code-cell} python
:tags: ["raises-exception", "hide-output"]
import random
num = random.randint(0, 10)
if num > 5:
print(num)
```

3\. What is wrong with the following:

```{code-cell} python
:tags: ["raises-exception", "hide-output"]
def print_header(title)
    print(title)
    print("============================================")
```

4\. How many statements are in the following:

```{code-cell} python
:tags: ["hide-output"]
name = "Jack" ; age = 24 ; print(name, "is", age, "years old")
```

Today we learned
----------------

* **statement**: an instruction to Python
* **execute**: when Python runs a statement
* **simple-statement**: a statement that can be written on a single line by itself, even if it is not actually written that way
* **compound-statement**: a number of statements grouped together as a single unit
* **implicit line continuation**: when a simple statement is broken into multiple lines inside of `(` `)`, `[` `]` or `{` `}` after operators.
* **explicit line continuation**: when a simple statement is broken into multiple lines by appending a `\` to the end of each line
