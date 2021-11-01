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
depth: 2
---
Functions
=========

In this lesson you'll learn about some slightly more advanced or obscure
function writing.

:::{important}

Be sure to complete the fundamentals [](../functions.md) lesson first.

:::

```{contents} Table of Contents
:backlinks: top
:local:
:depth: 2
```

Part 1: Optional arguments
--------------------------

### Part 1.1: Default Values

{{ leftcol }}

You can make an argument optional by giving it a default value.

{{ rightcol }}

```{code-cell} python
:class: full-width
def hr(width=20):
    print("-" * width)
```

{{ newrow }}

When you call the function, you can pass an arguent as you normally would.

{{ rightcol }}

```{code-cell} python
:class: full-width
hr(10)
```

{{ newrow }}

Or skip the argument to use the default value.

{{ rightcol }}

```{code-cell} python
:class: full-width
hr()
```

{{ newrow }}

Any parameters without default values have to go before any with default
values.

{{ rightcol }}

```{code-cell} python
:class: full-width
def hr(char, width=20):
    print(char * width)
```

{{ endcols }}

### Part 1.2: Exercise

`````{exercise} Defaults
:label: defaults-exercise

Define a function `write()` that takes three arguments:

* `message`
* `before` with a default of `0`
* `after` with a default of `0`

The function should print `message` with the specified number of blank lines
`before` and `after`, then print the string `"----"` at the end.

Call it with all variations of missing and present default arguments.

`````

`````{solution} defaults-exercise
:class: dropdown

```{code-block} python
:caption: "Defaults Exercise"
:class: full-width
:linenos:

def write(message, before=0, after=0):
  print("\n"*before, end="")
  print(message)
  print("\n"*after, end="")
  print("----")

write("hello")
write("bonjour", after=1)
write("hola", before=1)
write("aloha", before=1, after=1)
```

`````

### Part 1.3: Mutable Defaults

{{ leftcol }}

Avoid using a {term}`mutable` object as a default value, since it is evaluated
only once when the function is defined.

{{ rightcol }}

```{code-cell} python
:class: full-width
def setup(project, options={}):
    if "title" not in options:
        options["title"] = project
    print(id(options), options)

```

{{ newrow }}

Therefore any call that uses the default value will have the *exact same
object*.

{{ rightcol }}

```{code-cell} python
:class: full-width
setup("home")
setup("work")
setup("school", {"title": "School Work"})
```

{{ newrow }}

For mutable types, set the default value to `None`. Then in the body of the
function, assign the value if the argument is {term}`falsy`.

{{ rightcol }}

```{code-cell} python
:class: full-width
def setup(project, options=None):
    if not options:
        options = {}
    if "title" not in options:
        options["title"] = project
    print(id(options), options)
```

{{ newrow }}

This will ensure that every time the function is called, a new value is created
and assigned.

{{ rightcol }}

```{code-cell} python
:class: full-width
setup("home")
setup("work")
setup("school", {"title": "School Work"})
```

{{ newrow }}

A shorthand for this is:

{samp}`{NAME} = {NAME} or {DEFAULT}`

{{ rightcol }}

```{code-cell} python
:class: full-width
def setup(project, options=None):
    options = options or {}
    if "title" not in options:
        options["title"] = project
    print(id(options), options)
```

{{ newrow }}

{{ rightcol }}

```{code-cell} python
:class: full-width
setup("home")
setup("work")
setup("school", {"title": "School Work"})
```

{{ endcols }}

% ### Part 1.4: Exercise

% `````{exercise} Mutable Defaults
% :label: mutable-defaults-exercise

% `````

% `````{solution} mutable-defaults-exercise
% :class: dropdown

% ```{code-block} python
% :caption: "Mutable Defaults Exercise"
% :class: full-width
% :linenos:

% ```

% `````

Part 2: Arbitrary arguments
---------------------------

Sometimes you want a function to be able to take an arbitrary arguments. These
are called {term}`variadic` arguments.

### Part 2.1: Positional

{{ leftcol }}

This can be done with a single asterisk before a parameter name.  Any
positional arguments will then be in a tuple with that name, in this case
`args`.

{{ rightcol }}

```{code-cell} python
:class: full-width

def thing(*args):
    print(args)
    if args:
      print(args[0])
```

{{ newrow }}

You can then call it with no arguments...

{{ rightcol }}

```{code-cell} python
:class: full-width
thing()
```

{{ newrow }}

One argument...

{{ rightcol }}

```{code-cell} python
:class: full-width
thing("a")
```

{{ newrow }}

Or any number of arguments...

{{ rightcol }}

```{code-cell} python
:class: full-width
thing("a", "b", "c", "d", "e")
```

{{ endcols }}

### Part 2.2: Keyword

{{ leftcol }}

To take arbitrary keyword arguments, put two astricks before a paramater name.
The keyword arguments will then be in a dictionary with that name, in this case
`kwargs`.

{{ rightcol }}

