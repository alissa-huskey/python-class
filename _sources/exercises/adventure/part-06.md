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
Part 6: Take things
===================

In this section we'll add the `take` command.

{{ source | format("adventure-6.1.py") }}

Part 6.1: Add command
---------------------

{{ clear }}

{{ left }}

In this section we'll define a `do_take()` function that gets called when the
player types `t`, `take`, or `grab`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-6.1.cast
:poster: npt:0:02
:rows: 16
```

`````

{{ endcols }}

### A: Define a `do_take()` function

{{ left }}

1. `[ ]` Define a `do_take()` function.
1. `[ ]` In it, use the `debug()` function to print something like {samp}`"Trying to take: {args}."`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-6.1.py
:linenos:
:lineno-match:
:start-at: "def do_take"
:end-before: "def"
```

`````

{{ endcols }}

### B: in `main()`, in the `while` loop

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is `"t"`, `"take"` or
         `"grab"`.
   * `[ ]` if so, call `do_take()`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-6.1.py
:linenos:
:lineno-match:
:start-at: '        if command in ["q", "quit", "exit"]:'
:end-at: '            continue'
:emphasize-lines: "16-17"
```

`````

{{ endcols }}

{{ source | format("adventure-6.2.py") }}

Part 6.2: Validate item
-----------------------

{{ clear }}

{{ left }}

In this section we'll check to make sure that the player entered a valid, takeable
item in the current place.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-6.2.cast
:poster: npt:0:12
:rows: 16
```

`````

{{ endcols }}

### A: in `ITEMS`

{{ left }}

1. `[ ]` For any item you wish for the player to be able to `take`, add
         `"can_take": True` to the items dictionary.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-6.2.py
:linenos:
:lineno-match:
:start-at: '    "book": {'
:end-at: '    },'
:emphasize-lines: "3"
```

`````

{{ endcols }}

### B: in `do_take()`: make sure the item is valid in the current place

1. `[ ]` Check to see if `args` is {term}`falsy`, if so:
   * `[ ]` Use the `error()` function to print a message saying:
   `"Which way do you want to go?"`
   * `[ ]` return
1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `place_name`
1. `[ ]` get the value from `PLACES` associated with `place_name` and assign it to `place`
1. `[ ]` assign the first item of the `args` list to the variable `name` and make it lowercase
1. `[ ]` Get the list of items in the `place` dictionary using `.get()` with a
         default value of `[]`. Check to see if `name` is in the list. If not:
     * `[ ]` Print an error message like:

       {samp}`"Sorry, I don't see a {name} here."`
     * `[ ]` `return`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-6.2.py
:linenos:
:lineno-match:
:start-at: "def do_take"
:end-before: "# get the item information"
:emphasize-lines: "5-"
```

`````

### C: still in `do_take()`: make sure the item is takeable

1. `[ ]` Using `.get()`, get the value from `ITEMS` associated with the `name`
         key and assign it to the variable `item`.
1. `[ ]` If `item` is {term}`falsy`,
     * `[ ]` Print an error message like:

       {samp}`"Woops! The information about {name!r} seems to be missing."`
     * `[ ]` `return`
1. `[ ]` Using `.get()`, get the value from `item` associated with the `"can_take"`
         key. Check to see if it is {term}`falsy`. If so:
     * `[ ]` Use `wrap()` to print a message like:

       {samp}`"You try to pick up {item['name']}, but you find you aren't able to lift it."`
     * `[ ]` `return`


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-6.2.py
:linenos:
:lineno-match:
:start-at: "def do_take"
:end-before: "def"
:emphasize-lines: "23-"
```

`````

{{ source | format("adventure-6.3.py") }}

Part 6.3: Take it
-----------------

{{ clear }}

{{ left }}

In this section we'll actually take the item.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-6.3.cast
:poster: npt:0:08
:rows: 16
```

`````

{{ endcols }}

### A: in `PLAYER`

{{ left }}

1. `[ ]` Add `"inventory": {}` to the `PLAYER` dictionary.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-6.3.py
:linenos:
:lineno-match:
:start-at: 'PLAYER = {'
:end-at: '}'
:emphasize-lines: "3"
```

`````

{{ endcols }}

### B: in `do_take()`

In this section we will add the item to our inventory, remove it from the
place, and let the player know that it's done.

1. `[ ]` Call `.setdefault()` on `PLAYER["inventory"]` with the arguments `name` and `0`.

    This will set the current inventory for `name` to `0` if it is not already
    in our inventory.
1. `[ ]` Add `1` to `PLAYER["inventory"][name]`
1. `[ ]` Remove `name` from the `place["items"]` list using the `.remove()` method
1. `[ ]` Use the `wrap()` function to print a message like:

    {samp}`"You pick up {name} and put it in your pack."`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-6.3.py
:linenos:
:lineno-match:
:start-at: 'def do_take(args):'
:end-at: 'wrap(f"You pick up'
:emphasize-lines: "35-"
```

`````

{{ source | format("adventure-6.4.py") }}

Part 6.4: Examine inventory
---------------------------

{{ clear }}

{{ left }}

In this section we'll modify `do_examine()` so it can be used to look at inventory items.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-6.4.cast
:poster: npt:0:32
:rows: 16
```

`````

{{ endcols }}

### A: in `do_examine()`

1. `[ ]` Find the if statement where you check if `name` is not in the `place`
         items list. Modify it so that it shows the error if `name` is not in
         `place` items **and** `name` is not in `PLAYER["inventory"]`.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-6.4.py
:linenos:
:lineno-match:
:start-at: "def do_examine"
:end-before: "# make sure the item is in the ITEMS dictionary"
:emphasize-lines: "19"
```

`````
