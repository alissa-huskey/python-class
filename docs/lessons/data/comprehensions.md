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
Comprehensions
==============

```{include} ../../toc.md
```

Part 1: List Comprehensions
---------------------------

Python provides a special syntax called {term}`comprehensions <comprehensions>`
to accomplish it easily.

{{ leftcol }}

The syntax is:

```{include} ../../templates/syntax/list-comprehension.md
```

{{ rightcol }}

```{include} ../../templates/desc/comprehension.md
```

{{ br }}

{{ endcols }}

Lets say for example that you want to take a list of strings and transform each
of them to title case.

Notice that the {samp}`for {VAR} in {ITERABLE}` part is the same in both
examples, as `w.title()`.

{{ leftcol }}

Here's how we would do it with a for loop:

```{code-block-hl} python
:class: full-width
:linenos:

words = ['group', 'short', 'steal']
caps = []

!!!for w in words!!!:
    caps.append(!!!w.title()!!!)

print(caps)
```

{{ rightcol }}

Here is the same thing as a list comprehension:

```{code-block-hl} python
:class: full-width
:linenos:

words = ['group', 'short', 'steal']

caps = [!!!w.title()!!! !!!for w in words!!!]

print(caps)
```

{{ endcols }}

Reference
---------

### Glossary

```{glossary} comprehensions
comprehension
  ...
```

### See Also

```{seealso}

* [python.org > Tutorial > List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

```

----

% TODO
% - set comprehensions
% - dict comprehensions
% - list comprehensions
%
% - zip
