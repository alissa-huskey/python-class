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
Part 2: Go places
=================

In this section we'll be writing the `go` command, and the system to go from
one place to another.

To start out we'll add just two places: `"home"` and the `"town-square"`. A map
of the game world would look something like this:

```{kroki}
:type: ditaa

   +--------+      +--------+
   | home   |      | town   |
   |        *------* square |
   |        |      |        |
   +--------+      +--------+

```

You are welcome to add your own places. However, I strongly recommend that you
first get your `go` command working with these two places.

You also may want to keep a map of the game world in a docstring or another
text file. Here's an example of how you might represent a slightly more
populated world.

```python
"""
Text-based adventure game
https://alissa-huskey.github.io/python-class/exercises/adventure.html

  =========
  World Map
  =========

            market
              |
  home -- town square -- woods -- hill
              |                    |
            bakery                cave

"""

```

{{ source | format("adventure-2.1.py") }}

Part 2.1: Split reply into command and arguments
------------------------------------------------

{{ clear }}

{{ left }}

This will be the first command that we've written that takes an argument. That
is, the player needs to type not just `go`, but also which direction to go like
`north`.

That means we need to split the string that is returned from `input()` into a
list. That way we if the player types `go north` we can figure out that `go` is
the command, and `north` is the direction.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-2.1.cast
:poster: npt:0:07
:rows: 15
```

`````

{{ endcols }}

### A. Define do_go

1. `[ ]` Define a `do_go()` function that takes one argument: `args`.
2. `[ ]` In `do_go()` print {samp}`Trying to go: {args}`

### B. In main(), in the while loop

1. `[ ]` Strip the value returned from `input()` using the `.strip()` method.

   This means if a player enters `" quit"` or `"quit "` the program still knows
   to call `do_quit()`.
2. `[ ]` Call `.split()` on `reply` and assign it to the variable `args`.

   Now the `args` variable will contain a list where each word is an item in
   the list.
3. `[ ]` Use an `if` statement to check if `args` is {term}`falsy`. If it is,
   `continue`.

   This means that if a player doesn't enter anything, the program will ignore it
   and start the loop over.
4. `[ ]` Remove the first item from `args` using the `.pop()` method and assign it to
   the variable `command`.

   Now `command` will contain the first word the player entered, and `args` will
   contain a list of the remaining commands. If there were no additional words,
   then `args` will be an empty list.
5. `[ ]` In each clause of the `if` statement where we check the value of `reply`,
   change it to `command`.
6. `[ ]` Add an `elif` clause that checks if `command` is equal to `"g"` or `"go"`.
   If it is, call `do_go()` and pass `args`.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.1.py
:linenos:
:emphasize-lines: "35-37, 42-50, 53, 56-57"
```

`````

{{ source | format("adventure-2.2.py") }}

Part 2.2: Create PLAYER and PLACES
----------------------------------

{{ clear }}

Now we'll make global `PLACES` dictionary which will store information about
the different areas in the game.

Like the `ITEMS` dictionary, `PLACES` will be a nested dictionary, where the
key is a unique identifier for each place, and the value is a dictionary with
detailed information about that place.

{{ left }}

The keys of the child dictionary will be:

* `"key"` -- the same thing as the key
* `"name"` -- a short description
* `"description"` -- a longer description
* `"east"`, `"west"`, `"north"`, `"south"` -- the key to the place in that
  direction. (More on that next.)

{{ right }}

Here is an example:

```{code-block-hl} python
:name: places-direction-to-place

PLACES = {
    "home": {
        "key": "home",
        "name": "Your Cottage",
        "east": "town-square",
        "description": "A cozy stone cottage with a desk and a neatly made bed.",
    },
}
```

{{ endcols }}

{{ br }}

The `"north"`, `"south"`, `"east"` and `"west"` values will be used to tell
which way the player can go from a particular place and what is in that
direction.

For example, going `"east"` from `"home"` is the `"town-square"`.

{{ left }}

```{code-block-hl} python

PLACES = {
    "home": {
        "key": "home",
        "name": "Your Cottage",
        "east": !!!"town-square"!!!,
        ...
    },
    "town-square": {
        "key": "town-square",
        "name": "The Town Square",
        "west": "home",
        ...
    },
}
```

{{ right }}

