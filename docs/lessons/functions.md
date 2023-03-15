---
myst:
  substitutions:
    left:  '{{ leftcol | replace("col", "col-5") }}'
    right: '{{ rightcol | replace("col", "col-7") }}'
    row: '{{ newrow | replace("col", "col-5") }}'
    label: '<div class="text-right">Syntax:</div>'

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
Functions
=========

Often in programming you want to do the same task again and again. Instead of
repeatedly typing the same code or copy and pasting it, you can save the code
in a reusable function.

A function is a set of Python instructions or {term}`statements <statement>`
that can be executed later. If you're familiar with macros in spreadsheet
programs, it's kind of like that.

```{include} ../toc.md
```

Part 1: Defining and calling
----------------------------

```{image} assets/playing-piano.jpg
:align: right
:scale: 35%
```

When you create or {term}`define` a function, you can imagine it's like a
[music roll][music-roll] for a [self-playing piano][playing-piano].

Later when you want to use or "play" it, you {term}`call` the function.

{{ clear }}

{{ br }}

{{ leftcol }}

<div class="text-right"> Function syntax: </div>

{{ br }}

To define a function you'll write a {term}`compound statement` that starts with
the `def` keyword. Next choose a name or {term}`identifier` that will be used
to call it, followed immediately by a pair of parenthesis and a colon.

On a new, indented line, add the statements that make up what the function
does. Each of the statements indented at the same level will be part of the
function.

{{ rightcol }}

```{include} ../templates/syntax/def.md
```

```{include} ../templates/desc/def.md
```

{{ newrow }}

Here's a simple example.

{{ rightcol }}

```{code-cell} python
def hello():
    print("Hello.")
```

{{ newrow }}

To {term}`call` a function add a pair of parenthesis immediately after the
function name. For example, here's how to call the `hello` function.

{{ rightcol }}

```{code-cell} python
hello()
```

{{ endcols }}

### Part 1.1: Exercise

```{exercise} horizontal line function
:label: hr-exercise

Write a function called `hr` to print a line of dashes 100 characters wide, like so:

`--------------------------------------------------`


```

`````{solution} hr-exercise
:class: dropdown

```{code-block} python
def hr():
  print("-" * 100)
```

`````

[music-roll]: https://en.wikipedia.org/wiki/Piano_roll
[playing-piano]: https://en.wikipedia.org/wiki/Player_piano
[piano]: assets/playing-piano.jpg

Part 2: Parameters and Arguments
--------------------------------

While it is useful to be able to repeat exactly the same lines of code, often
we want to repeat tasks that are *almost* the same. This is where parameters
and arguments come in, because they let us change the value of specific
variables when a function is called.

### Part 2.1: Parameters and Arguments

A {term}`parameter` is a variable name you give to data that the function gets
later. You add it to the function definition as you'll see below.

The actual values, called {term}`arguments <argument>`, get sent to the
function and assigned when the function is called, then cease to exist when the
function is done being executed.

{{ leftcol }}

To define a function with a parameter, put the parameter (variable) name you
picked inside the parenthesis on the `def` line.

{{ rightcol }}

```{code-cell} python
def hello(name):
    message = "Hello " + name + "."
    print(message)
```

{{ newrow }}

{{ endcols }}

{{ leftcol }}

Similarly, put the {term}`argument`, (the variable value) inside the
parenthesis when calling the function.

{{ rightcol }}

```{code-cell} python
hello("John")
```

{{ endcols }}

When the function is executed the argument value is assigned to a variable with
the parameter name you chose. As if each time you call the function, the line
{samp}`{PARAM} = {ARG}` is run first.

{{ leftcol }}

So that this:

```{code-block-hl} python
def hello(!!!name!!!):
    message = "Hello " + name + "."
    print(message)

hello(!!!"Mary"!!!)
```

{{ rightcol }}

Is equivalent to:

```{code-block-hl} python
!!!name!!! = !!!"Mary"!!!
message = "Hello " + name + "."
print(message)

```

{{ endcols }}

{{ leftcol }}

Separate multiple parameters with a comma.

{{ rightcol }}

```{code-cell} python
def greet(time, name):
  message = "Good " + time + " " + name + "."
  print(message)
```

{{ newrow }}

The same with multiple arguments.

{{ rightcol }}

```{code-cell} python
:linenos:

greet("morning", "Mr. Smith")
greet("afternoon", "Mrs. Doe")
```

{{ endcols }}

### Part 2.2: Exercise

`````{exercise} header function
:label: header-exercise

Write a `header()` function that takes one string parameter `title` and prints
the title followed by a line of dashes the same length of the title, like so:

```{code-block} python
>>> header("Chapter One")
Chapter One
-----------
```

`````

