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
Dragon Realm
============

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm.py") }}
```

> Based on:
> http://inventwithpython.com/invent4thed/chapter5.html

```{include} ../toc.md
```

Introduction
------------

The game you will create in this chapter is called Dragon Realm. The player
decides between two caves which hold either treasure or certain doom.

```{screencast} assets/dragon_realm.cast
:poster: npt:0:01
:rows: 15
```

Part 1: A Script Template: Shebang, Docstring, Scope
----------------------------------------------------

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm_part1.py") }}
```

We're going to start with a bare bones script that will serve as a template for
all future scripts.

Follow the instructions in [Repl.it Tips](../tools/replit.md) to create
a new file called `dragon_realm.py` and change your `.replit` file to run it.
Copy and paste the following code into it.

:::{dropdown} code

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part1.py
:caption: dragon_realm.py
:linenos:
```

:::

### Part 1.1: Shebang, Encoding

The very first line of any executable file (script) is the ***shebang*** line.
The line starts with a `#!` then is immediately followed (without a space) by
the path to the interpreter. In this case it is telling the computer to run
this script using `python3`.

The next line tells Python (as well as some editors) what the ***encoding*** to
expect. That is, what kinds of characters. This line might be different if, for
example, we were going to include Chinese characters.

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part1.py
:caption: dragon_realm.py
:linenos:
:end-at: 'coding: utf'
```

### Part 1.2: Docstrings

The first ***expression*** in a Python script should always be a
***Docstring***. A Docstring, surrounded by `"""` or `'''`, is similar to a
comment in that its contents will not be executed. Docstrings however, are
stored by the interpreter as documentation for a particular file, module,
class, or function.

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part1.py
:caption: dragon_realm.py
:linenos:
:lineno-match:
:start-at: '"""'
:end-before: "def"
```

### Part 1.3: Scope, `__main__` and `main()`

Up until now we have been writing all our code in the body of the file. (Aside
from a few functions in the PyPet project.) This is what is referred to as the
***global scope*** or ***global namespace***.

Scope refers to the place where an identifier (variable or function) can be
used. When a variable is defined in the body of the file it is available to
everything in the file--globally. When a variable is defined in a function it
is only available to the code inside of that function.

It is a good idea to keep the amount of code in the global scope to a minimum.
This avoids problems like accidentally reusing the same variable name and
causing unintended results.

In order to achieve this, organize code into functions.  The convention is to
write a function called `main()` and call it when your script is executed.

Note that `main()` has a docstring too. This will describe the purpose of the
function.

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part1.py
:caption: dragon_realm.py
:linenos:
:lineno-match:
:start-at: "def main"
```


Part 2: Beginning and end
-------------------------

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm_part2.py") }}
```

In this section we'll add a description of the imaginary game world that will
be printed when the player first starts the game.

At the end of the game, we'll ask the player if they want to continue instead
of just exiting.

### Part 2.1: Global Variables

Global variables are called that because they are available to everything in
the file. Whereas a variable that is defined inside a function is called a
local variable, and it goes away when the function is done executing.

#### A. Conventions

{{ leftcol }}

You generally want to define them at the top of the file, and name them with
`ALL_CAPS` to help you tell them apart from local variables.

{{ rightcol }}

```{code-cell} python
MY_GLOBAL = True
```

{{ endcols }}

#### B. Add `WIDTH`

The `WIDTH` global variable is for the number of horizontal characters we want our
game to take up.

1. Add the global variable `WIDTH` under the docstring and set it to `58` as a
   starting point. (You can always change it later.)

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part2.py
:caption: dragon_realm.py
:linenos:
:lineno-match:
:start-at: '"""'
:end-at: "WIDTH ="
:emphasize-lines: 7
```

### Part 2.2: intro()

In this section we'll write the `intro()` function which will print out a
paragraph to the player that describes the players surroundings.

#### A. Multi-line strings

{{ leftcol }}

You can use the docstring syntax to make a string and use it anywhere you would
normally use a string. This is useful if you have a multi-line string such as
the paragraph we want to print in the `intro()` function.

This will retain all whitespace--both newlines and indentation.

{{ rightcol }}

