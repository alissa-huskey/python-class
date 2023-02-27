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
PyPet Battle
============

```{div} float-right
{{ code.format("battle.py", "lessons/battle.py") }}
```

The game you're going to make takes our old PyPets and has them battle until
one of them wins.

```{include} ../toc.md
```

Part 1. Create a New Script
----------------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part01.py") }}
```

First, we're going to create a new script based off of the template we worked
on in the Dragon Realm lesson.

### Part 1.1: Download the Template

**In the Console**

We'll use a program called `curl` which is used to communicate with web
servers.

```bash
curl -O https://raw.githubusercontent.com/alissa-huskey/python-class/master/pythonclass/template.py
```

### Part 1.2: Add the Script

Now we'll use the `cp` command to copy the script.

**In the Console**

```bash
cp template.py battle.py
```

Then follow the instructions in [Repl.it Tips](../tools/replit.md) to edit your
`.replit` file to point to your new script.

### Part 1.3: Basic script setup

Now let's change the script docstring at the beginning of the file to a
description of the game. Copy these rules rules from here:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part01.py
:caption: "battle.py: docstring"
:start-at: '"""'
:end-before: "# The convention"
:linenos:
:lineno-match:
```

Change the docstring for the `main()` function:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part01.py
:caption: "battle.py: main()"
:start-at: "def main"
:end-before: "print"
:linenos:
:lineno-match:
:emphasize-lines: 2
```

And let's change the print statement in the `main()` function to
something more fitting for this game like maybe:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part01.py
:caption: "battle.py: main()"
:start-at: "def main"
:end-at: "print"
:linenos:
:lineno-match:
:emphasize-lines: 3
```

Now run your script and let's see it go!


Part 2. Make a function outline
-------------------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part02.py") }}
```

We're going to approach this a little differently--we're going to take a guess
at what we think the game will look like and write minimal functions for those
parts. We're going to do a version of "write a function and call it", except
for now the functions will be placeholders where we will put future code.

If we look at the game description in the script docstring, we get a pretty
good idea of how the script might look.

### Part 2.1: Choose the fighters

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: task for this section"
:start-at: "Two fighters are randomly"
:end-before: "[ ]"
:emphasize-lines: "1-"
```

We need a function that will choose two items from the `PETS` list and return
them.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: lotto()"
:start-at: "def lotto"
:end-at: Return two
:lineno-match:
```

In `main()` add a line to call the new `lotto()` function, then assign the
results to a variable named `fighters`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: main()"
:start-at: "def main"
:end-at: "fighters ="
:lineno-match:
:emphasize-lines: 5
```

Let's get rid of the rest of the comments under the `# Functions` comment line,
then add a new comment heading under it: `top-level game functions`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: comment headers"
:start-at: "# Functions"
:end-before: "def"
:lineno-match:
:emphasize-lines: 3
```

Then add the `lotto()` function. For now, it will only have the docstring, and
return an empty list (`[]`).

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: lotto()"
:pyobject: lotto
:linenos:
:lineno-match:
:emphasize-lines: 3
```

### Part 2.2: Introduce the fighters

Next we'll need a function to introduce the fighters.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: task for this section"
:start-at: "Print out details about the chosen fighters"
:end-before: "[ ]"
:emphasize-lines: 1-
```

Under the end of the `lotto()` function add an `intro()` function, which will
take one argument `fighters`. This function won't return anything so it one
will just contain the docstring for now.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: intro()"
:pyobject: intro
:linenos:
:lineno-match:
```

In `main()` add a line to call the new `intro()` function with the argument
`fighters`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: main()"
:start-at: "def main"
:end-at: "intro(fighters)"
:linenos:
:lineno-match:
:emphasize-lines: 6
```

### Part 2.3: The fight

Now the fighters fight!

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: task for this section"
:start-at: "Each fighter takes a turn"
:end-before: "- Each"
:emphasize-lines: 1-
```

Add a `fight()` function that that takes the list of fighters as an argument.
We know it will return a dictionary from the `PET` list, so as a placeholder
return an empty dictionary (`{}`).

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: fight()"
:pyobject: fight
:linenos:
:lineno-match:
```

Let's add it to the `main()` function add a line to call our new `fight()`
function and assign the results to a variable named `winner`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: main()"
:start-at: "def main"
:end-at: "winner ="
:linenos:
:lineno-match:
:emphasize-lines: 7
```

### Part 2.4: Winner, winner

Now we wrap up the game by announcing the winner.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: task for this section"
:start-at: "At the end"
:end-before: '"""'
:emphasize-lines: "1-"
```

Add an `endgame()` function that will take the `winner` as an argument. We know
it will return a dictionary from the `PET` list, so as a placeholder return an
empty dictionary (`{}`).

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: endgame()"
:pyobject: endgame
:linenos:
:lineno-match:
```

In `main()` add a line to call the new `endgame()` function with the argument
`winner`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part02.py
:caption: "battle.py: main()"
:pyobject: main
:linenos:
:lineno-match:
:emphasize-lines: 8
```

By now you should have a pretty good idea of how the script will end up working
and what each part will do.

Even though you won't expect to see any changes in output go ahead and run your
script anyway to make sure there are no errors.

Part 3. `pets` module
---------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part03.py") }}
{{ code.format("pets.py", "lessons/pets.py") }}
```

One of the handy things about code is that it is reusable. So we're going to
make a pets module that we could reuse in future projects.

