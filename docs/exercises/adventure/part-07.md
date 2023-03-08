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
Part 7: Show inventory
======================

In this section we'll add the `inventory` command.

{{ source | format("adventure-7.1.py") }}

Part 7.1: Add command
---------------------

{{ clear }}

{{ left }}

In this section we'll define a `do_inventory()` function that gets called when the
player types `i`, or `inventory`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-7.1.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

### A: Define a `do_inventory()` function

{{ left }}

1. `[ ]` Define a `do_inventory()` function.
1. `[ ]` In it, use the `debug()` function to print something like `"Trying to show inventory."`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-7.1.py
:linenos:
:lineno-match:
:start-at: 'def do_inventory():'
:end-at: '    debug'
```

`````

{{ endcols }}

### B: in `main()`, in the `while` loop

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is `"i"`, or
         `"inventory"`.
   * `[ ]` if so, call `do_inventory()`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-7.1.py
:linenos:
:lineno-match:
:start-at: '        if command in ["q", "quit", "exit"]:'
:end-at: '            continue'
:emphasize-lines: "19-21"
```

`````

{{ endcols }}

{{ source | format("adventure-7.2.py") }}

Part 7.2: Print inventory
-------------------------

{{ clear }}

{{ left }}

In this section we'll print the players inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-7.2.cast
:poster: npt:0:06
:rows: 16
```

`````

{{ endcols }}

### A: in `do_inventory()`

1. `[ ]` Use the `header()` function to print `"Inventory"`
1. `[ ]` If `PLAYER["inventory"]` is {term}`falsy`:
   * `[ ]` use the `write()` function to print `"Empty."`
1. `[ ]` Iterate over the results of `.items()` on `PLAYER["inventory"]` using
         the variables `name` and `qty`.
   * `[ ]` Get the value associated with the `name` key from `ITEMS` and assign it to `item`.
   * `[ ]` Use the `write()` function to print the `qty` and `item["name"]`
1. `[ ]` Print a blank line

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-7.2.py
:linenos:
:lineno-match:
:start-at: 'def do_inventory():'
:end-at: '    print()'
:emphasize-lines: "6-"
```

`````