```{code-cell} python
print("""
  a
    b
      c
        d
"""
)
```

{{ endcols }}

#### B. Newlines

{{ leftcol }}

The backslash (`\`) in a string tells Python that the next character has
special meaning. `\n`, for example, is for a new line

{{ rightcol }}

```{code-cell} python
print("a\nb\nc\n")
```

{{ endcols }}

#### C. Add `intro()`

Let's use the concepts we just learned to define the `intro()` function.

1. Define the `intro()` function
2. Add a docstring describing what the function does
3. Using docstring syntax, print the intro description copied from below (or make up your own!)

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part2.py
:caption: "dragon_realm.py: intro()"
:linenos:
:lineno-match:
:pyobject: intro
```

### 2.3. Keep playing

In this section we'll ask the player if they want to keep playing when the game
ends, instead of just exiting.

#### A. `input()`

To make a program interactive, we need to get feedback from the user. To do this
we call the `input()` function and whatever the user types will be returned.

{{ leftcol }}

The syntax is:

{{ rightcol }}

{samp}`{VAR} = input({PROMPT})`

{{ newrow }}

In this example, whatever the user typed before hitting enter would be assigned
to the variable `response`.

{{ rightcol }}

```{code-block} python
:caption: example
response = input("Are you sure? ")
```

{{ newrow }}

The user would see something like this:

{{ rightcol }}

```{code-block} text
:caption: prompt
Are you sure? ▉
```

{{ endcols }}

Be sure to always add the space at the end of the prompt string, otherwise
there will be no space between the text the user sees and their cursor.

We'll use the `input()` function to ask the player if they want to keep
playing.

#### B. Objects and `str.lower()`

In Python, all values are {term}`objects`. An object is data that can have values
and functions attached to it. An objects values are called {term}`attributes` and
its functions are called {term}`methods`.

{{ leftcol }}

For example, `list` objects have a method `.count()` which will tell you how
many of a certain thing the list contains.

{{ rightcol }}

```{code-cell} python
votes = ["red", "blue", "red", "red", "blue", "blue"]
votes.count("blue")
```

{{ newrow }}

If you want to know what methods or attributes an object has you can use the
`dir()` function and pass it either an object or a type. (Just scroll past all
the ones that start with `__` for now.)

{{ rightcol }}

```{code-cell} python
:tags: [output_scroll]
dir(str)
```

{{ newrow }}

You can use the `help()` function to get more information about a method.

You can use either the object (like `"hello"`) or the type (like `str`)
followed by a dot and the method name.

{{ rightcol }}

```{code-cell} python
help(str.lower)
```

{{ newrow }}

You can see that `str` objects have a `.lower()` method. Let's try it out.

{{ rightcol }}

```{code-cell} python
"OH HAI THERE".lower()
```
{{ endcols }}

We'll use the `.lower()` function to change the player's answer to lower case.
That way we'll understand if they type `"YES"`, `"Yes"` or `"yes"`.

#### B. Boolean and Membership Operators

In programming, sometimes we don't just want to see if something is the same as
something else, but the same as a couple of things.

{{ leftcol }}

One way that we could do this would be using the `or` boolean operator.

{{ rightcol }}

```{code-cell} python
answer = "Y"
answer.lower() == "y" or answer.lower() == "yes"
```

{{ newrow }}

We're going to learn to use the `in` operator to easily check if a `value` is a
member of a `sequence`.

The syntax is:

{{ rightcol }}

`<value> in <sequence>`

{{ newrow }}

For example:

{{ rightcol }}

```{code-cell} python
answer = "Y"
answer.lower() in ["y", "yes"]
```

{{ endcols }}

We'll use the `in` operator to check the player's answer against multiple
acceptable answers.

#### C. Repeating strings

{{ leftcol }}

Python provides an easy way to repeat a string using multiplication. Just use
the `*` operator to multiply a `str` by an `int`.

{{ rightcol }}

```{code-cell} python
"echo... " * 3
```

{{ newrow }}

This is a handy way to quickly make a visual line that is whatever width you
want.

{{ rightcol }}

```{code-cell} python
"~" * 30
```

{{ endcols }}

We'll use this to print a line at the start of each game.

#### E. while loops

Sometimes we want our program to repeat the same steps over and over again. One
way to do this is to use a `while` loop which will repeat the same block of
code as long as a certain condition is met.

{{ leftcol }}

The syntax is:

{{ rightcol }}

```{include} ../templates/syntax/while.md
```

```{include} ../templates/desc/while.md
```

{{ newrow }}

In this example if the user hits enter before typing anything, they'll be asked
again repeatedly until they do.

{{ rightcol }}


```{code-block} python
:caption: example
answer = ""

while not answer:
  answer = input("Your choice: ")
```

{{ newrow }}

:::{caution}
Beware of infinite loops!
:::

Infinite loops happen when the condition is *always* met. While not
inherently bad, they can wreak havoc on your system when unintended.

This is a simple example of a `while True` infinite loop.

{{ rightcol }}

```{code-block} python
:caption: example
import time

while True:
  print("this is the song that never ends...")
  time.sleep(1)
```

{{ endcols }}

We'll use a while loop in `main()` to let the user keep playing if they want to.

#### F. In `main()`

1. Change your docstring to reflect the way `main()` will work when we're done
2. Add a variable `answer` and set it to `"yes"`
3. Add a while loop that will keep going as long as lower cased `answer`
   matches any of a list of the strings `["y", "yes"]`
4. In the while loop:
   * Print a line by multiplying a dash by `WIDTH`. Add a newline at the end
   * Call the `intro()` function
   * Ask the user if they want to play again using the `input()` function and
     assign the result to the variable `answer`

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part2.py
:caption: "dragon_realm.py: main()"
:pyobject: main
:linenos:
:lineno-match:
:emphasize-lines: "2, 4-"
```

Part 3: Player, `choose()` a Cave
---------------------------------

In this section we will prompt the player to choose a cave, then make sure
their response is a valid cave.

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm_part3.py") }}
```

Add a global variable `CAVES` to the top of your script where `WIDTH` is
defined.

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part3.py
:caption: "dragon_realm.py: global variables"
:linenos:
:start-at: "WIDTH ="
:end-at: "CAVES ="
:emphasize-lines: 2
```

Add the `valid_cave()` function

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part3.py
:caption: "dragon_realm.py: valid_cave()"
:linenos:
:pyobject: valid_cave
```

Add the `choose()` function

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part3.py
:caption: "dragon_realm.py: choose()"
:linenos:
:pyobject: choose
```

Edit your `main()` function to add `cave = choose()`.

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part3.py
:caption: "dragon_realm.py: main()"
:linenos:
:pyobject: main
:emphasize-lines: 8
```

### Part 3.1: Conditionals Expressions Resolve to Boolean Values

We have used conditional expressions in if-statements

```python3
if a == b:
  ...
```

And we have used conditional expressions in while-statements

```python3
while a < b:
  ...
```

A key think to understand is that a conditional expression always resolves to a
Boolean value, either `True` or `False`.

```python3
>>> 2*2 == 4
True
>>> "5" == str(5)
True
>>> import random
>>> 5 < random.randint(0, 10)
False
>>> 57 in [ range(0, 10) ]
False
```

That means that we can treat a conditional expression as just another value.
Which is why we can return the result of this conditional in the `valid_cave()`
function.

```python3
return response in CAVES
```

### Part 3.2: Method Chaining

Since all values are objects in Python, all values may have methods. ***Method
chaining*** is a way to take advantage of that to write less code.

In this case, since `input()` always returns a string, we can call `lower()`
from the return result of input() by chaining them together with a dot.

```python3
    # these two lines of code...
    cave = input("(right, left): ")
    cave = cave.lower()

    # have the same result as this one
    cave = input("(right, left): ").lower()
```


Part 4: Enter the Cave
----------------------

Now that the player has picked a cave, it's time to tell them what happens when
they enter it. We'll add a new `enter()` function and use the `sleep()`
function in the `time` module to add a delay between messages.

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm_part4.py") }}
```

Above your global variables, import the `time` module.

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part4.py
:caption: "dragon_realm.py: imports"
:linenos:
:start-at: '"""'
:end-at: "import"
:emphasize-lines: 7
```

Add a global variable `DELAY`

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part4.py
:caption: "dragon_realm.py: global variables"
:linenos:
:start-at: '"""'
:end-at: "CAVES ="
:emphasize-lines: 10
```

Add the `enter()` function

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part4.py
:caption: "dragon_realm.py: enter()"
:linenos:
:pyobject: enter
```

And change your `main()` function to call `enter()`

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part4.py
:caption: "dragon_realm.py: main()"
:linenos:
:pyobject: main
:emphasize-lines: 9
```

Part 5: Prettier output with `describe()`
-----------------------------------------

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm_part5.py") }}
```

It is getting a little hard to tell which lines of the game are description and
which parts are prompts. Lets make that clearer by indenting the text. To do
that we're going to add a function `describe()` which we'll use to print
anything that is not related to getting input.

Add a `describe()` function

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part5.py
:caption: "dragon_realm.py: describe()"
:linenos:
:pyobject: describe
```

Then change your `intro()` function to call it instead of `print()`.

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part5.py
:caption: "dragon_realm.py: intro()"
:linenos:
:pyobject: intro
:emphasize-lines: 3
```

And call `describe()` in `enter()`

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part5.py
:caption: "dragon_realm.py: enter()"
:linenos:
:pyobject: enter
:emphasize-lines: 10
```

Part 6: Wrap text using the `textwrap` module
---------------------------------------------

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm_part6.py") }}
```

That looks nicer, but the intro looks funky because only the first line is
indented. Let's fix that by using the `textwrap` module's `wrap()` function. It
takes two arguments, the string to wrap, and the width to wrap it to. It
returns a list where each item in the list is one line of the string.

Import the `textwrap` module

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part6.py
:caption: "dragon_realm.py: imports"
:linenos:
:start-at: '"""'
:end-at: "import textwrap"
:emphasize-lines: 8
```

Add a global variable `WRAP`

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part6.py
:caption: "dragon_realm.py: global variables"
:linenos:
:start-at: '"""'
:end-at: "CAVES ="
:emphasize-lines: 11
```

Then change your `describe()` function

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part6.py
:caption: "dragon_realm.py: describe()"
:linenos:
:pyobject: describe
:emphasize-lines: "2-"
```

The `wrap()` function strips trailing newlines so we'll need to change the
`intro()` function. Remove the `\n` and add a `print()` statement to the end of
the function.

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part6.py
:caption: "dragon_realm.py: intro()"
:linenos:
:pyobject: intro
:emphasize-lines: "6-"
```

Part 7: Pick the Friendly Dragon
--------------------------------

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm_part7.py") }}
```

Next we need to randomly pick a dragon to be the friendly one.

Import the `random` module

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part7.py
:caption: "dragon_realm.py: imports"
:linenos:
:start-at: '"""'
:end-at: "import random"
:emphasize-lines: 9
```

Add a `is_friendly()` function

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part7.py
:caption: "dragon_realm.py: is_friendly()"
:linenos:
:pyobject: is_friendly
```

Add a line to the end of your `enter()` function to save the resulting value

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part7.py
:caption: "dragon_realm.py: enter()"
:linenos:
:pyobject: enter
:emphasize-lines: 13
```

### Part 7.1 Accessing List Elements

You may recall that dictionaries have keys. Dictionary elements can be accessed
by adding square brackets to the end of the variable name containing the key.

```python3
>>> car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
>>> print(car["brand"])
Ford
```

List elements have an ***index number*** which always starts at `0` and
increases for each element in the list. List elements can be accessed by their
index number the same way that dictionary elements can. Since the index is
always a number, don't use quotes.

```python3
>>> brands = [ "Ford", "Chevrolet", "Honda" ]
>>> print(brands[1])
Chevrolet
```

List elements are in the order they are added in, unless changed by the
programmer.

```python3
>>> letters = [ 3, 2, 1 ]
>>> print(letters[0])
3

>>> letters = [ "a", "b", "z", "c", "d" ]
>>> print(letters[2])
z
```

The CAVES list defined earlier contains the elements `[ "right", "left"
]`, which means that the value of `CAVES[0]` is `"right"` and the value of
`CAVES[1]` is `"left"`.

Here we generate a random number between `0` and `1` to use as the index in the
`CAVES` list, so `CAVES[friendly]` will be either `"right"` or `"left"`.

Then we compare it to the value of `dragon`. `dragon == CAVES[friendly]` will
resolve to either `True` or `False`. That is the value that the function
returns.

```python3
    friendly = random.randint(0, 1)
    print("The friendly dragon is:", CAVES[friendly])
    return dragon == CAVES[friendly]
```

Part 8: The Dragon Acts
-----------------------

```{div} float-right
{{ code.format("dragon_realm.py", "lessons/dragonrealm/dragon_realm_part8.py") }}
```

Finally, we'll tell the player what the dragon does.

**Edit Your Script**

Add a `dragon()` function

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part8.py
:caption: "dragon_realm.py: dragon()"
:linenos:
:pyobject: dragon
```

Add a line to the end of your `enter()` function to call it

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part8.py
:caption: "dragon_realm.py: enter()"
:linenos:
:pyobject: enter
:emphasize-lines: 13
```

Finally, remove or comment out the `print()` line in your `is_friendly()` function

```{literalinclude} ../../pythonclass/lessons/dragonrealm/dragon_realm_part8.py
:caption: "dragon_realm.py: is_friendly()"
:linenos:
:pyobject: is_friendly
:emphasize-lines: 4
```

### Part 8.1: Dictionary Keys

In the past we've used strings for dictionary keys, but other types can be other
keys too.

Ints and Floats can be keys.

```python3
>>> dewey = {
...   610: "Medicine & health",
...   610.3: "Medical encyclopedias",
...   610.6: "Medical organizations & professions",
...   610.72: "Medical research",
...   610.9: "Geography and history of medicine",
... }
>>>
>>> dewey[610]
'Medicine & health'
>>> dewey[610.6]
'Medical organizations & professions'
```

Booleans can be keys

```python3
>>> d = { True: "true", False: "false" }
>>> d[True]
'true'
```

However, `True` and `False` are equal to `1` and `0` respectively, so you can't
mix them.

```python3
>>> d = { True: "true", False: "false", 1: "one", 0: "zero" }
>>> d[True]
'one'
>>> d[False]
'zero'
>>> d[1]
'one'
>>> d[0]
'zero'
```

Here we're using booleans as keys in the `actions` dictionary, then looking
them up using `actions[is_friendly]`.

```python3
    actions = {
        # friendlyness: action
        True: "Gives you his treasure!",
        False: "Gobbles you down in one bite!",
    }
```

We could have written the dictionary like this:

```python3
    actions = {
        "friendly": "Gives you his treasure!",
        "unfriendly": "Gobbles you down in one bite!",
    }
```

But then we would have had to add an if-statement based on the boolean value of
the `is_friendly` variable.

---

Make it Your Own
------------------------

Change the game to make it your own. Here are some ideas.

* Add a third cave in the middle with a silly dragon who does a little jig.

* Make a dictionary for each dragon and give them other details like names,
  colors, sizes, if they breath fire. Print the additional values when you walk
  in the cave.

* If the player gets treasure from the dragon, add another level to the game.
  Perhaps the player encounters a well and can either make a wish with coin, or
  take a drink. Randomly decide if the wish is granted, or if the water is
  poisoned.

* Add a rarely occurring event that may sometimes take place instead of the
  usual friendly/unfriendly actions. Perhaps the dragon transforms into a toad,
  or it falls in love with you. Calculate it by using some datetime information
  (like, it only occurs on Friday the 13th or after midnight on odd numbered
  days) combined with some randomness.


What We've Learned
------------------

* The shebang
* Docstrings as documentation
* Scope, `main()`, and global variables
* Docstrings as multi-line strings
* Objects
* `str.lower()`, `time.sleep()` and `textwrap.wrap()`
* Repeating strings with `*`
* Escape characters and `\n`
* Method chaining
* List indexes and more dictionary key types
* Conditional expressions evaluate to boolean values
* The `not`, `in` and `or` operators