### Part 3.1: Create a `pets.py` file

Make a new file named `pets.py`. Add a docstring then copy the following `PICS`
dictionary into it.

```{literalinclude} ../../pythonclass/lessons/pets.py
:caption: "pets.py"
:end-before: "PETS ="
:linenos:
:lineno-match:
```

### Part 3.2: Add your pets list

#### A. Review

By now you know how to add simple strings or integers to lists:

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm.py
:caption: "dragon_realm.py"
:start-at: CAVES
:end-at: CAVES
:linenos:
:lineno-match:
```

In the pypet project, you also learned how to add dictionary items to a list
using variables.

```{literalinclude} ../../pythonclass/lessons/pypet.py
:caption: "pypet.py"
:start-at: "cat ="
:end-at: "pets ="
:linenos:
:lineno-match:
```

In the next section we'll learn how to make a nested list of literal
dictionaries.

#### B. Nested lists

We could add our list of pets the same way we did in the pypet game.

```{code-block} python
:caption: example
:linenos:
FLUFO = {"name": "Flufo"}
SCALEY = {"name": "Scaley"}

PETS = [FLUFO, SCALEY]
```

You can also embed dictionaries in a list without using variables by putting
the dictionary where you would have put the variable otherwise.

```{code-block} python
:caption: example
:linenos:
PETS = [{"name": "Flufo"}, {"name": "Scaley"}]
```

When you're dealing with a nested list or dictionary it's a good idea to split
up the list items so that each dictionary item is on a line of its own. This
makes it a lot easier to read.

```{code-block} python
:caption: example
:linenos:
PETS = [
  {"name": "Flufo"},
  {"name": "Scaley"}
]
```

In all three of the above examples the `PETS` list is exactly the same.

You can access an element of a nested list the way you normally would with the
syntax `variable[index]`.

```{code-block} python
:caption: example
:linenos:
:lineno-start: 5

pet = PETS[3]
print(pet['name'], "says hello!")
```

You can access also access nested dictionary values from a list by adding the
`[]` reference straight to the end of the previous `[]` with the syntax
`variable[index][key]`.

```{code-block} python
:caption: example
:linenos:
:lineno-start: 5

print(PETS[3]['name'], "says hello!")
```

#### C. In `pets.py`

Use what you just learned to add pet dictionaries to a list named `PETS` in
`pets.py`. Each dictionary should have the keys `name` and `species`.

```{literalinclude} ../../pythonclass/lessons/pets.py
:caption: "pets.py"
:start-at: "PETS ="
:end-at: "]"
:linenos:
:lineno-match:
```

### Part 3.3: Import your module

In order to use `PICS` and `PETS` in your battle game you'll need to import
them.

#### A. Partial imports

By now you know how to import a whole module at once using the import
statement. And you know that to access the things in that module you use the
syntax `module.object`.

```{code-block} python
:caption: example
:linenos:
import random

number = random.randint(0, 100)
```

You can also import objects one at a time from a module with the syntax:

`from <module> import <object>`

This allows you to only import part of a module, and also imports it into the
global namespace. That means that when we refer to the imported functions (or
in this case, variables) we don't need to use the module name.

```{code-block} python
:caption: example
:linenos:
from random import randint

number = randint(0, 100)
```

#### B. At the top of `battle.py`

Now import `PICS` and `PETS` in the `# Imports` section at the top of
`battle.py`:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part03.py
:caption: "battle.py: imports"
:start-at: "# Imports"
:end-at: "from pets import"
:linenos:
:lineno-match:
:emphasize-lines: 3
```

Part 4. Fill in the `lotto()` function
--------------------------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part04.py") }}
```

Now let's start making the our functions actually do things, starting with the
`lotto()` function.

### Part 4.1: Import the `random` module

We'll need the `random` module in the `lotto()` function.

At the end of our `Imports` section add a line to import it.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part04.py
:caption: "battle.py: imports"
:start-at: "# Imports"
:end-at: "import random"
:linenos:
:lineno-match:
:emphasize-lines: 4
```

### Part 4.2: Write the `lotto()` function

Then we'll fill in the `lotto()` function.

First we'll use a new function `random.shuffle` to randomly reorder the contents
of the PETS list. Then we'll return a new list that contains the first two
elements of PETS.

The new `lotto()` function should look like this.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part04.py
:caption: "battle.py: lotto()"
:pyobject: lotto
:linenos:
:lineno-match:
```

Run your script to make sure it works.


Part 5. Fill in the `intro()` function
--------------------------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part05.py") }}
```

Here's a preview of what our new `intro()` function will look like when we're
done.

:::{dropdown} intro()

```{literalinclude} ../../pythonclass/lessons/battle/battle_part05.py
:caption: "battle.py: intro()"
:pyobject: intro
:linenos:
:lineno-match:
```

:::

### Part 5.1: Import `time`

We'll use the `time` module to add some suspense to our announcement. At the
end of the `# Imports` section add:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part05.py
:caption: "battle.py: imports"
:start-at: "# Imports"
:end-at: "import time"
:linenos:
:lineno-match:
:emphasize-lines: 5
```

### Part 5.2: Add `DELAY` and `WIDTH`

Then we'll need `DELAY` and `WIDTH` global variables. Add these to the end of
the `# Global Variables` section.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part05.py
:caption: "battle.py: global variables"
:start-at: "# Global"
:end-at: "WIDTH ="
:linenos:
:lineno-match:
:emphasize-lines: "3-7"
```


### Part 5.3: Print "Tonight..." then sleep

The first part of the `intro()` function prints out the word "Tonight..." then
calls the `time.sleep()` function.

Add this to the end of the `intro()` function.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part05.py
:caption: "battle.py: intro()"
:start-at: "def intro"
:end-at: "time.sleep"
:emphasize-lines: "4-5"
```

