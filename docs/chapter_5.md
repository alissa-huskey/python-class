Chapter 5: Dragon Realm
=======================

> Based on: http://inventwithpython.com/invent4thed/chapter5.html

The game you will create in this chapter is called Dragon Realm. The player
decides between two caves, which hold either treasure or certain doom.

![demo](assets/dragon_realm.gif "demo")


Table of Contents
-----------------

- [Part 1: A Script Template: Shebang, Docstring, Scope](#part-1-a-script-template-shebang-docstring-scope)
- [Part 2: Print intro() and Keep Playing](#part-2-print-intro-and-keep-playing)
- [Part 3: Player, choose() a Cave](#part-3-player-choose-a-cave)
- [Part 4: Player, enter() Your Cave](#part-4-player-enter-your-cave)
- [Part 5: Prettier output with describe()](#part-5-prettier-output-with-describe)
- [Part 6: Wrap text using the textwrap module](#part-6-wrap-text-using-the-textwrap-module)
- [Part 7: Pick the Friendly Dragon](#part-7-pick-the-friendly-dragon)
- [Part 8: The Dragon Acts](#part-8-the-dragon-acts)


Part 1: A Script Template: Shebang, Docstring, Scope
----------------------------------------------------

[dragon_realm_part1.py](../computer-games/chapter_5/dragon_realm_part1.py)

We're going to start with a bare bones script that will serve as a template for
all future scripts.

Follow the instructions in [Repl.it Tips](replit-tips.md) to create
a new file called `dragon_realm.py` and change your `.replit` file to run it.

#### Edit Your Script

***dragon_realm.py***

```python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dragon Realm - A game where the player decides between two caves, which hold
  either treasure or certain doom.
  Inspired by: http://inventwithpython.com/invent4thed/chapter5.html
"""


def main():
    """The Dragon Realm Game"""
    print("Welcome to Dragon Realm!")


# this means that if this script is executed, then
# the main() function will be called
if __name__ == '__main__':
    main()
```

#### Shebang, Encoding

The very first line of any executable file (script) is the ***shebang*** line.
The line starts with a `#!` then is immediately followed (without a space) by
the path to the interpreter. In this case it is telling the computer to run
this script using `python3`.

The next line tells Python (as well as some editors) what the ***encoding*** to
expect. That is, what kinds of characters. This line might be different if, for
example, we were going to include Chinese characters.

```python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

#### Docstrings

The first ***expression*** in a Python script should always be a
***Docstring***. A Docstring, surrounded by `"""` or `'''`, is similar to a
comment in that its contents will not be executed. Docstrings however, are
stored by the interpreter as documentation for a particular file, module,
class, or function.

```python3
"""
Dragon Realm - A game where the player decides between two caves, which hold
  either treasure or certain doom.
  Inspired by: http://inventwithpython.com/invent4thed/chapter5.html
"""
```

#### Scope, `__main__` and `main()`

Up until now we have been writing all our code in the body of the file. (Aside
from a few functions in the PyPet project.) This is what is referred to as the
***global scope*** or ***global namespace***.

Scope refers to the place where an identifier (variable or function) can be
used. When a varible is defined in the body of the file it is available to
everything in the file--globally. When a variable is defined in a function it
is only available to the code inside of that function.

It is a good idea to keep the amount of code in the global scope to a minimum.
This avoids problems like accedentally reusing the same variable name and
causing unintended results.

In order to achieve this, organize code into functions.  The convention is to
write a function called `main()` and call it when your script is executed.

Note that `main()` has a docstring too. This will describe the purpose of the
function.

```python3
def main():
    """The Dragon Realm Game"""
    print("Welcome to Dragon Realm!")


# this means that if this script is executed, then
# the main() function will be called
if __name__ == '__main__':
    main()
```


Part 2: Print `intro()` and Keep Playing
----------------------------------------

[dragon_realm_part2.py](../computer-games/chapter_5/dragon_realm_part2.py)

#### Edit Your Script

Add the `WIDTH` global variable, the `intro()` function, and change the
`main()` function.

***dragon_realm.py***

```python3
WIDTH = 60


def intro():
    """Display the introduction description to the player"""
    print("""You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.""")
    print()


def main():
    """Keep playing the game until the user doesn't say yes"""
    print("Welcome to Dragon Realm!")
    again = "yes"
    while again.lower() in ["y", "yes"]:
        print("-" * WIDTH, "\n")
        intro()
        again = input("Play again? ")
```

#### Global Variables

In programming a variable that cannot be changed is called a ***constant***.
Python does not provide any way to make sure that a variable is never changed,
but the convention is to define variables that you intend to never be changed
at the top of the file and to name them with `ALL_CAPS`.

Here we're defining the width of the screen (or really, just the line) to 60.

```python3
WIDTH = 60
```

#### Multiline Strings

The `intro()` function will print out a paragraph to the player that describes
the surroundings. It starts with a docstring to say what the function does.

Because the intro text is long it will be on several lines. One way to do this
is to use the same `"""` syntax of a docstring. This will retain all
whitespace--both newlines and indentation. That is why lines 4-6 of the
function are not indented. If they were, the indention would be printed too.

The intro string ends with a `\n`. The backslash (`\`) tells the interpreter
that the next character has special meaning. In this case, `\n` means add a
newline.

```python3
def intro():
    """Display the introduction description to the player"""
    print("""You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.\n""")
```

#### Objects and `str.lower()`

In Python, all values are ***objects***. An object is data that can have values
and functions attached to it. An objects values they are called
***attributes*** and its functions are called ***methods***.

Python provides a nifty way to find out more informatin about an object--the
`dir()` function. In your console start the Python shell by typing `python3`,
then try typing `dir("")` This will tell you all of the attributes and
functions available for strings. Then you can type `help(str.lower)` to get
more information about the `lower()` function.

```python3
again.lower()
```

#### Boolean and Membership Operators

In programming, sometimes we don't just want to see if something is the same as
something else, but the same as a couple of things. One way that we could do
this would be using the `or` boolean operator.

```python3
answer.lower() == "y" or answer.lower() == "yes"
```

But then answer.lower() would be called twice. Instead, we're going to use the
`in` membership operator. The syntax is `<value> in <sequence>` which will result
in a True or False value. It will check if the `value` is a member of the
`sequence`. In this case the sequence is a list of answers `["y", "yes"]`.

So the following is has exactly the same result as above.

```python3
again.lower() in ["y", "yes"]
```

#### Repeating with `*`

An easy way to repeat a string is by using the `*` operator. At your Python
shell, try typing `""hello " * 3"`.

Here, we use the `*` operator to repeat the `-` character to easily print a
line, then add an extra newline at the end.

```python3
print("-" * WIDTH, "\n")
```


Part 3: Player, `choose()` a Cave
---------------------------------

[dragon_realm_part3.py](../computer-games/chapter_5/dragon_realm_part3.py)

#### Edit Your Script

Add a global variable `CAVES` to the top of your script where
WIDTH is defined, then add the `choose()` and valid_cave()
functions.

***dragon_realm.py***

```python3
CAVES = ["right", "left"]


def valid_cave(response):
    """Return true if response is in the list of valid CAVES"""
    return response in CAVES


def choose():
    """Prompt the player to choose "right" or "left" then return response."""
    cave = ""
    while not valid_cave(cave):
        print("Do you enter the cave on the right or left?")
        cave = input("(right, left): ").lower()

        if cave in ["q", "quit", "exit"]:
            exit()

        if not valid_cave(cave):
            print('Type "right" or "left". \n')

    print()
    return cave
```

Then edit your `main()` function to add `cave = choose()`.


```python3
    while again.lower() in ["y", "yes"]:
        print("-" * WIDTH, "\n")
        intro()
        cave = choose()
        again = input("Play again? ")
```


Part 4: Player, `enter()` Your Cave
-----------------------------------

[dragon_realm_part4.py](../computer-games/chapter_5/dragon_realm_part4.py)

#### Edit Your Script

***dragon_realm.py***

Above your global variables, import the `time` module.

```python3
import time
```

Add a global variable `DELAY`

```python3
DELAY = 1
```

Add the `enter()` function

```python3
def enter(cave):
    messages = [
        "You approach the cave...",
        "It is dark and spooky...",
        "A large dragon jumps out in front of you!",
        "He opens his jaws and...",
    ]

    for message in messages:
        print(message)
        time.sleep(DELAY)
```

And change your `main()` function

```python3
    while again.lower() in ["y", "yes"]:
        print("-" * WIDTH, "\n")
        intro()
        cave = choose()
        enter(cave)
        again = input("Play again? ")
```


Part 5: Prettier output with `describe()`
-----------------------------------------

[dragon_realm_part5.py](../computer-games/chapter_5/dragon_realm_part5.py)

It is getting a little hard to tell which lines of the game are description and
which parts are prompts. Lets make that clearer by indenting the text. To do
that we're going to add a function `describe()` which we'll use to print that
is not related to getting input.

#### Edit Your Script

***dragon_realm.py***

Add a `describe()` function

```python3
def describe(message):
    print("  ", message)
```

Then change your `intro()` function to call it instead of `print()`.

The `wrap()` function strips trailing newlines, so remove the `\n` and add a
`print()` statement to the end of the function.

```python3
def intro():
    """Display the introduction description to the player"""
    describe("""You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.""")
    print()
```

And call `describe()` in your `message()` function

```python3
    for message in messages:
        describe(message)
        time.sleep(DELAY)
```


Part 6: Wrap text using the `textwrap` module
---------------------------------------------

[dragon_realm_part6.py](../computer-games/chapter_5/dragon_realm_part6.py)

That looks nicer, but the intro looks funky because only the first line is
indented. Let's fix that by using the `textwrap` module's `wrap()` function. It
takes two arguments, the string to wrap, and the width to wrap it to. It
returns a list, where each item in the list is one line of the string.

#### Edit Your Script

***dragon_realm.py***

Import the `textwrap` module

```python3
import textwrap
```

Add a global variable `WRAP`

```python3
WRAP = 50
```

Then change your `describe()` function

```python3
def describe(message):
    for line in textwrap.wrap(message, WRAP):
        print("  ", line)
```


Part 7: Pick the Friendly Dragon
--------------------------------

[dragon_realm_part7.py](../computer-games/chapter_5/dragon_realm_part7.py)

Next we need to randomly pick a dragon to be the friendly one.

#### Edit Your Script

***dragon_realm.py***

Import the `random` module

```python3
import random
```

Add a `is_friendly()` function

```python3
def is_friendly(dragon):
    """Return True if dragon is in the randomly chosen friendly one"""
    friendly = random.randint(0, 1)
    print("The friendly dragon is:", CAVES[friendly])
    return dragon == CAVES[friendly]
```

Add a line to the end of your `enter()` function to save the resulting value

```python3
nature = is_friendly(cave)
```

Part 8: The Dragon Acts
-----------------------

[dragon_realm_part8.py](../computer-games/chapter_5/dragon_realm_part8.py)

Finally, we'll tell the player what the dragon does.

#### Edit Your Script

***dragon_realm.py***

Add a `dragon()` function

```python3
def dragon(is_friendly):
    """Print the dragon action for a friendly or unfriendly dragon"""
    actions = {
        True: "Gives you his treasure!",
        False: "Gobbles you down in one bite!",
    }
    print()
    describe(actions[is_friendly])
    print()
```

Add a line to the end of your `enter()` function to call it

```python3
    dragon(nature)
```

Finally, Remove or comment out the `print()` line in your `is_friendly()` function

```python3
    #  print("The friendly dragon is:", CAVES[friendly])
```
