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
Chapter 3: Guess the Number
===========================

```{div} float-right
{{ code.format("guess.py", "lessons/guess.py") }}
```

> Based on: [Chapter 3: Guess the Number](http://inventwithpython.com/invent4thed/chapter3.html)

```{include} ../toc.md
```

Introduction
------------

In this chapter, you’re going to make a Guess the Number game. The computer
will think of a secret number from `1` to `20` and ask the user to guess it.
After each guess, the computer will tell the user whether the number is too
high or too low. The user wins if they can guess the number within six tries.

This is a good game to code because it covers many programming concepts in
a short program. You’ll learn how to convert values to different data
types and when you would need to do this. Since this program is a game,
from now on we’ll call the user the player.

```{screencast} assets/dragon_realm.cast
:poster: npt:0:01
:rows: 15
```

Part 1. Setup
-------------

Create a new file called `guess.py`.

:::{admonition} Repl.it
:class: tip

For more information on creating and running new scripts on Repl.it see
[Repl.it Tips](../tools/replit.html#running-new-scripts).

:::

Start by adding a docstring, surrounded by three double or single quotes, to
the first line of your file with a brief description of this script.

```{code-block} python
:caption: guess.py
:linenos:

"""This is a Guess the Number game."""
```

Even though the script doesn't do anything yet, go ahead and run it to make
sure there are no errors.

Part 2. Use the `random` Module
-------------------------------

Python provides some functions that are built into the language like the
`print()` function that you are already familiar with. There are even more
functions available through {term}`modules`.

A {term}`module` is a kind of reusable code that can be loaded into your
scripts using the `import` keyword followed by the name of the module.

The collection of modules provided by Python is called the standard library,
and that's what we'll be using today.  We are going to use the `random` module
in this script. It has a function `randint()` which we will use to get a random
number.

To call a function that is part of a module, put the module
{term}`namespace` in front of the function followed by a dot, then the
function name.

The `randint()` function takes two arguments. The first is the minimum
number, the second is the maximum number.

### Try it in the Python Shell

The {term}`Python shell` is an easy way to execute Python code interactively.
You can think of it kind of like a whiteboard for code. It lets you quickly try
small code snippets to see how they work. (See also [](../tools/python-shell.md).)

At the command line, start a Python shell by typing `python`. The prompt will
change to `>>>`.

```{code-block} python
:caption: Python shell

Python 3.8.3 (default, May 14 2020, 20:11:43)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import random
>>> random.randint(1,20)
```

:::{hint}

In the Python shell, you can hit the up arrow to fill in the last line you typed again.

:::


### Edit `guess.py`

Now that you understand how importing works, import the module, then save
a random number to the `number` variable by calling `random.randint()`.

Let's also set the maximum number of guesses.

```{code-block} python
:caption: guess.py
:linenos:
:emphasize-lines: "4-5"

"""This is a Guess the Number game."""
import random

number = random.randint(1, 20)
max_guesses = 6
```

Part 3: Welcome the Player
--------------------------

We've used the `input()` function before to get feedback from the user. It
can take an optional {term}`argument`, a string that will be presented to
the user as a prompt just to the left of their cursor.

Let's use this new way of calling `input()` to get the players name and
then use `print()` to greet them.

### Edit `guess.py`

```{code-block} python
:caption: guess.py
:linenos:
:emphasize-lines: "7-10"

"""This is a Guess the Number game."""
import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")
print()
```

Note the space after the `?` in the `input()` line. This way there will be
a space between the prompt and the cursor.


Part 4: Let the Player Guess
----------------------------

We've used a `for` loop before to loop over items in a list. Here we will
use the `range()` function, which allows us to easily repeat the loop
a specific number of times. We will give it two arguments: the starting
number and the `max_guesses` that we defined earlier.

We've also the `print()` function before but in the past we've always
passed it only one argument. It can take as many arguments as you want and
it will convert them each to strings and then print them with spaces
in-between. Let's use this handy way to print the guess number each round.


### Edit `guess.py`

```{code-block} python
:caption: guess.py
:linenos:
:emphasize-lines: "12-14"

"""This is a Guess the Number game."""
import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")
print()

for guess_count in range(1, max_guesses+1):
    print("Guess", guess_count, "of", max_guesses)
    guess = input("Your guess: ")
```

Part 5: Check the Guess
-----------------------

The value in the `guess` variable is a string, because `input()` always
returns a string. But we need a number variable to check the guess. To
convert a string to an integer, we will use the `int()` function.

Once it is converted, we can use an {term}`if statement` to check it. We'll
use the `break` keyword to exit the loop early if the guess is correct.

### Edit `guess.py`

```{code-block} python
:caption: guess.py
:linenos:
:emphasize-lines: "16-27"

"""This is a Guess the Number game."""
import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")
print()

for guess_count in range(1, max_guesses+1):
    print("Guess", guess_count, "of", max_guesses)

    guess = input("Your guess: ")
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        break

    print()

```


Part 6: Check if the Player Won
-------------------------------

When the code runs to the point where it exits the {term}`for loop` both the
`guess` and the `guess_count` variables will still be the last value each
was set to when the loop ran for the final time.

We'll use an {term}`if statement` to check the `guess` value to determine if
the player won or not and print out a message for each case.

Both the `guess` variable and the `number` variable are integers but we
need them to be strings in order to {term}`concatenate` them in the message
we print at the of the game. To convert an int to a string use the
`str()` function.

### Edit `guess.py`

```{code-block} python
:caption: guess.py
:linenos:
:class: full-width
:emphasize-lines: "30-36"

"""This is a Guess the Number game."""
import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")
print()

for guess_count in range(1, max_guesses+1):
    print("Guess", guess_count, "of", max_guesses)

    guess = input("Your guess: ")
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        break

    print()


if guess == number:
    guess_count = str(guess_count)
    print("Good job, " + player + "! You guessed my number in " + guess_count + " guesses!")

else:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")
```


Part 7: Make it your own
------------------------

Change the game to make it your own. Here are some ideas.

- Check to see if the player name is your own. If it is, let yourself
  cheat by printing out the number.

- Make two lists of strings called `winner_messages` and `loser_messages`.
  Randomly choose an item from the appropriate list and print it at the
  end of the game. Hint: You can use the `len()` function to find the
  length of a list.

- Ask the user if they want to play on easy, normal or hard mode when they
  start, then change the number of guesses or the range of possible
  numbers based on their answer.

- Keep track of how far away each guess is from the right number. If they
  get further away, print out an extra message to let them know.

- Don't end after the player wins or loses, but instead offer them the
  chance to play again. Keep track of their wins, losses and total number
  of games played and print it at the end of each round.


What we've learned
------------------

- How to import a module and call its functions.
- How to convert between strings and integers.
- How to use the `range()` function in a for loop.
- How to pass a prompt argument to the `input()` function.
- How to pass multiple arguments to the `print()` function to
  easily print spaces between them.