### Part 5.4: Announce the fighters using f-strings

#### A. f-strings

We've learned how to {term}`concatenate` strings using the `+` operator.

```{code-block} python
:caption: example
greeting = "Good " + time_of_day + " to you."
```

Now we are going to learn about {term}`string interpolation` which means to
embed code in a string. In Python, this is done with a special syntax called
f-strings.

The string starts with the letter `f` immediately before the string. A single
quote or double quote as usual starts and ends the string. And here's the fancy
part: any code you want to embed (usually a variable name) is put inside of
curly braces.

The same string from above could be written as:

```{code-block} python
:caption: example
:linenos:
greeting = f"Good {time_of_day} to you."
```

#### B. In `intro()`

Let's use this new syntax to make a variable called `header` that will contain
the names of the fighters.

At the end of the `intro()` add the following

```{literalinclude} ../../pythonclass/lessons/battle/battle_part05.py
:caption: "battle.py: intro()"
:start-at: "def intro"
:end-at: "header ="
:linenos:
:lineno-match:
:emphasize-lines: "7-8"
```

There's a lot going on in that f-string, so let's go through it in detail.

* `f"` starts the f-string
* `*** ` is a literal string
* `{` starts the code
* `fighters[0]` gets the first element of the fighters list
* `['name']` gets the `name` value from that pet's dictionary
* ` -vs - ` is a literal string
* `{` starts the code
* `fighters[1]` gets the second element of the fighters list
* `['name']` gets the `name` value from that pet's dictionary
* ` ***` is a literal string
* `"` ends the f-string

So of our fighters list contained:

```{code-block} python
:caption: "example: `fighters` list"
fighters = [
  { 'name': "Curious George" },
  { 'name': "Ol' Yeller" },
]
```

Then the value of the `header` variable would be:

```{code-block} text
:caption: "example: value of `header` variable"
*** Ol' Yeller -vs- Curious George ***
```

### Part 5.5: Print the announcement using `str.center()`

Python has a handy function on `str` objects for centering text. It takes a
width argument, for the total length of the resulting string.  We'll use the
`WIDTH` variable defined earlier.

Finally, we'll add two newlines (`\n`) to the end of the print statement.

At the end of the `intro()` function add the following:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part05.py
:caption: "battle.py: intro()"
:start-at: "def intro"
:end-at: "print(header"
:linenos:
:lineno-match:
:emphasize-lines: "9"
```

### Part 5.6: Pause for input

Let's give the player a chance to do something before the game continues.  We
won't actually do anything with the player feedback in this game. We just want
to give the player something to do.

We'll call the `input()` function with a prompt.

At the end of the `intro()` function add:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part05.py
:caption: "battle.py: intro()"
:start-at: "def intro"
:end-at: "input("
:linenos:
:lineno-match:
:emphasize-lines: "11-12"
```

### Part 5.7: Draw a line

Python has a neat way to repeat a string, with the `*` operator. We'll use this
handy trick to easily draw a line of a particular size. In this case, we'll
make the line out of dots (`.`) just to mix it up. Then we'll add an extra
newline (`\n`) at the end of the print statement.

At the end of the `intro()` function under line `64` add:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part05.py
:caption: "battle.py: intro()"
:pyobject: intro
:linenos:
:lineno-match:
:emphasize-lines: "13"
```

Run your script and see what you've got!


Part 6. Outline the `fight()` function
-------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part06.py") }}
```

The `fight()` function has a lot to do, so we'll start by writing a bit of an
outline for it.

Here's a preview of what those functions will look like when we're done.


:::{dropdown} fight()

```{literalinclude} ../../pythonclass/lessons/battle/battle_part06.py
:caption: "battle.py: fight()"
:pyobject: fight
:linenos:
:lineno-match:
```

:::


### Part 6.1: The `None` type

#### A. Null values

Python has a special type called `None`, which is what is known in programming
as a {term}`null` value.

Sometimes we need to know the difference between a value set to nothing, and
when it is set to zero or an empty string.

Imagine we had a program that would print out how many apples the user had. If
the program didn't know how many apples, it would ask them.

We would need to be able to tell if the user had told us that they had zero
apples, or if the user hadn't yet told us how many they have. That's where
`None` comes in.

Here is a handy picture to help clarify.

![Null Visualization](../assets/null.png "Null as described by toilet paper")

#### B. In `fight()`

Start your `fight()` function by setting the variable `winner` to `None`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part06.py
:caption: "battle.py: fight()"
:start-at: def fight
:end-at: "winner ="
:linenos:
:lineno-match:
:emphasize-lines: 5
```


### Part 6.2: Keep going until there's a winner

We're going to write a `while` loop to keep fighting until there's a winner.
We'll use the `None` type to tell that there is still no winner.

#### A. `while` loops

A `while` loop is a {term}`conditional statement`. That means that, like an
{term}`if statement` it uses a {term}`condition` to decide what to do with the
block of code that belongs to it.

But where an `if` statement will only execute its code block if the condition
is met, a `while` loop will keep repeating its code block for as long as the
condition is met.

{{ leftcol }}

```{code-block} python
:caption: "example: if statement"
:linenos:
i = random.randint(0, 100)