```{code-block-hl} python

PLACES = {
    "home": {
        "key": "home",
        "name": "Your Cottage",
        "east": "town-square",
        ...
    },
    !!!"town-square"!!!: {
        "key": "town-square",
        "name": "The Town Square",
        "west": "home",
        ...
    },
}
```

{{ endcols }}

{{ br }}

Likewise, going `"west"` from the `"town-square"` is `"home"`.

{{ left }}

```{code-block-hl} python

PLACES = {
    "home": {
        "key": "home",
        "name": "Your Cottage",
        "east": "town-square",
        ...
    },
    "town-square": {
        "key": "town-square",
        "name": "The Town Square",
        "west": !!!"home"!!!,
        ...
    },
}
```

{{ right }}

```{code-block-hl} python

PLACES = {
    !!!"home"!!!: {
        "key": "home",
        "name": "Your Cottage",
        "east": "town-square",
        ...
    },
    "town-square": {
        "key": "town-square",
        "name": "The Town Square",
        "west": "home",
        ...
    },
}
```

{{ endcols }}

We'll also make a global `PLAYER` dictionary that will save information about
the current game.

For now it will just have one key, the `place`, which point to where the player
is at. In the `do_go()` function, we will change that value to move the player
from one place to another.

{{ left }}

```{code-block-hl} python
:name: player-to-places

PLAYER = {
    "place": !!!"home"!!!,
}
```

{{ right }}

```{code-block-hl} python

PLACES = {
    !!!"home"!!!: {
        "key": "home",
        "name": "Your Cottage",
        "east": "town-square",
        ...
    },
    ...
}
```

{{ endcols }}

### A. At the top of your file

1. `[ ]` Create a `PLAYER` dictionary with the key `"place"` and the value `"home"`.
2. `[ ]` Create a `PLACES` dictionary where the key is a unique identifier for each place.
   The value is a dictionary that with information about each place:

   * `"key"` -- the same thing as the key
   * `"name"` -- a short description
   * `"description"` -- a longer description
   * `"east"`, `"west"`, `"north"`, `"south"` -- the key to the place in that

   Add two places, `"home"` and `"town-square"`.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.2.py
:linenos:
:emphasize-lines: "6-26"
:end-at: "ITEMS ="
```

`````

{{ source | format("adventure-2.3.py") }}

Part 2.3: Write message functions
---------------------------------

{{ clear }}

{{ left }}

We're going to take a brief interlude here to write a couple of functions for
printing messages to the player.

We'll add a `debug()` function which will print messages intended for us (the
programmer), but only if a global variable indicates that the program is in
debug mode.

We'll also add a `error()` function which will print an error message.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-2.3.cast
:poster: npt:0:04
:rows: 15
```

`````

{{ endcols }}

### A. At the top of the file

{{ left }}

1. `[ ]` Add a global variable `DEBUG` and set it to `True`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.3.py
:linenos:
:lines: "1-11"
:emphasize-lines: "6"
:lineno-match:
```

`````

{{ endcols }}


### B. Define debug() function

{{ left }}

1. `[ ]` Write a function named: `debug` with one parameter: `message`
1. `[ ]` In the function, check if `DEBUG` is `True` (or {term}`truthy`)
   * `[ ]` If so, then print `message`
   * `[ ]` Bonus: Print something before it like `"DEBUG: "`, or `"# "`, so you can more
                 easily tell that it is a debug message

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.3.py
:linenos:
:lines: "49-53"
```

`````

{{ endcols }}

### C. Define error() function

{{ left }}

1. `[ ]` Write a function named: `error` with one parameter: `message`
1. `[ ]` Print `message` with something before it like `"Error: "`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.3.py
:linenos:
:lines: "45-47"
```

`````

{{ endcols }}

### D. In do_go()

{{ left }}

1. `[ ]` Call `debug()` instead of `print()` for the message {samp}`Trying to go: {args}`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.3.py
:linenos:
:lines: "69-71"
:lineno-match:
:emphasize-lines: "3"
```

`````

{{ endcols }}

### E. In main(), in the while loop

1. `[ ]` At the beginning of the `while` loop call `debug()` with the message {samp}`You are at: {PLACE}`.
   Replace `PLACE` with the value in the `PLAYER` dictionary associated with the `"place"` key

   This will print a debug message with your current location every time the loop runs.