`````{solution} header-exercise
:class: dropdown

```{code-block} python
def header(title):
  print(title)
  print("-" * len(title))
```

`````

### Part 2.3: Positional Arguments

Most of the time functions are called using {term}`positional arguments <positional argument>`. That
is, each argument is assigned based on its position in the argument list.

{{ leftcol }}

Lets look at the following function as an example.

{{ rightcol }}

```{code-cell} python

def winners(first, second, third):
  """Print the contest winners"""
  print(f"The first place winner is: {first}")
  print(f"The second place winner is: {second}")
  print(f"The third place winner is: {third}")

```

{{ newrow }}

When we call it below, `"Alex"` is assigned to the variable `first` because
that argument is the first one passed; `"Bob"` is assigned to `second` because
that argument is the second passed, and so on.

{{ rightcol }}

```{code-cell} python
winners(
  "Alex",
  "Bob",
  "Celeste",
)
```

{{ newrow }}

When calling functions this way, changing the order of the arguments will
change the parameters they are assigned to.

{{ rightcol }}

```{code-cell} python
winners(
  "Celeste",
  "Alex",
  "Bob"
)
```

{{ endcols }}

### Part 2.4: Keyword Arguments

{{ leftcol }}

You can also use {term}`keyword arguments <keyword argument>` when calling a function to make it
clear which argument is which. Just put the parameter name followed by an `=`
in front of the argument value.

{{ rightcol }}

```{code-cell} python
winners(
  first="Alex",
  second="Bob",
  third="Celeste"
)
```

{{ newrow }}

You can even mix and match positional arguments and keyword arguments, as long
as you put all of the positional arguments first.

{{ rightcol }}

```{code-cell} python
winners(
  "Alex",
  second="Bob",
  third="Celeste"
)
```

{{ newrow }}

When using keyword arguments, you can change the order of your arguments
without effecting how they are assigned.

{{ rightcol }}

```{code-cell} python
winners(
  second="Bob",
  first="Alex",
  third="Celeste"
)
```

{{ newrow }}

It can also be useful to use keyword arguments to make your code more clear.
For example, imagine a `calculate_cost` function that takes a bunch of numeric
arguments.

{{ rightcol }}

```{code-cell} python
def calculate_cost(price, quantity, tax, tip):
  ...
```

{{ newrow }}

Which of the following lines of code do you think is easier to understand?

{{ rightcol }}

```{code-cell} python
cost = calculate_cost(
  4.75,
  30,
  0.08,
  0.2,
)
```

```{code-cell} python
cost = calculate_cost(
  price=4.75,
  quantity=30,
  tax=0.08,
  tip=0.2,
)
```

{{ newrow }}

Some functions have default values for arguments, making them optional. When
there are multiple arguments with default values, you can use keyword arguments
to pass some arguments while skipping others.

For example, the `print()` function can take the optional keyword arguments
`end`, for what string to append to the end of the text (default `"\n"`), and
`sep`, for what string to put between each argument when printed (default: `" "`).

You can use keyword arguments to specify either or both.

{{ rightcol }}

```{code-cell} python
# called normally without keyword arguments
print("hello")
print("there")
```

```{code-cell} python
# passing the `end` keyword argument
print("hello", end=" ")
print("there", end=".")
```

```{code-cell} python
# called normally without keyword arguments
print("555", "555", "5555")
```

```{code-cell} python
# passing the `sep` keyword argument
print("555", "555", "5555", sep="-")
```

{{ endcols }}

### Part 2.5: Exercises

```{exercise} keyword arguments
:label: keyword-arguments-exercise

1. Call the `print()` function with the arguments `"a"`, `"b"`, and `"c"` with
   a value of `"\n"` for the `sep` keyword argument.
2. Call the `print()` function multiple times in a row, with the value of `"... "`
   for the `end` keyword argument.
3. a. Write a function called `birthday` that takes the arguments `name`, `month`,
   `day` and `year`, and prints `"____s birthday is on ___ __, ____."`

   For example:
   "Homer Simpsons birthday is on May 12, 1956."

   b. Call it with multiple names and birthdays, using positional arguments and
      keyword arguments.
```

`````{solution} keyword-arguments-exercise
:class: dropdown


1\. Call the `print()` function with the arguments `"a"`, `"b"`, and `"c"` with
   a value of `"\n"` for the `sep` keyword argument.

```{code-block} python
>>> print("a", "b", "c", sep="\n")
a
b
c
```

2\. Call the `print()` function multiple times in a row, with the value of `"... "`
   for the `end` keyword argument.

```{code-block} python
>>> print("x", end="... ") ; print("y", end="... ") ; print("z", end="... ")
x... y... z...
```

3a. Write a function called `birthday` that takes the arguments `name`, `month`,
   `day` and `year`, and prints `"____s birthday is on ___ __, ____."`

```{code-block} python
def birthday(name, month, day, year):
   print(f"{name}s birthday is on {month} {day}, {year}.")