if i < 50:
  print(f"You have: {i}")
```

{{ rightcol }}

```{code-block} python
:caption: "example: while loop"
:linenos:
i = 0

while i < 50:
  i = i + 1
  print(f"You have: {i}")
```

{{ newrow }}

In this if statement `i` would be printed once, and only if it happened to be less
than `50`.

{{ rightcol }}

In this while loop `i` would be printed over and over again until it reaches
`50`.

{{ endcols }}

#### B. In `fight()`

We're going to use a `while` loop to keep going for as long as the value of `winner` is `None`.

Add to your `fight()` function:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part06.py
:caption: "battle.py: fight()"
:start-at: def fight
:end-at: "while winner"
:linenos:
:lineno-match:
:emphasize-lines: "7-9"
```

### Part 6.3: Add a placeholder winner


Just so we can test our script without looping forever, we'll put a placeholder
in the loop that randomly selects a winner from our list of `fighters`. (This
means that the loop will only run once for now.)

We'll use the `random.choice()` function, which randomly selects an element
from a list.

#### In `fight()`

Add to your `fight()` function inside the `while` loop:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part06.py
:caption: "battle.py: fight()"
:start-at: def fight
:end-at: "winner = random"
:linenos:
:lineno-match:
:emphasize-lines: "11-12"
```

### Part 6.4: Print a round-end line

So we can see that when a round happens, we'll add a line at the end of every loop.

#### In `fight()`

Add to your `fight()` function inside the `while` loop:

```{literalinclude} ../../pythonclass/lessons/battle/battle_part06.py
:caption: "battle.py: fight()"
:start-at: def fight
:end-at: "print("
:linenos:
:lineno-match:
:emphasize-lines: "14-15"
```

### Part 6.5: return the `winner`

#### A. In `fight()`, around the while loop

Add comments at the beginning and end of the while loop so we can tell where
the code is that executes each round.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part06.py
:caption: "battle.py: fight()"
:start-at: "def fight"
:end-at: "# end of"
:linenos:
:lineno-match:
:emphasize-lines: "7-8, 17-18"
```

#### B. In `fight()`, after the while loop

Now change the last line of your function to return `winner` instead of an
empty dictionary.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part06.py
:caption: "battle.py: fight()"
:pyobject: fight
:linenos:
:lineno-match:
:emphasize-lines: "20-21"
```

Notice that the return statement is *outside* of the while loop. That is
because we want to make sure that all the rounds are finished before exiting
the function.

Part 7. Print the fighter health
--------------------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part07.py") }}
```

In this section we will print out the fighters health for each round. Here's
what the game output will look like when we're done:

```{code-block} text
:caption: output
Welcome to the THUNDERDOME!

  Tonight...

       *** Count Chocula -vs- Curious George ***


ARE YOU READY TO RUMBLE?!
........................................................


Count Chocula /|\^..^/|\                      100 of 100
Curious George @('_')@                        100 of 100
--------------------------------------------------------
```

We'll make changes to the `fight()` and `main()` functions and add `show()` and
`setup()` functions.

Here's a preview of what those functions will look like when we're done.

:::{dropdown} code

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: fight()"
:pyobject: fight
:linenos:
:lineno-match:
```

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: main()"
:pyobject: main
:linenos:
:lineno-match:
```

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: setup()"
:pyobject: setup
:linenos:
:lineno-match:
```

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: show()"
:pyobject: show
:linenos:
:lineno-match:
```

:::

### Part 7.1: Print each fighter's info

Let's make a function that will eventually print out the health for a pet and
call it `show()`.

### Part 7.1: Add `show()`

#### A. Add `# pet functions` header

At the top of the `Functions` section let's add a new comment section for
`# pet functions`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: comment headers"
:start-at: "# Functions"
:end-before: "def"
:lineno-match:
:emphasize-lines: "3-4"
```

#### B. Add `show()`

Under your new header add a `show()` function that takes one argument `pet`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: comment headers"
:start-at: "def show"
:end-at: "Takes a"
:lineno-match:
```

### Part 7.2: Print info each round

You already know that what goes on inside the while loop in `fight()`
represents what happens each round of a fight.

We'll want to print out the health for each fighter, and have it happen at the
end of every round.

To do this we'll use a `for` loop and in it we'll call the `show()` function.

#### In `fight()`, inside the while loop

In the `fight()` function, inside the for loop and just above where you print a
line:

1. Call the `print()` function with no arguments to print a blank line
2. Write a for loop that iterates over the `fighters` and uses the variable `combatant`
3. *Inside* the for loop, call the `show()` function with the argument `combatant`

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: fight()"
:pyobject: fight
:lineno-match:
:emphasize-lines: "14-17"
```

### Part 7.3: `MAX_HEALTH`

Add a `MAX_HEALTH` variable at the end of the `Global Variables` section add to
keep track of the maximum health.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: global variables"
:start-at: "# Global"
:end-at: "MAX_HEALTH ="
:lineno-match:
:emphasize-lines: "9"
```

### Part 7.4: Setup `setup()`

To print the fighter info, we'll need pets health and pic. To do this we'll add
a new function called `setup()` then call it from `main()`.

#### A. Add `setup()`

