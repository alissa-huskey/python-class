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
Statements
==========

A {term}`statement` is an instruction that Python can run or {term}`execute` as
a unit.

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

A {term}`simple statement` is a single instruction, one that does not group together
other statements. In comparison to prose a simple statement is like a sentence.
While there are exceptions, a simple statements is essentially a line of code.

To be more accurate, a simple statement is a single instruction that *could* be
written on one line by itself, even if it is actually written differently.
This is referred to as a {term}`logical line`.


### Single line statements

Most of the time simple statements are written one per line. The newline
character tells Python that the statement is complete.

```{code-block} python
---
caption: examples of simple statements, each on one physical line
---
name = "Alissa"
print("Hello", name)
import random
colors = ["red", "green", "blue"]
```

### Multi-line statements

A statement can be broken into multiple lines following an {term}`operator` or
{term}`delimiter` symbol as long it is enclosed by `(` `)`, `[` `]` or `{` `}`.

This is called {term}`implicit line continuation`.

```{code-block} python
---
linenos:
caption: the same simple statement, shown in both single and multi-line formats
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
caption: two simple statement examples split via implicit line continuation
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

If the operators or delimiters are not enclosed by anything you can still can
break a statement into multiple lines by adding a `\` to the end of each line.

This is called {term}`explicit line continuation`.

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
statement. You can think of a semicolon as a substitute newline.
```{code-block} python
---
linenos:
caption: two simple statements on one physical line
---
import random; num = random.randint(1, 10)
```

> This is usually discouraged as poor coding practice, but it's fine in the
> Python shell where it can be a handy shortcut.

Compound Statements
-------------------

A {term}`compound statement` is a a number of statements grouped together as a
single unit.  If a simple statement like a sentence, a compound statement is
more like a paragraph.

One example is a function definition.

```{code-block} python
---
linenos:
caption: this function has three simple statements in its suite (lines `2`-`4`) controlled by the header (line `1`)
---
def welcome_player():
  name = input("Player name: ")
  print("Welcome", name)
  return name
```

A compound statement is made up of at least one {term}`header` statement and
the group of statements, called a {term}`suite`, that belong to it.

A header statement always starts with a a keyword (like `def` or `if`) and ends
in a `:`. This header tells Python that a compound statement has started, that
it is in charge of all of the indented lines to follow, and how and when they
should be executed.

The header line and the suite of statements that belong to it are called a
{term}`clause`.

### Multi-clause statements

Some compound statements can have more than one clause. This allows a different
set of statements to be triggered depending on the circumstances.

Here is an example of an if-statement with three clauses.

```{code-block} python
---
linenos:
caption: this is a single if-statement though it contains three clauses (the `if` clause lines `1`-`2`, the `elif` clause lines `3`-`4`, and the `else` clause lines `5`-`6`)
---
if answer < 0:
    print("Answer must be a positive number")
elif answer > 5:
    print("Answer must be less than five.")
else:
    print("Your answer was:", answer)
```

You can think of compound statements as a hierarchy where statements at the
same indentation level are under the authority of the most recent header
statement that's back one indentation level.
```{code-block} python
---
linenos:
caption: an if-statement with two clauses
---
if name == "Picard":
  print("Riker")
  print("Data")
  print("Worf")
elif name == "Riker":
  print("Data")
  print("Worf")
```

In this example, the `Picard` header (line `1`) is in charge of `Riker`,
`Data` and `Worf` (lines `2`-`4`), and the `Riker` header (line `5`) is in
charge of `Data` and `Worf` (lines `6` and `7`).


### Nested statements

Compound statements contain other compound statements. The suites of the nested
compound statements would then be indented one additional level. 

An example is a function that contains an if-statement.

```{code-block} python
---
linenos:
caption: an if-statement within a function definition, followed by two simple statements
---

def action(choice, item):
  if choice == "a":
    print("Adding item")
    return add(item)
  elif choice == "d":
    print("Deleting item")
    return delete(item)
  elif choice == "q":
    print("Quitting.")
    exit()
  print("Invalid response, please try again.")
  return False

response = show_menu()
action(response)
```

* The `def` header on line `1` controls lines `2`-`12`.
* The `if` header on line `2` controls lines `3`-`4`
* The `elif` header on line `5` controls lines `6`-`7`
* The `elif` header on line `8` controls lines `9`-`10`
* Lines `11`-`12` are inside the function, but not the `if` statement
* Lines `14`-`15` are outside of the function entirely


### Summary

Compound statements:

* start with a header statement that begin with a keyword like `if` or `def` and end with a `:`
* followed by a suite of one or more indented statements
* some compound statements have more than one clause, like in an `if` statement with an `else` clause


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

Reference
----------------

### Glossary

```{glossary}
statement
  an instruction that Python can execute as a unit

physical line
  a line of code, the way it was written

logical line
  - a physical line of code containing a single complete statement
  - multiple physical lines of code joned by explicit or implicit line continuation
  - a single statement part of multi-statement physical line of code 

execute
  when Python runs a statement (or script)

simple statement
  a single statement that can be written on one line by itself, even if it is not actually written that way

delimiter
  a seperating symbol, most often a `,`

implicit line continuation
  when a simple statement is broken into multiple lines inside of `(` `)`, `[` `]` or `{` `}` after operators.

explicit line continuation
  when a simple statement is broken into multiple lines by appending a `\` to the end of each line

compound statement
  a number of statements grouped together as a single unit consisting of one or
  more clauses, each made up of a header statement and a suite of statements
  the header controls

header
  the first line in a compound statement clause, beginning with a keyword and
  ending with a `:`, that controls when and how the suite of statements in the
  clause will be executed. 

suite
  a group of statements in a compound statement that are controlled by a header

clause
  a header and the suite of statements that it controls in a compound statment
```
---

### More info

**The Python Language Reference**

* [Lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html)
* [Simple statements](https://docs.python.org/3/reference/simple_stmts.html)
* [Compound statements](https://docs.python.org/3/reference/compound_stmts.html)

