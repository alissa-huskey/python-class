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
Loops
=====

Normally Python reads one statement at a time, one at a time. But loops give us
the ability to repeat a set of statements.

While loops
-----------

A {term}`while loop` is a {term}`compound statement`. Like an {term}`if statement`
while loops include a conditional expression and a {term}`suite` of
statements that will be repeated until the expression evaluates to false.

Each time that the suite of statements is repeated in a loop it is called an
{term}`iteration`. Likewise, the process of repeating a loop is called
{term}`iterating`.


Here's a simple example that will keep asking the user for their name until
they answer.

```{code-block} python
---
caption: a simple while loop example
linenos:
---

reply = ""

while not reply:
  reply = input("What is your name? ")

print("Name:", reply)
```

:::{admonition,hint,details,exercise}

1. Write a while loop that asks the user `"Heads or tails?"` until they answer
with either `"heads"` or `"tails"`. *Hint: Use the `not in` operator.*

2. Write a while loop that prints a random number between `1` and `100` until
   the answer is greater than `50`.

:::

### Infinite loops

When a program is written in such a way that the loop condition is always met
the result is called an {term}`infinite loop`. These are easy to cause by
mistake.

Here are a couple examples:

```{code-block} python
---
caption: forgetting to increment `i`
linenos:
---

i = 0

while i < 10:
  print("Iteration:", i+1)
```

```{code-block} python
---
caption: value of `num` will never get to `15`
linenos:
---

num = 0

while num < 15:
  num = random.randint(0, 10)
  print("The number is:", num)

```

### Quitting a loop

The `break` statement can be used to stop loop iteration.

This example intentionally creates an infinite loop then in each iteration asks
the user if they would like to keep going and uses the `break` statement if
they reply with `"n"`.

```{code-block} python
---
caption: stopping a loop with `break`
linenos:
---
import random

while True:
    num = random.randint(1, 10)
    print("The number is:", num)
    reply = input("Keep going? ")
    if reply == "n":
        break
```

:::{admonition,hint,details,exercise}

Write a loop that prints a random number, then ask the user if they would like
to keep going. Exit the loop if they answer with a `"n"`.

:::


### Skipping part of an iteration

You can skip the rest of the statements in a loop iteration by using the
`continue` statement.

This example uses the `continue` statement to skip the rest of the iteration if
the user does not enter a number.

```{code-block} python
---
caption: using the `continue` statement
linenos:
---
balance = 100
while balance > 0:
    reply = input("amount: ")
    if not reply.isnumeric():
        print("Numbers only.")
        continue
    balance = balance - int(reply)
    print("Your balance is:", balance)
```

:::{admonition,hint,details,exercise}

Make an empty `rolls` list then write a loop that repeats `10` times. In each
iteration:

- Get a random number between `1` and `6`
- print `"You rolled:"` followed by the number.
- Ask the user if they want to keep the roll.
- If they reply with `"n"`, use the `continue` statement to skip the rest of
  the iteration
- Append the number to a list of `rolls`
- print the `rolls` list

:::

Loop patterns
-------------

In this section we're going to go over some of the ways that loops are commonly used.

### Incrementing

Often in programming we want to repeat a suite of statements a specific number
of times.

One way to do this is to keep track of which iteration the loop is currently
executing by incrementing (or decrementing) a number.

```{code-block} python
---
caption: incrementing the `i` variable
linenos:
---

i = 0

while i < 10:
  print("Iteration:", i+1)
  i = i + 1
```

:::{admonition,hint,details,exercise}

Write a loop that counts down from `3` to `1`. In each iteration print out the
current number then use the `time.sleep` function to pause for one second.

:::

### Iterating over a list

You can use a `while` loop to iterate over the items in a list. To do this
we'll increment an `i` variable just like we did above but we'll use the
`len()` function to determine the length of the list and therfore how many
times the loop should repeat.

Then we can use the `i` variable to access each item in the list.

```{code-block} python
---
caption: iterating over a list
linenos:
---

i = 0
colors = ["red", "green", "blue"]

while i < len(colors):
  print("Color", i, "is:", colors[i])
  i += 1
```

:::{admonition,hint,details,exercise}

Print a lunch menu. Make a list of lunch `choices` on a menu. Use a while loop
to print out each item in the list with the number next to it.

:::

You can also use this to iterate over list-like values. For example, a string
can be used like a list of characters. So we can use the same pattern to
iterate over all of the characters in a string.

```{code-block} python
---
caption: iterating over the characters in a string
linenos:
---

word = input("Enter a word: ")

i = 0
while i < len(word):
    print("Letter", i, "is:", word[i])
    i += 1
```

:::{admonition,hint,details,exercise}

Print the vowels in a word. Ask the user for a word then iterate over each
letter. If the letter is not a vowel, (*hint: make a list of vowels the use
`not in`*) use a `continue` statement to skip the rest of the iteration. Then
print the character number and the character.

:::

### Nested loops

Just like you can have an if statement inside of another if statement, you can
also have a while loop inside of another while loop.

This example prints out a score card for three rounds of three players each.

```{code-cell} python
---
caption: score card
linenos:
tags: [hide-output]
---

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
---
caption: coordinates grid
linenos:
tags: [ hide-output ]
---

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

:::{admonition,hint,details,exercise}

Print a multiplication table grid with `9` rows and `9` columns.

:::


Practice exercises
------------------

Here are some more practice exercises with loops you can work on.

1. Print a cheer for your name. For each letter print {samp}`"Gimme a {letter}!"`.
   Then end it with, {samp}`"What does it spell? {name}!"`

2. Print the lyrics to the jolly good fellow song. "For he's a jolly good
   fellow..." three times, then "Which nobody can deny!" once.

3. Print the 12 Days of Christmas song. Use a nested list with a list for each
   lyric containing the ordinal word for the day (ie "second") and the gift for
   that day.

4. Write a hangman game.
     - choose a short word, give the player 6 chances to guess letters
     - each turn:
       - print their chances with `x` to show used chances, and `_` to show remaining \
         example: `chances: xx____`
       - print the word, but replace `_` for unguessed letters \
         example: `5 letters: _e___`
    - tell the user at the end if they won or lost