Under the `# pet functions` header add a `setup()` function.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: setup()"
:start-at: "def setup"
:end-at: "Takes a"
:lineno-match:
```

#### B. In `main()`

Now we'll call it from inside `main()` and pass it the argument `fighters`.
This should go just after the line where `fighters` is assigned.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: main()"
:pyobject: main
:lineno-match:
:emphasize-lines: 6
```

### Part 7.5: Initialize fighter info

In the `setup()` function, use a for loop to assign the `'health'` and `'pic'`
keys in each dictionary in the `fighters` list.

#### A. Set pet health

For each pet, we'll set the `health` to `MAX_HEALTH`.

1. Use a for loop to iterate over `pets` with the variable `pet`
2. Assign `pet['health']` to `MAX_HEALTH`

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: setup()"
:start-at: "def setup"
:end-at: "= MAX_HEALTH"
:lineno-match:
:emphasize-lines: "3-"
```

#### B. Getting the pic

We'll need to get the picture for each `pet`. In order to do that we'll use the
`pet['species']` as the key to the `PICS` dictionary.

{{ leftcol }}

One way to do that is to assign the value of `pet['species']` to a variable
`species` which we can then use as the key to `PICS`.

{{ rightcol }}

```{code-block} python
:caption: example
:linenos:

species = pet['species']
print(PICS[species])
```

{{ newrow }}

You can avoid setting a temporary variable by putting `pet['species']` where
you would have put the variable.

{{ rightcol }}

```{code-block} python
:caption: example
:linenos:

print(PICS[pet['species']])
```

{{ endcols }}

These both have the same effect, so it's up to you which you prefer.

#### C. In `setup()`, inside the for loop

Use the syntax that you just learned to get the pet pic from the `PICS`
dictionary using the `pet['species']` key. Assign it to `pet['pic']`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: setup()"
:pyobject: setup
:lineno-match:
:emphasize-lines: "5"
```


### Part 7.6: Fill in the `show()` function

Now that each `pet` in the `fighters` list has all of the information we need
we can fill in the `show()` function to actually print the name, pic and
health.

#### In `show()`

1. Assign a `name_display` variable to the string {samp}`{name} {pic}`
2. Assign a `health_display` variable to `"x of y"` health, where `x` the
   `pet["health"]` and `y` is `MAX_HEALTH`
3. Print both variables

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.6.py
:caption: "battle.py: show()"
:pyobject: show
:lineno-match:
:emphasize-lines: "3-"
```

When you run your program your output should look something like this:

```text
Welcome to the THUNDERDOME!

  Tonight...

       *** Curious George -vs- Count Chocula ***


ARE YOU READY TO RUMBLE?!
........................................................


Curious George @('_')@ 100 of 100
Count Chocula /|\^..^/|\ 100 of 100
--------------------------------------------------------
```

### Part 7.7: Make columns with `str.rjust()`

Now let's get a little fancy let's and right-align the health display.

#### A. Right aligning

To right align text we can use the built in `.rjust()` method on `str` objects.
It works just like like `str.center()` and takes a width variable.

Here's an example that prints a list of numbers and uses `.rjust()` to right
align them to a width of `30`.

{{ leftcol }}

```{code-block} python
:caption: example

for i in range(0, 5):
  i = str(i)
  print(i.rjust(30))
```

{{ rightcol }}

```{code-block} text
:caption: output

                             0
                             1
                             2
                             3
                             4
```

{{ endcols }}

#### B. In `show()`

But wait, in this case we want to print part of the line left aligned, and part
of it right aligned. How do we manage that?

To accomplish this, we'll need to figure out how long the left-aligned part of
the string is and use that to adjust the width passed to `.rjust()`.

1. Subtract the length of `name_display` from `WIDTH`
2. Subtract `1` more to account for the space that `print()` adds
3. Assign the result to a variable `rcol_width`
4. Inside of `print()` call the `.rjust()` method on `health_display` with the argument `rcol_width`

```{literalinclude} ../../pythonclass/lessons/battle/battle_part07.py
:caption: "battle.py: show()"
:pyobject: show
:lineno-match:
:emphasize-lines: "5-"
```

Now when you run your script it should look something like this:

```{code-block} text
:caption: output
Welcome to the THUNDERDOME!

  Tonight...

        *** Flufosourus -vs- Curious George ***


ARE YOU READY TO RUMBLE?!
........................................................


Flufosourus =^..^=                            100 of 100
Curious George @('_')@                        100 of 100
--------------------------------------------------------
```

Part 8. Choose who attacks
---------------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part08.py") }}
```

Continuing with the `fight()` function, we need switch back and forth between
the two fighters for who attacks each round.

Here's a preview of the updated `fight()` function:

:::{dropdown} fight()

```{literalinclude} ../../pythonclass/lessons/battle/battle_part08.py
:caption: "battle.py: fight()"
:pyobject: fight
:linenos:
:lineno-match:
```

:::

### Part 8.1: Set a `current` variable

We're going to use a variable `current` to keep track whose turn it is
according to their index number the `fighters` list.

Remember, lists have index numbers that start at `0` and can be accessed like
this: `mylist[0]`.


#### In `fight()`, before the while loop

Add the `current` variable to the top of the `fight()` function, before the
`while` loop and set it to `0`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part08.py
:caption: "battle.py: fight()"
:start-at: "def fight"
:end-at: "current ="
:linenos:
:lineno-match:
:emphasize-lines: "8-9"
```

### Part 8.2: Pick the `attacker`

#### A. Toggling with `not`

{{ leftcol }}

We've used the `not` operator in if statements before. For example:

{{ rightcol }}

```{code-cell} python
if not False:
    print("double negatives ftw!")
