Functions
=========

A function is a set of Python instructions or {term}`statements <statement>` that can be
executed later.

Defining functions
------------------

Functions are {term}`compound-statements`, and are made up of an
{term}`identifier` and the group of {term}`statements` it contains.

```{code-block} python
---
caption: the identifer is `hello`
---
def hello():
  print("Hello.")
```

Calling functions
-----------------

To {term}`call` or execute a function, use the function {term}`identifier`
followed by `(``)`.

```{code-block} python
---
caption: 'executes `print("Hello.")`'
class: full-width

---
hello()
```


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

Parameters and arguments
------------------------

Functions can be written with one or more {term}`parameters` separated by `,`.

```{code-block} python
---
caption: defined with one parameter, `name`.
---
def hello(name):
  print("Hello", name, ".")
```

```{code-block} python
---
caption: defined with two parameters, `first_name` and `last_name`.
---
def formal_greeting(first_name, last_name):
  print("Dear", first_name, last_name, ",")
```

When calling the function the values passed are called {term}`arguments`.

Put the values you wish to send to the function inside the parenthesis
separated by `,`. When the function is executed the argument(s) will be
assigned to variables with the same names as the parameters in the function
definition.

```{code-block} python
:linenos:
hello("John")
hello("Mary")

formal_greeting("John", "Smith")
formal_greeting("Jane", "Doe")
```

```{code-block} python
---
caption: 'executes `print("Hello.")`'
class: full-width

---
hello()
```


`````{exercise} header function
:label: header-exercise

Write a `header()` function that takes one string parameter `title` and prints
the title followed by a line of dashes the same length of the title, like so:

```{code-block} python
:caption: Python shell
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

### Positional Arguments

Most of the time functions are called using {term}`positional arguments`. That
is, each argument is assigned based on its position in the argument list.

Lets look at the following function as an example.

```{code-block} python
def winners(first, second, third):
  """Print the contest winners"""
  print(f"The first place winner is: {first}")
  print(f"The second place winner is: {second}")
  print(f"The third place winner is: {third}")
```

When we call it below, `"Alex"` is assigned to the variable `first` because
that argument is the first one passed; `"Bob"` is assigned to `second` because
that argument is the second passed, and so on.

```python
>>> winners("Alex", "Bob", "Celeste")
The first place winner is: Alex
The second place winner is: Bob
The third place winner is: Celeste
```

When calling functions this way, changing the order of the arguments will
change the parameters they are assigned to.

```python
>>> winners("Celeste", "Alex", "Bob")
The first place winner is: Celeste
The second place winner is: Alex
The third place winner is: Bob
```

### Keyword Arguments

You can also use {term}`keyword arguments` when calling a function to make it
clear which argument is which. Just put the parameter name followed by an `=`
in front of the argument value.

```python
>>> winners(first="Alex", second="Bob", third="Celeste")
The first place winner is: Alex
The second place winner is: Bob
The third place winner is: Celeste
```

You can even mix and match positional arguments and keyword arguments, as long
as you put all of the positional arguments first.

```python
>>> winners("Alex", second="Bob", third="Celeste")
The first place winner is: Alex
The second place winner is: Bob
The third place winner is: Celeste
```

When using keyword arguments, you can change the order of your arguments
without effecting how they are assigned.

```python
>>> winners(second="Bob", first="Alex", third="Celeste")
The first place winner is: Alex
The second place winner is: Bob
The third place winner is: Celeste
```

It can also be useful to use keyword arguments to make your code more clear.
For example, imagine a `calculate_cost` function that takes a bunch of numeric
arguments.

```{code-block} python
def calculate_cost(price, quantity, tax, tip):
  ...
```

Which of the following lines of code do you think is easier to understand?

```{code-block} python
>>> cost = calculate_cost(4.75, 30, 0.08, 0.2)
>>> cost = calculate_cost(price=4.75, quantity=30, tax=0.08, tip=0.2)
```

