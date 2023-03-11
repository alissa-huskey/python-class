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
Part 5: Look around
===================

In this section we'll add the `look` command.

Part 5.1: Add command
---------------------

{{ source | format("adventure-5.1.py") }}

{{ left }}

In this section we'll define a `do_look()` function that gets called when the
player types `l` or `look`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-5.1.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

### A: Define `do_look()`

{{ left }}

1. `[ ]` Define a `do_look()` function.
1. `[ ]` In it, use the `debug()` function to print something like `"Trying to look around."`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-5.1.py
:linenos:
:lineno-match:
:start-at: "def do_look"
:end-before: "def"
```

`````

{{ endcols }}

### B: Modify `main()`, in the while loop

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is `"l"` or
         `"look"`.
   * `[ ]` if so, call `do_look()`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-5.1.py
:linenos:
:lineno-match:
:start-at: "if command"
:end-before: "if __name__"
:emphasize-lines: "13-14"
```

`````

{{ endcols }}

Part 5.2: Print place name and description
------------------------------------------

{{ source | format("adventure-5.2.py") }}

{{ left }}

In this section we'll look up the place info and print the name and description.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-5.2.cast
:poster: npt:0:02
:rows: 16
```

`````

{{ endcols }}

### A: Modify `do_look()`: look up and print the current place

{{ left }}

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `place_name`
1. `[ ]` get the value from `PLACES` associated with `place_name` and assign it to `place`
1. `[ ]` Print the value associated with the `"name"` key of the `place` dictionary using the `header()` function.
1. `[ ]` Print the value associated with the `"description"` key of the `place` dictionary using the `wrap()` function.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-5.2.py
:linenos:
:lineno-match:
:start-at: "def do_look"
:end-before: "def"
:emphasize-lines: "6-"
```

`````

{{ endcols }}

Part 5.3: Print the place items
-------------------------------

{{ source | format("adventure-5.3.py") }}

{{ left }}

In this section we'll print the list of items in the current place.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-5.3.cast
:poster: npt:0:02
:rows: 16
```

`````

{{ endcols }}

### A: Modify `do_look()`, at the end

In this section you will use each of the items in the current places `"items"`
list to get the item information from `ITEMS` then construct a list of each
items `"name"`.

1. `[ ]` Use the `.get()` method on the `place` dictionary to get the value
         associated with the `items` key with a default value of `[]`, and assign it to
         the variable `items`.
1. `[ ]` If `items` is {term}`truthy`:
   1. `[ ]` Make an empty list assigned to the variable `names`
   1. `[ ]` Iterate over the `items` list using the variable name `key` for each item. For each item:
      * `[ ]` Get the value from `ITEMS` associated with the `key` key and assign it to the variable `item`
      * `[ ]` Append the value associated with the `"name"` key from the `items` dictionary to the `names` list

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-5.3.py
:linenos:
:lineno-match:
:start-at: "def do_look"
:end-at: "names.append"
:emphasize-lines: "5-"
```

`````

### B: Modify `do_look()`, in `if items`

In this section we're going to construct a plain English sentence listing the items in this place. If there is only one item it will look like:

    y

If there are two items it will look like:

    x and y

And if there are three or more items it will look like:

    x, x and y

1. `[ ]` Remove the last item from the `names` list using the `.pop()` method and assign it to the variable `last`.
1. `[ ]` Join the `names` list using `", "` as a delimiter and assign it to the variable `text`
1. `[ ]` If `text` is {term}`truthy` then append `" and "` to text.
1. `[ ]` Append `last` to `text`
1. `[ ]` Print a blank line
1. `[ ]` Use the `write()` function to print:
   {samp}`You see {text}.`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-5.3.py
:linenos:
:lineno-match:
:start-at: "if items"
:end-before: "def"
:emphasize-lines: "10-"
```

`````

Part 5.4: Print the nearby places
---------------------------------

{{ source | format("adventure-5.4.py") }}

{{ left }}

In this section we'll print the name of each of any places directly to the
`"north"`, `"south"`, `"east"` or `"west"` of the players current place.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-5.4.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}


### A: Modify `do_look()`, at the end

1. `[ ]` print a blank line
1. `[ ]` Use a for loop to iterate over a list: `"north"`, `"east"`, `"south"`, and `"west"` using the variable name `direction`. For each one:
   * `[ ]` Get the value associated with the `direction` key from the `place` dictionary and assign it to the variable `name`.
   * `[ ]` If `name` is {term}`falsy`, then continue
1. `[ ]` Get the place dictionary from `PLACES` associated with the `name` key and assign it to `destination`.
1. `[ ]` Use the `write()` function to print: {samp}`"To the {direction} is {name}."`.
         Get *`name`* from the `destination` dictionary.


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-5.4.py
:linenos:
:lineno-match:
:start-at: "def do_look"
:end-before: "def"
:emphasize-lines: "42-"
```

`````