```

{{ newrow }}

`not` is really shorthand for `False ==`.

That means another way to write the above is:

{{ rightcol }}

```{code-cell} python
if False == False:
    print("double negatives ftw!")
```

{{ newrow }}

When we use a comparison operator like `not` or `==` it is part of an
expression that evaluates to a `bool` value.

That means we can use a standalone condition to get either `True` or `False`.

{{ rightcol }}

```{code-cell} python
True == True
```

```{code-cell} python
False == True
```

{{ newrow }}

That means that if you want to get the opposite of a `bool` value, just put
`not` in front of it.

{{ rightcol }}

```{code-cell} python
not True
```

```{code-cell} python
not False
```

{{ newrow }}

We can use this trick to alternate back and forth between `True` and `False` in
a loop.

{{ rightcol }}

```{code-cell} python
alternating = True
for i in range(0, 5):
    print(alternating)
    alternating = not alternating
```

{{ endcols }}

We'll use this trick to alternate whose turn it is in the `fight()` function.

#### B. `bool` and `int`

Under the hood a `bool` is just a special kind of `int` that has a name in
Python.

{{ leftcol }}

Specifically, `False` is `0` and `True` is `1`.

{{ rightcol }}

```{code-cell} python
False == 0
```

```{code-cell} python
True == 1
```

{{ newrow }}

You use `True` and `False` as an `int` in ways that might surprise you.

{{ rightcol }}

```{code-cell} python
True + True + True
```

{{ newrow }}

One example is that you can use `True` and `False` as index numbers in a list.

{{ rightcol }}

```{code-cell} python
options = ["No", "Yes"]
print(options[True])
```

{{ endcols }}

That means that we can use the `bool` result of `not current` to pick a pet
from the `fighters` list.

#### C. In `fight()`, at the beginning of the while loop

We'll need to pick whose turn it is at the beginning of each round. That means
this code needs to be the first lines inside the while loop.

1. Assign the `fighters[current]` to the variable `attacker`
2. Assign the `fighters[not current]` to the variable `rival`

```{literalinclude} ../../pythonclass/lessons/battle/battle_part08.py
:caption: "battle.py: fight()"
:start-at: "def fight"
:end-at: "rival ="
:linenos:
:lineno-match:
:emphasize-lines: "14-16"
```

### Part 8.3: Switch fighter's turn

We'll use the `not` trick again at the end of the `while` loop to switch back
and forth between the two fighters.

#### In `fight()`, at the end of the while loop

In the `fight()` function at the end of the `while` loop, set `current` to be
the opposite of itself.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part08.py
:caption: "battle.py: fight()"
:start-at: "# check for a loser"
:end-at: "return winner"
:linenos:
:lineno-match:
:emphasize-lines: "12-13"
```

### Part 8.4: Print the attacker

Finally we want to print out the attacker for each round. We prompt for input
again, but once again this is just to give the player a chance to do
something--we don't do anything with the input.

#### In `fight()`, inside the while loop

In the `fight()` function just after the line where `rival` is assigned add the
following.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part08.py
:caption: "battle.py: fight()"
:start-at: "def fight"
:end-at: "input("
:lineno-match:
:emphasize-lines: "18-19"
```

When you run your script your output should see a new line prompting the first
pet to fight.

```{code-block} text
:caption: output
:emphasize-lines: 12

Welcome to the THUNDERDOME!

  Tonight...

         *** Flufosourus -vs- Count Chocula ***


ARE YOU READY TO RUMBLE?!
........................................................


Flufosourus FIGHT>

Flufosourus =^..^=                            100 of 100
Count Chocula /|\^..^/|\                      100 of 100
--------------------------------------------------------
```

Part 9. Attack
---------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part09.py") }}
```

In this section we'll be adding the `attack()` function and making changes to the `fight()` function.

:::{dropdown} code

```{literalinclude} ../../pythonclass/lessons/battle/battle_part09.py
:caption: "battle.py: attack()"
:pyobject: attack
:linenos:
:lineno-match:
```

```{literalinclude} ../../pythonclass/lessons/battle/battle_part09.py
:caption: "battle.py: fight()"
:pyobject: fight
:linenos:
:lineno-match:
```

:::

### Part 9.1: Add `attack()`

We'll need a function that picks what kind of attack to do, calculates damage
the damage and modifies the `health` of the `rival`.

We're going to call this the `attack()` function, which will take one argument,
the `foe`.

#### A. Add `# game event functions`

In the `# Functions` section after `show()` and `setup()` add a new subsection
for `# game event functions`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part09.py
:caption: "battle.py: # Functions"
:start-at: "# Functions"
:end-before: "def attack"
:linenos:
:lineno-match:
:emphasize-lines: "21-22"
```

#### B. Multiple returning and assigning

Python functions can return nothing, a single value, or more than one values.
In this case, we're returning both the damage amount, and the attack description.

{{ leftcol }}

The syntax when returning multiple values is:

{{ rightcol }}

`return <val1>, <val2>`

{{ newrow }}

For example

{{ rightcol }}

```{code-cell} python
def gimme():
  return (1, 2)
