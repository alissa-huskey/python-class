---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'
  row: '{{ newrow | replace("col", "col-5") }}'
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
Beginner Tutorial
=================

> Approximate time ~ 2 hours

```{contents}
:backlinks: top
:local:
:depth: 2
```

Introduction
------------

This guide was created for complete beginners (i.e. with no programming or
computer science experience) and will teach you programming fundamentals in a
language called [Python][]. Following a project-driven learning philosophy you
will learn as you build your own project. There will be GIFs and screenshots
throughout this guide to make everything as clear as possible.

As you complete this guide you'll be creating a virtual pet we'll call "PyPet"
(a "Python-pet"). Remember [tamagochis][]? (Or if you were born in the 90s then
think POKEMON!) With each new Python programming concepts you learn, you will
add new features to your "PyPet".


### What is Python?

Python is a [scripting programming language][] known for both its
simplicity and wide breadth of applications. For this reason it is considered
one of the best languages for beginners. Used for everything from Web
Development to Scientific Computing (and SO much more), Python is referred to
as a "general purpose" language by the greater programming community.

Many Python programmers (aka "Pythonistas") love this language because it
maintains a certain philosophy of best practices, described in Tim Peter’s
famous ["Zen of Python"][]. There is a large Python community both off and
online that is welcoming and supportive of beginners, and you can find a
plethora of additional materials in the resources section of this guide.

