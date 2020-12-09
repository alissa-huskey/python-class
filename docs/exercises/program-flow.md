Program Flow Exercises
======================

Today we're going to write some code for game characters, working with the
concepts of {term}`variables<variable>` and {term}`functions<function>` that we
discussed last week.

Start by making a new file `character.py`. We're going to use the `random`
module today, so start off by importing it at the top of the file.

```{code-block} python
---
caption: character.py
linenos:
---
import random
```

Part 1: Variable assignment and reference
-----------------------------------------

Last week we discussed that...

* A {term}`variable` is like a storage container for data.
* To create a variable, you simply {term}`assign` a value to
  it, using the `=` operator. This is like adding an item to
  your inventory.
* To retrieve the stored information you {term}`reference` it using the
  variable name or {term}`identifier`.


### Step 1: Setup your character

Let's start by {term}`assigning<assign>` two new variables:

* `name` a string (`str`)
* `level` an integer (`int`) that is a random number between `1` and `5`.

```{code-block} python
---
caption: character.py
linenos:
---
import random

name = "Ash"
level = random.randint(1,5)
```

Notice that for this first part there is no program output. That's because our
assignment statements are saving the information for future use.

### Step 2: Print character info

Now we'll {term}`reference` these variables in a print statement.

```{code-block} python
---
caption: character.py
linenos:
---
import random

name = "Ash"
level = random.randint(1,5)

print(name, "is at level", level)
```

### Step 3: Give your character a job

Assign a new variable.  This should be at the top, just under where you assign
`level` on line `4`.

* `title` a string (`str`) -- one of `"mage"`, `"thief"`, or `"warrior"`

Now change your `print` statement on line `6` so that it prints your characters
`title`. It should print out something that looks like:

```
Rowan is a level 2 mage
```

### Step 4: Level up

Now we'll level our character up.

We'll calculate the new level with a simple math `level + 2` which references
the current value of `level`. Then we `assign` the result of the expression to
the `level` variable using the `=` operator.

```{code-block} python
---
caption: character.py
linenos:
---
import random

name = "Ash"
level = random.randint(1,5)
title = "thief"

print(name, "is a level", level, title)

level = level + 2

print(name, "is now level", level)
```

Part 2: Function definition and calling
=======================================

Last week we discussed that...

* A {term}`function` is a set of instructions or statements
  that can be executed later.
* When you {term}`define` a function, it is like learning the skill. The
  information is saved for future reference, but it has no effect on the
  program yet.
* You define a function using a compound statement starting with the `def`
  keyword.
* When you {term}`call` a function, it is like using the skill. This is when
  the stored statements are actually {term}`executed<execute>`.
* You call a function by using its name, followed by parenthisis.
* Functions can take {term}`arguments<argument>`.
* When defining the function, these go inside the parenthisis of the
  {term}`header` line which creates a temporary variable that only exists
  inside the function.
* When calling functions, arguments are passed inside the parenthisis of the
  calling line with commas seperating them.

### Step 1: Make a character info function

Let's make it easier to print out character information by turning it into a function.

Back at the top of the program, above where you assign the variables, let's add
a `character_info` function that takes three arguments. Then replace your print
statement from line 7 with a call to your newly created function.

```{code-block} python
---
caption: character.py
linenos:
emphasize-lines: 3-4, 10
---
import random

def character_info(character_name, character_title, character_level):
    print(character_name, "is a level", character_level, character_title)

name = "Ash"
level = random.randint(1,5)
title = "thief"

character_info(name, level, title)

level = level + 2

print(name, "is now level", level)
```

### Step 2: Print out more characters

The thing that makes functions useful is that you can call them multiple times.
For functions that take arguments, you can call them with different arguments.

Lets call our new function with different values for all three arguments.

```{code-block} python
---
caption: character.py
linenos:
emphasize-lines: 16-18
---
import random

def character_info(character_name, character_title, character_level):
    print(character_name, "is a level", character_level, character_title)

name = "Ash"
level = random.randint(1,5)
title = "thief"

character_info(name, level, title)

level = level + 2

print(name, "is now level", level)

character_info("Shay", "warrior", 7)
character_info("Quinn", "thief", 3)
character_info("Max", "mage", 5)
```

You'll notice that we didn't need to assign new `name`, `level` and `trade`
variables. We just passed the values in directly.


### Step 3: Make a character_level function

The message for when a character changes levels is different, so make a
function for that too.

* Function name: `character_level`
* Arguments:
  * `character_name` (`str`)
  * `character_level` (`int`)
* Example output: `Max is now level 8`

Add it near the top of your program, just under where you define
`character_info` on lines `3`-`4`.

Then replace your print statement on line `14` with a call to your new
`character_level` function.
