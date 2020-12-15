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
Flow Control
============

In this lesson we are going to learn about some of the ways to control the flow
of a program.

When you run a program, the Python interpreter reads and executes each
statement in a very orderly fashion, from top to bottom, one statement at a time.

With flow control statements, we can guide Python along different paths
depending on the circumstances. Like a choose-your-own-adventure, we can have
some statements only execute in in certain cases. Or we can have statements
executed multiple times.

If-Statements
-------------

```{image} assets/kings-quest-fork.png
---
alt: fork
align: left
---
```

To continue with our video game analogy, if-statements are like a fork in the road.

An if-statement is a way to change what happens depending on the circumstances.

<div class="clear"></div>

{term}`If-statements` are compound statements, made up of the one or more
conditions, followed by the group of statements that belong to it.

An if-statement can have three types of clauses:

* an `if` clause is always present, followed by a {term}`condition`
* an optional `elif` clause may appear multiple times and is also followed by a {term}`condition`
* and an optional `else` clause, which is like a default, and has no condition.

Let's take a look at some examples.

```{code-block} python
---
caption: one `if` clause
---
if status == "failed":
  print("Sorry, you don't have access.")
  exit()
```

```{code-block} python
---
caption: an `if` and `else` clause
---
if winner == player:
  print("Congratulations, you win!")
else:
  print("Better luck next time.")

```


```{code-block} python
---
caption: an `if` clause, multipe `elif` clauses, and an `else` clause
---
if choice == "left":
  print("You decide to take the path to the left.")
elif choice == "right":
  print("You decide to take the path to the right.")
elif choice == "middle":
  print("You decide to take the middle path.")
else:
  print("Invalid choice.")
```


### Questions

1\. What is the value of `options` if `level` is `"moderator"`.

```{code-block} python
options = ["view", "list", "exit"]

if level == "admin":
  options.append("remove")
elif level == "moderator":
  options.append("flag")
elif level == "owner":
  options.append("edit")
```


2\. Fix the following.

```{code-cell} python
:tags: ["raises-exception", "hide-output"]
if choice > max:
  print("Sorry, your pick choice is too high.")
else choice < min:
  print("Sorry, your pick choice is too low.")
```

Conditions
----------

The {term}`expressions<expression>` following the `if` and `elif`
{term}`keyword` in an if-statement are called conditions. This is what tells
Python whether to execute the {term}`suite` of statements in this clause.

### Comparison Operators

Conditional statements often use {term}`Comparison operators` which compare two
values and evaluate to either `True` or `False`.

Some examples of expressions using comparison operators:

* `5.5 < 3`
* `"fox" in "The quick brown fox jumps over the lazy dog"`
* `5*3 == 30`

```{table} Comparison operators

| operator    | meaning                   | examples                |                               |
|-------------|---------------------------|-------------------------|-------------------------------|
| `==`        | equivalent values         | `choice == "a"`         | `5.0 == 5`                    |
| `!=`        | not equivalent values     | `a != b`                |                               |
| `<`         | less than                 | `"a" < "c"`             | `balance < price`             |
| `<=`        | less than or equal to     | `a <= b`                |                               |
| `>`         | greater than              | `"z" > "d"`             | `price > balance`             |
| `>=`        | greater than or equal to  | `a >= b`                |                               |
| `in`        | is member of              | `"h" in "hello"`        | `5 in [1, 3, 5, 7, 9]`        |
| `not in`    | is not a member of        | `"a" not in "hello  "`  | `2 not in [1, 3, 5, 7, 9]`    |
```

#### Questions

Open up a {term}`Python shell` and use comparison operators to answer each of the following.

1. Is `F` (capital A) greater than `z` (lower case z)?
2. Is `0.0` equal to `0`
3. Is `[1, 2, 3, 4]` greater than `[5, 6, 7]`?
4. Is the letter `"z"` in the string `"zebra"`?
5. Is the number `5` in the list `[1, 2, 4]`?

### Logical Operators

When you have more than one expression in a condition, you need a
{term}`logical operator` which evaluates to either True or False depending on
the boolean value of both the left and right hand values.

Some examples of expressions using logical operators:

* `5 < 3 or 5 > 2`
* `"h" in "hello" and "H" in "hello"`
* `not 1 == 2`

```{table} Logical operators

| operator    | meaning                   | example                            |
|-------------|---------------------------|------------------------------------|
| `and`       | both conditions are true  | `choice > min and choice < max`    |
| `or`        | either condition is true  | `choice < min or choice > max`     |
| `not`       | the following is not true | `not something`                    |
```

The `not` operator is special in that it does not include a `left-hand value`.
You can think of it like the opposite of the value that follows.


### Truthy and Falsy

Python evaluates conditional expressions in a {term}`boolean context` which
determines if the resulting value is {term}`Truthy` or {term}`Falsy`.

A `Truthy` value is one that Python considers to be the equivalent of `True`,
while a `Falsy` value is one that Python considers to be the equivalent of
`False`. It determies this by first converting it to a `boolean` value, which
can be done using the `bool()` function.

Some examples of `Falsy` values are 

* `0` zero
* `""` an empty string
* `[]` an empty list

Some examples of `Truthy` values are:

* `5` a non-zero number
* `"hello"` a non-blank string
* `[35, 32, 89]` a non-empty list

Here are details for each data type.

```{table} Truthy and Falsy examples for each data type

| type       | name         | Falsy         | Truthy         |
|------------|--------------|---------------|----------------|
| `str`      | string       | `""`          | `"a"`          |
| `int`      | integer      | `0`           | `1`            |
| `float`    | float        | `0.0`         | `0.5`          |
| `dict`     | dictionary   | `{}`          | `{"a": 1}`     |
| `list`     | list         | `[]`          | `[1]`          |
| `tuple`    | tuple        | `()`          | `(1)`          |
| `bool`     | boolean      | `False`       | `True`         |
| `None`     | none         | `None`        |                |
```

#### Questions

Open up a {term}`Python shell` and use the `bool()` function to find out if
each of the following is `Truthy` or `Falsy`.

1. `-1` negative one
2. `" "` a space
3. `{}` an empty dictionary
4. `[0]` a list containing the value `0`