Some functions have default values for arguments, making them optional. When
there are multiple arguments with default values, you can use keyword arguments
to pass some arguments while skipping others.

For example, the `print()` function can take the optional keyword arguments
`end`, for what string to append to the end of the text (default `"\n"`), and
`sep`, for what string to put between each argument when printed (default: `" "`).

You can use keyword arguments to specify either or both.

```python
>>> # called normally without keyword arguments
>>> print("hello") ; print("there")
hello
there

>>> # passing the `end` keyword argument
>>> print("hello", end=" ") ; print("there", end=".")
hello there.

>>> # called normally without keyword arguments
>>> print("555", "555", "5555")
555 555 5555

>>> # passing the `sep` keyword argument
>>> print("555", "555", "5555", sep="-")
555-555-5555
```

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

Returning values
----------------

The `return` statement is used to leave a function.

By itself `return` works similar to the `break` statement in a for loop. No
other code in the function will be executed.

```{code-block} python
:linenos:

def print_stuff():
  print("this will be printed")
  return
  print("this will never be printed")
```

It's common to return inside an if statement, for example, to avoid errors.

```{code-block} python
:linenos:

def hr(width):
  if width < 0:
    print("width can't be negative'")
    return

  print("=" * width)
```

The return statement can optionally send a value back to the caller, so that
the function call will then evaluate to that value.

Lets take a look at the difference between printing in the function, and returning.

<div class="row"><div class="col">

```{code-block} python
:linenos:
:caption: prints a string
def hello(name):
  print(f"hello {name}")
```

```{code-block} python
:caption: python shell
>>> text = hello("you")
hello you
>>> print(type(text))
<class 'NoneType'>
>>> print(text)
None
```

When the function is called, the string `"hello you"` is
printed. Since nothing is returned, `text` is `None`.

</div><div class="col">

```{code-block} python
:caption: returns a string
def hello(name):
  return f"hello {name}"
```

```{code-block} python
:caption: python shell
>>> text = hello("you")
>>> print(type(text))
<class 'str'>
>>> print(text)
hello you
```

Nothing is printed when the function is called and `text` is assigned the
string `"hello you"`.

</div></div>

```{exercise} random function
:label: random-function-exercise

Write a `number()` function to return a random number between 1 and 100.

```

`````{solution} random-function-exercise
:class: dropdown

```{code-block} python
import random

def number():
  return random.randint(1, 100)
```

`````


Docstrings
----------

Docstrings are a special kind of string in Python that are enclosed with three
single `'''` or double `"""` quotes.  They can be used as a normal string that
has the added bonus of being able to span multiple lines.

Their namesake, and the reason we are interested in them today, comes from the
fact that when a docstring is the very first line of a file, function, or
class, it serves as documentation.

```{code-block} python
:linenos:
def formal_greeting(first_name, last_name):
  """Returns a string to start a letter"""
  return "Dear" + first_name + last_name + ","
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
  print("Hello", name, ".")

def formal_greeting(first_name, last_name):
  """Returns a string to start a letter"""
  return "Dear" + first_name + last_name + ","
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
    formal_greeting(first_name, last_name)
        Returns a string to start a letter

    hello(name)
        Print hello to name

FILE
    .../greetings.py
```

Ideally all functions should have a simple doctring describing what the
function does, any parameters, and any return value. For simple functions a
one line brief description will do the trick.

For more complicated functions, you can take advantage of the multiline
abilities of docstrings to add detailed information. Here's a long docstring example.

```{code-block} python
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

```{exercise} docstrings
:label: docstrings-exercise

Add a simple docstring to your file and all of the functions you've written
today. Import them into a Python shell and use the `help()` function to view them.

```


% [ ] returning multiple values
% [ ] default arguments
% [ ] arbitrary argument list
% [ ] arbitrary keyword argument list
% [ ] unpacking arguments
% [ ] annotations

% [x] keyword arguments
% [x] docstrings

% glossary
% --------
% [ ] return
% [ ] positional arguments
% [ ] keyword arguments