```

3b. Call it with multiple names and birthdays, using positional arguments and
    keyword arguments.

```python
>>> birthday("Homer Simpson", "May", 12, 1956)
Homer Simpsons birthday is on May 12, 1956.

>>> birthday(name="Homer Simpson", month="May", day=12, year=1956)
Homer Simpsons birthday is on May 12, 1956.

>>> birthday(year=1984, month="April", day=1, name="Bart Simpson")
Bart Simpsons birthday is on April 1, 1984.

>>> birthday(month="May", day=9, year=1986, name="Lisa Simpson")
Lisa Simpsons birthday is on May 9, 1986.
```

`````

Part 3: Returning values
------------------------

The {term}`return` statement is used to exit a function and optionally send
data back to the caller.

{{ leftcol }}

By itself `return` works similar to the `break` statement in a for loop. No
other code in the function will be executed.

{{ rightcol }}

```{code-cell} python
:linenos:

def print_stuff():
  print("this will be printed")
  return
  print("this will never be printed")

print_stuff()
```

{{ newrow }}

It's common to `return` inside an `if` statement, for example, to avoid errors.

{{ rightcol }}

```{code-cell} python

def hr(width):
  if width < 0:
    print("Error: width can't be negative")
    return

  print("=" * width)
```

```{code-cell} python
hr(-10)
```

```{code-cell} python
hr(20)
```

{{ newrow }}

The `return` statement can optionally send a value back to the caller, so that
the function call will then evaluate to that value.

{{ rightcol }}

```{code-cell} python
def is_between(num, start_range, end_range):
    if num >= start_range and num <= end_range:
        return True
    else:
        return False
```

{{ newrow }}

Then you can call the function anywhere you want to use the value it returns.

For example, assigning it to a variable...

{{ rightcol }}

```{code-cell} python
from random import randint

height = randint(36, 108)
too_short = is_between(height, 1, 48)
words = ("can", "cannot")

print(f'A person of {height}" {words[too_short]} ride the ride.')
```

{{ newrow }}

...in an `if` statement...

{{ rightcol }}

```{code-cell} python
score = randint(-200, 200)

if not is_between(score, 1, 100):
    print(f"Error: Invalid score: {score}")
else:
    print(f"Your score is: {score}%")
```

{{ newrow }}

...or as part of an expression.

{{ rightcol }}

```{code-cell} python
rating = randint(0, 10)
text = is_between(rating, 1, 5) * f"Stars: {'*' * rating}"

if not text:
    print(f"Invalid rating: {rating}")
else:
    print(text)
```

{{ endcols }}

Lets take a look at the difference between printing in the function, and returning.

{{ leftcol }}

```{code-cell} python
:linenos:
:caption: prints a string
def hello(name):
  print(f"hello {name}")
```

```{code-cell} python
text = hello("you")
```

```{code-cell} python
print(type(text))
```

```{code-cell} python
print(text)
```

When the function is called, the string `"hello you"` is
printed. Since nothing is returned, `text` is `None`.

{{ rightcol }}

```{code-cell} python
def hello(name):
  return f"hello {name}"
```

```{code-cell} python
text = hello("you")
```

{{ br }}
{{ br }}
{{ br }}
{{ br }}

```{code-cell} python
print(type(text))
```

```{code-cell} python
print(text)
```

Nothing is printed when the function is called and `text` is assigned the
string `"hello you"`.

{{ endcols }}

### Part 3.1: Exercise

```{exercise} random function
:label: random-function-exercise

Write a `number()` function to `return` a random number between `1` and `100`.

```

`````{solution} random-function-exercise
:class: dropdown

```{code-block} python
import random

def number():
  return random.randint(1, 100)
```

`````

Part 4: Docstrings
------------------

Docstrings are a special kind of string in Python that are enclosed with three
single `'''` or double `"""` quotes.  They can be used as a normal string that
has the added bonus of being able to span multiple lines.

Their namesake, and the reason we are interested in them today, comes from the
fact that when a docstring is the very first line of a file, function, or
class, it serves as documentation.

```{code-cell} python
def greet(time, name):
  """Return a greeting message based on the time of day"""
  message = "Good " + time + " " + name + "."
  return message
```

