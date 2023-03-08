---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'
  icon: '{opticon}`file-code`'

  # green "source code" badge linking to my github
  # usage: {{ source | format("filename.py") }}
  source: |
    ```{div} float-right
      {bdg-link-info-line}`source code <https://github.com/alissa-huskey/python-class/blob/master/pythonclass/adventure/%s>`
    ```
  # two green badges, one for adventure-VERSION.py and one for test_game-VERSION.py
  # usage: {{ sources.format("VERSION") }}
  # note: double curley braces make one literal brace (for .format())
  sources: |
    ```{{div}} float-right
    {{{{ code.format("adventure.py", "adventure/adventure-{0}.py") }}}} {{{{ code.format("test_game.py", "adventure/test_game-{0}.py") }}}}
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
Part 3: Prettify
================

In this section we'll start making things prettier by wrapping text and adding
colors and styles.

We'll also make sure that the way we print things is consistent by always
printing via our custom functions: `header()`, `wrap()`, `write()`,
`error()`, or `debug()`.

{{ source | format("adventure-3.1.py") }}

Part 3.1: Text wrapping
-----------------------

{{ clear }}

{{ left }}

In this section we're going to add a `wrap()` function, which we'll use to
print paragraphs of text like place or item descriptions. We'll both indent and
wrap the text so that it looks nice.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-3.1.cast
:poster: npt:0:02
:rows: 15
```

`````

{{ endcols }}

### A. At the top of your file

{{ left }}

1. `[ ]` import the `textwrap` module
1. `[ ]` Add a global variable `WIDTH` and assign it the value `60` (or so, to taste).
1. `[ ]` Add a global variable `MARGIN` and assign it to `2` or `3` (or so, to taste).

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.1.py
:linenos:
:lines: "6-15"
:lineno-match:
:emphasize-lines: "2-6"
```

`````

{{ endcols }}


### B. Make wrap()

1. `[ ]` Define a `wrap()` function which takes one argument `text`.
1. `[ ]` For now, just print `text` in the function, so we can
         make sure it works.

### C. In do_go(), at the end

{{ left }}

1. `[ ]` Instead of calling `print()` to print the place description, call the
         `wrap()` function you just wrote.

{{ right }}


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.1.py
:linenos:
:start-at: "# print information about the new place"
:end-before: "def "
:lineno-match:
:emphasize-lines: "3"
```

`````

{{ endcols }}

### D. In wrap()

```{margin}

:::{seealso}

Functions > [Keyword Arguments](../lessons/functions.html#part-2-4-keyword-arguments)

:::

```

In this section we'll call `textwrap.fill()` function to wrap a paragraph of
text.

1. `[ ]` Multiply a single space (`" "`) by `MARGIN` and assign it to the local
         variable `margin` (note that the two different cases).
1. `[ ]` Remove the line where you previously printed `text`.
1. `[ ]` Call the `fill()` function from the `textwrap` module and assign the
   result to the variable `paragraph`. Pass the arguments:
   * `text`
   * `WIDTH`
   * keyword argument `initial_indent` with the value `margin`
   * keyword argument `subsequent_indent` with the value `margin`
1. `[ ]` Print `paragraph`.

[keyword-args]: ../lessons/functions.html#part-2-3-keyword-arguments


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.1.py
:linenos:
:start-at: 'def wrap'
:end-before: 'def'
:lineno-match:
:emphasize-lines: "2-"
```

`````

{{ source | format("adventure-3.2.py") }}

Part 3.2: Colors
----------------

{{ clear }}

In this section we're going to use the `console` module to make our game more
colorful.

### A. Install console

{{ left }}

1. `[ ]` Follow the instructions [here](../lessons/cli.html#installation) to install.


{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-3.2.cast
:poster: npt:0:03
:rows: 15
```

`````

{{ endcols }}

### B. At the top of your file

{{ left }}

1. `[ ]` Import `fg`, `bg`, and `fx` from `console`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.2.py
:linenos:
:lines: "6-9"
:lineno-match:
:emphasize-lines: "4"
```

`````

{{ endcols }}

### C. In error(), debug(), other places...

{{ left }}

1. In the places you want it, such as in the `error()` and `debug()` function,
   add colors and styles to your taste.

{{ right }}

`````{dropdown} Code
:open:

```{literalinclude} ../../../pythonclass/adventure/adventure-3.2.py
:linenos:
:lineno-match:
:emphasize-lines: "3, 9"
:start-at: "def error"
:end-before: "def do_"
```

```{literalinclude} ../../../pythonclass/adventure/adventure-3.2.py
:linenos:
:lineno-match:
:emphasize-lines: "7"
:start-at: 'def main'
:end-at: 'args ='
```

`````

{{ endcols }}

{{ source | format("adventure-3.3.py") }}

Part 3.3: Header and write functions
------------------------------------

{{ clear }}

{{ left }}

In this section we're going to write a `header()` function to print pretty
headers and a `write()` function to print all other one-line messages.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-3.3.cast
:poster: npt:0:03
:rows: 15
```

`````

{{ endcols }}


### A. Define write() function

{{ left }}

In this section we'll define a `write()` function that we'll use to print
non-wrapping messages to the player. This is to make sure that they're all
indented at the same level, or to add any extra formatting.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.3.py
:linenos:
:start-at: 'def write'
:end-before: 'def'
:lineno-match:
```

`````

{{ endcols }}

1. `[ ]` Write a function named: `write` with one parameter: `text`
1. `[ ]` In the function: print `MARGIN` multiplied by a single space (`" "`),
         followed by `text`. You can do this as an f-string or pass the keyword argument
         `sep` with the value `""` to avoid adding an extra space between them.

### B. Define header() function

{{ left }}

The `header()` function should style the `title` text using the `fx`, `fg`
and/or `bg` objects, add any additional desired formatting, then print it by
calling the `write()` function.

These steps are to add a blank line before and after the title and to make it
bold, but you can change it to suit your taste.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.3.py
:linenos:
:start-at: 'def header'
:end-before: 'def'
:lineno-match:
```

`````

{{ endcols }}


1. `[ ]` Write a function named: `header` with one parameter: `title`
1. `[ ]` In the function:
   * `[ ]` Print a blank line.
   * `[ ]` Use the `bold` method on the `fx` object to make
         `title` bold. (Or whatever other styles/colors you
         want.)
   * `[ ]` Pass the result as an argument to `write()`.
   * `[ ]` Print a blank line.

### C. In do_shop():

{{ left }}

Replace `print()` calls with `header()` and `write()` calls.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.3.py
:linenos:
:start-at: 'def do_shop'
:end-before: 'def'
:lineno-match:
:emphasize-lines: "4, 7"
```

`````

{{ endcols }}

1. `[ ]` When printing the title (`"Items for sale"`) call `header()` instead
         of `print()`.
1. `[ ]` When printing the item name and description, change
         the call to the `print()` function to call the `write()`
         function instead.

### D. In do_quit():

{{ left }}

Replace `print()` call with `write()` call.

1. `[ ]` When printing any message (like `"Goodbye"`) call `write()` instead of
         `print()`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.3.py
:linenos:
:start-at: 'def do_quit'
:end-before: 'def'
:lineno-match:
:emphasize-lines: "3"
```

`````

{{ endcols }}

### E. In do_go():

{{ left }}

Replace `print()` call with `header()` call.

1. `[ ]` When printing the place name call `header()` instead of `print()`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-3.3.py
:linenos:
:start-at: "# print information about the new place"
:end-before: 'def'
:lineno-match:
:emphasize-lines: "2"
```

`````

{{ endcols }}
