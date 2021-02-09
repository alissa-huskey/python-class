---
substitutions:
  output: |
    ```{panels}
    :container: m-0 p-0
    :body: text-monospace text-white bg-dark
    :card: shadow-none m-0 p-0
    :footer: text-white-50 bg-secondary
    OUTPUT
    ++++++++++++++
    output
    ```
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
Reading Code
============

Warmup Exercises
----------------

`````{exercise} Ice cream flavors
:class: notitle
:label: ice-cream

Make a list of ice cream flavors, then print a menu with a number next to
each flavor.

Flavors: Banana, Chocolate, Lemon, Pistachio, Raspberry, Strawberry, Vanilla

`````

`````{exercise} Ice cream combinations
:label: ice-cream-combos
:class: notitle

Print every possible sorbet duos from the same list of flavors. Don't print
recipes with twice the same flavor (no "Chocolate Chocolate"), and don't
print twice the same recipe (if you print "Vanilla Chocolate", don't print
"Chocolate Vanilla", or vice-versa).

Flavors: Banana, Chocolate, Lemon, Pistachio, Raspberry, Strawberry, Vanilla

`````

Intro
-----

We spend most of our time learning to write code, but just as important is
knowing how to read and understand code. So for this exercise we're going to
practice reading code.

We'll step through a small code sample, similar to how we did in in our
[](flow.md) lesson. For each line that we walk through, you'll see a
section that looks like this. (Labels in blue are just for this example.)


% =====================================
% START EXAMPLE
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

`````{sidebar} line 5

% start context -----------------------

```{admonition} variables

|         |          |
|---------|----------|
| `level` | `1`      |
| `name`  | `Yoshi`  |

```

```{div} alert, alert-primary
**↑ Variables**

```

% evaluation steps --------------------

```{code-block} python
:caption: steps to evaluate line
:class: full-width
>>> print("Welcome", name)
>>> print("Welcome", "Yoshi")
```

```{div} alert, alert-primary
**↑ Steps to evaluate**
```

% output ------------------------------

```{panels}
:container: m-0 p-0
:body: text-monospace text-white bg-dark
:card: shadow-none m-0 p-0
:footer: text-white-50 bg-secondary

Starting level 1

**Welcome Yoshi**

++++++++++++++
output
```

```{div} alert, alert-primary
**↑ Output**
```

`````
% ~~~~~~~~~~~
% end sidebar
% ~~~~~~~~~~~

% code --------------------------------

```{code-block} python
:linenos:
:emphasize-lines: 5, 5
level = 1
name = "Yoshi"

print("Starting level", level)
print("Welcome", name)
```

```{div} alert, alert-primary w-50
**↑ Code sample**
```

{{clear}}

% -------------------------------------
% END EXAMPLE
% =====================================

Each breakdown has 5 sections:
* **code sample** (on the left) -- shows the code with the current line highlighted
* **variables** (1st on the right) -- shows the variables that exist at the time when the line is evaluated
* **steps to evaluate** (2nd on the right) -- shows the step by step process of evaluating the code
* **output** (3rd on the right) -- shows the output of the code, with the current line highlighted

The above example is a breakdown of line `5`.

Reading a while loop
--------------------

Let's walk through a simple while loop.


$CONTENTS


Exercises
---------

`````{exercise}

In the following code sample, what is the value of `name` on line `12`?

```{code-block} python
:linenos:
characters = [
    "mario",
    "luigi",
    "yoshi",
    "bowser"
]

i = 0

while i < len(characters):
    name = characters[i].upper()
    print(i+1, name)
    i += 1
```

`````