You can see this works like a comment while looking at the code. Niftier still,
a functions docstring is saved by Python and can be used from the interpreters
`help()` function.

Say we have the following {file}`greetings.py` file:

```{code-block} python
:caption: greetings.py
:linenos:
"""Functions for greeting people"""

def hello(name):
    """Print hello to name"""
    message = "Hello " + name + "."
    print(message)

def greet(time, name):
  """Return a greeting message based on the time of day"""
  message = "Good " + time + " " + name + "."
  return message
```

We could then import our functions from a Python shell, and call the `help()` on
our own `hello` function.

```{code-block} python
:caption: Python shell

>>> from greetings import hello
>>> help(hello)
Help on function hello in module greetings:

hello(name)
    Print hello to name
```

Or we could do the same thing for the whole `greetings` module:

```{code-block} python
:caption: Python shell
>>> import greetings
>>> help(greetings)
Help on module greetings:

NAME
    greetings - Functions for greeting people

FUNCTIONS
    greet(time, name)
        Return a greeting message based on the time of day

    hello(name)
        Print hello to name

FILE
    .../greetings.py
```

Ideally all functions should have a simple doctring describing what the
function does, any parameters, and any return value. For simple functions a
one line brief description will do the trick.

For more complicated functions, you can take advantage of the multi-line
abilities of docstrings to add detailed information. Here's a long docstring
example.

```{code-block} python
:linenos:

def prettify(message, align, width):
    """Return a formatted message

    Params
    ------
    message (str): Message to format
    align (str): Alignment of text (left, center, right)
    width (int): Width of text

    Returns
    -------
    message (str): formatted message

    Examples
    --------
    >>> prettify("hello", "center", 100)
    '            hello             '
    >>> prettify("goodbye", "right", 100)
    '                       goodbye'
    """

    if align not in ("left", "center", "right"):
      print(f"Invalid align argument: '{align}'")
      return

    if align == "center":
      message = message.center(width)
    elif align == "right":
      message = message.rjust(width)

    return message
```

Part 5: Exercises
-----------------

### Part 5.1: `welcome()` function

`````{exercise} welcome
:label: extra-exercise-a

Write a function named `welcome` that prints `"Welcome to coding class!"`

```python
>>> welcome()
```

`````

`````{solution} extra-exercise-a
:class: dropdown

```{code-block} python
:linenos:
def welcome():
   print("Welcome to coding class!")
```

```python
>>> welcome()
Welcome to coding class!
```

`````

### Part 5.2: `letter_count()` function

`````{exercise} letter_count
:label: extra-exercise-b

Write a function called `letter_count` that takes one argument `text` and
prints `"There are __ characters in '___'."`  Call it multiple times with
different arguments.

`````

`````{solution} extra-exercise-b
:class: dropdown

```{code-block} python
:linenos:
def letter_count(text):
  print(f"There are {len(text)} characters in '{text}'.")
```

```python
>>> letter_count("hello")
There are 5 characters in 'hello'.

>>> letter_count("goodbye")
There are 7 characters in 'goodbye'.

>>> letter_count("many thanks")
There are 11 characters in 'many thanks'.

>>> letter_count("")
There are 0 characters in ''.
```

`````

### Part 5.3: `is_vowel()` function

`````{exercise} is_vowel
:label: extra-exercise-c

a. Write a function named `is_vowel` that returns `True` if a character is a
   vowel and `False` otherwise. Don't print anything in the function. Bonus:
   make it case-insensitive.

```python
>>> is_vowel("a")
True

>>> is_vowel("E")
True

>>> is_vowel("c")
False

>>> is_vowel("something")
False
```

b. Call the function with a letter assign the result to a variable like
`answer`.  Print `"is '_____' a vowel?: ___"`. (Note: this should be
__outside__ of the function.) Do this same thing with multiple arguments.

`````

`````{solution} extra-exercise-c
:class: dropdown

```{code-block} python
:linenos:
def is_vowel(letter):
   return letter.lower() in ["a", "e", "i", "o", "u"]
```

```python
>>> ltr = "a" ; answer = is_vowel(ltr)
>>> print(f"is '{ltr}' a vowel?: {answer}")
is 'a' a vowel?: True

>>> ltr = "z" ; answer = is_vowel(ltr)
>>> print(f"is '{ltr}' a vowel?: {answer}")
is 'z' a vowel?: False

>>> ltr = "E" ; answer = is_vowel(ltr)
>>> print(f"is '{ltr}' a vowel?: {answer}")
is 'E' a vowel?: True

>>> ltr = "word" ; answer = is_vowel(ltr)
>>> print(f"is '{ltr}' a vowel?: {answer}")
is 'word' a vowel?: False

