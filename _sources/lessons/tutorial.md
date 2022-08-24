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
Beginner Tutorial
==================================

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

As you complete this guide you'll be creating a virtual pet we'll call "Pypet"
(a "Python-pet"). Remember [tamagochis][]? (Or if you were born in the 90s then
think POKEMON!) With each new Python programming concepts you learn, you will
add new features to your "Pypet".

There are no software or computer requirements for this guide except that you
need access to a web browser (which you obviously already have at this point).
You will learn how to use a free tool called [Repl.it][replit] to set up your
developer environment which takes away the typical pain of setting up a coding
environment. It is also cloud based so you can log in from any computer to view
your code.

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

:::{attention}

The instructions and screenshots in this section are for a service that seems
to no longer be active, Nitrous.io. We will be using [Repl.it][replit] instead,
but you'll have to muddle through the best you can until I get around to
updating it.

:::

To get started we'll need a "development environment", aka *a place to write
and execute code*. For this we'll use [Repl.it][replit], a
fast and free way to get you up and running. Repl.it is a cloud-based developer
environment that works well for programming in python. Since Repl.it is a
web application it won't matter whether you have a Mac or Windows or even Linux
computer to run and test your code. Follow the instructions below to set up
your Repl.it Development Environment.

1. Go to [Repl.it][replit] and create an account. *NOTE: You will have to check your
   email and activate your account before you can sign in.*
2. Once you have confirmed your email and signed in, click the "open dashboard"
   button on their [homepage][replit]. You should be prompted to create your
   first project aka developer environment.