```

{{ newrow }}

The syntax when assigning the results is:

{{ rightcol }}

`<var1>, <var2> = fun()`

{{ newrow }}

For example:

{{ rightcol }}

```{code-cell} python
a, b = gimme()
```

{{ endcols }}

We'll use this syntax in the new `attack()` function to return both the damage
value and a description of the attack.

#### C. Add `attack()`

Under `# game event functions` add an `attack()` function with one argument
`foe`.

It should return a `tuple` containing two values:

* an `int` for the damage
* a `str` for the description

For now just have it return hardcoded values.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part09.py
:caption: "battle.py: attack()"
:pyobject: attack
:linenos:
:lineno-match:
```

### Part 9.2: `attack()` in `fight()`

Now in each round of the fight the `rival` should be attacked using the
`attack()` function.

#### In `fight()`

After pausing for input call the `attack()` function with the argument `rival`.
Using multiple assignment, assign the results to `damage` and `act`.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part09.py
:caption: "battle.py: fight()"
:start-at: "def fight"
:end-at: "damage, act ="
:lineno-match:
:emphasize-lines: "21-22"
```

### Part 9.3: Print attack details

Now we just need to print out all of the details of the attack. We'll use the
`time.sleep()` function to add pauses between output for effect.

We'll want to print who attacked who and how, as well as the damage that was
done.

#### In `fight()`

In the `fight()` function after the `attack()` line:

1. Call `time.sleep()` with the argument `DELAY`
2. Print the attackers name, the `act` and the rivals name, followed by "..."
3. Call `time.sleep()` with the argument `DELAY`
4. Print the `damage` as a negative number, followed by the rivals name. Center
   this whole string using `WIDTH`
5. Call `time.sleep()` with the argument `DELAY`

```{literalinclude} ../../pythonclass/lessons/battle/battle_part09.py
:caption: "battle.py: fight()"
:start-at: "while winner is None"
:end-at: "current = not current"
:lineno-match:
:emphasize-lines: "12-21"
```

When you run your game you should see what happened in the round.

```{code-block} text
:caption: output
:emphasize-lines: "14-16"

Welcome to the THUNDERDOME!

  Tonight...

           *** Scaley -vs- Curious George ***


ARE YOU READY TO RUMBLE?!
........................................................


Scaley FIGHT>

  Scaley smacks upside the head Curious George...

                   -10 Curious George


Scaley <`)))><                                100 of 100
Curious George @('_')@                        100 of 100
--------------------------------------------------------
```

Part 10. Attack, For Realsies
-----------------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part10.py") }}
```

In this section we'll make the attack actually do something.

We'll be adding global variables `POWER` and `FIGHTIN_WORDS` and filling in the
`attack()` function.

Here's what the code will look like when we're done.


:::{dropdown} code

```{literalinclude} ../../pythonclass/lessons/battle/battle_part10.py
:caption: "battle.py: global variables"
:start-at: "# Global"
:end-before: "# Functions"
:linenos:
:lineno-match:
```

```{literalinclude} ../../pythonclass/lessons/battle/battle_part10.py
:caption: "battle.py: attack()"
:pyobject: attack
:linenos:
:lineno-match:
```

:::

### Part 10.1: The `tuple` type

We've learned about lists and dictionaries already. These are both
{term}`collections` or {term}`container` types. That means that they contain
some number of children elements.

The `tuple` is another container type. It is very similar to a list, except
that it is {term}`immutable` meaning that once it is defined it cannot be
changed. This is handy for global variables where only intend to read the data
in the script and never to modify it. They're also faster and consume less
memory.

{{ leftcol }}

Tuples are defined using parenthesis `(` `)`.

{{ rightcol }}

```{code-cell} python
CAVES = ("right", "left", "middle")
```

{{ newrow }}

Elements are accessed with index numbers (just like lists).

{{ rightcol }}

```{code-cell} python
print(CAVES[0])
```

{{ newrow }}

Tuples are immutable, so you can't change them later.

{{ rightcol }}

```{code-cell} python
:tags: [raises-exception]
CAVES[0] = "east"
```

{{ endcols }}

To review Python container types:


| Keyword | Creating                                       | Accessing       | Attributes                 |
|---------|------------------------------------------------|-----------------|----------------------------|
| `list`  | `groceries = ["eggs", "milk", "shampoo"]`      | `groceries[0]`  | ordered, mutable           |
| `tuple` | `menu = ("prev", "next", "quit")`              | `menu[0]`       | ordered, immutable         |
| `dict`  | `favs = {'color': "purple", 'season': "fall"}` | `favs['color']` | unordered, mutable         |
| `set`   | `used = {'red', 'red', 'green', 'blue' }`      | `'red' in used` | unordered, mutable, unique |
|         |                                                |                 |                            |

### Part 10.2: Them's Fightin' Words

Let's make a list of attacks using the tuple type we just learned about. At the
end of the global variables section add the following. Feel free to change
these or get creative and add your own.

```{literalinclude} ../../pythonclass/lessons/battle/battle_part10.py
:caption: "battle.py: global variables"
:start-at: "# a list of attacks"
:end-before: "# Functions"
:linenos:
:lineno-match:
```

### Part 10.3: Pick an attack

Now that we have some attacks to choose from, let's edit our `attack()`
function to pick one.

#### In `attack()`

1. Use the `random.choice()` function to pick from the new `FIGHTING_WORDS`
   list and assign it to the variable `act`
2. In the `return` statement replace your hardcoded attack string with the
   `act` variable

