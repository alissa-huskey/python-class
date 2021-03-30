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
Conditional Statements
======================


If-Statements
-------------

```{image} assets/kings-quest-fork.png
---
alt: fork
align: left
---
```

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
linenos:
---
if status == "failed":
  print("Sorry, you don't have access.")
  exit()
```

```{code-block} python
---
caption: an `if` and `else` clause
linenos:
---
if winner == player:
  print("Congratulations, you win!")
else:
  print("Better luck next time.")

```


```{code-block} python
---
caption: an `if` clause, multipe `elif` clauses, and an `else` clause
linenos:
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


### Exercises and questions

1\. What is the value of `options` if `level` is `"moderator"`.

```{code-block} python
:linenos:
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
---
linenos:
tags: ["raises-exception", "hide-output"]
---
if choice > highest:
  print("Sorry, your pick choice is too high.")
else choice < lowest:
  print("Sorry, your pick choice is too low.")
```

Conditions
----------

The {term}`expressions` following the `if` and `elif`
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

#### Exercises and questions

Open up a {term}`Python shell` and use comparison operators to answer each of the following.

1. Is `F` (capital F) greater than `z` (lower case z)?
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

| operator    | meaning                   | example                                   |
|-------------|---------------------------|-------------------------------------------|
| `and`       | both conditions are true  | `choice > lowest and choice < highest`    |
| `or`        | either condition is true  | `choice < lowest or choice > highest`     |
| `not`       | the following is not true | `not something`                           |
```

The `not` operator is special in that it does not include a `left-hand value`.
You can think of it like the opposite of the value that follows.

#### Exercises and questions

```{admonition} Tip: Check if a number is divisible by another
---
class: tip
---
To test if a number is divisible by another number use the modulo operator `%`
which will give you the division remainder.

For example, `5/2` is `2.5`, or `2` with a remainder of `1`. \
So `5%2` is `1`.

And so to check if a number is divisible by another, just check if the
remainder is zero.

`num % 2 == 0`
```

For each of the following get a random number using `random.randint()`.

1. Get a random number between `1` and `100` then check to see if it is greater
than `50` or if it's an even number.


2. Get a random number between `1` and `100` then check to see if it is an even
number and divisible by ten.


3. Use the `input()` function to ask for a number and save it to a variable
called `num`. Check `num.isnumeric()` and print an error message if it is not.

### Truthy and Falsy

Python evaluates conditional expressions in a {term}`boolean context` which
determines if the resulting value is {term}`truthy` or {term}`falsy`.

A truthy value is one that Python considers to be the equivalent of `True`,
while a falsy value is one that Python considers to be the equivalent of
`False`. It determies this by first converting it to a `boolean` value, which
can be done using the `bool()` function.

Some examples of falsy values are

* `0` zero
* `""` an empty string
* `[]` an empty list

Some examples of truthy values are:

* `5` (a non-zero number)
* `"hello"` (a non-blank string)
* `[35, 32, 89]` (a non-empty list)

Here are details for each data type.

```{table} truthy examples and falsy values for each data type

| Type       | Name         | Falsy         | Truthy         |
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

Since conditions are evaluated in a boolean context (meaning the result of
the expression is converted to a `bool`) you can use a value as condition for
truthiness, or add the `not` operator for falsiness.

In this example we check the truthiness of an integer which we know will be
either `1` or `0`.

```{code-block} python
---
caption: the truthiness of an int
linenos:
---
is_winner = random.randint(0, 1)
if is_winner:
  print("Contgratulations, you win!")
```

This example checks to make sure that a user response is not blank.

```{code-block} python
---
caption: the falsyness of a string
linenos:
---
response = input("What's your name? ")
if not response:
  print("Didn't get that. Try again.")
```

This example function expects a list of items. It checks to make sure the list
is not empty first.

```{code-block} python
---
caption: the falsyness of a list
linenos:
---
def buy_items(items):
  if not items:
    print("Oops, the list of items is empty.")
    return

  print("You are buying", len(items), "items.")
  for item in items:
    buy(item)
```

#### Exercises and questions

Open up a {term}`Python shell` and use the `bool()` function to find out if
each of the following is truthy or falsy.

1. `-1` negative one
2. `" "` a space
3. `{}` an empty dictionary
4. `[0]` a list containing the value `0`

Exercises
---------

```{exercise} Flip a coin

1. Pick a random number between `0` and `1` and assign it to a variable `coin`.
2. Print "You tossed", and the value of `coin`.
3. If the value of `coin` is truthy, print "You win the coin toss!"

```

```{exercise} Computer guessing game

  1. Pick a number between `1` and `100` and assign it to the variable `pick`. (Note: not random.)
  2. Get a random number between between `1` and `100` and assign it to the variable `guess`.
  3. Print `"The computer guessed`" and the value of `guess`.
  4. If `guess` is the same as pick print `"The computer got it right!"`
  5. If guess is within `30` of pick print `"The computer was close."`  (Hint: You'll need the `and` operator.)
  6. Otherwise print `"The computer got it wrong."`

```

```{exercise} Heads or Tails

In this exercise use the `and` operator and determine the truthiness of a value.

1. Ask the user `"heads or tails?"`
2. If the answer is blank, tell them they have to enter something.
3. If the answer is not `"heads"` or `"tails"`, tell them they need to pick
   `"heads"` or `"tails"`.  (Bonus: Make this case-insensitive.)
4. Randomly decide if they won the coin toss.

```
