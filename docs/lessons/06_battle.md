PyPet Battle
============

The game you're going to make takes our old PyPets and has them battle until
one of them wins.

Table of Contents
-----------------

* [Part 1. A Brief Tour of the Console](#part-1-a-brief-tour-of-the-console)
* [Part 2. Update your repo](#part-2-update-your-repo)
* [Part 3. Create a New Script](#part-3-create-a-new-script)
* [Part 4: Make a function outline](#part-4-make-a-function-outline)
* [Part 5: pets module](#part-5-pets-module)
* [Part 6: Fill in the lotto() function](#part-6-fill-in-the-lotto-function)
* [Part 7: Fill in the intro() function](#part-7-fill-in-the-intro-function)
* [Part 8: Outline the fight() function](#part-8-outline-the-fight-function)
* [Part 9: Print the fighter health](#part-9-print-the-fighter-health)
* [Part 10: Choose who attacks](#part-10-choose-who-attacks)
* [Part 11: Attack](#part-11-attack)

Part 1. A Brief Tour of the Console
-----------------------------------

We've talked about the **Python Shell** -- it is an interface where you can
type in python code, and it will run it and print out the results.

When people use the term ***console***, ***command-line*** or ***shell***, they
mean the ***Operating System Shell***. Here the input we type is in a language
called ***bash*** then run by the underlying operating system.

### Part 1.1: Open "The Shell"

We're going to learn a new way to access the console, and that is using a
Repl.it feature they call "The Shell".  You can open it by by pressing
`ctrl+shift+S` or `cmd+shift+S`.

Go ahead and collapse the left two panes so you only see The Console and The
Shell panes.

You should see something like this in the new pane:

```bash
~$
```

This is the ***bash prompt***, which is the same thing you get in the Console
pane when you see `>`.


### Part 1.2: Anatomy of A Command

The most basic kind of command has the form of:

`<program-name> [<argument> <argument>...]`

For example, to start the Python shell we use the command:

```bash
python3
```

* `python3` is the name of the program
* in this case there are no arguments

Or, to run our PyPet script, the command would be:

```bash
python3 pypet.py
```

* `python3` is the program name
* `pypet.py` is an argument -- in this case, the filename for our script

This tells the Python Interpreter (`python3`) to run the code found inside the
file `pypet.py`.


This, by the way, is exactly how the Run button works. It reads our `.replit`
file and takes the value of the `run` variable inside of it, and sends it to
the bash prompt in the Console pane.


### Part 1.2: Subcommands and Flags

A program may take all sorts of arguments or none at all.

Some programs have their own set of commands, known as `subcommands`.

`git` is one such command. For example in the command:

```bash
git status
```

* `git` is the name of the program
* `status` is a subcommand argument

When an argument starts with a `-` or `--` it is called a ***flag*** or an
***option flag***. Usually this tells a program or its subcommand to set an
option so that it behaves in a certian way.

For example, in the command:

```bash
git diff --staged
```

* `git` is the name of the program
* `diff` is a subcommand argument
* `--staged` is an option flag argument

Flags take a number of common forms.

`git status -s               #` Short flags start with one dash (`-`) and a single letter
`git log --oneline           #` Long flags have two dashes (`--`) followed by a word
`git log --pretty=oneline    #` Sometimes option flags take a value following the equal sign (`=`)
`python3 -c 'print("hello")' #` Sometimes option flags take the next argument passed as a value


### Part 1.3: Common Arguments


* `-h` \| `--help` show usage information for this command
* `<program> help <subcommand>` show the usage information for the <subcommand>
* `-V` \| `--version` show the programs version
* `-v` \| `--verbose` print extra detailed information while running a command
* `-q` \| `--quiet` print less detailed information or none at all while running a command
* `--` this means that any arguments following it should not be considered options

### Part 1.2: Try Some Commands

Here are some commands. Pick a few and try them for yourself.

* `cal`
* `cal -h`
* `cal -3`
* `ncal -e`
* `file pypet.py`
* `whoami`
* `uname -a`
* `uptime`
* `date`
* `echo hello`

Part 2. Update your repo
------------------------

Before we start coding, we want to make sure there are no uncommitted changes.
Check this by using the `git status` command.

### Part 2.1: Review the Repo Status

#### In the Console or Shell:

```bash
~$ git status
On branch master
Your branch is behind 'origin/master' by 4 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
```

If you have no local changes it will say `nothing to commit`.

If there are new changes in the `remote` branch, it will say `Your branch is behind 'origin/master' by...`.

### Part 2.2: Pull any Changes

If there were changes to your remote branch `pull` them:

#### In the Version Control Pane

1. Click the Fork icon / Version Control link in the sidebar.

2. If there are any changes, you will see a `Pull` button. Click the Pull button.

Alternately, you could do this at the console:

#### In the Console or Shell

```bash
~$ git pull
Updating 19620c4..add2dea
Fast-forward
 .replit                       |  3 +--
 docs/git-concepts.md          | 98 ++++++++++++++++++++++++++++++++++++++++++-------------------------------
 docs/setup-version-control.md |  3 ---
 3 files changed, 57 insertions(+), 47 deletions(-)
```


Part 3. Create a New Script
----------------------------

First, we're going to create a new script based off of the template we worked
on in the Dragon Realm lesson.

### Part 3.1: Download the Template

#### In the Console:

We'll use a program called `curl` which is used to communicate with web
servers.

```bash
curl -O https://raw.githubusercontent.com/alissa-huskey/python-class/master/pythonclass/template.py
```

### Part 3.2 Commit & Push

Let's commit and push this right away.

#### In the Version Control Pane

1. Click the Fork icon / Version Control link in the sidebar.

2. Type a description in the `What did you change` text area like, `Add script template.`

3. Click the `commit & push` button.

### Part 3.3: Add the Script

Now we'll use the `cp` command to copy the script.

#### In the Console:

```bash
cp template.py battle.py
```

Then follow the instructions in [Repl.it Tips](replit-tips.md) to edit your
`.replit` file to point to your new script.

### Part 3.4: Basic script setup

Now let's change the script docstring on line `4` to a description of the game.
Copy these rules rules from here:

```python
"""
PyPet Battle Game:
* Two fighters are randomly chosen from a list of PETS, each starting with a
health of 100
* Print out details about the chosen fighters
* Each fighter takes a turn attacking the other until one fighter wins.
    - Each attack will have a description and do randomly selected amount of
    damage between 10-30
    - Each attack will print out the description of the attack, the damage it
    did, and the health of each fighter at the end of the turn
    - Whoever reaches 0 first loses and the other player wins.
* At the end of the game, announce the winner
"""
```

Change the docstring for the `main()` function on line `53`:

```python
"""PyPet Battle Game"""
```

And let's change the print statement in the `main()` function on line `54` to
something more fitting for this game like maybe:

```python
print("Welcome to the THUNDERDOME!")
```

Now run your script and let's see it go!


Part 4: Make a function outline
-------------------------------

We're going to approach this a little differently--we're going to take a guess
at what we think the game will look like and write minimal functions for those
parts. We're going to do a version of "write a function and call it", except
for now the functions will be placeholders where we will put future code.

If we look at the game description in the script docstring, we get a pretty
good idea of how the script might look.

### Part 4.1: Choose the fighters

We need a function that will choose two PETs and return them.

```python
"""
* Two fighters are randomly chosen from a list of PETS, each starting with a
health of 100
"""
```

Let's add a new line in `main()` under line `54` to call the new function.

I'll call my function `lotto()`, then I'll assign the results to a variable named `fighters`.

```python
def main():
    """PyPet Battle Game"""
    print("Welcome to the THUNDERDOME!")

    fighters = lotto()
```

Under the `Functions` comment line `37`, let's get rid of the template comments
on lines `39` through `47`.

Starting on the new line `39` add a comment header for `top-level game functions`.

Then add the `lotto()` function. For now, it will only have the docstring, and
return an empty list (`[]`).


```python
# ### top-level game functions ###
#

def lotto():
    """Return two randomly chosen PETs"""
    return []
```


### Part 4.2: Introduce the fighters

Next we'll need a function to introduce the fighters.

```python
"""
* Print out details about the chosen fighters
"""
```

Let's add a new line in `main()` under line `56` to call the new function.

I'll call this function `intro()` and it will take the list of `fighters` as an argument.

```python
def main():
    """PyPet Battle Game"""
    print("Welcome to the THUNDERDOME!")

    fighters = lotto()
    intro(fighters)
```

Under the end of the `lotto()` function on line `43` add the `intro()` function.

This function doesn't return anything, so this one will just have the docstring for now.

```python
def intro(fighters):
    """Takes a list of two PETs (fighters) and prints their details"""
    ...
```


### Part 4.3: The fight

Now the fighters fight!

```python
"""
* Each fighter takes a turn attacking the other until one fighter wins.
"""
```

We'll add a `fight()` function that that takes the list of fighters as an
argument. We'll assign the results to a variable named `winner`.

Let's add it to the `main()` function under line `60`.

```python
def main():
    """PyPet Battle Game"""
    print("Welcome to the THUNDERDOME!")

    fighters = lotto()
    intro(fighters)
    winner = fight(fighters)
```

Under the end of the `intro()` function on line `49` add the `fight()`
function. We know it will return a PET, so as a placeholder for now we'll
return an empty dictionary (`{}`).


```python
def fight(fighters):
    """Repeat rounds of the fight until one wins then
       Take a list of two PETs and return the winning PET"""
    return {}
```


### Part 4.4: Winner, winner

Now we wrap up the game by announcing the winner.

```python
"""
* At the end of the game, announce the winner
"""
```

We'll add an `endgame()` function that will take the `winner` as an argument.

Let's add it to the `main()` function under line `67`.

```python
def main():
    """PyPet Battle Game"""
    print("Welcome to the THUNDERDOME!")

    fighters = lotto()
    intro(fighters)
    winner = fight(fighters)
    endgame(winner)
```

Under the end of the `fight()` function on line `45` add the `endgame()`
function. We know it will return a PET, so as a placeholder for now we'll
return an empty dictionary (`{}`).


```python
def endgame(winner):
    """Takes a PET (winner) and announce that they won the fight"""
```


Now when you run your script you won't see any changes. But you will have a
pretty good idea of how the script will end up working and what each part will
do.


Part 5: `pets` module
---------------------

One of the handy things about code is that it is reusable. So we're going to
make a pets module that we could reuse in future projects.

#### Part 5.1: Create a `pets.py` file

Make a new file named `pets.py`. Add the shebang, the encoding line, and the
docstring. And copy the PICS dictionary into it.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pets Data"""

# a hash of pet pics
# species: pic
PICS = {
    'cat': "=^..^=",
    'fish': "<`)))><",
    'owl': "{O,o}",
    'snake': "_/\\__/\\_/--{ :>~",
    'bat': "/|\\^..^/|\\",
    'monkey': "@('_')@",
    'pig': "^(*(oo)*)^",
    'mouse': "<:3 )~~~",
    'bird': ",(u°)>",
    'cthulhu': "^(;,;)^",
    'fox': "-^^,--,~",
}
```

### Part 5.2: Add your pets list

In the pypet project, we wrote a list by adding one pet at a time.

```python
cat = {'name': "Flufosourus",
      'species': "cat"
}

fish = {'name': "Scaley",
        'species': "fish"
}

pets = [cat, fish]
```

We've also added simple strings or integers to lists all at once:

```python
caves = ["right, "left"]
```

We can also add dictionary items to a list all at once.

##### In `pets.py`

Add your list of pets to the end of your `pets.py` file. For this game we only
need the `name` and `species`.

```python
PETS = [
    {'name': "Flufosourus", 'species': "cat"},
    {'name': "Scaley", 'species': "fish"},
    {'name': "Count Chocula", 'species': "bat"},
    {'name': "Curious George", 'species': "monkey"},
]
```

### Part 5.3: Import your module

We're going to call `import` in a new way this time. The syntax is:

`from <module> import <item>`

This allows you to only import part of a module, and also imports it into the
global namespace. That means that when we refer to the imported functions (or
in this case, variables) we don't need to use the module name.

##### Edit `battle.py`

In the `Imports` section at the top of `battle.py` under line `30` add:

```python
from pets import PICS, PETS
```

Part 6: Fill in the `lotto()` function
--------------------------------------

Now let's start making the our functions actually do things, starting with the
`lotto()` function.

### Part 6.1: Import the `random` module

For it, we'll need to import the `random` module.

At the end of our `Imports` section under line `30` add a line to import our
well-known `random` module.

```python
import pets
import random
```

### Part 6.2: Write the `lotto()` function

Then we'll fill in the `lotto()` function.

First we'll use a new function `random.shuffle` to randomly reorder the contents
of the PETS list. Then we'll return a new list that contains the first two
elements of PETS.

The new `lotto()` function should look like this.

```python
def lotto():
    """Return two randomly chosen PETs"""
    # randomly reorder the PETS list
    random.shuffle(PETS)

    # return the first two items in the PETS list
    return [PETS[0], PETS[1]]
```

Run your script to make sure it works.


Part 7: Fill in the `intro()` function
--------------------------------------

Here's a preview of what our new `intro()` function will look like.

```python
def intro(fighters):
    """Takes a list of two PETs (fighters) and prints their details"""

    print("\n  Tonight...\n")
    time.sleep(DELAY)

    # announce the fighters
    header = f"*** {fighters[0]['name']} -vs- {fighters[1]['name']} ***"
    print(header.center(WIDTH, " "), "\n\n")

    # pause for input
    input("ARE YOU READY TO RUMBLE?!")
    print("." * WIDTH, "\n")
```

Now I'll explain.


### Part 7.1: Import `time`

We'll use the `time` module to add some suspense to our announcement. At the
end of the `Imports` section on like `31` add:

```python
import time
```

### Part 7.1: Add `DELAY` and `WIDTH`

Then we'll need `DELAY` and `WIDTH` global variables. Add these to the end of
the `Global Variables` section under line `34`.

```python
# the number of seconds to pause for dramatic effect
DELAY = 1

# the max width of the screen
WIDTH = 55
```

### Part 7.2: Print "Tonight..." then sleep

The first part of the `intro()` function prints out the word "Tonight..." then
calls the `time.sleep()` function.

Add this to the end of the `intro()` function on line `58`.

```python
    print("\n  Tonight...\n")
    time.sleep(DELAY)
```

### Part 7.3: Announce the fighters using f-strings

We've learned how to concatonate strings using the `+` opearator.

```python
greeting = "Good " + time_of_day + " to you."
```

Now we are going to learn about ***string interpolation***, where you embed a
code into a string. In Python, this is done with a special syntax called f-strings.

The string starts with the letter `f` immediately before the string. Then a
single quote or double quote as usual to start and end the string. Then any
code you want to embed (usually a variable name) is put inside of curley braces.

The same string from above could be written as:

```python
greeting = f"Good {time_of_day} to you."
```

Let's use this new syntax to make a variable called `header` that will contain
the names of the fighters.

At the end of the `intro()` function under line `62` add:

```python
    # announce the fighters
    header = f"*** {fighters[0]['name']} -vs- {fighters[1]['name']} ***"
```

To explain in a little more detail:

* `f"` starts the f-string
* `*** ` is part of the string literal
* `{` starts the code
* `fighters[0]` gets the first element of the fighters list
* `['name']` gets the `name` value from that pet's dictionary
* ` -vs - ` is part of the string literal
* `{` starts the code
* `fighters[1]` gets the second element of the fighters list
* `['name']` gets the `name` value from that pet's dictionary
* ` ***` is part of the string literal
* `"` ends the f-string

So of our fighters list looked like this:

```python
fighters = [
  { 'name': "Ol' Yeller" },
  { 'name': "Curious George" },
]
```

Then the value of the `header` variable would be:

```python
*** Ol' Yeller -vs- Curious George ***
```

### Part 7.4: Print the announcement using `str.center()`

Python has a handy function on the `str` object for centering text. It takes
a width argument, for the total length of the resulting string.  We'll use the
`WIDTH` variable defined earlier.

Finally, we'll add two newlines (`\n`) to the end of the print statement.

At the end of the `intro()` function under line `64` add:

```python
    print(header.center(WIDTH), "\n\n")
```

### Part 7.5: Pause for input

Let's give the player a chance to do something before the game continues.  We
won't actually do anything with the player feedback in this game. We just want
to give the player something to do.

We'll call the `input()` function with a prompt.

At the end of the `intro()` function under line `64` add:

```python
# pause for input
input("ARE YOU READY TO RUMBLE?!")
```

### Part 7.6: Draw a line

Python has a neat way to repeat a string, with the `*` opeartor. We'll use this
handy trick to easily draw a line of a particular size. In this case, we'll
make the line out of dots (`.`) just to mix it up. Then we'll add an extra
newline (`\n`) at the end of the print statement.

At the end of the `intro()` function under line `64` add:

```python
print("." * WIDTH, "\n")
```

Run your script and see what you've got!


Part 8: Outline the `fight()` function
-------------

The `fight()` function has a lot to do, so we'll start by writing a bit of an
outline for it.

Here's a preview of the `fight()` function for now:

```python
def fight(fighters):
    """Repeat rounds of the fight until one wins then
       Take a list of two PETs and return the winning PET"""

    winner = None

    # ### rounds of the fight
    #
    while winner is None:

        # check for a loser (placeholder)
        winner = random.choice(fighters)

        # print a line at the end of every round
        print("-" * WIDTH, "\n")

    #
    # ### end of fighting rounds

    # return the winner
    return winner
```


### 8.1: The `None` type

Python has a special type called `None`, which is what is known in programming
as a ***null*** value.

Sometimes we need to know the difference between a value set to nothing, and
when it is set to zero or an empty string.

Imagine we had a program that would print out how many apples the user had. If
the program didn't know how many apples, it would ask them.

We would need to be able to tell if the user had told us that they had zero
apples, or if the user hadn't yet told us how many they have. That's where
`None` comes in.

Here is a handy picture to help clarify.

![Null Visualization](null.png "Null as described by toilet paper")

##### Edit `battle.py`

Start your `fight() function by setting the variable `winner` to `None`.

```python
    winner = None
```


### Part 8.2: Keep going until there's a winnner

We're going to write a `while` loop, using the `None` type.

Remember, a `while` loop is like an `if` statement, except it keeps repeating
for as long as the condition is met.

The condition of this `while` loop is `winner is None`.

##### Edit `pets.py`

Add to your `fight()` function:

```python
    while winner is None:
```

### Part 8.3: Add a placeholder winner


Just so we can test our script without looping forever, we'll put a placeholder
in the loop that randomly selects a winner from our list of `fighters`. (This
means that the loop will only run once for now.)

We'll use the `random.choice()` function, which randomly selects an element
from a list.

##### Edit `pets.py`

Add to your `fight()` function inside the `while` loop:

```python
# check for a loser (placeholder)
winner = random.choice(fighters)
```

### Part 8.4: Print a round-end line

So we can see that when a round happens, we'll add a line at the end of every loop.

##### Edit `pets.py`

Add to your `fight()` function inside the `while` loop:

```python
# print a line at the end of every round
print("-" * WIDTH, "\n")
```

### Part 8.5: return the `winner`

Finally, add a comment showing where the fighting rounds end, then change the
return line to `return winner`.

##### Edit `battle.py`

This is how the end of the `fight()` function should look (trimmed):

```python
def fight(fighters):
    # ### rounds of the fight
    #
    while winner is None:

    ...

    #
    # ### end of fighting rounds

    # return the winner
    return winner
```


Part 9: Print the fighter health
--------------------------------

Let's continue filling out the `fight()` function.

### Part 9.1: Print each fighter's info

We'll want to print out the health for each fighter at the end of every round.
We'll use a `for` loop to loop through each fighter, then we'll want a function
that will handle printing out the information. Let's call it `show()`.

Add this in the `fight()` function under the `winner =` placeholder on line `100`.

```python
# print updated fighter health
print()
for combatant in fighters:
    show(combatant)
```

### Part 9.2: Add the `show()` function

At the top of the `Functions` section under line `44, let's add a new comment
section for `pet functions`.

Then add a placeholder functions for `setup()` and `show()`.

```python
# ### pet functions ###
#


def show(pet):
    """Takes a pet and prints health and details about them"""
```


def setup(pets):
    """Takes a list of pets and sets initial attributes"""


### Part 9.3: `MAX_HEALTH`

It looks like we'll need a `MAX_HEALTH` variable. At the end of the `Global
Variables` section under line `42` add:

```python
MAX_HEALTH = 100
```

### Part 9.5: Initialize fighter health

Turns out we'll also need to set the fighter's health and pic. We'll add a new
function called `setup()`, and we'll call it from `main()` right before we call
`fight()`.

##### Edit `battle.py`

This is what the new `main()` function should look like.

```python
def main():
    """PyPet Battle Game"""
    print("\nWelcome to the THUNDERDOME!")

    fighters = lotto()
    setup(fighters)

    intro(fighters)
    winner = fight(fighters)
    endgame(winner)
```

### Part 9.4: Fill in the `setup()` function

In the `setup()` function, we'll uses a `for` loop to loop through the list of
`pets`. (The `fighters` passed from ) `main()`.

For each pet, we'll set the `health` to `MAX_HEALTH`.

Then we're going to use the `species` value to get the `pic` from the `PICS`
dictionary in the `pets` module.


##### Edit `battle.py`

```python
def setup(pets):
    """Takes a list of pets and sets initial attributes"""
    for pet in pets:
        pet['health'] = MAX_HEALTH
        pet['pic'] = PICS[pet['species']]
```

The syntax for geetting the `pic` might look a little confusing.

```python
`PICS[pet['species']]`
```

This is the same as:

```python
species = pet['species']
`PICS[species]`
```


### Part 9.4: Fill in the `show()` function

Now we can print the name, pic and health.

At the end of the `show()` function set a `name_display` variable that will
store out the `pet['name']` and `pet['pic']`, and a `health_display` variable
that will store their `x of y` health. Finally, print each variable.


```python
def show(pet):
    """Takes a pet and prints health and details about them"""
    name_display = f"{pet['name']} {pet['pic']}"
    health_display = f"{pet['health']} of {MAX_HEALTH}"
    print(name_display, health_display)
```


### Part 9.5: Make columns with `str.rjust()`

Now to get a little fancy let's right-align the health display using the
`str.rjust()` function. Like `str.center()` it takes a width variable.

To calculate the `rjust()` width, take the length of the `name_display`
variable and subtract it from `WIDTH`. Then subtract `1` more, to account for
the space that `print()` will add.

Under line `59` add:

```python
rcol_width = WIDTH - len(name_display) - 1
```

Then change the `print()` line on line `61 to add the `rjust()` call to the end
of the `health_display` variable:

```python
    print(name_display, health_display.rjust(rcol_width))
```

The `show()` function should now look like this:

```python
def show(pet):
    """Takes a pet and prints health and details about them"""
    name_display = f"{pet['name']} {pet['pic']}"
    health_display = f"{pet['health']} of {MAX_HEALTH}"
    rcol_width = WIDTH - len(name_display) - 1
    print(name_display, health_display.rjust(rcol_width))
```

Now run the script and see how it looks.

Part 10: Choose who attacks
---------------------------

Continuing with the `fight()` function, we need switch back and forth between
the two fighters for who attacks each round.

Here's a preview of the updated `fight()` function:

```python
def fight(fighters):
    """Repeat rounds of the fight until one wins then
       Take a list of two PETs and return the winning PET"""

    # winning fighter
    winner = None

    # the index in the fighters list of the attacker in each round
    current = 0

    # ### rounds of the fight
    #
    while winner is None:
        # set the roles for this round
        #
        # `not <value>` is a handy way to switch 0 and 1
        #   it is the same as `<value> == False`
        attacker = fighters[current]
        rival = fighters[not current]

        # pause for input
        input(f"\n{attacker['name']} FIGHT>")

        # check for a loser (placeholder)
        winner = random.choice(fighters)

        # print updated fighter health
        print()
        for combatant in fighters:
            show(combatant)

        # print a line at the end of every round
        print("-" * WIDTH, "\n")

        # flip current to the other fighter for the next round
        current = not current


    #
    # ### end of fighting rounds

    # return the winner
    return winner
```

### Part 10.1: Set a `current` variable

We're going to use a variable `current` to keep track of the index number in
the `fighters` list of the current attacker.

Remember, lists have index numbers that start at 0. and can be accessed like
this: `mylist[0]`.


##### Edit `battle.py`

Add the `current` variable to the top of the `fight()` function, before the
`while` loop and set it to `0`.

```python
# the index in the fighters list of the attacker in each round
current = 0
```

### 10.2: Pick the `attacker` and `rival`

We've used the `not` operator in if statements before. The `not` operator can
also be used to switch between `1` and `0` values. Here's how it works.

The `not` operator is shorthand for `False ==`.
And recall that `True` is equal to `1`
And `False` is equal to 0.

So `not 0`
is the same as `False == 0`

And `not 1`
is the same as `False == 1`

If you run these in the Python Shell, you'll see:

```python
>>> False == 0
True
>>> not 0
True
>>> False == 1
False
>>> not 1
False
>>>
```

Which means `not 1` always evaluates to `0`
and `not 0` always evalutes to `1`.

---

We're going to use this trick to pick who attacks for each round. 

We'll set the `attacker` to `fighters[current]` and the `rival` to
`fighters[not current]`.


##### Edit `battle.py`

In the `fight()` function, at the `top of the `while` loop under line `104`
add:

```python
# set the roles for this round
#
# `not <value>` is a handy way to switch 0 and 1
#   it is the same as `<value> == False`
attacker = fighters[current]
rival = fighters[not current]
```

### Part 10.2: Switch fighter's turn

We'll use the `not` trick again at the end of the `while` loop to switch back
and forth between the two fighters.

##### Edit `battle.py`

In the `fight()` function at the end of the `while` loop, under line `121` add:

```python
# flip current to the other fighter for the next round
current = not current
```

### Part 10.3: Print the attacker

Finally we want to print out the attacker for each round. We prompt for input
again, but once again this is just to give the player a chance to do
something--we don't do anything with the input.


##### Edit `battle.py`

In the `fight()` function just under the `rival =` line, add:

```python
# pause for input
input(f"\n{attacker['name']} FIGHT>")
```

Now run your script!

Part 11: Attack
---------------

Preview of code:

```python
# ### game event functions ###
#

def attack(foe):
    """Inflict a random amount of damage is inflicted on foe, then return the
       damage and attack used"""
    return 10, "smacks upside the head"
...

def fight(fighters):
    """Repeat rounds of the fight until one wins then
       Take a list of two PETs and return the winning PET"""

    # winning fighter
    winner = None

    # the index in the fighters list of the attacker in each round
    current = 0

    # ### rounds of the fight
    #
    while winner is None:
        # set the roles for this round
        #
        # `not <value>` is a handy way to switch 0 and 1
        #   it is the same as `<value> == False`
        attacker = fighters[current]
        rival = fighters[not current]

        # pause for input
        input(f"\n{attacker['name']} FIGHT>")

        # the attack
        damage, act = attack(rival)

        # pause for effect, then print attack details
        time.sleep(DELAY)
        print(f"\n  {attacker['name']} {act} {rival['name']}...\n")

        # pause for effect, then print damage
        time.sleep(DELAY)
        print(f"-{damage} {rival['name']}".center(WIDTH), "\n")

        # one more pause before the round ends
        time.sleep(DELAY)

        # check for a loser (placeholder)
        winner = random.choice(fighters)

        # print updated fighter health
        print()
        for combatant in fighters:
            show(combatant)

        # print a line at the end of every round
        print("-" * WIDTH, "\n")

        # flip current to the other fighter for the next round
        current = not current

    #
    # ### end of fighting rounds

    # return the winner
    return winner

```

### Part 11.1: The `attack()` function

We'll need a function that picks what kind of attack to do, calculates damage
the damage and modifies the `health` of the `rival`.

We're going to call this the `attack()` function, which will take one argument,
the `rival`.

##### Edit `battle.py`

In the `fight()` function just under the attacker prompt on line `122` add:

```python
# the attack
damage, act = attack(rival)
```

### Part 11.2: Add the placeholder `attack()` functoin

Then let's add a placholder `attack()` function. We'll have it return some
hardcoded values until we fill in the rest.


##### Edit `battle.py`

Under the `Functions` section, add a new subsection for `game event functions`.

Add the `attack` function in this new subsection. Have it return a hardcoded
damage value and string for the attack description.

```python
# ### game event functions ###
#

def attack(foe):
    """Inflict a random amount of damage is inflicted on foe, then return the
       damage and attack used"""
    return 10, "smacks upside the head"
```

---

Python functions can return nothing, a single value, or more than one values.
In this case, we're returning both the damage amount, and the attack descripton.

The syntax when returning multple values is: `return <val1>, <val2>`.

The syntax when assigning the results is: `<var1>, <var2> = fun()`

### Part 11.3: Print attack details

Now we just need to print out all of the details of the attack.

##### Edit `battle.py`

In the `fight()` function under the `attack()` statement on line `125` add:

```python
# pause for effect, then print attack details
time.sleep(DELAY)
print(f"\n  {attacker['name']} {act} {rival['name']}...\n")

# pause for effect, then print damage
time.sleep(DELAY)
print(f"-{damage} {rival['name']}".center(WIDTH), "\n")

# one more pause before the round ends
time.sleep(DELAY)
```
