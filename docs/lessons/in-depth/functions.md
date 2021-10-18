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
def hr(width=40):
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
positional arguments will then be in a tuple with that name.

{{ rightcol }}

```{code-cell} python
:class: full-width

def thing(*args):
    print(args)
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

Or you put two astricks before a paramater name.

{{ rightcol }}

```{code-cell} python
:class: full-width
def thing(**kwargs):
    print(kwargs)
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
  ...

annotations
  ...

lambda
  ...
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
