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
[Program Flow](flow.md) lesson. For each line that we walk through, you'll see a
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

:::{jinja}
{% set contents %}
Starting level 1

**Welcome Yoshi**
{% endset %}

{% include "lessons/reading-code-output.jinja" %}
:::

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

---

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

% =====================================
% START LINE 1
% -------------------------------------

:::{jinja}
{% set line = 1 %}

{% set variables %}
*none*
{% endset %}

{% set evaluation %}
>>> total = 0
{% endset %}

{% set output %}
&nbsp;
{% endset %}

{% set em_lines = "1" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LINE 1
% =====================================

% =====================================
% START LINE 2
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set line = 2 %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `0` |
{% endset %}

{% set evaluation %}
>>> i = 0
{% endset %}

{% set output %}
&nbsp;
{% endset %}

{% set em_lines = "2" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LINE 2
% =====================================

% =====================================
% START LOOP 0, LINE 3
% -------------------------------------

:::{jinja}
{% set loop, line = (0, 3) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `0` |
| `i`     | `0` |
{% endset %}

{% set evaluation %}
>>> i < 3
>>> 0 < 3  # True, so go to line 4
{% endset %}

{% set output %}
&nbsp;
{% endset %}

{% set em_lines = "3" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 0, LINE 3
% =====================================

% =====================================
% START LOOP 0, LINE 4
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (0, 4) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `0` |
| `i`     | `0` |
{% endset %}

{% set evaluation %}
>>> print("loop", i)
>>> print("loop", 0)
{% endset %}

{% set output %}
**loop 0**
{% endset %}

{% set em_lines = "4" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 0, LINE 4
% =====================================

% =====================================
% START LOOP 0, LINE 5
% -------------------------------------

:::{jinja}
{% set loop, line = (0, 5) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `0` |
| `i`     | `0` |
{% endset %}

{% set evaluation %}
>>> total = total + i
>>> total = 0 + 0
>>> total = 0
{% endset %}

{% set output %}
loop 0
{% endset %}

{% set em_lines = "5" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 0, LINE 5
% =====================================

% =====================================
% START LOOP 0, LINE 6
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (0, 6) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `0` |
| `i`     | `0` |
{% endset %}

{% set evaluation %}
>>> i = i + 1
>>> i = 0 + 1
>>> i = 1
>>> # end of loop, go to line 3
{% endset %}

{% set output %}
loop 0
{% endset %}

{% set em_lines = "6" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 0, LINE 6
% =====================================

% =====================================
% START LOOP 1, LINE 3
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (1, 3) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `0` |
| `i`     | `1` |
{% endset %}

{% set evaluation %}
>>> i < 3
>>> 1 < 3  # True, so go to line 4
>>> True  # True, so go to line 4
{% endset %}

{% set output %}
loop 0
{% endset %}

{% set em_lines = "3" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 1, LINE 3
% =====================================

% =====================================
% START LOOP 1, LINE 4
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (1, 4) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `0` |
| `i`     | `1` |
{% endset %}

{% set evaluation %}
>>> print("loop", i)
>>> print("loop", 1)
{% endset %}

{% set output %}
loop 0

**loop 1**
{% endset %}

{% set em_lines = "4" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 1, LINE 4
% =====================================

% =====================================
% START LOOP 1, LINE 5
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (1, 5) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `0` |
| `i`     | `1` |
{% endset %}

{% set evaluation %}
>>> total = total + i
>>> total = 0 + 1
>>> total = 1
{% endset %}

{% set output %}
loop 0

loop 1
{% endset %}

{% set em_lines = "5" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 1, LINE 5
% =====================================

% =====================================
% START LOOP 1, LINE 6
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (1, 6) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `1` |
| `i`     | `1` |
{% endset %}

{% set evaluation %}
>>> i = i + 1
>>> i = 1 + 1
>>> i = 2
>>> # end of loop, go to line 3
{% endset %}

{% set output %}
loop 0

loop 1
{% endset %}

{% set em_lines = "6" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 1, LINE 6
% =====================================

% =====================================
% START LOOP 2, LINE 3
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (2, 3) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `1` |
| `i`     | `2` |
{% endset %}

{% set evaluation %}
>>> i < 3
>>> 2 < 3  # True, go to line 4
>>> True  # True, go to line 4
{% endset %}

{% set output %}
loop 0

loop 1
{% endset %}

{% set em_lines = "3" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 2, LINE 3
% =====================================

% =====================================
% START LOOP 2, LINE 4
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (2, 4) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `1` |
| `i`     | `2` |
{% endset %}

{% set evaluation %}
>>> print("loop", i)
>>> print("loop", 2)
{% endset %}

{% set output %}
loop 0

loop 1

**loop 2**
{% endset %}

{% set em_lines = "4" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 2, LINE 4
% =====================================

% =====================================
% START LOOP 2, LINE 5
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (2, 5) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `1` |
| `i`     | `2` |
{% endset %}

{% set evaluation %}
>>> total = total + i
>>> total = 1 + 2
>>> total = 3
{% endset %}

{% set output %}
loop 0

loop 1

loop 2
{% endset %}

{% set em_lines = "5" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 2, LINE 5
% =====================================

% =====================================
% START LOOP 2, LINE 6
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set loop, line = (2, 6) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `3` |
| `i`     | `2` |
{% endset %}

{% set evaluation %}
>>> i = i + 1
>>> i = 2 + 1
>>> i = 3
>>> # end of loop, go to line 3
{% endset %}

{% set output %}
loop 0

loop 1

loop 2
{% endset %}

{% set em_lines = "6" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 2, LINE 6
% =====================================

% =====================================
% START LOOP 3, LINE 3
% -------------------------------------

:::{jinja}
{% set loop, line = (3, 3) %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `3` |
| `i`     | `3` |
{% endset %}

{% set evaluation %}
>>> i < 3
>>> 3 < 3
>>> False  # False, so go to line 7
{% endset %}

{% set output %}
loop 0

loop 1

loop 2
{% endset %}

{% set em_lines = "3" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LOOP 3, LINE 3
% =====================================

% =====================================
% START LINE 7
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

:::{jinja}
{% set line = 7 %}

{% set variables %}
|         |     |
|---------|-----|
| `total` | `3` |
| `i`     | `3` |
{% endset %}

{% set evaluation %}
>>> print("The total is:", total)
>>> print("The total is:", 3)
{% endset %}

{% set output %}
loop 0

loop 1

loop 2

**The total is: 3**
{% endset %}

{% set em_lines = "7" %}

{% include "lessons/reading-code-step.jinja" ignore missing %}
:::

{{ clear }}

---

% -------------------------------------
% END LINE 7
% =====================================


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