>>> ltr = "" ; answer = is_vowel(ltr)
>>> print(f"is '{ltr}' a vowel?: {answer}")
is '' a vowel?: False
```

`````

### Part 5.4: `tip()` function

`````{exercise} tip
:label: extra-exercise-d
a. Write a function `tip` that takes the arguments, `cost` and `percent`, and
returns the tip amount. Do not print anything inside the function.

```python
>>> tip(100, 20)
20.0
```

b. Call the function with an argument for `cost` and `percent` and assign the
result to a variable like `amount`.  Print the result like: `"A ____% tip on a
$_____ bill is: $_____"`. (Note: this should be __outside__ of the function.)
Do this same thing with multiple arguments.

`````

`````{solution} extra-exercise-d
:class: dropdown

```{code-block} python
:linenos:
def tip(cost, percent):
   return cost * (percent/100)
```

```python
>>> c, p = 100, 20 ; amount = tip(c, p)
>>> print(f"A {p}% tip on a ${c} bill is: ${amount}")
A 20% tip on a $100 bill is: $20.0

>>> c, p = 10, 15 ; amount = tip(c, p)
>>> print(f"A {p}% tip on a ${c} bill is: ${amount}")
A 15% tip on a $10 bill is: $1.5

>>> c, p = 500, 10 ; amount = tip(c, p)
>>> print(f"A {p}% tip on a ${c} bill is: ${amount}")
A 10% tip on a $500 bill is: $50.0
```

`````

### Part 5.5: `total()` function

`````{exercise} total
:label: extra-exercise-e
a. Write a function `total` that takes the arguments, `bill` and `tip_percent`,
and returns the total including the tip. To calculate the tip call your
`tip()` function from the `total()` function. Do not print anything inside the
function.

```python
>>> total(100, 20)
120.0
```

b. Call the function with an argument for `bill` and `tip_percent` and assign the
result to a variable like `final`.  Print the result like:
`"The final total on a $___ bill including a __% tip is: $_____"`.
(Note: this should be __outside__ of the function.) Do this same thing with
multiple arguments.

`````

`````{solution} extra-exercise-e
:class: dropdown

```{code-block} python
:linenos:
def total(bill, tip_percent):
   return bill + tip(bill, tip_percent)
```

```python
>>> b = 100 ; t = 20 ; final = total(b, t)
>>> print(f"The final total on a ${b} bill including a {t}% tip is: ${final}")
The final total on a $100 bill including a 20% tip is: $120.0

>>> b = 10 ; t = 15 ; final = total(b, t)
>>> print(f"The final total on a ${b} bill including a {t}% tip is: ${final}")
The final total on a $10 bill including a 15% tip is: $11.5

>>> b = 500 ; t = 10 ; final = total(b, t)
>>> print(f"The final total on a ${b} bill including a {t}% tip is: ${final}")
The final total on a $500 bill including a 10% tip is: $550.0
```

`````

### Part 5.6: Docstring exercise

```{exercise} docstrings
:label: docstrings-exercise

Add a simple docstring to your file and all of the functions you've written
today. Import them into a Python shell and use the `help()` function to view them.

```

Reference
---------

### Glossary

```{glossary} functions

argument
  A {term}`value` that is passed as input to a function.

call
  code that tells the computer to {term}`execute` the code within a previously
  defined function or method by using the function name followed by `(` `)`,
  with any arguments inside the parenthisis.

define
defining a function
  Creating a function by specifying its name, the parameters it takes, and what
  it does. In Python, this is done using the `def` keyword.


docstring
  a special kind of string surrounded by triple double-quotes `"""` or triple
  single-quotes `'''` that can span multiple lines. When a docstring appears as
  the first expression in a file, module, class, or function it is stored by
  Python as documentation and can be seen by using the `help()` function in the
  {term}`Python shell`.

function
  a named block of reusable code. A function may or may not take arguments, and
  may or may not return a value. In Python it is recommended to use the
  `lower_case_with_underscores` for function names.

keyword argument
  when arguments passed to a function are preceeded by the paramater name and
  an equals sign (`=`) so that they are assigned to the specified parameter
  regardless of the order in which they appear

parameter
  The named variables that appear in a function definition to specify the
  arguments it can accept.

positional argument
  when arguments are passed to a function so that they are assigned based on
  the order in which they appear

return
  a statement that can be used in a function to exit the function and
  optionally send a value to the caller

```

### See Also

```{seealso}

* [python.org > Tutorial > Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [python.org > Tutorial > Documentation Strings](https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings)
* [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
* [Real Python > The Python return Statement: Usage and Best Practices](https://realpython.com/python-return-statement/)

```

