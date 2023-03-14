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
Part 8: Drop things
===================

In this section we'll add the `drop` command.

Part 8.1: Add command
---------------------

{{ source | format("adventure-8.1.py") }}

{{ left }}

In this section we'll define a `do_drop()` function that gets called when the
player types `drop`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-8.1.cast
:poster: npt:0:02
:rows: 16
```

`````

{{ endcols }}

### A: Define `do_drop()`

{{ left }}

1. `[ ]` Define a `do_drop()` function.
1. `[ ]` In it, use the `debug()` function to print something like {samp}`"Trying to drop {args}."`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-8.1.py
:linenos:
:lineno-match:
:start-at: 'def do_drop'
:end-at: '    debug'
```

`````

{{ endcols }}

### B: Modify `main()`, in the while loop

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is `"drop"`.
   * `[ ]` if so, call `do_drop()` and pass `args`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-8.1.py
:linenos:
:lineno-match:
:start-at: '        if command in ("q", "quit", "exit"):'
:end-at: '            continue'
:emphasize-lines: "21-23"
```

`````

{{ endcols }}

Part 8.2: Validate
------------------

{{ source | format("adventure-8.2.py") }}

{{ left }}

In this section we'll check to make sure that the player entered an item they
have in inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-8.2.cast
:poster: npt:0:06
:rows: 16
```

`````

{{ endcols }}

### A: Modify `do_drop()`

1. `[ ]` Check to see if `args` is {term}`falsy`, if so:
   * `[ ]` Use the `error()` function to print a message saying:

     `"What do you want to drop?"`
   * `[ ]` `return`
1. `[ ]` assign the first item of the `args` list to the variable `name` and make it lowercase
1. `[ ]` Check if `name` is not in `PLAYER["inventory"]` or if `PLAYER["inventory"][name]` is {term}`falsy`. If so:
   * `[ ]` Use the `error()` function to print a message saying:

     {samp}`"You don't have any {name}."`
   * `[ ]` `return`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-8.2.py
:linenos:
:lineno-match:
:start-at: 'def do_drop'
:end-before: 'def '
:emphasize-lines: "6-"
```

`````

Part 8.3: Drop it
-----------------

{{ source | format("adventure-8.3.py") }}

{{ left }}

In this section we'll check remove the item from the players inventory and add
it to the place items.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-8.3.cast
:poster: npt:0:14
:rows: 16
```

`````

{{ endcols }}

### A: Modify `do_drop()`: remove from inventory

1. `[ ]` subtract `1` from `PLAYER["inventory"][name]`
1. `[ ]` remove item from inventory if the quantity is `0` by:

   if `PLAYER["inventory"][name]` is {term}`falsy`:
   * `[ ]` call `.pop()` on `PLAYER["inventory"]` with the argument `name`


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-8.3.py
:linenos:
:lineno-match:
:start-at: 'def do_drop'
:end-before: '    # look up where the player is now'
:emphasize-lines: "20-"
```

`````

### B: Modify `do_drop()`: add to place

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `place_name`
1. `[ ]` get the value from `PLACES` associated with `place_name` and assign it to `place`
1. `[ ]` call `.setdefault()` on `place` with the argument `"items"` and `[]`
1. `[ ]` append `name` to `place["items"]`
1. `[ ]` print a message using the `wrap()` function like:
         {samp}`You set down the {name}.`


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-8.3.py
:linenos:
:lineno-match:
:pyobject: 'do_drop'
:emphasize-lines: "25-"
```

`````
