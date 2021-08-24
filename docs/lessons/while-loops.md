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

While loops
===========

Normally Python reads one statement at a time, one at a time. But loops give us
the ability to repeat a set of statements. In this lesson we will be learning
about `while` loops.


Table of Contents
-----------------

* [Introduction](#introduction)
* [Syntax](#syntax)
   * [Exercises](#exercises)
   * [Quitting a loop](#quitting-a-loop)
      * [Exercise](#exercise)
   * [Skipping part of an iteration](#skipping-part-of-an-iteration)
* [Loop patterns](#loop-patterns)
   * [Incrementing and decrementing](#incrementing-and-decrementing)
      * [Exercise](#exercise-1)
   * [Infinite loops](#infinite-loops)
   * [Iterating over a list](#iterating-over-a-list)
   * [Nested loops](#nested-loops)
      * [Exercises](#exercises-1)
* [Exercises](#exercises-2)
* [Reference](#reference)
   * [Glossary](#glossary)
   * [See also](#see-also)


Introduction
------------

A {term}`while loop` is a {term}`compound statement`. Like an {term}`if statement`
while loops include a conditional expression and a {term}`suite` of
statements that will be repeated until the expression evaluates to {term}`falsy`.

Each time that the suite of statements is repeated in a loop it is called an
{term}`iteration`. Likewise, the process of repeating a loop is called
{term}`iterating`.

Syntax
------

The syntax for a `while` loop is:

{{ leftcol | replace("col", "col-5") }}

```{include} ../templates/syntax/while.md 
```

{{ rightcol | replace("col", "col-7") }}

```{include} ../templates/desc/while.md
```

{{ endcols }} 

Here's a simple example that will keep asking the user for their name until
they answer.

```{literalinclude} ../templates/examples/while.py
:caption: while loop example
:class: full-width
:linenos:
```


### Exercises

```{exercise} Heads or Tails
:label: heads-or-tails-exercise

Write a while loop that asks the user `"Heads or tails?"` until they answer
with either `"heads"` or `"tails"`. *Hint: Use the `not in` operator.*
```

`````{solution} heads-or-tails-exercise
:class: dropdown

```{code-block} python
:caption: Heads or Tails Exercise
:class: full-width
:linenos:

answer = None
while answer not in ["heads", "tails"]:
  answer = input("Heads or tails? ")
```

`````

```{exercise} Random numbers less than 50
:label: random-less-than-50-exercise

Write a while loop that prints a random number between `1` and `100` as long as
the number is less than `50`.
```

`````{solution} random-less-than-50-exercise
:class: dropdown

```{code-block} python
:caption: Random numbers less than 50 Exercise
:class: full-width
:linenos:

import random

num = 0
while num < 50:
  num = random.randint(1, 100)
  print(num)

```

`````

### Quitting a loop

The `break` statement can be used to stop loop iteration.

This example intentionally creates an infinite loop then in each iteration asks
the user if they would like to keep going and uses the `break` statement if
they reply with `"n"`.

```{code-block} python
:caption: stopping a loop with `break`
:class: full-width
:linenos:

import random

while True:
    num = random.randint(1, 10)
    print("The number is:", num)
    reply = input("Keep going? ")
    if reply == "n":
        break
```

#### Exercise

```{exercise} Random number not divisible by ten
:label: random-number-not-divisible-by-ten-exercise

Write a while loop that prints a random number between `1` and `1000` as long as
the number is less than `500`. If the number is divisible by `10`, quit the
loop. *Hint: Use the `%` operator.*

```

`````{solution} random-number-not-divisible-by-ten-exercise
:class: dropdown

```{code-block} python
:class: full-width
:linenos:
import random
num = -1
while num < 500:
    num = random.randint(1, 1000)
    print(num)
    if num % 10 == 0:
        print("num is divisible by 10, quitting")
        break

```

`````

### Skipping part of an iteration

You can skip the rest of the statements in a loop iteration by using the
`continue` statement.

This example uses the `continue` statement to skip the rest of the iteration if
the user does not enter a number.

```{code-block} python
:caption: using the `continue` statement
:class: full-width
:linenos:

balance = 100
while balance > 0:
    reply = input("amount: ")
    if not reply.isnumeric():
        print("Numbers only.")
        continue
    balance = balance - int(reply)
    print("Your balance is:", balance)
```

```{exercise} Dice
:label: dice-exercise

1. Assign `chances` to `0`
1. Assign `rolls` to an empty `list`
1. Write a loop that repeats `10` times. In each iteration:
    1. Assign random number between `1` and `6` to the `num` variable
    1. Print {samp}`"You rolled: {num}"`
    1. Add `1` to `chances`
    1. Ask the user if they want to keep the roll
    1. If they reply with `"n"`, use the `continue` statement to skip the rest of the iteration
    1. Append `num` to a list of `rolls`
    1. Print the `rolls` list
```

`````{solution} dice-exercise
:class: dropdown

```{code-block} python
:class: full-width
:linenos:

chances, rolls = 0, []

while chances < 10:
  num = random.randint(1, 6)
  print(f"You rolled: {num}")

  chances += 1

  keep = input("Keep? ")
  if keep.lower() == "n":
    continue

  rolls.append(num)
  print(f"Your rolls so far: {rolls}")


```

`````


Loop patterns
-------------

In this section we're going to go over some of the ways that loops are commonly used.

### Incrementing and decrementing

Often in programming we want to repeat a suite of statements a specific number
of times.

One way to do this is to keep track of which iteration the loop is currently
executing by {term}`incrementing` or {term}`decrementing` a number.

```{code-block} python
:caption: incrementing the `i` variable
:class: full-width
:linenos:

i = 0

while i < 10:
  print("Iteration:", i+1)
  i = i + 1
```

#### Exercise

```{exercise} Countdown
:label: countdown-exercise

Write a loop that counts down from `3` to `1`. In each iteration print out the
current number then use the `time.sleep` function to pause for one second.

```

`````{solution} countdown-exercise
:class: dropdown

```{code-block} python
:class: full-width
:linenos:

import time

num = 3
while num >= 1:
  print(f"{num}...")
  num = num - 1
  time.sleep(1)
```

`````

### Infinite loops

When a program is written in such a way that the loop condition is always met
the result is called an {term}`infinite loop`. These are easy to cause by
mistake.

The simplest infinite loop is `while True` with no `break`:

```{code-block} python
:caption: while `True`
:class: full-width
:linenos:

import time

while True:
  print("Are we there yet?")
  time.sleep(1)
```

A common mistake is to forget to increment your counter, as demonstrated below.

```{code-block} python
:caption: forgetting to increment `i`
:class: full-width
:linenos:

import time

i = 0

while i < 10:
  print("Iteration:", i)
  time.sleep(1)
```

Infinite loops are not always a bad thing though. In the example below an
infinite loop is used to always return the user to a main menu.

```{code-block} python
:caption: infinite loop used to keep a program running
:class: full-width
:linenos:

CHOICES = {
  "draw": "draw a card",
  "play": "play a card",
  "pass": "pass this turn",
}

def menu():
  """Print user interface, and act according to user choice"""
  print("menu:", ", ".join(CHOICES))
  selection = input("> ").lower().strip()
  if selection not in CHOICES:
    print(f'"{selection}" is not a valid selection, try again.')
    return

  text = CHOICES[selection]
  print(f"{text}...")

def main():
  """."""
  while True:
    menu()
    print()

main()

```

### Iterating over a list

You can use a `while` loop to iterate over the items in a list. To do this
we'll increment an `i` variable just like we did above but we'll use the
`len()` function to determine the length of the list and therfore how many
times the loop should repeat.

Then we can use the `i` variable to access each item in the list.

```{code-block} python
:caption: iterating over a list
:class: full-width
:linenos:

i = 0
colors = ["red", "green", "blue"]

while i < len(colors):
  color = colors[i]
  print("Color", i, "is:", colors[i])
  i += 1
```

```{exercise} Lunch menu
:label: lunch-menu-exercise

Print a lunch menu. Make a list of lunch `choices` for a menu. Use a while loop
to print out each item in the list with the number next to it.

```

`````{solution} lunch-menu-exercise
:class: dropdown

```{code-block} python
:caption: Lunch Menu Exercise
:class: full-width
:linenos:

choices = [
  "Pepperoni pizza",
  "Ham sandwich",
  "Fish tacos",
  "Bean burrito",
]

i = 0

print("Lunch menu")
print("----------", "\n")

while i < len(choices):
  item = choices[i]
  print(f"{i+1}. {item}")
  i += 1
```

`````

You can also use this to iterate over list-like values. For example, a string
can be used like a list of characters. So we can use the same pattern to
iterate over all of the characters in a string.

```{code-block} python
:caption: iterating over the characters in a string
:class: full-width
:linenos:

word = input("Enter a word: ")

i = 0
while i < len(word):
    print("Letter", i, "is:", word[i])
    i += 1
```

```{exercise} Vowels
:label: vowels-exercise

Print the vowels in a word. Ask the user for a word then iterate over each
letter. If the letter is a vowel print the letter.  (*Hint: make a list of
vowels the use the `in` operator*)

```

`````{solution} vowels-exercise
:class: dropdown

```{code-block} python
:caption: Vowels Exercise
:class: full-width
:linenos:

VOWELS = ["a", "e", "i", "o", "u", "y"]
word = input("Enter a word: ")

i = 0
while i < len(word):
  letter = word[i]
  if letter in VOWELS:
    print(letter, end="")
  i += 1
print()


```

`````

### Nested loops

Just like you can have an if statement inside of another if statement, you can
also have a while loop inside of another while loop.

This example prints out a score card for three rounds of three players each.

```{code-cell} python
:tags: [hide-output]

rounds, players = 3, 3
r = 0
while r < rounds:
    print("Round:", r+1, "\n")
    p = 0
    while p < players:
        print("Player", p+1, "score:", "______________")
        p += 1
    print()
    r += 1
```

A few things to pay attention to with nested loops:

- The child `p` counter needs to be set to `0` **inside the parent loop**. If
  you forget this, the score line for each player will only be printed in the
  first round.

- The child `p` counter must be incremented **inside of the child loop**.

- In this case it doesn't matter, but you generally want to increment the `r`
  counter **at the end** of the parent loop, just in case you need to use the
  current value of `r` inside of the child loop.

Here's another example that prints out a grid of `x, y` coordinates.

```{code-cell} python
:tags: [ hide-output ]

rows, cols = 5, 5
r = 0
while r < rows:
    c = 0
    while c < cols:
        output = str(r) + "," + str(c) + "   "
        print(output, end="")
        c += 1
    print("\n")
    r += 1
```

#### Exercises

```{exercise} multiplication-table
:label: multiplication-table-exercise

Print a multiplication table grid with `9` rows and `9` columns.
```


`````{solution} multiplication-table-exercise
:class: dropdown

```{code-block} python
:caption: Multiplication Table Exercise
:class: full-width
:linenos:

SIZE = 9

print()

x = 1
while x <= SIZE:
    print("  ", end="")
    y = 1
    while y <= SIZE:
        val = x * y
        print(str(val).rjust(4), end="  ")
        y += 1
    x+=1
    print("\n")

main()
```

`````


Exercises
---------

```{exercise} Name Cheer
:label: name-cheer-exercise

Print a cheer for your name. For each letter print {samp}`"Gimme a {letter}!"`.
Then end it with, {samp}`"What does it spell? {name}!"`

```

`````{solution} name-cheer-exercise
:class: dropdown

```{code-block} python
:caption: Name Cheer Exercise
:class: full-width
:linenos:

import time

NAME = "Alissa"

i = 0
while i < len(NAME):
    print("Gimme a", NAME[i].upper() + "!")
    i += 1
    time.sleep(0.5)

print("\nWhat does it spell?")
print(NAME.upper() + "!")

```

`````

```{exercise} Check Password
:label: check-password-exercise

1. Assign a `secret` variable to a string of your choice for the correct password.
1. Assign a `chances` variable to `3`
1. Assign a `password` variable to `None`
1. Assign a `locked` variable to `True`
1. Write a while loop that continues as long as `password` is not equal to `secret`.
1. In the loop:
   1. Ask the user for the password using the `input()` function, and assign the result to `password`.
   1. If `password` is equal to `secret`, set `locked` to `False`
   1. Quit the loop if there are no more chances
   1. subtract `1` from `chances`
1. After the loop: if `locked` is `False`
   1. Print `"Welcome!"`

```

`````{solution} check-password-exercise
:class: dropdown

```{code-block} python
:caption: Check Password Exercise
:class: full-width
:linenos:

secret = "00000"
password, locked, chances = None, True, 3

while password != secret:
  password = input("Enter the password: ")
  if password == secret:
    locked = False

  if not chances:
    print("Too many attempts, try again later.")
    break

  chances = chances - 1

if not locked:
  print("Welcome.")

```

`````

```{exercise} Jolly Good Fellow
:label: jolly-exercise

Print the lyrics to the jolly good fellow song. `"For he's a jolly good
fellow..."` three times, then "Which nobody can deny!" once.

```

`````{solution} jolly-exercise
:class: dropdown

```{code-block} python
:caption: Jolly Good Fellow Exercise
:class: full-width
:linenos:

i = 0
while i < 3:
    print("For he's a jolly good fellow...")
    i += 1

print("Which nobody can deny!")

```

`````


`````{exercise} 12 Days of Christmas
:label: days-of-xmas-exercise

Print the 12 Days of Christmas song.

1. Create a nested list, where each item is a list containing two items: the
   ordinal word for the day (ie "second") and the gift for that day.
2. Iterate over each day to print the parent day lyric {samp}`"On the {ordinal} day of Christmas my true love gave to me {gift}."`
3. Use a nested `while` loop to iterate over each of the days lower than parent day in descending order.
4. For each child day, print the lyric {samp}`"{day} {gift},"`

::::{dropdown} Show lyrics

```{include} 12-days-of-xmas-lyrics.md
```

::::

`````

`````{solution} days-of-xmas-exercise
:class: dropdown

```{code-block} python
:caption: 12 Days of Christmas Exercise
:class: full-width
:linenos:

import time

DAYS = [
    ['first', "a partridge in a pear tree"],
    ['second', "turtle doves"],
    ['third', "french hens"],
    ['forth', "calling birds"],
    ['fifth', "golden rings"],
    ['sixth', "geese a laying"],
    ['seventh', "swans a swimming"],
    ['eighth', "maids a milking"],
    ['ninth', "ladies dancing"],
    ['tenth', "lords a leaping"],
    ['eleventh', "pipers piping"],
    ['twelfth', "drummers drumming"],
]

i = 0
while i < len(DAYS):
    day, gift = DAYS[i]
    print("On the", day, "day of Christmas my true love gave to me")

    x = i
    while x >= 0:
        gift = DAYS[x][1]
        time.sleep(0.5)

        # indent the line
        line = "  "

        # add the "and" in "and a partridge in a pear tree"
        if i and x == 0:
            line += "and "

        # add the number of gifts
        if x:
            line += str(x+1) + " "

        # add the gift given
        line += gift

        # add the "," or "."
        if x:
            line += ","
        else:
            line += "."

        # print the line
        print(line)

        x -= 1

    i += 1

    print()

```

`````

```{exercise} Hangman
:label: hangman-exercise

Write a hangman game.

1. Choose a short word, give the player 6 chances to guess letters
1. Each turn:
    1. Print their chances with `x` to show used chances, and `_` to show remaining \
       example: `chances: xx____`
    1. Print the word, but replace `_` for unguessed letters \
       example: `5 letters: _e___`
    1. Ask the player to guess a letter
    1. Bonus: make sure the user enters exactly one character
1. Tell the user at the end if they won or lost

```

`````{solution} hangman-exercise
:class: dropdown

```{code-block} python
:caption: Hangman Exercise
:class: full-width
:linenos:

import random

WORDS = [ "hello", "goodbye", "secret", "satisfy", "apple", "bear" ]

def info(turn, chances, guess):
    """print the used vs unused chances and guessed vs unguessed letters
       example:
           chances: xx____ 7 letters: _e_____
    """
    print(" "*40, "chances:", ("x"*turn)+("_"*(chances-turn)), len(guess), "letters:", guess)

def main():
    """."""
    turn, chances, word = 1, 6, random.choice(WORDS)
    guess = "_" * len(word)

    info(0, chances, guess)

    while guess != word and turn <= chances:
        char = input("Guess a letter: ").lower()
        if not char:
            continue
        elif len(char) > 1:
            print(" Just one letter!")
            continue
        if char in word:
            letters = list(guess)
            for i,c in enumerate(word):
                if c == char:
                    letters[i] = c
            guess = "".join(letters)
        print(" "*40, "chances:", ("x"*turn)+("_"*(chances-turn)), len(word), "letters:", guess)
        turn += 1
    if guess == word:
        print("You win!!")
    else:
        print("Too bad. The word was:", word)

main()

```

`````

Reference
---------

### Glossary

```{glossary} while-loops
while loop
  A {term}`compound statement` that repeats a {term}`suite` of statements as
  long as a {term}`condition` evaluates to {term}`truthy`.

infinite loop
  When a program is written in such a way that the loop continues forever.

increment
incrementing
  Adding to a number, usually `1`.

decrement
decrementing
  Subtracting from a number, usually `1`.

```

### See also

```{seealso}

* [python.org > Iterator Types](https://docs.python.org/3/library/stdtypes.html#typeiter)
* [Loop Better: a deeper look at iteration in Python](https://treyhunner.com/2019/06/loop-better-a-deeper-look-at-iteration-in-python/)
* [Python’s built-in container data types: categorisation and iteration](http://blog.wachowicz.eu/?p=132)
