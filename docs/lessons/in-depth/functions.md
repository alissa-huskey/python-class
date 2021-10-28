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
Functions
=========

:::{important}

Be sure to complete the fundamentals [](../functions.md) lesson first.

:::

Optional arguments
------------------

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

{{ newrow }}

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

% TODO
% [ ] order of optional params
% [ ] mutable arguments

Arbitrary arguments
-------------------

Sometimes you want a function to be able to take an arbitrary arguments. These
are called {term}`variadic` arguments.

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

{{ newrow }}

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

Annotations
-----------

Python provides a syntax for documenting the type of various values called
annotations. While annotations have no effect on how a function behaves, it can
be helpful in clarifying the intended usage.

{{ leftcol }}

You can specify the expected type of each parameter by adding a colon after the
parameter name, followed by the type.

{{ rightcol }}

```{code-block-hl} python
:class: full-width

def debug(message!!!: str!!!):
    print(message)
```

{{ newrow }}

Incidentally, you can specify the the type of a particular variable the same
way.

{{ rightcol }}

```{code-block-hl} python
:class: full-width

maximum!!!: int!!! = 100
name!!!: str!!!
```

{{ newrow }}

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

Lambdas
-------

Python provides an inline syntax for short functions called {term}`lambda`.

{{ leftcol }}

```{code-block-hl} python
:class: full-width

def random():
    return randint(1, 100)
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

Shorthand
---------

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
  Syntax for specifying the type of a variable, class attribute, function
  parameter or return value.

lambda
  An anonymous inline function consisting of a single expression.
```


% [ ] default arguments
%     [ ] note about mutable types ie `def x(y=[])`
%     [ ] order of default args
%     [ ] `/`: positional only
%     [ ] `*`: keyword only
% [ ] *args
% [ ] *kwargs
% [ ] annotations
% [ ] one line functions
% [ ] lambda
% [ ]
