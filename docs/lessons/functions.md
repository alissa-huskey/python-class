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

Functions can be written to accept data as one or more {term}`parameters` separated by `,`.

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

Returning values
----------------

The {term}`return` statement is used to leave a function.

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

% [ ] returning multiple values
% [ ] default arguments
% [ ] keyword arguments
% [ ] arbitrary argument list
% [ ] arbitrary keyword argument list
% [ ] unpacking arguments
% [ ] docstrings
% [ ] annotations