1. `[ ]` After assigning `command`, use `debug()` to print `command` and `args`.
1. `[ ]` Call `error()` instead of `print()` for the message {samp}`No such command.`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.3.py
:linenos:
:lines: "73-101"
:lineno-match:
:emphasize-lines: "5, 14, 26"
```

`````

### F. Test debug messages

1. `[ ]` Test with `DEBUG` set to `True` as well as with `DEBUG` set to `False`

{{ source | format("adventure-2.4.py") }}

Part 2.4: Fill in `go` command
------------------------------

{{ clear }}

{{ left }}

In this section we'll be filling in the rest of the `go` command.

We'll need to make sure that we get a valid direction in `args`. Then look up
where we are now from `PLAYER["place"]` and `PLACES`; and look up where we want
to go by looking at direction (ie `"east"`) key in the current place dictionary.

Finally, we'll change the current `"place"` in the `PLAYER` dictionary, and
print the `"name"` and `"description"`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-2.4.cast
:poster: npt:0:12
:rows: 15
```

`````

{{ endcols }}

### A. In do_go(): ensure that the player typed a valid direction

In this section we'll be making sure there is at least one item in the `args`
list and that it is a valid direction.

1. `[ ]` Check to see if `args` is {term}`falsy`, if so:
   * `[ ]` Use the `error()` function to print a message saying:
   `"Which way do you want to go?"`
   * `[ ]` return
1. `[ ]` assign the first item of the `args` list to the variable `direction` and make it lowercase
1. `[ ]` Check if `direction` is one of `"north"`, `"south"`, `"east"`, `"west"`. If not:
   * `[ ]` Use the `error()` function to print a message saying:
       {samp}`"Sorry, I don't know how to go: {direction}.")`
   * `[ ]` return

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lines: "69-85"
:lineno-match:
:emphasize-lines: "6-8, 12, 15-17"
```

`````

### B. (still) in do_go(): look up where the player is at

In this section we'll be using the `PLAYER["place"]` to get the current place
from the `PLACES` dictionary, as shown {ref}`here <player-to-places>`.

{{ left }}

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `old_name`
1. `[ ]` get the value from `PLACES` associated with `old_name` and assign it to `old_place`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lineno-match:
:lines: 87-89
:emphasize-lines: "2-"
```

`````

{{ endcols }}

### C. (still) in do_go(): look up what is in that direction from here

In this section we'll use the direction (ie. `"east"`) the player wants to go
to look up the name of the next place (if any) in the current place dictionary
as seen {ref}`here <places-direction-to-place>`.

1. `[ ]` use the `.get()` method on `old_place` to get the value associated
         with the `direction` key and assign it to `new_name`
1. `[ ]` Check if `new_name` is falsy. If so:
   * `[ ]` Use the `error()` function to print a message saying:
       {samp}`"Sorry, you can't go {direction} from here.")`
   * `[ ]` return

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lineno-match:
:lines: 91-97
:emphasize-lines: "2, 5-7"
```

`````


### D. (still) in do_go(): figure out where we're going

Next we'll get the info for where the player is going from `PLACES`, or print an
error message if it's not found.

1. `[ ]` use the `.get()` method on `PLACES` to get the value associated
         with the `new_name` key and assign it to `new_place`
1. `[ ]` Check if `new_place` is falsy. If so:
   * `[ ]` Use the `error()` function to print a message saying:
       {samp}`"Woops! The information about {new_name} seems to be missing."`

   This will only happen if you made a mistake somewhere in your code. But just
   in case we do, we want to have a clear error message so we can tell what
   went wrong.
   * `[ ]` return

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lines: 99-107
:lineno-match:
:emphasize-lines: "2, 7-9"
```

`````

### E. (still) in do_go(): update the players place and describe it

Finally, we can now update the `PLAYER` dictionary to point to the new place
name and print the place information.

{{ left }}

1. `[ ]` In the `PLAYER` dictionary change value associated with the `"place"` key to `new_name`
1. `[ ]` Print the values associated with the `"name"` and `"description"` keys of the `new_place` dictionary

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lines: 109-114
:lineno-match:
:emphasize-lines: "2, 5-6"
```

`````

{{ endcols }}
