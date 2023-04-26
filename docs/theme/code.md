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
Code
====

Code Fence
----------

* [Jupyter Book > MyST syntax cheat sheet > Code and syntax highlighting](https://jupyterbook.org/en/stable/reference/cheatsheet.html#code-and-syntax-highlighting)
* [Myst Parser > Source code and APIs > Basic block syntax highlighting](https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html#basic-block-syntax-highlighting)
* [Pandoc > Fenced code blocks](https://pandoc.org/MANUAL.html#fenced-code-blocks)
* [CommonMark Spec > 4.5 Fenced Code Blocks](https://spec.commonmark.org/0.30/#fenced-code-blocks)

```python
print('this is python')
```

Code Blocks
-----------

* [Sphinx > rst Directives > code-block](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block)
* [Sphinx > rst Directives > literalinclude](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude)
* [reStructuredText Directives > Code](https://docutils.sourceforge.io/docs/ref/rst/directives.html#code)
* [Bootstrap > Code Blocks](https://getbootstrap.com/docs/5.0/content/reboot/#code-blocks)

The `code` directive constructs a literal block containing code. This has an
alias of ``code-block``.

```{code-block} python
:linenos:

from typing import Iterator

# This is an example
class Math:
    @staticmethod
    def fib(n: int) -> Iterator[int]:
        """Fibonacci series up to n"""
        a, b = 0, 1
        while a < n:
            yield a
            a, b = b, a + b


result = sum(Math.fib(42))
print("The answer is {}".format(result))
```

### Plain text

Code blocks with `none` or `text` specified as the language are rendered
without syntax highlighting.

```{code-block} none

# Taken from https://en.wikipedia.org/wiki/Pseudocode#Example
algorithm ford-fulkerson is
    input: Graph G with flow capacity c,
        source node s,
        sink node t
    output: Flow f such that f is maximal from s to t

    (Note that f(u,v) is the flow from node u to node v, and c(u,v) is the flow capacity from node u to node v)

    for each edge (u, v) in GE do
        f(u, v) ← 0
        f(v, u) ← 0

    while there exists a path p from s to t in the residual network Gf do
        let cf be the flow capacity of the residual network Gf
        cf(p) ← min{cf(u, v) | (u, v) in p}
        for each edge (u, v) in p do
            f(u, v) ←  f(u, v) + cf(p)
            f(v, u) ← −f(u, v)

    return f
```

### Caption

```{code-block} json
    :caption: Code Blocks can have captions, which also adds a link to it.

    {
      "session_name": "shorthands",
      "windows": [
        {
          "panes": [
            {
              "shell_command": "echo 'This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly.'"
            }
          ],
          "window_name": "long form"
        }
      ]
    }
```


### Emphasized Lines

```{code-block} python
:linenos:
:emphasize-lines: 3,5

def some_function():
    interesting = False
    print("This line is highlighted.")
    print("This one is not...")
    print("...but this one is.")
    print(
        "This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly."
    )
```

Doctest Blocks
--------------

* [Docutils > Doctest Blocks](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#doctest-blocks)
* [Sphinx > reStructuredText Primer > Doctest blocks](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#doctest-blocks)

Doctest blocks are interactive Python sessions cut-and-pasted into docstrings.
They are meant to illustrate usage by example, and provide an elegant and
powerful testing environment via the doctest module in the Python standard
library.


```{eval-rst}

>>> print('Python-specific usage examples; begun with ">>>"')
Python-specific usage examples; begun with ">>>"
>>> print("(cut and pasted from interactive Python sessions)")
(cut and pasted from interactive Python sessions)
>>> print("This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly.")
This is an intentionally very long line because I want to make sure that we are handling scrollable code blocks correctly.

```

Code Cells
----------

* [Jupyter Book > Code Cells](https://jupyterbook.org/en/stable/file-types/myst-notebooks.html#code-cells)
* [Jupyter Book > Formatting Code Outputs](https://jupyterbook.org/en/stable/content/code-outputs.html)
* [Jupyter Book > Hide code Cell content](https://jupyterbook.org/en/stable/interactive/hiding.html#hide-code-cell-content)
* [Jupyter Book > Remove code Cell content](https://jupyterbook.org/en/stable/interactive/hiding.html#removing-code-cell-content)

```{code-cell} python
:linenos:
import time

width = 70
today = time.localtime()

greeting = "Hello"

if today.tm_hour < 11:
  greeting = "Good morning"  # before 12pm

# put together the message and make it centered
message = (greeting + " world!").center(width)

print(message)
```

### Tags

#### full-width

```{code-cell} python
:tags: ["full-width"]
print("This is a test.")
```

#### output-scroll

```{code-cell} ipython3
:tags: ["output_scroll"]
for ii in range(100):
  print("This is a test.")
```

#### margin

```{code-cell} ipython3
:tags: ["margin"]
print("This is a test.")
```

{{ clear }}

#### hide-input

```{code-cell} ipython3
:tags: ["hide-input"]
print("This is a test.")
```

#### hide-output

```{code-cell} ipython3
:tags: ["hide-output"]
print("This is a test.")
```

#### hide-cell

```{code-cell} ipython3
:tags: ["hide-cell"]
print("This is a test.")
```

#### remove-input

```{code-cell} ipython3
:tags: ["remove-input"]
print("This is a test.")
```

#### remove-output

```{code-cell} ipython3
:tags: ["remove-output"]
print("This is a test.")
```

#### remove-cell

```{code-cell} ipython3
:tags: ["remove-cell"]
print("This is a test.")
```

#### raises-exception

```{code-cell} ipython3
:tags: ["raises-exception"]
while True print('Hello world')
```

See Also
--------

:::{seealso}

* [Sphinx > rst Directives > highlight](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-highlight)

:::