3. First choose "Python" as your template. Next you can rename your box to
   anything you like or just leave it as is. Finally, don't worry about the
   optional section that says "Download a GitHub repo". Here's an example:

	![](http://i.imgur.com/gBTqt8X.png)

4. Click "Create Box" and then click "Next" until you see your box. Click on
   your box and then launch your environment by clicking the orange IDE button
   (which just stands for Integrated Development Environment). Now you have a
   powerful, cloud-based development environment that comes pre-installed with
   Python!

5. Let's take a quick tour:
    - In the **left panel**, you’ll see the File Browser. Here you can navigate
      the files in your home folder. At this point, you will just have the
      "workspace" folder and a README file introducing you to Repl.it When you
      have more files, you can open them in Repl.it’s text editor by double
      clicking on them in the File Browser.
    - The **middle panel** is the Text Editor. This is where you can write and
      edit code.
    - The **right panel** is for chatting if you’re using Repl.it in
      collaborative mode. Close this window for now by clicking the X in the
      upper right hand corner so you get more screen real estate.
    - The **bottom panel** is your console for actually running your python
      file.

![](http://i.imgur.com/6bXzy6A.png)

### Running Python for the first time

Here is a GIF demonstrating how to run your first python program. Feel free to
either skip down and read the steps in the text below.

![](http://i.imgur.com/kDyVy2I.gif)

1. Create a new file containing the following code in the text editor (middle panel):

	```python
	print("Welcome to Pypet!")
	```

2. Go ahead and save the file as {file}`pypet.py`.

3. Now type `python pypet.py` into your Repl.it console (in the bottom panel)
   and hit enter. By doing this you are telling your console to open the file
   `pypet.py` and execute it using the program called `python`. The console
   will output "Welcome to Pypet!".

![](http://i.imgur.com/QNGI0Xx.png)

You’ve just written your first print statement. *♬♩♪♩ Celebratory dance time! ♬♩♪♩*. The
print statement is a python function which prints things in the console — it's
very handy for learning Python and debugging your code.

If you're stuck, take another look at the GIF above.

[replit]: https://replit.com/

Part 2: Creating your Pypet
---------------------------

In this section we're going to learn how to store some different kinds of basic
information in [variables][].

Variables are a way of storing information in Python. Below we"ll create
different variables for our Pypet such as name, weight, etc. Below is a GIF
that shows how you will create variables for your Pypet in this section. You
can refer back to this as you follow along with the instructions below.

![](http://i.imgur.com/6o6eiaA.gif)

1. Create a variable called `name` equal to `"Fluffy"` (or `"Spike"` or
   `"Sir Patrick"`).

   ```python
   name = "Fluffy"
   ```

   Using an equals sign (`=`) sets a variable to a given value such as
   `name = "Fluffy"`.

   Variables can store different types of data. In this case, `name` is
   something called a **string** because `"Fluffy"` has quotations around it. A
   **string** is just a set of characters surrounded by quotations (for example
   `"Bob"`, `"New York"` or `"h4ck3r"`). *NOTE: Strings can use either single or
   double quotes in Python.* A string can also include numbers, so long as it"s
   in between quotes. **Integers** on the other hand do not have quotations.
   Let’s look at some additional data types.

2. Create three additional variables to track `age`, `weight` and `hungry`.

   ```python
   name = "Fluffy"
   age = 5
   weight = 9.5
   hungry = False
   ```

   The `age` variable is an **integer** and therefore must be a whole number.
   The `weight` variable is a **float**. Floats are a numbers that can have
   values after the decimal point.  The `hungry` variable is a a **Boolean**.
   Booleans store a value of either `True` or `False`. *NOTE: Don"t use
   quotations for these three data types, otherwise they"d all be considered
   strings*

3. Choose your Pypet"s "pic". We"ve included a few options you can use below,
   but feel free to customize it. *NOTE: Keep your Pypet"s "pic" to just one
   line as it will make the initial steps easier to follow.*

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

   Or make up your own! `(^‘0M0’^)`

   :::{admonition} Does your pic have a single quote (`'`), double quote (`"`) or backslash (`\\`)?
   :class: important, dropdown
   In strings we sometimes come across characters that require special
   handling.

   | Character              | Example      | What to Do                                                  |
   |------------------------|--------------|-------------------------------------------------------------|
   | **D**ouble quote (`"`) | `'@("_")@'`  | Enclose in single quotes to avoid closing the string early. |
   | **S**ingle quote (`'`) | `"<('--')>"` | Enclose in double quotes to avoid closing the string early. |
   | **B**ackslash (`\\`)   | `"(\\_/)"`   | Use two backslashes to avoid escaping the next character.   |

   [More info][special-characters]

   :::

4. Now add another variable that is a **string** containing this `pic` variable of our pet.

   ```python
   name = "Fluffy"
   age = 5
   weight = 9.5
   hungry = False
   pic = "(=^o.o^=)__"
   ```

5. Add some print statements to your code so you can see your Pypet in the console.

   ```python
   name = "Fluffy"
   age = 5
   weight = 9.5
   hungry = False
   pic = "(=^o.o^=)__"

   print("Hello " + name)
   print(pic)
   ```
   By writing `print("Hello " + name)` we just concatenated (aka *linked
   together*) the string `"Hello "` with the variable `name` so that the
   console will print out `Hello Fluffy`. Don"t forget to type
   `python pypet.py` in the console (bottom window) and hit enter after you
   save to see this happen. Your console should look like:

   ![](http://i.imgur.com/EDsC0Fk.png)

Part 3: Getting Organized
-------------------------

We need a way to tell Python that all of these variables represent one cat (or
dog, fish, creature, etc). One way to do this is to use a Python
[dictionary][]. Dictionaries are a way of storing multiple variables that
contain different values. Here is another GIF that you can refer back to as you
follow along with the instructions below.

![](http://i.imgur.com/yXLUVFA.gif)

1. Place your variables in a dictionary. Try using different values than the
   ones we have here.

   ```python
   cat = {
     "name": "Fluffy",
     "hungry": True,
     "weight": 9.5,
     "age": 5,
     "pic": "(=^o.o^=)__",
   }

   ```

   Here we’ve created a dictionary called `cat`. Each line contains a different
   cat attribute. Attributes have both a *key* (ex. `"name"`, `"weight"`,
   `"age"` etc) as well as a *value* (ex. `"Fluffy"`, `True`, `9.6` etc).
   Unlike assigning variables, which use an equals sign (`name = "Fluffy"`),
   dictionary attributes use a colon and need to include a comma `,` after each
   value (`"name":"Fluffy",`)

2. Add a print statement to view your new Pypet dictionary in the console.

   ```python
   cat = {
     "name": "Fluffy",
     "hungry": True,
     "weight": 9.5,
     "age": 5,
     "pic": "(=^o.o^=)__",
   }

   print(cat)
   ```

3. Print your Pypet"s name and pic. You can access variables in an list by
   using the format `dictionary["attribute"]` such as `cat["name"]`.

   ```python
   cat = {
     "name": "Fluffy",
     "hungry": True,
     "weight": 9.5,
     "age": 5,
     "pic": "(=^o.o^=)__",
   }

   print("Hello " + cat["name"])
   print(cat["pic"])

   print(cat)
   ```

   Don"t forget to first save your file and then run your file in the console
   by typing `python pypet.py` and pressing enter.

   Make sure to take another look at the GIF above if you get stuck.

Part 4: Feeding your Pypet
--------------------------

Let"s "feed" our pypet using a Python function. A [function][] is a block of
organized, reusable code that is used to perform a single action. First, we
must define our function — `feed` — which changes our pypet’s `hungry`
attribute to `False` to show that it is no longer hungry.

![](http://i.imgur.com/dmjTM4H.gif)

1. Create this simple function by writing the following below your other code.

   ```python
   def feed(pet):
      pet["hungry"] = False
   ```

   There are a couple of things to take note of here. By writing
   `def feed(pet):` you defining a function called `feed` that accepts one
   variable `pet`. You"ll also notice we indent the next line
   `pet["hungry"] = False`. *NOTE: In python the contents of a function must be
   indented.*

2. Add `feed(cat)` below your function to use the `feed` function on your
   Pypet, in this case `cat`.

   ```python
   def feed(pet):
      pet["hungry"] = False

   feed(cat)
   ```

   By calling `feed(cat)` we are passing the variable `cat` into the function
   in place of `pet`. `pet` acts as a placeholder for whatever variable we
   decide to pass into the function.

   We should also increase the Pypet’s weight a bit since it has eaten.

3. Add `cat["weight"] = cat["weight"] + 1` to your `feed` function.

   ```python
   def feed(cat):
      cat["hungry"] = False
      cat["weight"] = cat["weight"] + 1
   ```

   Use this notation to increase floats and integers.

4. Try setting your original Pypet’s hungry variable to `True` and include a
  `print(cat)` statement after `feed(cat)` to see if your Pypet"s `hungry`
  variable changed to `False` and their `weight` variable incrased.

   ```python
   print("Welome to Pypet!")

   cat = {
     "name": "Fluffy",
     "hungry": True,
     "weight": 9.5,
     "age": 5,
     "pic": "(=^o.o^=)__",
   }

   def feed(pet):
      pet["hungry"] = False
      pet["weight"] = pet["weight"] + 1

   print(cat)
   feed(cat)
   print(cat)
   ```

   When the cat is printed out the second time his weight attribute will have
   increased. Don"t forget to save and then run your python file from the
   console.

Part 5: Making Choices
----------------------

But what if our Pypet is not hungry? We need to take into account whether or
not the hungry variable is set to `True` or `False`. In order to know whether
our Pypet is hungry, we are going to use an [if statement][]. In Python, if
statements check to see whether a specific condition (such as whether or not
`hungry = True`). Take a look at the GIF below to get an idea of what this
looks like.

![](http://i.imgur.com/gKijQky.gif)

If the Pypet is hungry the program will set his hungry variable to `False` and
increase his weight. If the Pypet is not hungry then it will print
`The Pypet is not hungry!` in the console.

1. Add an if statement inside of your function.

   ```python
   def feed(pet):
    if pet["hungry"] == True:
      pet["hungry"] = False
      pet["weight"] = pet["weight"] + 1
    else:
      print("The Pypet is not hungry!")

   print(cat)
   feed(cat)
   print(cat)
   ```

   Notice that we use two equals sign (`==`) to check a condition (for example
   `pet["hungry"] == True`). Only if the condition is not met the code beneath
   the `else:` will execute. Remember, one equal sign is used to assigned a
   value to a variable (`pet["hungry"] = True` makes our Pypet hungry), two
   equal signs are used to check if a condition is true
   (`pet["hungry"] == True` checks whether our Pypet is hungry).

2. Add another `feed(cat)` below your function and try feeding the cat twice to
   see if the function worked!

   ```python
   def feed(pet):
      if pet["hungry"] == True:
          pet["hungry"] = False
          pet["weight"] = pet["weight"] + 1
      else:
          print("The Pypet is not hungry!")

   print(cat)
   feed(cat)
   print(cat)
   feed(cat)
   ```

If you get stuck don"t forget to look back at the GIF above!

Part 6: Making Friends
----------------------

In this section we'll learn how to hold multiple values together in a [list][].

1. Let’s create another Pypet using a dictionary. Add (or customize) the code
   below under your previous Pypet dictionary.

   ```python
   mouse = {
     "name": "Mouse",
     "age": 6,
     "weight": 1.5,
     "hungry": False,
     "pic": "<:3 )~~~~",
   }
   ```

   *NOTE: Make sure to place this new Pypet above your function (use the GIF as
   reference if you are confused)*

2. Create a list to hold both of your Pypets using `pets = [cat, mouse]`.

   ```python
   pets = [cat, mouse]
   ```

   Now that we have more than one Pypet we can store them in a Python list. A
   [list][] is another data type; lists stores variables in order. If python
   isn"t the first programming language you are learning, you may have heard of
   this same concept in other programming languages as an array.

Part 7: Going in Circles
------------------------

What if we want to feed all the pets in our list? If we want to run a function
on each variable in a list we can use something in Python called a loop. The
[for loop][] in Python has the ability to iterate over the items of any
sequence, such as a list.

```python
for pet in pets:
	feed(pet)
  	print(pet)
```

Take a screenshot of your Pypets and tweet them [@Thinkful][] so I can share
your creation with the world!

BONUS
-----

Once you have completed the steps above, you should feel free to add additional
features that you design yourself! Here are some ideas to get you started:

- keep track of a health points variable
- create a boolean variable for asleep
- create a `play()` function
- create a list of phrases your python can say at random
- get input from the user with `raw_input()`

## Conclusion & Resources

Congrats for reaching the end of this guide! For your convenience we've placed
a final version of our Pypet [on GitHub][pypet.py], if you would like to take a
look at the code. If you are stuck tweet [@Thinkful][] and we'd love to help.
Feel free to customize any or all of your project and try new things.

This guide is just the beginning of what you can do with Python. If you enjoyed
the work you’ve done here, go through any of the additional resources below.

Free Resources:

- [The Official Python Tutorial][] -- this tutorial at [Python.org][]
  introduces the reader informally to the basic concepts and features of the
  Python language and system. It is not comprehensive, but rather touches on
  Python’s most noteworthy features, and will give you a good idea of the
  language’s flavor and style.
- [Learn Python Programming][] -- a beginner-friendly step-by-step interactive
  Python course provided by [Programiz][].
- [Interactive Python](https://www.coursera.org/course/interactivepython) -- a
  19 hour online course provided by [Coursera][] for students with little or no
  computing background.
- [Think Python 2e][] -- a book intended as an introduction to Python
  programming for beginners. It's available online or as a PDF download for
  free at [Green Tea Press][].
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
[function]: http://www.tutorialspoint.com/python/python_functions.htm
[list]: http://www.tutorialspoint.com/python/python_lists.htm
[for loop]: http://www.tutorialspoint.com/python/python_for_loop.htm

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
