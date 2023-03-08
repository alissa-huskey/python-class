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
Part 4: Examine items
=====================

In this section we'll add the `examine` command.

{{ source | format("adventure-4.1.py") }}

Part 4.1: Add new items
-----------------------

{{ clear }}

In this section we'll add a `"desk"` and `"book"` items to the `ITEMS`
dictionary, which will eventually be added to the `"home"` place. The book is
where we'll find the hint about petting dragons.

We'll also have to modify `do_shop()`, so that items without prices (like
`"book"` and `"desk"`) aren't listed for sale.

Note: At the end of this section, there will be no difference in how the game
behaves. But check and make sure that the book and desk are not listed when you
do the `shop` command.

### A. In ITEMS:

{{ left }}

1. `[ ]` Add two items to the `ITEMS` dictionary with keys: `"desk"` and
        `"book"`. Like previous items, each element one should be a dictionary
        with a `"name"` and `"description"`; unlike the others, these will have
        no `"price"`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.1.py
:linenos:
:lines: "40-68"
:lineno-match:
:emphasize-lines: "14-"
```

`````

{{ endcols }}

For now, keep the descriptions for both simple. Something like:

**Desk**

    A wooden desk with a large leather-bound book open on its surface.

**Book**

    A hefty leather-bound tome open to an interesting passage.

Note: If you try the `shop` command before the next section, you will see
`"book"` and `"desk"` in the list.

### B. In PLACES:

We'll keep track of which items are in a particular place by adding a `"items"`
key to the place dictionary. In this case, we're going to add the keys for the `"book"` and
`"desk"` items to the `"home"` place.

{{ left }}

1. `[ ]` In the dictionary for `"home"` the key `"items"`. The value should be
a list that contains two items, the strings `"book"` and `"desk"`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.1.py
:linenos:
:start-at: 'PLACES'
:end-at: '},'
:lineno-match:
:emphasize-lines: "7"
```

`````

{{ endcols }}

### C. In do_shop(), in the for loop:

{{ left }}

1. `[ ]` Before printing each item, check if the item has a `"price"` key.
`continue` if not.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.1.py
:linenos:
:start-at: 'def do_shop'
:end-before: 'def do_'
:lineno-match:
:emphasize-lines: "7-8"
```

`````

{{ endcols }}

Be sure to test the `shop` command and make sure book and desk aren't listed.

{{ source | format("adventure-4.2.py") }}

Part 4.2: Add `do_examine()`
----------------------------

{{ clear }}

{{ left }}

In this section we'll add an `examine` command.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-4.2.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

### A. Make do_examine():

{{ left }}

1. `[ ]` Add a function `do_examine()` with one parameter: `args`.
1. `[ ]` Use the `debug()` function to print the value of `args`, something like:

   {samp}`Trying to examine: {args}`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.2.py
:linenos:
:start-at: 'def do_examine'
:end-before: 'def'
:lineno-match:
```

`````

{{ endcols }}

### B. In main(), in the while loop:

{{ left }}

1. `[ ]` Add an `elif` clause that checks if `command` is `"x"`, `"exam"`, or `"examine"`.

   * If it is, call `do_examine()` and pass `args`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.2.py
:linenos:
:lineno-match:
:start-at: 'if command'
:end-before: 'if __name__'
:emphasize-lines: "10-11"
```

`````

{{ endcols }}

:::{tip}

This is a good time to test and make sure `x`, `exam` and `examine` all trigger
calling the `do_examine()` function.

:::

{{ source | format("adventure-4.3.py") }}

Part 4.3: Finish examine command
--------------------------------

{{ clear }}

{{ left }}

In this section we'll write the rest of the `do_examine()` function.

This will be very similar to the `do_go()` function. In that we'll need to make
sure the player typed something after the command, (in `args`) and that it is
an item in the current place; then we'll get the item from the `ITEMS`
dictionary and print its information.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-4.3.cast
:poster: npt:0:13
:rows: 16
```

`````

{{ endcols }}

### A. In do_examine() ensure args is not empty

{{ left }}

1. `[ ]` Check to see if `args` is {term}`falsy`, if so:
   * `[ ]` Use the `error()` function to print a message saying:
   `"What do you want to examine?"`
   * `[ ]` return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.3.py
:linenos:
:start-at: 'def do_examine'
:end-at: "return"
:lineno-match:
:emphasize-lines: "6-9"
```

`````

{{ endcols }}

### B. Still in do_examine(): get the current place

{{ left }}

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `place_name`
1. `[ ]` get the value from `PLACES` associated with `place_name` and assign it to `place`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.3.py
:linenos:
:start-at: "do_examine"
:end-at: "place ="
:lineno-match:
:emphasize-lines: "11-13"
```

`````

{{ endcols }}

### C. Still in do_examine(): check the name

1. `[ ]` assign the first element from the `args` list to the variable `name` and make it lowercase
1. `[ ]` check if `name` is in the list of items available at this place by:
   * `[ ]` use an `if` statement with the following condition:
     * `[ ]` check if `name` is not in the list returned in the next step
     * `[ ]` use the `.get()` method on `place` and pass it two arguments:
       * `[ ]` the key: `"items"`
       * `[ ]` the default value to return if missing: an empty list
   * `[ ]` if the above condition is met:
     * `[ ]` print an error message like: {samp}`"Sorry, I don't know what this is: {name}."`
     * `[ ]` return
1. `[ ]` Check if `name` is a key in the `ITEMS` dictionary, if not:
     * `[ ]` Print an error message like:

       {samp}`"Woops! The information about {name} seems to be missing."`

       This will only happen if you made a mistake somewhere in your code. But just
       in case we do, we want to have a clear error message so we can tell what
       went wrong.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.3.py
:linenos:
:start-at: "def do_examine"
:end-before: "# make sure the item is in the ITEMS dictionary"
:lineno-match:
:emphasize-lines: "15-"
```

`````

### D. Still in do_examine(): get and print the item info

1. `[ ]` Get the value from the `ITEMS` dictionary associated with the `name`
         key and assign it to the variable `item`
1. `[ ]` Using the `header()` function print the item name
1. `[ ]` Using the `wrap()` function print the item description

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-4.3.py
:linenos:
:start-at: "def do_examine"
:end-before: "def"
:lineno-match:
:emphasize-lines: "28-"
```

`````