```{code-block} python
:caption: "battle.py: attack()"
:linenos:
:lineno-start: 89
:emphasize-lines: "5-"
def attack(foe):
    """Inflict a random amount of damage is inflicted on foe, then return the
       damage and attack used"""
    # choose an attack
    act = random.choice(FIGHTIN_WORDS)

    return 10, act
```

### Part 10.4: What's your damage

Now we need to figure out how much damage the attack will do. First we'll add a
global variable POWER to set the possible damage range for each attack.


#### A. In global variables

```{literalinclude} ../../pythonclass/lessons/battle/battle_part10.py
:caption: "battle.py: global variables"
:start-at: "# Global"
:end-at: "POWER ="
:linenos:
:lineno-match:
:emphasize-lines: "3-"
```

#### B. In `attack()`

Now we can use the good old `randint` function to randomly select a value in
that range.

1. Call `random.randint` and pass it the two values in the `POWER` tuple as
   arguments. Assign the result to the variable `damage`

```{literalinclude} ../../pythonclass/lessons/battle/battle_part10.py
:caption: "battle.py: attack()"
:start-at: "def attack"
:end-at: "damage ="
:linenos:
:lineno-match:
:emphasize-lines: "7-8"
```

#### C. Shortcut operators

In this section we'll learn about some operators to do math and assign at the same time.

{{ leftcol }}

In programming you often want to do some math on a value, then assign the
result back to the original variable. For example:

{{ rightcol }}

```{code-cell} python
x = 1
x = x + 1
print(x)
```

{{ newrow }}

A quicker way to do this is to use the `+=` operator.

{{ rightcol }}

```{code-cell} python
x = 1
x += 1
print(x)
```

{{ newrow }}

The same thing comes up with subtracting a value from itself.

{{ rightcol }}

```{code-cell} python
:tags: [raises-exception]
x = 1
x = x - 1
print(x)
```

{{ newrow }}

The shorthand operator for subtract and assign is `-=`.

{{ rightcol }}

```{code-cell} python
x = 1
x -= 1
print(x)
```

{{ endcols }}

Let's use this operator to reduce the health of `foe`.

#### D. In `attack()`

Now that we have the `damage` value set, we can finally inflict it upon our the
`foe`.

1. Use the `-=` operator to subtract `damage` from `foe['health']`
2. In the `return` statement replace your hardcoded damage `int` with the
   `damage` variable

```{literalinclude} ../../pythonclass/lessons/battle/battle_part10.py
:caption: "battle.py: attack()"
:pyobject: attack
:linenos:
:lineno-match:
:emphasize-lines: "10-"
```

Now when you run your game you should see a randomized
value of damage done, and that number will actually
effect one of the fighters health.

```{code-block} text
:emphasize-lines: "16, 20"
Welcome to the THUNDERDOME!

  Tonight...

           *** Scaley -vs- Count Chocula ***


ARE YOU READY TO RUMBLE?!
........................................................


Scaley FIGHT>

  Scaley throws mad shade at Count Chocula...

                   -27 Count Chocula


Scaley <`)))><                                100 of 100
Count Chocula /|\^..^/|\                       73 of 100
--------------------------------------------------------
```

Part 11. Find The Winner
------------------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part11.py") }}
```

In this section we're going to finish the `fight()` function by picking the
winner.

Here's how the function will look at the end:

:::{dropdown} fight()

```{literalinclude} ../../pythonclass/lessons/battle/battle_part11.py
:caption: "battle.py: fight()"
:pyobject: fight
:linenos:
:lineno-match:
```

:::

### Part 11.1: Check `rival` health

Instead of randomly choosing a `winner`, in this section we'll pick a real one.

Fist, we want to check if the `health` of the `rival` who was just attacked has
reached zero. If it has, then we know that the `winner` is the other guy (the
`attacker`).

Also, we don't want `health` be a negative number so we'll use the `<=`
operator, which means "less than or equal to". Then to account for when it is a
negative number, we'll set it to zero within the body of the if statement.

#### In `fight()`, inside the while loop

In the `fight()` function, find the `winner = random.choice()` line just above
where we print the updated fighter health. Remove that line and in its place
add the following.

1. Use an if statement to check if the `rival['health']` is less than or equal to `0`
2. If so
   * Set the `rival['health']` to `0`
   * Assign the variable `winner` to `attacker`


```{literalinclude} ../../pythonclass/lessons/battle/battle_part11.py
:caption: "battle.py: fight()"
:start-at: "while winner is None"
:end-at: "winner = attacker"
:linenos:
:lineno-match:
:emphasize-lines: "23-"
```

Part 12. Endgame
----------------

```{div} float-right
{{ code.format("battle.py", "lessons/battle/battle_part12.py") }}
```

Now that we have a winner, we can tell 'em they won!

Use some of the concepts you've learned to print a nice message congratulating
the winner. Try doing it on your own before looking at the code.

1. Use an f-string to print the name of the winner
2. Use the `.center()` method to center the method
3. Draw one or more lines by using the `*` operator to repeat a string

:::{dropdown} endgame()

```{literalinclude} ../../pythonclass/lessons/battle/battle_part12.py
:caption: "battle.py: endgame()"
:pyobject: endgame
:linenos:
:lineno-match:
```

:::

When you play your game, your fighters will go several rounds before a winner
emerges. Your game should end with a nice looking victory message that looks
something like this.

Feel free to get creative!

```{code-block} text
:caption: "output"
--------------------------------------------------------


                 Scaley is Victorious!

                        <`)))><

--------------------------------------------------------
```