```{code-cell} python
:class: full-width
def thing(**kwargs):
    print(kwargs)
    if "a" in kwargs:
        print(kwargs["a"])
```

{{ newrow }}

Then any keyword arguments will be in a dictionary with that name.

{{ rightcol }}

```{code-cell} python
:class: full-width
thing(a=1, b=2, c=3)
```

{{ endcols }}

Part 3: Unpacking Arguments
---------------------------

Sometimes want a function to take arbitrary arguments, sometimes you want to
send all of the values in a list or dictionary as arguments to a function. This
is known as {term}`unpacking`.

### Part 3.1: Calling

{{ leftcol }}

To send all elements in a list, tuple, or other {term}`sequence`, put an astrisk
before the object.

{{ rightcol }}

```{code-cell} python
:class: full-width
birth_stones = [
    "Garnet",
    "Amethyst",
    "Aquam",
    "Diamond",
    "Emerald"
]
print(*birth_stones)
```

{{ newrow }}

To send all elements of a dictionary as {term}`keyword arguments`, put two
astricts before the dictionary.

{{ rightcol }}

```{code-cell} python
:class: full-width
def show(red, green, blue, hex_code):
    print(f"Hex Color: #{hex_code} is RGB: ({red}, {green}, {blue})")

color = {
  "hex_code": "21abcd",
  "red": 33,
  "green": 171,
  "blue": 205,
}

show(**color)
```

{{ endcols }}

% ### Part 3.2: Exercises

% TODO
% [ ] order of positional, kwargs, unpacked args



Part 4: Annotations
-------------------

Python provides a syntax for documenting the type of various values called
annotations. While annotations have no effect on how a function behaves, it can
be helpful in clarifying the intended usage.

### Part 4.1: Parameter Hints

{{ leftcol }}

You can specify the expected type of each parameter by adding a colon after the
parameter name, followed by the type.

{{ rightcol }}

```{code-block-hl} python
:class: full-width

def debug(message!!!: str!!!):
    print(message)
```

{{ endcols }}

### Part 4.2: Variable Hints

{{ leftcol }}

Incidentally, you can specify the the type of a particular variable the same
way.

{{ rightcol }}

```{code-block-hl} python
:class: full-width

maximum!!!: int!!! = 100
name!!!: str!!!
```

{{ endcols }}

### Part 4.3: Return hints

{{ leftcol }}

You can specify the type of any returned value by adding `->` followed by the
type before the colon.

{{ rightcol }}

```{code-block-hl} python
:class: full-width

from random import randint

def random(limit: int=10) !!!-> int!!!:
    return randint(1, limit)
```

{{ endcols }}

Be aware that is strictly documentation. An annotation does not change or
enforce a the type of a given value.

Part 5: Lambdas
---------------

Python provides an inline syntax for short functions that return the results of
a single expression called {term}`lambdas <lambda>`.

{{ leftcol }}

```{code-block-hl} python
:class: full-width

def random():
    return !!!randint(1, 100)!!!
```

{{ rightcol }}

```{code-block-hl} python
:class: full-width

random = lambda: !!!randint(1, 100)!!!
```

{{ newrow }}

```{code-block-hl} python
:class: full-width

def random(!!!limit!!!):
    return !!!randint(1, limit)!!!
```

{{ rightcol }}

```{code-block-hl} python
:class: full-width

random = lambda !!!limit!!!: !!!randint(1, limit)!!!
```

{{ endcols }}

% TODO
% [ ] defaults
% [ ] sort

Part 6: Shorthand
-----------------

It is possible, though not recommended, to write a function (or any other
compound statement) all on one line, assuming that it contains a single line.

The following two functions are equilivant.

{{ leftcol }}

```{code-block} python
:class: full-width
:linenos:

def hello():
  print("hello")

```

{{ rightcol }}

```{code-block} python
:class: full-width
:linenos:

def hello(): print("hello")

```

{{ endcols }}

Reference
---------

### Glossary

```{glossary} functions
variadic
variadic arguments
    When any number of arguments may be passed to a function or method.

annotations
type hints
  Syntax for specifying the type of a variable, class attribute, function
  parameter or return value.

lambda
  An anonymous inline function consisting of a single expression.

unpacking
unpacking arguments
  Sending all elements in a collection as arguments to a function call.
```

### See Also

```{seealso}

* [python.org > Tutorial > More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
* [python.org > Tutorial > Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
* [python.org > Tutorial > Function Annotations](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)
* [python.org > Glossary > type hint](https://docs.python.org/3/glossary.html#term-type-hint)
* [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)

```



% TODO
% [ ] `/`: positional only
% [ ] `*`: keyword only
% [ ] unpacking: *args
% [ ] unpacking: **kwargs
% [ ] decorators
% [ ] recursive functions
% [ ] sending functions as arguments
% [ ] return multiple values
% [x] default arguments
%     [x] note about mutable types ie `def x(y=[])`
%     [x] order of default args
% [x] annotations
% [x] one line functions
% [x] lambda