[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[tamagochis]: https://en.wikipedia.org/wiki/Tamagotchi
[scripting programming language]: http://en.wikipedia.org/wiki/Scripting_language
["Zen of Python"]: https://www.python.org/dev/peps/pep-0020/

Part 1: Getting Started
-----------------------

To get our project off the ground we're going to get our development
environment all set up and write what is essentially a
["Hello World!" program][hello-world] -- that is, one of the simplest possible
programs that simply prints out a message -- usually `Hello World!`.

[hello-world]: https://en.wikipedia.org/wiki/%22Hello,_World!%22_program

### Part 1.1: Replit

To get started we'll need a {term}`development environment`, aka *a place to
write and execute code*. For this we'll use [Replit][replit], a fast and free
way to get you up and running.

Do everything in Part 1 of this [Replit Guide](../tools/replit.md) to get set
up with an account and new project.

### Part 1.2: Your first line of code

Now we'll write our first line of code and run it.

![](../tools/assets/replit-running.gif)

#### A. Write code in the editor

{{ left }}

If you haven't already, add the following line in the editor:

The `print()` function in Python will print things in the console — it's very
handy for learning Python and debugging your code.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-2.1.py
:caption: main.py
:class: full-width
:linenos:
:lines: "1"
:lineno-match:
```

{{ endcols }}

#### B. Run it

Click the {guilabel}`Run` button. The console will output:

`Welcome to PyPet!`

You’ve just written your Python program!

```{rst-class} centered
```

*♬♩♪♩ Happy dance! ♬♩♪♩*.

[replit]: https://replit.com/

Part 2: Creating your PyPet
---------------------------

% ![](http://i.imgur.com/6o6eiaA.gif)

::::{margin}

:::{seealso}

More on [variables][]

:::

::::

### Part 2.1: Setting Variables

Variables are a way of storing information in Python. We'll use
variables to keep track of information about our PyPet such as name, weight,
and so on.

#### A. Add a variable

Use an equals sign (`=`) to set a variable to a given value such as
`name = "Fluffy"`.

::::{margin}

:::{tip}

There won't be any difference in the output when you run your program. Even
though there is more code, we haven't printed anything else yet.

:::

::::

  {{ left }}

  Create a variable called `name` equal to `"Fluffy"` (or `"Spike"` or `"Sir
  Patrick"` or whatever strikes your fancy.).

  {{ right }}

  ```{literalinclude} ../../pythonclass/pypet/main-2.1.py
  :caption: main.py
  :class: full-width
  :linenos:
  :lines: "1-3"
  :lineno-match:
  :emphasize-lines: "3"
  ```

  {{ endcols }}

  Variables can store different types of data. In this case, `name` is
  something called a {term}`string` because `"Fluffy"` has quotation marks
  around it. (Either single or double quotes will work.)

  A {term}`string` is just a set of characters surrounded by quotations. For
  example `"Bob"`, `'New York'` or `"h4ck3r"`.  A string can also include
  numbers, so long as it's in between quotes.

#### B. Types of data

  ::::{margin}

  :::{tip}

  Never put quotation marks around these data types.

  :::

  ::::

  Let’s look at some additional data types.

  {{ left }}

  Create three more variables to track `age`, `weight` and `hungry`.

  {{ right }}

  ```{literalinclude} ../../pythonclass/pypet/main-2.1.py
  :caption: main.py
  :class: full-width
  :linenos:
  :lines: "1-6"
  :lineno-match:
  :emphasize-lines: "4-6"
  ```

  {{ endcols }}

  * The `age` variable is an {term}`integer` and therefore must be a whole number.

  * The `weight` variable is a {term}`float`. Floats are a numbers that can have
  values after the decimal point.

  * The `hungry` variable is a {term}`boolean` which may be either `True` or `False`.

::::{margin}

:::{admonition} Best practice

A single space is recommended before and after the equals sign (`=`).

:::

::::

#### C. Exercise

{{ left }}

Can you add another variable named `color` and give it a string value like
`"white"`?

{{ right }}

:::{dropdown} See the answer

```{literalinclude} ../../pythonclass/pypet/main-2.1.py
:caption: main.py
:class: full-width
:linenos:
:lineno-match:
:emphasize-lines: "7"
```

:::

{{ endcols }}

### Part 2.2: Special characters

Since this is a text-based program we'll have to get creative and use
[ASCII art][ascii-art] to make a picture of your PyPet.

[ascii-art]: https://en.wikipedia.org/wiki/ASCII_art

{{ leftcol | replace("col", "col-7") }}

ASCII art is any sort of picture or diagram drawn using basic text symbols.
While the simplest example is a smiley face: `:-)`, they can get a lot more
sophisticated.

{{ rightcol | replace("col", "col-5") }}

```{code-block} text
:caption: Bessie the cow
 _________
< oh hai.>
 ---------
       \   ,__,
        \  (oo)____
           (__)    )\
              ||--|| *
```

{{ endcols }}

For our purposes, we're going to go for a simple one-line picture like
`(=^o.o^=)_`.

  :::{dropdown} Choose an ASCII art animal

   {{ leftcol }}

   | `*` | Animal      | Pic                    |
   |-----|-------------|------------------------|
   |     | Alligator   | `-^^,--,~`             |
   |     | Bat         | `^O^`                  |
   |     | Bear        | `⊂(￣(ｴ)￣)⊃`          |
   |     | Bird        | `,(u°)>`               |
   | `B` | Bunny       | `(\\_/)`               |
   |     | Cat         | `(=^o.o^=)__`          |
   |     | Cthulhu     | `^(;,;)^`              |
   |     | Fish        | `< )))) >< `           |
   |     | Bat         | `=^..^=`               |
   |     | Koala       | `@( * O * )@`          |

   {{ rightcol }}

   | `*` | Animal      | Pic                    |
   |-----|-------------|------------------------|
   | `D` | Monkey      | `@("_")@`              |
   |     | Mouse       | `<:3 )~~~~`            |
   |     | Owl         | `{O,o}`                |
   |     | Pig         | `^(*(oo)*)^`           |
   |     | Robot       | `d[ o_0 ]b`            |
   | `S` | Sheep       | `<('--')>`             |
   | `B` | Snake       | `_/\\__/\\_/--{ :>~`   |
   |     | Squid       | `くコ:彡`              |
   | `B` | Toothless   | `/|\\{O_O}/|\\`        |
   | `B` | Worm        | `_/\\__/\\__0>`          |

   {{ endcols }}

   Or make up one of your own! `(^‘0M0’^)`

   :::

{{ left }}

Add another {term}`string` variable containing a one-line ASCII art `pic` of
your pet.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-2.2.py
:caption: main.py
:class: full-width
:linenos:
:lineno-match:
:emphasize-lines: "8"
```

{{ endcols }}

:::{attention}

Strings that contain a single quote (`'`), double quote (`"`) or backslash
(`\`) require special handling.

[More info][special-characters]

:::

---

{{ left }}

If a string contains **double quotes (`"`)** you must enclose it in single quotes
to avoid closing the string early.

{{ right }}

```{code-block-hl} python
:class: full-width
:caption: main.py
:linenos:
:lineno-start: 7
pic = !!!'!!!@("_")@!!!'!!!
```

{{ row }}

If a string contains **single quotes (`"`)** you must enclose it in double quotes
to avoid closing the string early.

{{ right }}

```{code-block-hl} python
:class: full-width
:caption: main.py
:linenos:
:lineno-start: 7
pic = !!!"!!!<('--')>!!!"!!!
```

{{ row }}

If a string contains a **backslash (`\`)** you must use two to avoid escaping the
next character.

{{ right }}

```{code-block} python
:class: full-width
:caption: main.py
:linenos:
:lineno-start: 7
pic = "(\\_/)"
```

{{ endcols }}

### Part 2.3: Using variables

You can use a variable that you previously created by simply placing the name
of the variable where you would otherwise put the literal value.

For example, imagine we wanted to print the name of your PyPet.

{{ left }}

We could do it the same way we did on the first line of our program--by putting the literal string
`"Fluffy"` inside the parenthesis of the `print()` function.

{{ right }}

```{code-block} python
:caption: main.py
:linenos:
:emphasize-lines: "10"
print("Welcome to PyPet!")

name = "Fluffy"
age = 5
weight = 9.5
hungry = False
color = "white"
pic = "(=^o.o^=)__"

print("Fluffy")
```
{{ endcols }}

::::{margin}

:::{tip}

Never put quotation marks around variable names.

:::

::::

{{ left }}

Instead we will replace the the string `"Fluffy"` with the variable `name`.

Since the variable `name` contains the string `"Fluffy"` it will have the exact
same effect.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-2.3.py
:caption: main.py
:class: full-width
:linenos:
:lines: "1-10"
:lineno-match:
:emphasize-lines: "10"
```

{{ row }}

Can you add a line to print the `pic` variable?

{{ right }}

:::{dropdown} See the answer

```{literalinclude} ../../pythonclass/pypet/main-2.3.py
:caption: main.py
:class: full-width
:linenos:
:lineno-match:
:emphasize-lines: "11"
```

:::

{{ endcols }}

### Part 2.4: Combining strings

Instead of printing just the PyPet name, we are going to change our program to
print the message `"Hello from Fluffy"`.

In order to do that we'll combine  the string `"Hello from "` with the `name`
variable. This is called {term}`concatenation`.

{{ left }}

To combine the two strings put the `+` operator between them.

{{ right }}

```{code-block} python
:caption: forms the string `"Hello from Fluffy"`
:class: full-width
"Hello from " + name
```

{{ endcols }}

::::{margin}

:::{attention}

Be sure to include the space at the end of `"Hello from "`.

:::

::::

{{ left }}

Change the line where we previously printed `name` to add that small piece of
code inside the parenthesis in the print function.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-2.4.py
:caption: main.py
:class: full-width
:linenos:
:lineno-match:
:emphasize-lines: "10"
```

{{ endcols }}

### Part 2.5: Documentation

We've taken in a lot of information so far. Now is a good time to think about
writing some documentation to make our program easy to understand when we come
back to it.

#### A. Docstrings

A {term}`docstring` is a special kind of string that is enclosed by
tripple double-quotes (`"""`) or triple single-quotes( `'''`). When used as the very
first line in a file it is documentation for that file.

Docstrings have the added benefit of being able to span multiple lines.

{{ left }}

Add a docstring to your program that includes a brief description of the file,
and any other information you deem relevant. For example, a link to this
tutorial.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-2.5.py
:caption: main.py
:class: full-width
:linenos:
:lines: "1-10"
:lineno-match:
:emphasize-lines: "1-7"
```

{{ endcols }}

#### B. Comments

::::{margin}

:::{seealso}

More on [comments][]

:::

::::

You can leave notes for future reference starting with a `#`. This tells Python
to ignore everything that follows until the end of the line.

Add some comments to your program describing what the code does.

```{literalinclude} ../../pythonclass/pypet/main-2.5.py
:caption: main.py
:class: full-width
:linenos:
:lineno-match:
:lines: "9-"
:emphasize-lines: "1, 4, 11-12, 16"
```

::::{margin}

:::{admonition} Best practice

A space is recommended after the hash mark (`#`).

:::

::::

#### C. Inline comments

A comment doeesn't have to be at the beginning of the line as long as it is not
inside of quotes.

```{code-block-hl} python
:caption: main.py
:class: full-width
:linenos:
:lineno-start: 9

# print to the screen by calling the print() function
print("Welcome to PyPet!")

# creating variables
name = "Fluffy"       !!!# string: quote enclosed text!!!
age = 5               !!!# integer: whole numbers!!!
weight = 9.5          !!!# float: decimal numbers!!!
hungry = False        !!!# boolean: True or False!!!
color = "white"       !!!# string!!!
pic = "(=^o.o^=)__"   !!!# string!!!
```


Part 3: Getting Organized
-------------------------

We need a way to tell Python that all of these values represent one pet. One
way to do this is to use a Python [dictionary][].

A {term}`dictionary` allows you to group a bunch of different values together
and assign the group to a single variable. The contents of a dictionary are
arranged by {term}`key`, the unique identifier chosen to look up a particular
{term}`value`.

### Part 3.1 Make a `cat` dictionary

::::{margin}

:::{attention}

Variables use equals sign (`=`) and their names **are not** in quotes:

`name = "Fluffy"`

Dictionary keys use colon (`:`) and their keys **may be** in quotes:

`"name": "Fluffy"`

:::

::::

{{ left }}

Create a dictionary called assigned to the variable `cat` using curly-braces
(`{ }`).

Inside the curly-braces add a list of attributes seperated by commas.
Attributes have both a {term}`key` (like `"name"`, `"weight"`, `"age"`)
as well as a {term}`value` (like `"Fluffy"`, `True`, `9.6`), with a colon `:`
between the two.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-3.1.py
:caption: main.py
:class: full-width
:linenos:
:lineno-match:
:lines: "12-28"
:emphasize-lines: "9-17"
```

{{ endcols }}

### Part 3.2: Print the dictionary

{{ left }}

Change the last line so that it prints out the whole `cat` dictionary instead
of the `pic`.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-3.1.py
:caption: main.py
:class: full-width
:linenos:
:lineno-match:
:lines: "20-"
:emphasize-lines: "16"
```

{{ endcols }}

### Part 3.3: Print dictionary values

{{ left }}

Print your PyPet's name and pic. You can access values in a dictionary the
format `dictionary["key"]` such as `cat["name"]`.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-3.3.py
:caption: main.py
:class: full-width
:linenos:
:lineno-match:
:lines: "20-"
:emphasize-lines: "13, 16"
```

{{ endcols }}

### Part 3.4: Remove old stuff

{{ left }}

Remove the old variables, or you can just comment them out if you would prefer
to keep them for reference.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-3.4.py
:caption: main.py
:class: full-width
:linenos:
:lines: "9-"
:lineno-match:
```

{{ endcols }}


Part 4: Feeding your PyPet
--------------------------

::::{margin}

:::{seealso}

More on [functions][]

:::

::::

Let's "feed" our pypet using a Python function. A {term}`function` is a block
of organized, reusable code that is used to perform a single action.

::::{margin}

:::{admonition} Best practice

Functions should usually be defined near the top of the file.

:::

::::

### Part 4.1: Define `feed()`

First, we must define our function — `feed` — which changes our pypet’s
`hungry` attribute to `False` to show that it is no longer hungry.

{{ left }}

Create this simple function by writing the following above your dictionary.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-4.1.py
:caption: main.py
:class: full-width
:linenos:
:lines: "9-14"
:emphasize-lines: "4-6"
:lineno-match:
```

{{ endcols }}

There are a couple of things to take note of here. By writing
`def feed(pet):` you defining a function called `feed` that accepts one
variable `pet`. You"ll also notice we indent the next line
`pet["hungry"] = False`.

*NOTE: In python the contents of a function must be indented.*

### Part 4.2: Call the function

{{ left }}

Add `feed(cat)` below your function to use the `feed` function on your
PyPet, in this case `cat`.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-4.2.py
:caption: main.py
:class: full-width
:linenos:
:lines: "26-"
:lineno-match:
:emphasize-lines: "8-9"
```

{{ endcols }}

By calling `feed(cat)` we are passing the variable `cat` into the function
in place of `pet`. `pet` acts as a placeholder for whatever variable we
decide to pass into the function.

### Part 4.3: Increase the pet weight

We should also increase the PyPet’s weight a bit since it has eaten.

{{ left }}

Add `cat["weight"] = cat["weight"] + 1` to your `feed` function.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-4.3.py
:caption: main.py
:class: full-width
:linenos:
:lines: "12-15"
:emphasize-lines: 4
:lineno-match:
```

{{ endcols }}

### Part 4.4: Test it

We'll want to make sure it works correctly, so we'll add some temporary
debugging statements so we can see what happens.

::::{margin}

:::{tip}

You can pass multiple, comma-seperated arguments to the `print()` function to
print them with a space between each.

This is sometimes easier than {term}`concatenation`, especially for debugging.

:::

::::

{{ left }}

Add a line to print the `cat` dictionary and a message just before and after
you call `feed()`.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-4.4.py
:caption: main.py
:class: full-width
:linenos:
:lines: "33-"
:emphasize-lines: "3, 5"
:lineno-match:
```

{{ row }}

Set or change your PyPet's `"hungry"` value to `True`.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-4.4.py
:caption: main.py
:class: full-width
:linenos:
:lines: "18-25"
:emphasize-lines: "5"
:lineno-match:
```

{{ row }}

Look at the output to confirm that the PyPet's hungy and weight values changed.
They should be:

{{ right }}

| Key        | Before | After   |
|------------|--------|---------|
| `"hungry"` | `True` | `False` |
| `"weight"` | `9.5`  | `10.5`  |

{{ endcols }}

### Part 4.5: Exercises

#### A. hello() function

```{exercise} Hello Exercise
:label: pypet-hello-exercise
:class: calm

Can you write a function named `hello` that prints `"Hello World!"`?

Don't forget to call it!

```

```{solution-start} pypet-hello-exercise
:class: dropdown
```

```{code-cell} python
def hello():
  print("Hello World!")

hello()
```

```{solution-end}
```

#### B. goodbye() function

```{exercise} Goodbye Exercise
:label: pypet-goodbye-exercise
:class: calm

Write a function named `goodbye` that takes one argument `name` and
prints {samp}`Goodbye {NAME}!`

Call it with your name.

What happens when you call it multiple times with different names?
```

```{solution-start} pypet-goodbye-exercise
:class: dropdown
```

```{code-cell} python
:caption: code
def goodbye(name):
  print("Goodbye " + name + "!")

goodbye("Cruel World")

goodbye("sweetheart")
goodbye("my friend")
goodbye("stranger")
goodbye("kiss")
```

```{solution-end}
```

Part 5: Making Choices
----------------------

::::{margin}

:::{seealso}

More on [if statements][if statements]

:::

::::

But what if our PyPet is not hungry? We need to take into account whether or
not the hungry variable is set to `True` or `False`. In order to know whether
our PyPet is hungry, we are going to use an {term}`if statement`.

In Python, if statements check to see whether a specific condition (such as
whether or not `hungry = True`).

If the PyPet is hungry the program will set his hungry variable to `False` and
increase his weight. If the PyPet is not hungry then it will print
`The PyPet is not hungry!` in the console.

::::{margin}

:::{tip}

One equals sign (`=`) sets variables.

Two equals signs (`==`) checks for equivilance.

:::

::::

### Part 5.1: Add if statement

{{ left }}

Add an if statement inside of your function.

{{ right }}

```{literalinclude} ../../pythonclass/pypet/main-5.1.py
:caption: main.py
:class: full-width
:linenos:
:lines: "12-18"
:lineno-match:
```

{{ endcols }}

Notice that we use two equals sign (`==`) to check a condition (for example
`pet["hungry"] == True`). Only if the condition is not met the code beneath
the `else:` will execute.

Remember, one equal sign is used to assigned a
value to a variable (`pet["hungry"] = True` makes our PyPet hungry), two
equal signs are used to check if a condition is true
(`pet["hungry"] == True` checks whether our PyPet is hungry).

### Part 5.2: Make sure it works

Repeat the steps from [Part 4](#part-4-4-test-it) to make sure the function
still works.

Then switch to the opposite `"hungry"` value and check the output to make sure
that the before and after values are the same.


Part 6: Making Friends
----------------------

In this section we'll learn how to hold multiple values together in a [list][].

1. Let’s create another PyPet using a dictionary. Add (or customize) the code
   below under your previous PyPet dictionary.

   ```{code-block} python
   :linenos:
   mouse = {
     "name": "Mouse",
     "age": 6,
     "weight": 1.5,
     "hungry": False,
     "pic": "<:3 )~~~~",
   }
   ```

   *NOTE: Make sure to place this new PyPet above your function (use the GIF as
   reference if you are confused)*

2. Create a list to hold both of your PyPet using `pets = [cat, mouse]`.

   ```{code-block} python
   :linenos:
   pets = [cat, mouse]
   ```

   Now that we have more than one PyPet we can store them in a Python list. A
   [list][] is another data type; lists stores variables in order. If Python
   isn"t the first programming language you are learning, you may have heard of
   this same concept in other programming languages as an array.

Part 7: Going in Circles
------------------------

What if we want to feed all the pets in our list? If we want to run a function
on each variable in a list we can use something in Python called a loop. The
[for loop][] in Python has the ability to iterate over the items of any
sequence, such as a list.

```{code-block} python
:linenos:
for pet in pets:
	feed(pet)
  	print(pet)
```

Take a screenshot of your PyPet and tweet them [@Thinkful][] so I can share
your creation with the world!

BONUS
-----

Once you have completed the steps above, you should feel free to add additional
features that you design yourself! Here are some ideas to get you started:

- keep track of a health points variable
- create a boolean variable for asleep
- create a `play()` function
- create a list of phrases your Python can say at random
- get input from the user with `raw_input()`

## Conclusion & Resources

Congrats for reaching the end of this guide! For your convenience we've placed
a final version of our PyPet [on GitHub][pypet.py], if you would like to take a
look at the code. If you are stuck tweet [@Thinkful][] and we'd love to help.
Feel free to customize any or all of your project and try new things.

This guide is just the beginning of what you can do with Python. If you enjoyed
the work you’ve done here, go through any of the additional resources below.

Free Resources:

- [Learn Python Programming][] -- a beginner-friendly step-by-step interactive
  Python course provided by [Programiz][].
- [The Official Python Tutorial][] -- this tutorial at [Python.org][]
  introduces the reader informally to the basic concepts and features of the
  Python language and system. It is not comprehensive, but rather touches on
  Python’s most noteworthy features, and will give you a good idea of the
  language’s flavor and style.
- [Think Python 2e][] -- a book intended as an introduction to Python
  programming for beginners. It's available online or as a PDF download for
  free at [Green Tea Press][].
- [Interactive Python](https://www.coursera.org/course/interactivepython) -- a
  19 hour online course provided by [Coursera][] for students with little or no
  computing background.
- [Real Python][] -- a great resource for the budding developer full of
  articles on every Python-related topic you can imagine and then some.

% ---

[Think Python 2e]: https://greenteapress.com/wp/think-python-2e/
[Green Tea Press]: http://greenteapress.com/
[The Official Python Tutorial]: https://docs.python.org/3/tutorial/index.html
[Python.org]: https://www.python.org/
[Learn Python Programming]: https://www.programiz.com/python-programming
[Programiz]: https://www.programiz.com/
[Interactive Python]: https://www.coursera.org/course/interactivepython
[Coursera]: https://www.coursera.org/
[Real Python]: http://www.realpython.com/

% ---

[variables]: https://www.tutorialspoint.com/python/python_variable_types.htm
[special-characters]: https://docs.python.org/3/tutorial/introduction.html#strings
[dictionary]: https://www.tutorialspoint.com/python/python_dictionary.htm
[functions]: http://www.tutorialspoint.com/python/python_functions.htm
[if statements]: https://www.tutorialspoint.com/python/python_decision_making.htm
[list]: http://www.tutorialspoint.com/python/python_lists.htm
[for loop]: http://www.tutorialspoint.com/python/python_for_loop.htm
[comments]: https://docs.python.org/3/tutorial/introduction.html#

Credits
-------

This tutorial can be found at its new home in [Python Class][class]:

<https://alissa-huskey.github.io/python-class/lessons/tutorial.html>

It was adapted from one that was originally available[^1] on
[thinkful.com](https://www.thinkful.com/blog/learn-python/).

* Owner: [Alissa Huskey](http://github.com/alissa-huskey/)
* Code: [pypet.py][]
* Original Author: [Tatiana Tylosky](https://twitter.com/tatianatylosky)
* Original guide: [Thinkful/guide-programming-fundamentals-in-python][guide]
* Original code: [pypet.py][old-pypet.py]

[class]: https://alissa-huskey.github.io/python-class/index.html
[pypet.py]: https://github.com/alissa-huskey/python-class/blob/master/pythonclass/lessons/pypet.py
[guide]: https://github.com/Thinkful/guide-programming-fundamentals-in-python
[old-pypet.py]: https://github.com/Thinkful/pypet/blob/master/pypet.py
[@Thinkful]: https://twitter.com/thinkful

[^1]: The URL for the tutorial no longer works, but it was:

      https://www.thinkful.com/learn/guide-programming-fundamentals-in-python

% TODO
% ----
%
% [ ] fix replit screenshots and add to repl.it page
% [x] add section about comments
% [ ] add function docstring
% [ ] fancy up code blocks
%     [ ] add captions
%     [ ] fix line numbers
%     [ ] highlight new code
%     [ ] add exercises
%     [ ] turn ordered lists into subheaders

