---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'
  icon: '{opticon}`file-code`'
  source: '{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/pythonclass/adventure/%s," %s",type=link, cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`'
  code: '{{link-badge}}`https://github.com/alissa-huskey/python-class/blob/master/pythonclass/adventure/{0}," {1}",type=link, cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`'
  sources: '{{{{ code.format("adventure-{0}.py", "adventure.py") }}}} {{{{ code.format("test_game-{0}.py", "test_game.py") }}}}'

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
Adventure Game
==============

Text adventure games, sometimes called interactive fiction, are an old genre
where the entire world is described with text. The gameplay is done through
simple commands like `go north` or `eat pie`.

Each area in the game, item, or action has its own description.

You can find a [demo][game-demo] of a game like this on Replit, and the
[source code][game-code] is on github. (Though the version we'll be writing is
much simpler to start.).

[game-demo]: https://replit.com/@alissahuskey/adventure
[game-code]: https://github.com/alissa-huskey/adventure

```{contents}
:backlinks: top
:local:
:depth: 2
```

Part 1: The game loop
---------------------

In this section we'll be writing the game loop--the main interface that allows
the player to enter commads, do something, print messages to the player, and
continue with the game.

We'll write a `main()` function to be the core of this interface. In it we'll
use an infinite `while` loop to run the game. Every time the loop runs it will
ask the player for input, then do something based on their response.

We will eventually write a function to coorespond to each of the commands
available in the game, which will be called from `main()` when the player enters
the relevant command.

For now though, we're just setting up the basic framework.

### Part 1.1: Setup

1. `[ ]` Create a new file called `adventure.py`. (You might consider creating a new
repo for it, if you're comfortable with git.)
2. `[ ]` Give the file a docstring that includes the link to this page.

### Part 1.2: The main() function

{{ source | format("adventure-1.2.py", "source code") }}

{{ clear }}

{{ left }}

1. `[ ]` Define a `main()` function, and have it print `"Welcome!"`
2. `[ ]` In `main()` make a `while` loop with the condition `True`.
3. `[ ]` In the loop, call the `input()` function, with the prompt `"> "`. Assign the returned value to the variable `reply`.
4. `[ ]` Outside of `main()`: Use an if statement to check if `__name__ == "__main__"`.
5. `[ ]` In the `if` statement, call `main()`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-1.2.cast
:rows: 16
:poster: npt:0:02
```

`````

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-1.2.py
:class: full-width
:linenos:
```

`````

{{ endcols }}


### Part 1.3: Your first command: quit

{{ source | format("adventure-1.3.py", "source code") }}

{{ clear }}

In this section we will actually look at what the player says, and make our first
command: the `quit` command.

#### A. Make do_quit()

{{ left }}

1. `[ ]` Make a `do_quit()` function.
1. `[ ]` In it, print `"Goodbye."`
1. `[ ]` Then call `quit()`

#### B. In main(), in the while loop:

1. `[ ]` After getting `reply`, check if `reply` is equal to `q` or `quit`.
1. `[ ]` If so, call `do_quit()`
1. `[ ]` Otherwise, print a messsage like: `"No such command."` then `continue`

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-1.3.cast
:poster: npt:0:03
:rows: 15
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-1.3.py
:class: full-width
:linenos:
:emphasize-lines: "5-9, 16-21"

```

`````

### Part 1.4 Create `ITEMS`

{{ source | format("adventure-1.4.py", "source code") }}

{{ clear }}

We're going to make our first real command: `shop`. We're skipping ahead a bit
so we can have our program do something interesting.

Create a dictionary `ITEMS` that is a global variable. This is where you'll
keep the information about the items that are for sale, or objects in any of
the rooms.

{{ left }}

This will be a nested dictionary, where the key is a unique identifier for
each item, and the value is a dictionary with detailed information about
that item. The keys of the child dictionary will be:

* `"key"` -- the same thing as the key
* `"name"` -- a short description
* `"description"` -- a longer description
* `"price"` -- how much it costs

Make a few items for your shop.

{{ right }}

Here is an example:

```python
ITEMS = {
    "elixr": {
        "key": "elixr",
        "name": "healing elixr",
        "description": "a magical elixr that will heal what ails ya",
        "price": -10,
    },
}
```

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-1.4.py
:linenos:
:emphasize-lines: "6-19"

```

`````

### Part 1.5: Make `do_shop()` function

{{ source | format("adventure-1.5.py", "source code") }}

{{ clear }}

{{ left }}

In this section we'll make a `shop` command that will list the items that we
defined in `ITEMS` above.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-1.5.cast
:poster: npt:0:02
:rows: 15
```

`````

{{ endcols }}

#### A. Define a do_shop() function

1. `[ ]` Define a `do_shop()` function.
1. `[ ]` Have it print `"Items for sale."`
1. `[ ]` Iterate over the `ITEMS` dictionary. Print the `name` and `description` of each.

#### B. in main()

1. `[ ]` In between your `if` and `else`, add an `elif` clause that checks if `reply`
   is equal to `shop`.
1. `[ ]` If so, call `do_shop()`

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-1.5.py
:linenos:
:emphasize-lines: "21-28, 43-44"
```

`````

Part 2: Go places
-----------------

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

### Part 2.1: Split reply into command and arguments

{{ source | format("adventure-2.1.py", "source code") }}

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

#### A. Define do_go

1. `[ ]` Define a `do_go()` function that takes one argument: `args`.
2. `[ ]` In `do_go()` print {samp}`Trying to go: {args}`

#### B. In main(), in the while loop

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

```{literalinclude} ../../pythonclass/adventure/adventure-2.1.py
:linenos:
:emphasize-lines: "35-37, 42-50, 53, 56-57"
```

`````

### Part 2.2: Create PLAYER and PLACES

{{ source | format("adventure-2.2.py", "source code") }}

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
:class: full-width

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
:class: full-width

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
:class: full-width

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
:class: full-width

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
:class: full-width

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
:class: full-width
:name: player-to-places

PLAYER = {
    "place": !!!"home"!!!,
}
```

{{ right }}

```{code-block-hl} python
:class: full-width

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

#### A. at the top of your file

1. `[ ]` Create a `PLAYER` dictionary with the key `"place"` and the value `"home"`.
2. `[ ]` Create a `PLACES` dictionary where the key is a unique identifier for each place.
   The value is a dictionary that with information about each place:

   * `"key"` -- the same thing as the key
   * `"name"` -- a short description
   * `"description"` -- a longer description
   * `"east"`, `"west"`, `"north"`, `"south"` -- the key to the place in that

   Add two places, `"home"` and `"town-square"`.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-2.2.py
:linenos:
:emphasize-lines: "6-26"
:end-at: "ITEMS ="
```

`````

### Part 2.3: Write message functions

{{ source | format("adventure-2.3.py", "source code") }}

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

#### A. At the top of the file

{{ left }}

1. `[ ]` Add a global variable `DEBUG` and set it to `True`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-2.3.py
:linenos:
:lines: "1-11"
:emphasize-lines: "6"
:lineno-match:
```

`````

{{ endcols }}


#### B. Define debug() function

{{ left }}

1. `[ ]` Write a function named: `debug` with one parameter: `message`
1. `[ ]` In the function, check if `DEBUG` is `True` (or {term}`truthy`)
   * `[ ]` If so, then print `message`
   * `[ ]` Bonus: Print something before it like `"DEBUG: "`, or `"# "`, so you can more
                 easily tell that it is a debug message

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-2.3.py
:linenos:
:lines: "49-53"
```

`````

{{ endcols }}

#### C. define error() function

{{ left }}

1. `[ ]` Write a function named: `error` with one parameter: `message`
1. `[ ]` Print `message` with something before it like `"Error: "`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-2.3.py
:linenos:
:lines: "45-47"
```

`````

{{ endcols }}

#### D. in do_go()

{{ left }}

1. `[ ]` Call `debug()` instead of `print()` for the message {samp}`Trying to go: {args}`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-2.3.py
:class: full-width
:linenos:
:lines: "69-71"
:lineno-match:
:emphasize-lines: "3"
```

`````

{{ endcols }}

#### E. in main(), in the while loop

1. `[ ]` At the beginning of the `while` loop call `debug()` with the message {samp}`You are at: {PLACE}`.
   Replace `PLACE` with the value in the `PLAYER` dictionary associated with the `"place"` key

   This will print a debug message with your current location every time the loop runs.

1. `[ ]` After assigning `command`, use `debug()` to print `command` and `args`.
1. `[ ]` Call `error()` instead of `print()` for the message {samp}`No such command.`

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-2.3.py
:class: full-width
:linenos:
:lines: "73-101"
:lineno-match:
:emphasize-lines: "5, 14, 26"
```

`````

#### F. Test debug messages

1. `[ ]` Test with `DEBUG` set to `True` as well as with `DEBUG` set to `False`

### Part 2.4: Fill in `go` command

{{ source | format("adventure-2.4.py", "source code") }}

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

#### A. in do_go(): ensure that the player typed a valid direction

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

```{literalinclude} ../../pythonclass/adventure/adventure-2.4.py
:class: full-width
:linenos:
:lines: "69-85"
:lineno-match:
:emphasize-lines: "6-8, 12, 15-17"
```

`````

#### B. (still) in do_go(): look up where the player is at

In this section we'll be using the `PLAYER["place"]` to get the current place
from the `PLACES` dictionary, as shown {ref}`here <player-to-places>`.

{{ left }}

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `old_name`
1. `[ ]` get the value from `PLACES` associated with `old_name` and assign it to `old_place`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lineno-match:
:lines: 87-89
:emphasize-lines: "2-"
```

`````

{{ endcols }}

#### C. (still) in do_go(): look up what is in that direction from here

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

```{literalinclude} ../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lineno-match:
:lines: 91-97
:emphasize-lines: "2, 5-7"
```

`````


#### D. (still) in do_go(): figure out where we're going

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

```{literalinclude} ../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lines: 99-107
:lineno-match:
:emphasize-lines: "2, 7-9"
```

`````

#### E. (still) in do_go(): update the players place and describe it

Finally, we can now update the `PLAYER` dictionary to point to the new place
name and print the place information.

{{ left }}

1. `[ ]` In the `PLAYER` dictionary change value associated with the `"place"` key to `new_name`
1. `[ ]` Print the values associated with the `"name"` and `"description"` keys of the `new_place` dictionary

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-2.4.py
:linenos:
:lines: 109-114
:lineno-match:
:emphasize-lines: "2, 5-6"
```

`````

{{ endcols }}

Part 3: Prettify
---------------------------

In this section we'll start making things prettier by wrapping text and adding
colors and styles.

We'll also make sure that the way we print things is consitent by always
printing via our custom functions: `header()`, `wrap()`, `write()`,
`error()`, or `debug()`.

### Part 3.1: Text wrapping

{{ source | format("adventure-3.1.py", "source code") }}

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

#### A. at the top of your file

{{ left }}

1. `[ ]` import the `textwrap` module
1. `[ ]` Add a global variable `WIDTH` and assign it the value `60` (or so, to taste).
1. `[ ]` Add a global variable `MARGIN` and assign it to `2` or `3` (or so, to taste).

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-3.1.py
:linenos:
:lines: "6-15"
:lineno-match:
:emphasize-lines: "2-6"
```

`````

{{ endcols }}


#### B. Make wrap()

1. `[ ]` Define a `wrap()` function which takes one argument `text`.
1. `[ ]` For now, just print `text` in the function, so we can
         make sure it works.

#### C. In do_go(), at the end

{{ left }}

1. `[ ]` Instead of calling `print()` to print the place description, call the
         `wrap()` function you just wrote.

{{ right }}


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-3.1.py
:class: full-width
:linenos:
:start-at: "# print information about the new place"
:end-before: "def "
:lineno-match:
:emphasize-lines: "3"
```

`````

{{ endcols }}

#### D. In wrap()

In this section we'll call `textwrap.fill()` function to wrap a paragraph of
text.

:::{hint}

If you don't know how keyword arguments work or would like a refresher take a
look at this section of the [functions lesson][keyword-args].

:::

1. `[ ]` Mulitply a single space (`" "`) by `MARGIN` and assign it to the local
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

```{literalinclude} ../../pythonclass/adventure/adventure-3.1.py
:class: full-width
:linenos:
:start-at: 'def wrap'
:end-before: 'def'
:lineno-match:
:emphasize-lines: "2-"
```

`````

### Part 3.2: Colors

{{ source | format("adventure-3.2.py", "source code") }}

{{ clear }}

In this section we're going to use the `console` module to make our game more
colorful.

#### A. Install console

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

#### B. At the top of your file

{{ left }}

1. `[ ]` Import `fg`, `bg`, and `fx` from `console`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-3.2.py
:class: full-width
:linenos:
:lines: "6-9"
:lineno-match:
:emphasize-lines: "4"
```

`````

{{ endcols }}

#### C. In error(), debug(), other places...

{{ left }}

1. In the places you want it, such as in the `error()` and `debug()` function,
   add colors and styles to your taste.

{{ right }}

`````{dropdown} Code
:open:

```{literalinclude} ../../pythonclass/adventure/adventure-3.2.py
:class: full-width
:linenos:
:lineno-match:
:emphasize-lines: "3, 9"
:start-at: "def error"
:end-before: "def do_"
```

```{literalinclude} ../../pythonclass/adventure/adventure-3.2.py
:class: full-width
:linenos:
:lineno-match:
:emphasize-lines: "7"
:start-at: 'def main'
:end-at: 'args ='
```

`````

{{ endcols }}

### Part 3.3: Header and write functions

{{ source | format("adventure-3.3.py", "source code") }}

{{ clear }}

{{ left }}

In this section we're going to write a `header()` function to print pretty
headers and a `write()` function to print all other one-line messsages.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-3.3.cast
:poster: npt:0:03
:rows: 15
```

`````

{{ endcols }}


#### A. Define write() function

{{ left }}

In this section we'll define a `write()` function that we'll use to print
non-wrapping messages to the player. This is to make sure that they're all
indented at the same level, or to add any extra formatting.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-3.3.py
:class: full-width
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

#### B. Define header() function

{{ left }}

The `header()` function should style the `title` text using the `fx`, `fg`
and/or `bg` objects, add any additional desired formatting, then print it by
calling the `write()` function.

These steps are to add a blank line before and after the title and to make it
bold, but you can change it to suit your taste.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-3.3.py
:class: full-width
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

#### C. In do_shop():

{{ left }}

Replace `print()` calls with `header()` and `write()` calls.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-3.3.py
:class: full-width
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

#### D. In do_quit():

{{ left }}

Replace `print()` call with `write()` call.

1. `[ ]` When printing any message (like `"Goodbye"`) call `write()` instead of
         `print()`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-3.3.py
:class: full-width
:linenos:
:start-at: 'def do_quit'
:end-before: 'def'
:lineno-match:
:emphasize-lines: "3"
```

`````

{{ endcols }}

#### E. In do_go():

{{ left }}

Replace `print()` call with `header()` call.

1. `[ ]` When printing the place name call `header()` instead of `print()`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-3.3.py
:class: full-width
:linenos:
:start-at: "# print information about the new place"
:end-before: 'def'
:lineno-match:
:emphasize-lines: "2"
```

`````

{{ endcols }}


Part 4: Examine items
---------------------

In this section we'll add the `examine` command.

### Part 4.1: Add new items

{{ source | format("adventure-4.1.py", "source code") }}

{{ clear }}

In this section we'll add a `"desk"` and `"book"` items to the `ITEMS`
dictionary, which will eventualy be added to the `"home"` place. The book is
where we'll find the hint about petting dragons.

We'll also have to modify `do_shop()`, so that items without prices (like
`"book"` and `"desk"`) aren't listed for sale.

Note: At the end of this section, there will be no difference in how the game
behaves. But check and make sure that the book and desk are not listed when you
do the `shop` command.

#### A. In ITEMS:

{{ left }}

1. `[ ]` Add two items to the `ITEMS` dictionary with keys: `"desk"` and
        `"book"`. Like previous items, each element one should be a dictionary
        with a `"name"` and `"description"`; unlike the others, these will have
        no `"price"`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-4.1.py
:class: full-width
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

#### B. In PLACES:

We'll keep track of which items are in a particular place by adding a `"items"`
key to the place dictionary. In this case, we're going to add the keys for the `"book"` and
`"desk"` items to the `"home"` place.

{{ left }}

1. `[ ]` In the dictionary for `"home"` the key `"items"`. The value should be
a list that contains two items, the strings `"book"` and `"desk"`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-4.1.py
:class: full-width
:linenos:
:start-at: 'PLACES'
:end-at: '},'
:lineno-match:
:emphasize-lines: "7"
```

`````

{{ endcols }}

#### C. In do_shop(), in the for loop:

{{ left }}

1. `[ ]` Before printing each item, check if the item has a `"price"` key.
`continue` if not.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-4.1.py
:class: full-width
:linenos:
:start-at: 'def do_shop'
:end-before: 'def do_'
:lineno-match:
:emphasize-lines: "7-8"
```

`````

{{ endcols }}

Be sure to test the `shop` command and make sure book and desk aren't listed.

### Part 4.2: Add `do_examine()`

{{ source | format("adventure-4.2.py", "source code") }}

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

#### A. Make do_examine():

{{ left }}

1. `[ ]` Add a function `do_examine()` with one parameter: `args`.
1. `[ ]` Use the `debug()` function to print the value of `args`, something like:

   {samp}`Trying to examine: {args}`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-4.2.py
:class: full-width
:linenos:
:start-at: 'def do_examine'
:end-before: 'def'
:lineno-match:
```

`````

{{ endcols }}

#### B. In main(), in the while loop:

{{ left }}

1. `[ ]` Add an `elif` clause that checks if `command` is `"x"`, `"exam"`, or `"examine"`.

   * If it is, call `do_examine()` and pass `args`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-4.2.py
:class: full-width
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

### Part 4.3: Finish examine command

{{ source | format("adventure-4.3.py", "source code") }}

{{ clear }}

{{ left }}

In this section we'll write the rest of the `do_examine()` function.

This will be very similar to the `do_go()` function. in that we'll need to make
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

#### A. In do_examine() ensure args is not empty

{{ left }}

1. `[ ]` Check to see if `args` is {term}`falsy`, if so:
   * `[ ]` Use the `error()` function to print a message saying:
   `"What do you want to examine?"`
   * `[ ]` return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-4.3.py
:class: full-width
:linenos:
:start-at: 'def do_examine'
:end-at: "return"
:lineno-match:
:emphasize-lines: "6-9"
```

`````

{{ endcols }}

#### B. Still in do_examine(): get the current place

{{ left }}

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `place_name`
1. `[ ]` get the value from `PLACES` associated with `place_name` and assign it to `place`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-4.3.py
:class: full-width
:linenos:
:start-at: "do_examine"
:end-at: "place ="
:lineno-match:
:emphasize-lines: "11-13"
```

`````

{{ endcols }}

#### C. Still in do_examine(): check the name

1. `[ ]` assign the first element from the `args` list to the variable `name` and make it lowercase
1. `[ ]` check if `name` is in the the list of items available at this place by:
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

```{literalinclude} ../../pythonclass/adventure/adventure-4.3.py
:class: full-width
:linenos:
:start-at: "def do_examine"
:end-before: "# make sure the item is in the ITEMS dictionary"
:lineno-match:
:emphasize-lines: "15-"
```

`````

#### D. Still in do_examine(): get and print the item info

1. `[ ]` Get the value from the `ITEMS` dictionary associated with the `name`
         key and assign it to the variable `item`
1. `[ ]` Using the `header()` funciton print the item name
1. `[ ]` Using the `wrap()` function print the item description

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-4.3.py
:class: full-width
:linenos:
:start-at: "def do_examine"
:end-before: "def"
:lineno-match:
:emphasize-lines: "28-"
```

`````

Part 5: Look around
-------------------

In this section we'll add the `look` command.

### Part 5.1: Add command

{{ source | format("adventure-5.1.py", "source code") }}

{{ clear }}

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

#### A: Define a `do_look()` function

{{ left }}

1. `[ ]` Define a `do_look()` function.
1. `[ ]` In it, use the `debug()` function to print something like `"Trying to look around."`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-5.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_look"
:end-before: "def"
```

`````

{{ endcols }}

#### B: in `main()`, in the `while` loop

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is `"l"` or
         `"look"`.
   * `[ ]` if so, call `do_look()`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-5.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "if command"
:end-before: "if __name__"
:emphasize-lines: "13-14"
```

`````

{{ endcols }}

### Part 5.2: Print place name and description

{{ source | format("adventure-5.2.py", "source code") }}

{{ clear }}

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

#### A: In `do_look()`: look up and print the current place

{{ left }}

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `place_name`
1. `[ ]` get the value from `PLACES` associated with `place_name` and assign it to `place`
1. `[ ]` Print the value associated with the `"name"` key of the `place` dictionary using the `header()` function.
1. `[ ]` Print the value associated with the `"description"` key of the `place` dictionary using the `wrap()` function.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-5.2.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_look"
:end-before: "def"
:emphasize-lines: "6-"
```

`````

{{ endcols }}

### Part 5.3: Print the place items

{{ source | format("adventure-5.3.py", "source code") }}

{{ clear }}

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

#### A: at the end of `do_look()`

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

```{literalinclude} ../../pythonclass/adventure/adventure-5.3.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_look"
:end-at: "names.append"
:emphasize-lines: "5-"
```

`````

#### B: still in `do_look()`, in `if items`

In this section we're going to construct a plain english sentence listing the items in this place. If there is only one item it will look like:

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

```{literalinclude} ../../pythonclass/adventure/adventure-5.3.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "if items"
:end-before: "def"
:emphasize-lines: "10-"
```

`````

### Part 5.4: Print the nearby places

{{ source | format("adventure-5.4.py", "source code") }}

{{ clear }}

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


#### A: at the end of `do_look()`

1. `[ ]` print a blank line
1. `[ ]` Use a for loop to iterate over a list: `"north"`, `"east"`, `"south"`, and `"west"` using the variable name `direction`. For each one:
   * `[ ]` Get the value associated with the `direction` key from the `place` dictionary and assign it to the variable `name`.
   * `[ ]` If `name` is {term}`falsy`, then continue
1. `[ ]` Get the place dictionary from `PLACES` associated with the `name` key and assign it to `destination`.
1. `[ ]` Use the `write()` function to print: {samp}`"To the {direction} is {name}."`.
         Get *`name`* from the `destination` dictionary.


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-5.4.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_look"
:end-before: "def"
:emphasize-lines: "42-"
```

`````

Part 6: Take things
-------------------

In this section we'll add the `take` command.

### Part 6.1: Add command

{{ source | format("adventure-6.1.py", "source code") }}

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

#### A: Define a `do_take()` function

{{ left }}

1. `[ ]` Define a `do_take()` function.
1. `[ ]` In it, use the `debug()` function to print something like {samp}`"Trying to take: {args}."`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-6.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_take"
:end-before: "def"
```

`````

{{ endcols }}

#### B: in `main()`, in the `while` loop

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is `"t"`, `"take"` or
         `"grab"`.
   * `[ ]` if so, call `do_take()`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-6.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: '        if command in ["q", "quit", "exit"]:'
:end-at: '            continue'
:emphasize-lines: "16-17"
```

`````

{{ endcols }}

### Part 6.2: Validate item

{{ source | format("adventure-6.2.py", "source code") }}

{{ clear }}

{{ left }}

In this section we'll check to make sure that the player entered a valid, takable
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

#### A: in `ITEMS`

{{ left }}

1. `[ ]` For any item you wish for the player to be able to `take`, add
         `"can_take": True` to the items dictionary.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-6.2.py
:class: full-width
:linenos:
:lineno-match:
:start-at: '    "book": {'
:end-at: '    },'
:emphasize-lines: "3"
```

`````

{{ endcols }}

#### B: in `do_take()`: make sure the item is valid in the current place

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

```{literalinclude} ../../pythonclass/adventure/adventure-6.2.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_take"
:end-before: "# get the item information"
:emphasize-lines: "5-"
```

`````

#### C: still in `do_take()`: make sure the item is takable

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

```{literalinclude} ../../pythonclass/adventure/adventure-6.2.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_take"
:end-before: "def"
:emphasize-lines: "23-"
```

`````

### Part 6.3: Take it

{{ source | format("adventure-6.3.py", "source code") }}

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

#### A: in `PLAYER`

{{ left }}

1. `[ ]` Add `"inventory": {}` to the `PLAYER` dictionary.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-6.3.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'PLAYER = {'
:end-at: '}'
:emphasize-lines: "3"
```

`````

{{ endcols }}

#### B: in `do_take()`

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

```{literalinclude} ../../pythonclass/adventure/adventure-6.3.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_take(args):'
:end-at: 'wrap(f"You pick up'
:emphasize-lines: "35-"
```

`````

### Part 6.4: Examine inventory

{{ source | format("adventure-6.4.py", "source code") }}

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

#### A: in `do_examine()`

1. `[ ]` Find the if statement where you check if `name` is not in the `place`
         items list. Modify it so that it shows the error if `name` is not in
         `place` items **and** `name` is not in `PLAYER["inventory"]`.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-6.4.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_examine"
:end-before: "# make sure the item is in the ITEMS dictionary"
:emphasize-lines: "19"
```

`````

Part 7: Show inventory
----------------------

In this section we'll add the `inventory` command.

### Part 7.1: Add command

{{ source | format("adventure-7.1.py", "source code") }}

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

#### A: Define a `do_inventory()` function

{{ left }}

1. `[ ]` Define a `do_inventory()` function.
1. `[ ]` In it, use the `debug()` function to print something like `"Trying to show inventory."`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-7.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_inventory():'
:end-at: '    debug'
```

`````

{{ endcols }}

#### B: in `main()`, in the `while` loop

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is `"i"`, or
         `"inventory"`.
   * `[ ]` if so, call `do_inventory()`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-7.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: '        if command in ["q", "quit", "exit"]:'
:end-at: '            continue'
:emphasize-lines: "19-21"
```

`````

{{ endcols }}

### Part 7.2: Print inventory

{{ source | format("adventure-7.2.py", "source code") }}

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

#### A: in `do_inventory()`

1. `[ ]` Use the `header()` function to print `"Inventory"`
1. `[ ]` If `PLAYER["inventory"]` is {term}`falsy`:
   * `[ ]` use the `write()` function to print `"Empty."`
1. `[ ]` Iterate over the results of `.items()` on `PLAYER["inventory"]` using
         the variables `name` and `qty`.
   * `[ ]` Get the value associated with the `name` key from `ITEMS` and assign it to `item`.
   * `[ ]` Use the `write()` function to print the `qty` and `item["name"]`
1. `[ ]` Print a blank line

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-7.2.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_inventory():'
:end-at: '    print()'
:emphasize-lines: "6-"
```

`````
Part 8: Drop things
-------------------

In this section we'll add the `drop` command.

### Part 8.1: Add command

{{ source | format("adventure-8.1.py", "source code") }}

{{ clear }}

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

#### A: Define a `do_drop()` function

{{ left }}

1. `[ ]` Define a `do_drop()` function.
1. `[ ]` In it, use the `debug()` function to print something like {samp}`"Trying to drop {args}."`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-8.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_drop'
:end-at: '    debug'
```

`````

{{ endcols }}

#### B: in `main()`, in the `while` loop

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is `"drop"`.
   * `[ ]` if so, call `do_drop()` and pass `args`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-8.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: '        if command in ("q", "quit", "exit"):'
:end-at: '            continue'
:emphasize-lines: "21-23"
```

`````

{{ endcols }}

### Part 8.2: Validate

{{ source | format("adventure-8.2.py", "source code") }}

{{ clear }}

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

#### A: in `do_drop()`

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

```{literalinclude} ../../pythonclass/adventure/adventure-8.2.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_drop'
:end-before: 'def '
:emphasize-lines: "6-"
```

`````

### Part 8.3: Drop it

{{ source | format("adventure-8.3.py", "source code") }}

{{ clear }}

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

#### A: in `do_drop()`: remove from inventory

1. `[ ]` subtract `1` from `PLAYER["inventory"][name]`
1. `[ ]` remove item from inventory if the quantity is `0` by:

   if `PLAYER["inventory"][name]` is {term}`falsy`:
   * `[ ]` call `.pop()` on `PLAYER["inventory"]` with the argument `name`


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-8.3.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_drop'
:end-before: '    # look up where the player is now'
:emphasize-lines: "20-"
```

`````

#### B: still in `do_drop()`: add to place

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `place_name`
1. `[ ]` get the value from `PLACES` associated with `place_name` and assign it to `place`
1. `[ ]` call `.setdefault()` on `place` with the argument `"items"` and `[]`
1. `[ ]` append `name` to `place["items"]`
1. `[ ]` print a message using the `wrap()` function like:
         {samp}`You set down the {name}.`


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-8.3.py
:class: full-width
:linenos:
:lineno-match:
:pyobject: 'do_drop'
:emphasize-lines: "25-"
```

`````

Part 9: Refactoring
-------------------

In this section we are going to work on refactoring our game.
{term}`Refactoring <refactoring>` is when you change code to make the code
better, but without changing what the software does.

It is key to make changes in small, incremental steps which are tested
regularily to ensure the program works properly throughout. Avoid tearing out
and reworking vast swaths of code at a time, which will often leave you with a
hopeless tangle of broken code.

Here we'll be focusing on the {term}`DRY`[^DRY] principle--don't repeat
yourself. This means that when you notice you're repeating the same, or nearly
the same, code over and over again, find a way to put it somewhere it can be
reused. In this case we'll be adding a few functions, then call those functions
in the places where the same code is repeated.

[^DRY]: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

### Part 9.1: Add abort()

{{ source | format("adventure-9.1.py", "source code") }}

{{ clear }}

The `abort()` function will be similar to the `error()` function, except it
will exit the game immediately. This function will be for errors that only
happen if there is a problem with the code, as opposed to errors that can be
caused by something the user typed in.

(This will actually result in a minor change in behavior. Now, when you
encounter any errors using the `abort()` function, your game will end
immediately instead of continuing on.)

#### A. Define `abort()`

The `abort()` function will simply call `error()` to print an error message,
then exit the program.

When `abort()` is called, a `return` statement will no longer be needed since
the program will end immediately.

{{ left }}

1. `[ ]` define an `abort()` function that takes one argument `message`
1. `[ ]` in `abort()`
   * `[ ]` call `error()` with the argument `message`.
   * `[ ]` call the built-in `exit()` function and pass it the argument `1`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.1.py
:linenos:
:lineno-match:
:pyobject: 'abort'
```

`````

{{ endcols }}

#### B. in `do_take()`

Since we always expect to be able to find an item in the `ITEMS` dictionary for
a key in the `place` items list, if we fail to find one that means that we
messed something up, not the player. This is a perfect place to use `abort()`
instead of `error()`.

Then because `abort()` exits the program immediately, we can remove the `return`.

{{ left }}

1. `[ ]` Call `abort()` instead of `error()` when you check if `item` is {term}`falsy`
1. `[ ]` remove the `return` statement
1. `[ ]` To test, temporarily change the key for `"book"` to somthing
         else, then type `take book` from home. It should print an error message
         then exit the program. After verifying that it works, change it back.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_take'
:end-before: 'if not item.get("can_take")'
:emphasize-lines: "28"
```

`````

{{ endcols }}

#### C. in `do_examine()`

This is nearly exactly the same as the previous section.

{{ left }}

1. `[ ]` Call `abort()` instead of `error()` when you check if `name` is not in `ITEMS`
1. `[ ]` remove the `return` statement
1. `[ ]` To test, temporarily change the key for `"book"` to somthing
         else, then type `take book` from home. It should print an error message
         then exit the program. After verifying that it works, change it back.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_examine'
:end-before: '# get the item dictionary'
:emphasize-lines: "25"
```

`````

{{ endcols }}

#### D. in `do_go()`

Similar to the previous two sections, we always expect to be able to find an
place in the `PLACES` dictionary for a key from another `place` dictionary, so
if we don't it means there's an error somewhere in the code.


{{ left }}

1. `[ ]` Call `abort()` instead of `error()` when you check if `new_place` is {term}`truthy`
1. `[ ]` remove the `return` statement
1. `[ ]` To test, temporarily change the value for `home["east"]` to somthing
         else, then type `go east` from home. It should print an error message
         then exit the program. After verifying that it works, change it back.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_go'
:end-before: '# move the player to the new place'
:emphasize-lines: "38"
```

`````

{{ endcols }}

### Part 9.2: Add get_place()

{{ source | format("adventure-9.2.py", "source code") }}

{{ clear }}

Since we're so often needing to get place information from the `PLACES`
dictionary, we'll wrap this functionality into a function called `get_place()`
that we can call from anywhere in our program where we need to get place
information.

#### A. Define `get_place()`

The `get_place()` function will take one argument, the `key` to get from the
`PLACES` dictionary. We'll make that argument optional though, and set the
default to `None`.

If the user passes a `key` argument, then we'll get the place information from
`PLACES` for that `key`. If they don't, we'll get the key from the `PLAYER`
dictionary for their current location. That way we can call `get_place()` with
no args to get the current place.

This function will also check to make sure the place is found in the `PLACES`
dictionary, and call `abort()` if it is not. That means that anywhere we call
`get_place()` will not have to do that error handling over and over.


{{ left }}

1. `[ ]` define a `get_place()` function that takes one optional argument `key` with a default value of `None`
1. `[ ]` if `key` is {term}`falsy` then assign `key` to the value of the `PLAYER` dict associated with the `"place"` value
1. `[ ]` get the value from the `PLACES` dictionary assocated from the `key` key and assign it to the variable `place`
1. `[ ]` If `place` is {term}`falsy`,
     * `[ ]` Use the `abort()` function to print an error message like:

       {samp}`"Woops! The information about the place {name} seems to be missing."`
1. `[ ]` return `place`


{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'get_place'
```

`````

{{ endcols }}

#### B. In `do_go()`

{{ left }}

1. `[ ]` Call `get_place()` with no arguments to get the value for `old_place`.
         (This will replace the existing `PLACES[old_place]`.)
1. `[ ]` Remove the line assigning `old_name` since that is taken care of in `get_place()`
1. `[ ]` Call `get_place()` with the argument `new_name` to get the value for `new_place`.
         (This will replace the existing `PLACES.get(new_place)`.)
1. `[ ]` Remove the lines that calls `abort()` if `new_place` is {term}`falsy`.


{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_go'
:emphasize-lines: '20, 31'
```

`````

{{ endcols }}

#### C. In `do_look()`

1. `[ ]` Replace the existing value for `place` with a call to `get_place()`.
1. `[ ]` Remove the line assigning `place_name` since that is taken care of in `get_place()`
1. `[ ]` Replace the existing value for `destination` with a call to `get_place()` with the argument `name`.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_look'
:emphasize-lines: '7, 51'
```

`````
#### D. In `do_take()`, `do_examine()` and `do_drop()`

1. `[ ]` Replace the existing value for `place` with a call to `get_place()`.
1. `[ ]` Remove the line assigning `place_name` since that is taken care of in `get_place()`

`````{dropdown} do_take()

```{literalinclude} ../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_take'
:emphasize-lines: '15'
```

`````

`````{dropdown} do_examine()

```{literalinclude} ../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_examine'
:emphasize-lines: '12'
```

`````

`````{dropdown} do_drop()

```{literalinclude} ../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_drop'
:emphasize-lines: '26'
```

`````

{{ endcols }}

### Part 9.3: Add get_item()

{{ source | format("adventure-9.3.py", "source code") }}

{{ clear }}

In this section we'll be adding a `get_item()` function which will be very
similar to `get_place()` but for items instead of places.

#### A. Define `get_item()`

The `get_item()` function will be almost exactly like `get_place()`. It will
also take one argument, the `key` to get from the `ITEMS` dictionary, but it
will not be optional. We'll call `abort()` if the `key` is not in the `ITEMS`
dictionary and finally return the `item` otherwise.


{{ left }}

1. `[ ]` define a `get_item()` function that takes one argument `key`
1. `[ ]` use the `.get()` method on the `ITEMS` dictionary to get the value assocated from the `key` key and assign it to the variable `item`
1. `[ ]` If `item` is {term}`falsy`,
     * `[ ]` Use the `abort()` function to print an error message like:

       {samp}`"Woops! The information about the item {name} seems to be missing."`
1. `[ ]` return `item`


{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'get_item'
```

`````

{{ endcols }}

#### B. Use `get_item()` in `do_look()` and `do_inventory()`

Throughout the rest of the program, you'll replace anywhere that you get an
item from the `ITEMS` dictionary using {term}`subscription` or the `.get()`
method with a call to `get_item()`.

1. `[ ]` Call `get_item()` with the argument `name` or `key` to get the value
   for `item`. This will replace the existing {samp}`ITEMS.get({key})` or
   {samp}`ITEMS[{key}]`.

`````{dropdown} do_look()

```{literalinclude} ../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'do_look'
:emphasize-lines: "23"
```

`````

`````{dropdown} do_inventory()

```{literalinclude} ../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'do_inventory'
:emphasize-lines: "13"
```

`````

#### C. Use `get_item()` in `do_examine()` and `do_take()`

In these functions we'll do a similar replacement as above. Additionally, we'll
remove error handling that is done in `get_item()`.

1. `[ ]` Call `get_item()` with the argument `name` or `key` to get the value
   for `item`. This will replace the existing {samp}`ITEMS.get({key})` or
   {samp}`ITEMS[{key}]`.
1. `[ ]` Remove the lines that calls `abort()` if `item` is {term}`falsy` or if
   `name` is not in `ITEMS`.


`````{dropdown} do_examine()

```{literalinclude} ../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'do_examine'
:emphasize-lines: "23"
```

`````

`````{dropdown} do_take()

```{literalinclude} ../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'do_take'
:emphasize-lines: "23"
```

`````

### Part 9.4: Validation functions

{{ source | format("adventure-9.4.py", "source code") }}

{{ clear }}

In this section we'll be several functions return `True` or `False` so that
they can be used for things we commonly need to check. Specifically the
functions `player_has()`, `place_has()`, and `is_for_sale()`.

#### A. Define `player_has()`

The `player_has()` function will return `True` if the player has a particular
item in inventory.


1. `[ ]` define a `player_has()` function that takes one argument `key`, and an optional argument `qty` with a default value of `1`
1. `[ ]` Check if the `key` is in the players inventory (stored in the `PLAYER`
         dict with the `"inventory"` key), and if so, if the value is greater than or
         equal to `qty`.
    * `[ ]` If so, return `True`
    * `[ ]` If not, return `False`


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: 'player_has'
```

`````

#### B. Call `player_has()` from `do_drop()`

Now in our if statements where we check the same thing we can replace it with a
call to `player_has()`.


1. `[ ]` Find the if statement where we check to see if the item is in not inventory.
1. `[ ]` Replace the part of the condition that checks with a call to
         `player_has()` and pass the argument `name()`. (Be sure to keep the `not`.)


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_drop
:emphasize-lines: "16"
```

`````

#### C. Call `player_has()` from `do_examine()`

1. `[ ]` Find the if statement where we check to see if the item is not in
         either the the current place or the inventory.
1. `[ ]` Replace the part of the condition that checks with a call to
         `player_has()` and pass the argument `name()`. (Be sure to keep the
         `not`, as well as the part that checks if the item is in the current
         place.)


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_examine
:emphasize-lines: "18"
```

`````

#### D. Define `place_has()`

The `place_has()` function will return `True` if the place has a particular
item.


1. `[ ]` define a `place_has()` function that takes one argument `item`.
1. `[ ]` In the function get the current place by calling `get_place()` assign it to the variable `place`.
1. `[ ]` Check if the `item` is in the list of items in the current place by
         using the `.get()` method on `place` with the key `"items"`.
    * `[ ]` If so, return `True`
    * `[ ]` If not, return `False`


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: 'place_has'
```

`````

#### E. Call `place_has()` from `do_take()`

Now in our if statements where we check the same thing we can replace it with a
call to `place_has()`.


1. `[ ]` Find the if statement where we check to see if the item is not in the current place.
1. `[ ]` Replace the part of the condition that checks with a call to
         `place_has()` and pass the argument `name()`. (Be sure to keep the `not`.)


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_take
:emphasize-lines: "18"
```

`````

#### F. Call `place_has()` from `do_examine()`

Now in our if statements where we check the same thing we can replace it with a
call to `place_has()`.


1. `[ ]` Find the if statement where we check to see if the item is not in the current place.
1. `[ ]` Replace the part of the condition that checks with a call to
         `place_has()` and pass the argument `name`. (Be sure to keep the
         `not` as well as the part that checks if the player has the item.)


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_examine
:emphasize-lines: "18"
```

`````

#### G. Define `is_for_sale()`

The `is_for_sale()` function will return `True` if an item is for sale.

1. `[ ]` Define a `is_for_sale()` function that takes one argument, `item`.
1. `[ ]` Check if the `"price"` key is in the `item` dictionary.
    * `[ ]` If so, return `True`
    * `[ ]` If not, return `False`


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: is_for_sale
```

`````

#### H. Call `is_for_sale()` from `do_shop()`

Now in our if statements where we check the same thing we can replace it with a
call to `is_for_sale()`.


1. `[ ]` Find the if statement where we check to see if the `"price"` key is in an `item` dictionary
1. `[ ]` Replace the part of the condition that checks with a call to
         `is_for_sale()` and pass the argument `item`. (Be sure to keep the `not`.)


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_shop
:emphasize-lines: "7"
```

`````

### Part 9.5: Add `inventory_change()`

{{ source | format("adventure-9.5.py", "source code") }}

{{ clear }}

In this section we'll be adding an `inventory_change()` function that will add
or remove items from the players inventory.

#### A. Define `inventory_change()`

The `inventory_change()` function will handle either adding items to a player's
inventory or removing from it. We'll use an optional argument `quantity` for
the number to add. (If the number is negative, then it the quantity will be
subtracted.)

In this function we'll use the `.setdefault()` method on the inventory
dictionary. This is kind of like the inverse of the `.get()` method--if the `key`
is not currently in the dictionary, it will set it `default` value. Otherwise,
nothing will happen.[^setdefault]

Once we are done changing the quantity in inventory, we'll remove the entire
item from dictionary if there is `0` (or less) of them left. This way items
with a zero quantity won't show up in `do_inventory()`.


1. `[ ]` Define a `inventory_change()` function that takes one argument `key`,
         and an optional argument `quantity` with a default value of `1`
1. `[ ]` Call the `.setdefault()` method on the players inventory (accessed in
         the `PLAYER` dict with the `"inventory"` key) with the arguments `key`
         and `0` for the default.
1. `[ ]` Add `quantity` to the players inventory (accessed in the `PLAYER` dict
         with the `"inventory"` key) for the `key` key.

   *Hint: Use the `+=` operator.*
1. `[ ]` Check if the value assocated with `key` in the players inventory is
         {term}`falsy`, or if it is less than or equal to zero.
    * `[ ]` If so, remove that key from the player's inventory by calling the
            `.pop()` method on the inventory dictionary with the `key` argument.

[^setdefault]: See `help(dict.setdefault)` in a python/iPython shell for more information.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.5.py
:linenos:
:lineno-match:
:pyobject: 'inventory_change'
```

`````

#### B. Call `inventory_change()` in `do_take()`

Now we can call `inventory_change()` anytime we want to add or remove something
from inventory. Let's start in the `do_take()` function. Since we currently can
only have one of something in a room at a time, we won't pass the `quantity`
argument, so it will default to `1`.

{{ left }}


1. `[ ]` Find where you add the item to the player's inventory. Replace those
         lines with a call to `inventory_change()` and pass the `name` argument.

{{ right }}


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.5.py
:linenos:
:lineno-match:
:pyobject: 'do_take'
:emphasize-lines: 30
```

`````

{{ endcols }}

#### C. Call `inventory_change()` in `do_drop()`

Next, we'll call it from `do_drop()`.

Here we'll be subtracting from inventory by passing in a negative value for
quantity by putting a `-` in front of the value. Then when the negative number
is added to the current inventory value in `inventory_change()`, it will be the
same as if we had subtracted a positive number.

We run into a little issue, since we can have more than one of something in the
player's inventory, but only one of something in a place. To account for this,
we'll zero out that item in inventory and only add one item to place. (Someday
we may want to make the place `"items"` a dictionary instead of a list so we
can have more than one of a thing in a particular place, but this will have to
do for now.)

{{ left }}


1. `[ ]` Find where you remove the item from the player's inventory. Right above
         that, get the amount the player has in their inventory (stored in the `PLAYER`
         dict with the `"inventory"` key) using the `name` key and assign it to the
         `qty` variable.
1. `[ ]` Replace the lines where you add to the inventory with a call to
         `inventory_change()` with the arguments `name` and `-qty`.

{{ right }}


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.5.py
:linenos:
:lineno-match:
:pyobject: 'do_drop'
:emphasize-lines: "20-24"
```

`````

{{ endcols }}

### Part 9.6: Add `place_add()`

{{ source | format("adventure-9.6.py", "source code") }}

{{ clear }}

In this section we'll be adding an `place_add()` function that will add
an item to the current place.

#### A. Define `place_add()`

The `place_add()` function will take care of looking up the current place,
making sure that the places `"items"` dictionary is set to an empty list if
it's missing, making sure that it's not already in the place, and finally
adding the item key to the place list.

1. `[ ]` Define a `place_add()` function that takes one argument `key`.
1. `[ ]` Get the current place by calling `get_place()` and assign it to the
         variable `place`.
1. `[ ]` Call `.setdefault()` on `place` with the arguments `"items"` and an
         empty list.
1. `[ ]` Check if `key` is in the `place["items"]` list
    * `[ ]` If not, append `key` to the `place["items"]` dict

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.6.py
:linenos:
:lineno-match:
:pyobject: 'place_add'
```

`````

#### B. Call `place_add()` in `do_drop()`

Now we can call `place_add()` anytime we want to add something to a place.
Right now, this only happens in the `do_drop()` function.

{{ left }}


1. `[ ]` Find where you add the item to the place. Replace those lines with a
         call to `place_add()` and pass the `name` argument.
1. `[ ]` You can also remove the line where you get the current place using the
        `get_place()` function.


{{ right }}


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.6.py
:linenos:
:lineno-match:
:pyobject: 'do_drop'
:emphasize-lines: 27
```

`````

{{ endcols }}

### Part 9.7: Add `place_remove()`

{{ source | format("adventure-9.7.py", "source code") }}

{{ clear }}

In this section we'll be adding an `place_remove()` function that will remove
an item from the current place.

#### A. Define `place_remove()`

The `place_remove()` function will take care of looking up the current place,
making sure that the item is in the place, and finally removing the item key
from the place list.

1. `[ ]` Define a `place_remove()` function that takes one argument `key`.
1. `[ ]` Get the current place by calling `get_place()` and assign it to the
         variable `place`.
1. `[ ]` Check if `key` is in the current place by calling `.get()` on `place`
         and passing the arguments `key` and an empty list for the default value.
    * `[ ]` If so, call `.remove()` on `place["items"]` with the `key` argument

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.7.py
:linenos:
:lineno-match:
:pyobject: 'place_remove'
```

`````

#### B. Call `place_remove()` in `do_take()`

Now we can call `place_remove()` anytime we want to remove something from a
place.  Right now, this only happens in the `do_take()` function.

{{ left }}


1. `[ ]` Find where you remove the item from the place. Replace those lines
    with a call to `place_remove()` and pass the `name` argument.
1. `[ ]` You can also remove the line where you get the current place using the
        `get_place()` function.


{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-9.7.py
:linenos:
:lineno-match:
:pyobject: 'do_take'
:emphasize-lines: 30
```

`````

{{ endcols }}

Part 10: Buy things
-------------------

In this section we'll add the buy command, add the market, make sure that the
buy and shop commands only work in the market, and make add information to the
buy shop and examine commands.

### Part 10.1: Add market

{{ source | format("adventure-10.1.py", "source code") }}

{{ clear }}

{{ left }}

First we'll need to add the market to our `PLACES` dictionary so we can
navigate to and from there.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-10.1.cast
:poster: npt:0:04
:speed: 0.5
:rows: 16
```

`````

{{ endcols }}

#### A. Add market to `PLACES`

{{ left }}

1. `[ ]` Add a `"market"` dictionary to your `PLACES` dictionary.
   * `[ ]` Be sure to add the relavant directions. For example, since I have it just north of `"town-square"`
           I have `"south": "town-square"`.  But you can put it somewhere else if
           it suits you.
   * `[ ]` Also add the `"items"` list with a list of keys of the items that
           are for sale in the market. For example, I have `"book"` and
           `"dagger"` in mine.
1. `[ ]` Add the direction values to the other adjacent place dictionaries. For
         example, in my `"town-square"` dictionary I have `"north": "market"`.
1. `[ ]` Test this by making sure you can get to and from the market.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.1.py
:linenos:
:lineno-match:
:start-at: 'PLACES = {'
:end-before: 'ITEMS ='
:emphasize-lines: "13, 19-28"
```

`````
{{ endcols }}

#### B. In `do_shop()` get items from the market

Now that we have a legit market, we can get our items from the market rather
than going through all items.

1. `[ ]` At the beginning of the `do_shop()` function, get the market
         dictionary by calling `get_place()` and assign it to the variable `place`.
1. `[ ]` Change your for loop, instead of iterating over `ITEMS.values()`, use the
         `.get()` method on `place` with the arguments `"items"` and an empty list, and
         iterate over that instead. Also rename the variable from `item` to `key`.
1. `[ ]` Inside the the for loop at the beginning, call `get_item()` with the
         argument `key` and assign it to the variable `item`.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.1.py
:linenos:
:lineno-match:
:pyobject: do_shop
:emphasize-lines: "4, 8-9"
```

`````

### Part 10.2: Add `place_can()`

{{ source | format("adventure-10.2.py", "source code") }}

{{ clear }}

{{ left }}

Some commands can only happen when you are in a particular place. The way we
initially wrote the `do_shop()` function, you can shop from anywhere. Now we're
going to store some extra information on place dictionaries to let us know if
the action is restricted to certain places.

Similar to place `"items"`, we'll store this information as a list of strings,
this time with the key `"can"`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-10.2.cast
:poster: npt:0:02
:speed: 0.5
:rows: 16
```

`````

{{ endcols }}


#### A: In `PLACES` add `"can"` list to market

In the next section we'll write a function to use that information.

{{ left }}

1. `[ ]` In your `market` place dictionary, add the key `"can"`; and for the
         value a list with one item, `"shop"`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.2.py
:linenos:
:lineno-match:
:start-at: '"market": {'
:end-at: '},'
:emphasize-lines: "6"
```

`````

{{ endcols }}

#### B: Define `place_can()`

The `place_can()` function will let us know if a place supports a particular
action. This function will be very similar to the `place_has()` function, but
for actions instead of items.

1. `[ ]` Add the `place_can()` function that takes one argument, `action`.
1. `[ ]` Get the current place by calling `get_place()` and assign it to the variable `place`
1. `[ ]` Check if `action` is not in the list of place items by calling
         `.get()` on `place` with the key `"can"` and an empty list for the default
         argument.
   * `[ ]` If so, return `True`
   * `[ ]` Otherwise, return `False`

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.2.py
:linenos:
:lineno-match:
:pyobject: place_can
```

`````

#### C: Call `place_can()` from `do_shop()`

{{ left }}

1. `[ ]` In `do_shop()` at the very beginning of the function check if shopping
         is supported in the current place by calling `place_can()` with the
         argument `"shop"`.
   * `[ ]` If not, print an error message like {samp}`Sorry, you can't {action} here.` then return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.2.py
:linenos:
:lineno-match:
:pyobject: do_shop
:emphasize-lines: "4-6"
```

`````

{{ endcols }}

### Part 10.3: Add buy command

{{ source | format("adventure-10.3.py", "source code") }}

{{ clear }}

{{ left }}

Now we'll add the buy command.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-10.3.cast
:poster: npt:0:26
:speed: 0.75
:rows: 16
```

`````

{{ endcols }}

#### A. Add game info

First we'll need to give the player some gems, add buy to the market `"can"`
list, and add gems to the items list.

{{ left }}

1. `[ ]` For now, let's give the player some free gems so we can test out
         buying things. Add a `"gems"` key to the `PLAYER` inventory dictionary with a
         value of `50` or so.
1. `[ ]` In the `PLACES` dictionary, add a `"buy"` to the `"can"` list to the market dictionary.
1. `[ ]` In `ITEMS` add a `"gems"` item.

{{ right }}

`````{dropdown} PLAYER

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'PLAYER ='
:end-before: 'PLACES ='
:emphasize-lines: 3
```

`````

`````{dropdown} PLACES

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'PLACES ='
:end-before: 'ITEMS ='
:emphasize-lines: 24
```

`````

`````{dropdown} ITEMS

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'ITEMS ='
:end-before: '# Message functions'
:emphasize-lines: "30-36"
```

`````

{{ endcols }}


#### B: Define a `do_buy()` function

Here we'll define the function that is called when the player types `"buy"`.

{{ left }}

1. `[ ]` Define a `do_buy()` function that takes one argument, `args`
1. `[ ]` In it, use the `debug()` function to print something like {samp}`Trying to buy {args}.`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-at: 'debug'
```

`````

{{ endcols }}

#### C: In `main()`

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is equal to `buy`
   * `[ ]` If so, call `do_buy()` and pass `args`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:pyobject: main
:emphasize-lines: "40-41"
```

`````

{{ endcols }}

#### D: In `do_buy()`, Make sure the place supports buying

{{ left }}

1. `[ ]` Check if you can buy things in the current place buy calling `place_can()` with the argument `"buy"`.
   * `[ ]` If not, print a message like {samp}`Sorry, you can't buy things here.` then return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-at: 'return'
:emphasize-lines: "6-8"
```

`````

{{ endcols }}

#### E: Still in `do_buy()`, make sure the player typed in something to buy

{{ left }}

1. `[ ]` Check if `args` is {term}`falsy`
   * `[ ]` If so, print a message with the `error()` function like `What do you want to buy?` then return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-before: '# get the item name'
:emphasize-lines: "10-13"
```

`````

{{ endcols }}

#### F: Still in `do_buy()`, make sure the item is in this place

{{ left }}

1. `[ ]` assign the first item of the `args` list to the variable `name` and make it lowercase
1. `[ ]` check if the item is in this place by calling `place_has()` with the argument `name`
   * `[ ]` if not, print an error message `"Sorry, I don't see a {name} here."` then return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-before: '# get the item info'
:emphasize-lines: "15-22"
```

`````

{{ endcols }}

#### G. Still in `do_buy()`, make sure the item is for sale

{{ left }}

1. `[ ]` Get the item dictionary by calling `get_item()` with the
         argument `name` and assign it to the variable `item`.
1. `[ ]` Check if the item is for sale by calling `is_for_sale()` with the argument `item`
   * `[ ]` If not print an error message like {samp}`Sorry, {name} is not for sale` then return
1. `[ ]` To test this, add another item that is not for sale to the `market`,
         or temporarily remove the `"price"` from one of the items in your market.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-before: 'price ='
:emphasize-lines: "24-29"
```

`````

{{ endcols }}

#### H. Still in `do_buy()`, make sure the player can afford the item

{{ left }}

1. `[ ]` Get the price from the item dictionary, and make it positive (if
         neccessary) by calling `abs()`, then assign it to the variable `price`
1. `[ ]` Check if the player has enough gems by calling `player_has()` with the
         arguments `"gems"` and `price`. If not:
   * `[ ]` Get the number of gems the player currently has from the `PLAYER`
           inventory dictionary by calling the `.get()` method with the arguments
           `"gems"` and `0` for the default value. Assign it to the variable `gems`.
   * `[ ]` Print an error message like {samp}`Sorry, you can't afford {name} because it costs {price} and you only have {gems}.`
   * `[ ]` return
1. `[ ]` To test this, temporarily change the price of one of your items to be more than the amount of gems you have.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-before: '# remove gems'
:emphasize-lines: "31-35"
```

`````

{{ endcols }}

#### I. In `do_buy()`, buy the item

{{ left }}

1. `[ ]` Remove gems from inventory by calling `inventory_change()` with the values `"gems"` and negative `price`.
1. `[ ]` Add the item to inventory by calling `inventory_change()` with the value `name`
1. `[ ]` Remove the item from the current place by calling `place_remove()` with the argument `name`
1. `[ ]` Print a message like {samp}`"You bought {name}."`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:pyobject: 'do_buy'
:emphasize-lines: "37-"
```

`````

{{ endcols }}


### Part 10.4: Clean up the shop

{{ source | format("adventure-10.4.py", "source code") }}

{{ clear }}

{{ leftcol | replace("col", "col-2") }}

In this section we'll make a number of small changes to improve the shop and examine commands.

{{ rightcol | replace("col", "col-10") }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-10.4.cast
:poster: npt:0:06
:speed: 0.5
:rows: 16
```

`````

{{ endcols }}

#### A: Show price in `do_shop()`

We should add the price to the information we print out about each item. This
is also a good chance to make this look prettier.

{{ left }}

1. `[ ]` Print the `item` `"price"` along with the name and description. If the
         number is negative, call `abs()` to make it a positive number.
1. `[ ]` Use [string formatting](../lessons/string-formatting-part-1) to align
         the information into columns.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.4.py
:linenos:
:lineno-match:
:pyobject: do_shop
:emphasize-lines: 17
```

`````

{{ endcols }}

#### B. Handle long descriptions

If your item descriptions are too long for a single line, you can do either one
of the following.

##### I. Truncate the description

The simplist way to handle too-long descriptions is to truncate them so that
they are all limited to a specific width. There are a few ways to do this, but
here we'll use the `textwrap.shorten()` function.

1. `[ ]` In your for loop, before you call `write()` to print the line, call
         `textwrap.shorten()` with two arguments: the item description, and the desired
         maximum width. Assign it to the variable `description`.
1. `[ ]` In the argument to your `write()` function, replace
         `item["description"]` with `description`.

`````{dropdown} Code

```{code-block}
:linenos:
:lineno-start: 233
:emphasize-lines: "17-18"

def do_shop():
    """List the items for sale."""

    if not place_can("shop"):
        error(f"Sorry, you can't {action} here.")
        return

    place = get_place()

    header("Items for sale.")

    for key in place.get("items", []):
        item = get_item(key)
        if not is_for_sale(item):
            continue

        description = textwrap.shorten(item["description"], 30)
        write(f'{item["name"]:<13}  {description:<30} {abs(item["price"]):>2} gems')

    print()
```

`````

##### II. Add a short `"summary"` to items dictionary

Another way to deal with the problem is to seperate the long `"description"`
from a shorter `"summary"` in the `ITEMS` dictionaries. Then here in
`do_shop()` we'll print the `"summary"`, and in `do_examine()` we'll show the
longer description.

This is fancier, but it will require coming up with more data for each item in
your game.

1. `[ ]` In each dictionary in `ITEMS` add a key `"summary"` with a one-line
         description of the item.
1. `[ ]` In `do_shop` when printing the item information, replace
        `item["description"]` with `item["summary"]`.

`````{dropdown} ITEMS

```{code-block}
:linenos:
:lineno-start: 73
:emphasize-lines: "4-8, 14-18"

    "elixr": {
        "key": "elixr",
        "name": "healing elixr",
        "summary": "a healing elixer",
        "desc": (
            "A small corked bottle filled with a swirling green liquid. "
            "It is said to have magical healing properties."
        ),
        "price": -10,
    },
    "dagger": {
        "key": "dagger",
        "name": "a dagger",
        "summary": "a double-edged 14 inch dagger",
        "description": (
            "A double-edged 14 inch dagger with a crescent shaped hardwood "
            "grip, metal cross guard, and curved studded metal pommel."
        ),
        "price": -25,
    },
```

`````

`````{dropdown} do_shop()

```{code-block}
:linenos:
:lineno-start: 233
:emphasize-lines: "17"

def do_shop():
    """List the items for sale."""

    if not place_can("shop"):
        error(f"Sorry, you can't {action} here.")
        return

    place = get_place()

    header("Items for sale.")

    for key in place.get("items", []):
        item = get_item(key)
        if not is_for_sale(item):
            continue

        write(f'{item["name"]:<13}  {items["summary"]:<30} {abs(item["price"]):>2} gems')

    print()
```

`````

#### C. Show price in `do_examine()`

Let's show the price to `do_examine()` if we're in the market (or somewhere else
where we can shop).

1. `[ ]` In `do_examine()` after the header, check if:
   * the place supports shopping by calling `place_can()` with the argument `"shop"` and
   * the place has the item by calling `place_has()` with the argument `name` and
   * the item is for sale by calling `is_for_sale()` with the argument `item`

   If so:
   * `[ ]` print the `item` `"price"`


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.4.py
:linenos:
:lineno-match:
:pyobject: do_examine
:emphasize-lines: "28-31"
```

`````

#### D. Show inventory quantity in `do_examine()`

1. `[ ]` Check if the player has the item in inventory by calling `player_has()` with the argument `name`. If so:
   * `[ ]` Print the quantity from the `PLAYER` inventory dictionary for `name`.


`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-10.4.py
:linenos:
:lineno-match:
:pyobject: do_examine
:emphasize-lines: "33-36"
```

`````

Part 11: Test things
--------------------

In this section we'll add a read command, which the player will use to read a
clue from the book.

Since our program is starting to get complicated, we'll also start writing
tests. This will help us find out if we break something, even if we don't
happen to play the part of the game that triggers it. Be sure to do the
[Testing Lesson](../practices/testing) if you haven't already.

### Part 11.1: Setup

{{ source | format("test_game-11.1.py", "source code") }}

{{ clear }}

{{ left }}

In this section we'll get a basic test up and running.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-11.1.cast
:poster: npt:0:06
:speed: 1.25
:rows: 16
```

`````

{{ endcols }}

#### A. Install pytest

1. `[ ]` Install `pytest` using the instructions
[here](../practices/testing.html#part-3-pytest).
1. `[ ]` To make sure it works, type `pytest --help` in the terminal.

#### B. Configure VS Code

1. `[ ]` Configure VS Code by following the first two steps
[here](../practices/testing.html#part-6-testing-in-vs-code). When you are
prompted to select the directory containing the tests, choose
{guilabel}`. Root directory`.
1. `[ ]` Install the extension [Python Test Explorer for Visual Studio Code][test-explorer].
         either from the marketplace or by typing the following into the terminal.

   ```console
   code --install-extension littlefoxteam.vscode-python-test-adapter
   ```
1. `[ ]` You may need to restart vscode.

[test-explorer]: https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter

#### C. Prepare for import

In order to run tests, we'll need to treat our game like a module. In order for
that to work, we'll need to make sure of a couple of things.

1. `[ ]` When you call `main()`, it must be under a `if __name__ == "__main__"`
         statement. Otherwise `main()` will be called when you do an import, and bad
         things will happen. (See [Part 1.2](#part-1-2-the-main-function) for
         more info.)
1. `[ ]` The filename for your game must be all lowercased with no spaces or
         other special characters except for underscores (`_`). Rename your
         file if you need to.

   {{ leftcol }}

   **Good**:

   * {file}`adventure_game.py`
   * {file}`game.py`

   {{ rightcol }}

   **Bad**:

   * {file}`Adventure Game.py`
   * {file}`My-Game.py`

   {{ endcols }}


#### D. Create and run tests

{{ left }}

1. `[ ]` Create a new file named `test_game.py`
1. `[ ]` In it, import your module with something like `import adventure`
1. `[ ]` Write a function called `test_truth()`
   * `[ ]` In it, write a simple assert statement `assert True`
1. `[ ]` Run your test by typing `pytest -v test_game.py` in the terminal.

{{ right }}

`````{dropdown} Code
:open:

```{literalinclude} ../../pythonclass/adventure/test_game-11.1.py
:linenos:
:caption: test_game.py
```

`````

{{ endcols }}

:::{tip}

You can add the following to your `pyproject.toml` to always run `pytest` in verbose mode.

```{code-block} toml
:caption: pyproject.toml

[tool.pytest.ini_options]
addopts = "-v"
```

:::


#### E. Run tests in vscode

1. `[ ]` Click the {guilabel}`Testing` icon (that looks like a test beaker)
1. `[ ]` You may need to click the {guilabel}`Refresh Tests` icon (that looks
         like a arrow in a circle) to find your tests.
1. `[ ]` Click the {guilabel}`Run Tests` icon (that looks like a play button).

(See [Running Tests](../practices/testing.html#part-6-2-running-tests) for more info.)


### Part 11.2: Test `is_for_sale()`

{{ source | format("test_game-11.2.py", "source code") }}

{{ clear }}

{{ left }}

For our first real test, we'll start with something simple. Let's test the
`is_for_sale()` function.

To do this, we'll call the `is_for_sale()` function with a fake item then check
the result with an `assert` statement.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-11.2.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

#### A. Write `test_is_for_sale()`

This first test will make sure that when `is_for_sale()` is called with an item
with a `"price"` key it returns `True`.

1. `[ ]` Modify the line where you import your game module to instead just
         import `is_for_sale` which should look something like
         `from adventure import is_for_sale`.
1. `[ ]` Write a function called `test_is_for_sale()`.
1. `[ ]` Make a fake item to pass to `is_for_sale()`.

    We know that an item is a dictionary, and that `is_for_sale()` checks to
    see if the dictionary has a `"price"` key. So all you really need for your
    fake item is a dictionary with a `"price"` key--for our purposes, it
    doesn't even matter what the value is. But to make it a little more clear,
    we'll add a `"name"` as well.

    Make a dictionary with `"name"` and `"price"` keys and assign it to the
    variable `fake_item`.
1. `[ ]` Call `is_for_sale()` with the argument `fake_item` and assign it to
         the variable `result`.
1. `[ ]` Write an `assert` statement that checks if `result` is truthy, and has
         a failure message like:

   `"is_for_sale() should return True if the item has a price"`
1. `[ ]` Run your test, either at the command line or in VS Code.

`````{dropdown} Code
:open:

```{literalinclude} ../../pythonclass/adventure/test_game-11.2.py
:linenos:
:caption: test_game.py
:end-before: 'def test_is_for_sale_without_price'
```

`````

#### B. Write `test_is_for_sale_without_price()`

We want to make sure to test the opposite condition as well -- that when an
item doesn't have a `"price"` key, `is_for_sale()` returns `False`.

1. `[ ]` Write a function called `test_is_for_sale_without_price()`.
1. `[ ]` Make a fake item to pass to `is_for_sale()`.

    This time all that matters is that it is a dictionary *without* a `"price"`
    key. But like before, let's include a `"name"` key for the sake of clarity.

    Make a dictionary with a `"name"` key and assign it to the variable
    `fake_item`.
1. `[ ]` Call `is_for_sale()` with the argument `fake_item` and assign it to
         the variable `result`.
1. `[ ]` Write an `assert` statement that checks if `result` is falsy, and has
         a failure message like:
1. `[ ]` Run your tests, either at the command line or in VS Code.

   `"is_for_sale() should return False if the item doesn't have a price"`

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-11.2.py
:linenos:
:caption: test_game.py
:emphasize-lines: "13-"
```

`````

### Part 11.3: Test `error()`

{{ source | format("test_game-11.3.py", "source code") }}

{{ clear }}

{{ left }}

Let's add another easy test, this time of the `error()` function.

Conceptually this will entail calling the `error()` function, then check what
is printed to make sure it is what we expect.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-11.3.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

```{tip}

The console module automatically detects if the code is being run by another
program (say, from a test) and disables colors and effects if so. This is
handy, so you won't have to account for those escape code characters in your
tests.

```

#### A. Write `test_error()`

With `is_for_sale()` we were able to check the value returned by the function.
This is typically how functions and unit tests should be written.

Since our game is interactive though, we've been printing rather than returning
a lot of the time. To test functions like that we'll have to take an extra step
of capturing the output--that is, sending the text somewhere we can access it
intead of actually printing it.

To do this we'll use a special object provided by pytest called `capsys` to
capture the printed output. After any code that prints we can call the
`.readouterr()` method to retrieve the captured output, and access it via the
`.out` property of the resulting object.

1. `[ ]` Add `error` to your import line, something like:
        `from adventure import is_for_sale, error`.
1. `[ ]` Add a `test_error()` function with the parameter `capsys`.
1. `[ ]` Call `error()` with any message you like
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that `output` equals what you expect to be
         printed, with a failure message like:
1. `[ ]` Run your tests, either at the command line or in VS Code.

   `"The formatted error message should be printed."`

`````{dropdown} Code
:open:

```{literalinclude} ../../pythonclass/adventure/test_game-11.3.py
:linenos:
:lineno-match:
:emphasize-lines: "1, 23-"
:caption: test_game.py
```

`````

### Part 11.4: Test `debug()`

{{ source | format("test_game-11.4.py", "source code") }}

{{ clear }}

{{ left }}

This should be very similar to `test_error()`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-11.4.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

#### A. Write `test_debug()`

1. `[ ]` Import the `debug` function.

   Since your import line is starting to get long, you might want to break it
   up onto multiple lines. Add an open parenthesis before the first function
   name, then put each function on its own line, ending with the closed
   parenthesis on a its own line.
1. `[ ]` Add a `test_debug()` function with the parameter `capsys`.
1. `[ ]` Call `debug()` with any message you like
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that `output` equals what you expect to be
         printed, with a failure message like:

   `"The formatted debug message should be printed."`
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-11.4.py
:linenos:
:lineno-match:
:end-before: def
:class: full-width
```

```{literalinclude} ../../pythonclass/adventure/test_game-11.4.py
:linenos:
:lineno-match:
:start-at: 'def test_debug'
:caption: test_game.py
:class: full-width
```

`````

### Part 11.5: Test `header()` and `write()`

{{ source | format("test_game-11.5.py", "source code") }}

{{ clear }}

{{ left }}

Can you write tests for the `header()` and `write()` functions on your own?

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-11.5.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}


`````{dropdown} header()

```{literalinclude} ../../pythonclass/adventure/test_game-11.5.py
:linenos:
:lineno-match:
:start-at: 'def test_header'
:end-before: 'def'
:caption: test_game.py
:class: full-width
```

`````


`````{dropdown} write()

```{literalinclude} ../../pythonclass/adventure/test_game-11.5.py
:linenos:
:lineno-match:
:start-at: 'def test_write'
:caption: test_game.py
:class: full-width
:caption: test_game.py
```

`````

### Part 11.6: Test `inventory_change()`

{{ source | format("test_game-11.6.py", "source code") }}

{{ clear }}

{{ left }}

In this section we'll write a test for the first function that changes the game
state.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-11.6.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

#### A. Add teardown

Much of our code cares about or interacts with the state of the game--that is,
the data we have stored in `PLAYER`, `PLACES` and `ITEMS`.

When writing tests that modify state, it's important to make sure that each
test is fully independent--that is, each test should be able to be run alone or
alongside other tests in any order. One component of that is making sure that
each test starts with a clean slate.

For this section we'll be adding teardown code--that is, code that will cleanup
after each test. Our code will save copies of our three state dictionaries
before anything is changed. Then in the teardown function we'll copy those
dictionaries back into our module.

To get the teardown function to run after each test we'll need to jump through
a few extra hoops, by taking advantage of some advanced pytest features. It's
not important that you understand this right now--you can go ahead and just
copy the relevant code into your test file.

```{literalinclude} ../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:end-before: "def test_"
:class: full-width
:emphasize-lines: "1-5, 15-"
:caption: test_game.py
```

#### B. Write `test_inventory_change()`

Another rule of thumb when writing tests that deal with state is that the test
should assume as little as possible.

For example, I happen to have `PLAYER["inventory"]["gems"]` set to `50` right
now. So I could write this test to call `inventory_change("gems")` then check
that `PLAYER["inventory"]["gems"] == 51`. The problem is, if I change my code
later to start with `0` gems, or rename gems to coins this test would fail even
though the the `inventory_change()` function would still work just fine.

So the first thing we'll do is add some fake data to `PLAYER["inventory"]`.

1. `[ ]` Import the `inventory_change` function.
1. `[ ]` Add a `test_inventory_change()` function
1. `[ ]` Add a key of your choice to `adventure.PLAYER["inventory"]` with
         whatever quantity you'd like.
1. `[ ]` Call `inventory_change()` with your new key as the argument
1. `[ ]` Write an `assert` statement that checks that the quantity for that key
         is now equal to whatever it was before plus one. Give it a failure message like:

   `"inventory_change() with no quantity argument should add 1."`
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code
:open:

```{literalinclude} ../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change"
:end-before: def
:class: full-width
:caption: test_game.py
```

`````

#### C. Write `test_teardown()`

In this test we'll make sure that the teardown code from
[part A](#a-add-teardown) is working.

1. `[ ]` Add a `test_teardown()` function
1. `[ ]` Add an `assert` statement that the key you added in the previous test
         is not in `PLAYER["inventory"]` with a failure message like:

   `"Each test should start with a fresh data set."`
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change()"
:end-before: "def test_inventory_change_"
:class: full-width
:emphasize-lines: "8-"
:caption: test_game.py
```

`````

#### D. Write `test_inventory_change_missing_key()`

Now we'll add another test case for `inventory_change()`. This one will make
sure that the function works even when the key is not already in the inventory
dictionary.

1. `[ ]` Add a `test_inventory_change_missing_key()` function
1. `[ ]` Set `adventure.PLAYER["inventory"]` to an empty dictionary.
1. `[ ]` Call `inventory_change()` with the key of your choice.
1. `[ ]` Write an `assert` statement that checks your new key is in the
         inventory dictionary.

   `"inventory_change() should add missing keys to the inventory"`
1. `[ ]` Write an `assert` statement that checks that the quantity for that key
         is now equal to `1`. Give it a failure message like:

   `"inventory_change() with no quantity argument should add 1."`
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change_missing_key()"
:end-before: def
:class: full-width
:caption: test_game.py
```

`````

#### E. Additional test cases

Can you add the next two tests on your own?

1. `[ ]` `inventory_change_subtract()` should use a negative number for the
         quantity argument and assert that that amount was subtracted from
         inventory
1. `[ ]` `inventory_change_remove()` should use a negative number for the
         quantity argument so that there will be `0` left and assert that the key was
         removed from inventory

`````{dropdown} test_inventory_change_subtract()

```{literalinclude} ../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change_subtract()"
:end-before: def
:class: full-width
:caption: test_game.py
```

`````

`````{dropdown} test_inventory_change_remove()

```{literalinclude} ../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change_remove()"
:class: full-width
:caption: test_game.py
```

`````

### Part 11.7: Test `do_drop()`

{{ source | format("test_game-11.7.py", "source code") }}

{{ clear }}

{{ left }}

Now that we've learned how to write tests in general, how to test captured
output, and how to safely test functions that change state, we can finally
write a test for one of our command functions.

We'll start with the `do_drop()` function.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-11.7.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

:::{caution}

We're going to use the `inventory_change()`, `player_has()`, and `place_has()`
functions to help in our `do_drop()` tests. It would be a good idea to write
tests for `player_has()` and `place_has()` first, that way you know that those
functions work reliably before using them in another test.

I encourage you to work on those. However, we won't be going into those tests
in detail here.

:::

#### A. Write `test_do_drop_no_args()`

The first test case is very simple. We want to check that if the user didn't
type anything, they get the appropriate error message.

1. `[ ]` Import the functions `do_drop`, `player_has` and `place_has`
1. `[ ]` Add the function `test_do_drop_no_args()` with the parameter `capsys`
1. `[ ]` Call `do_drop()` with an empty list for an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that the appropiate debug message is in `output`
1. `[ ]` Write an assert statement that the appropiate error message is in `output`
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-11.7.py
:linenos:
:lineno-match:
:end-before: PLAYER
:class: full-width
:emphasize-lines: "8, 13-14"

```

```{literalinclude} ../../pythonclass/adventure/test_game-11.7.py
:linenos:
:lineno-match:
:start-at: "def test_do_drop_no_args"
:end-before: def
:class: full-width
:caption: test_game.py

```

`````

#### B. Write `test_do_drop_missing_item()`

This test will check that if the player tries to drop something they don't have
in inventory, they they get the appropriate error message.

1. `[ ]` Add the function `test_do_drop_missing_item()` with the parameter `capsys`
1. `[ ]` Set `adventure.PLAYER["inventory"]` to an empty dictionary.
1. `[ ]` Call `do_drop()` with a list containing an any string as an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that the appropiate debug message is in `output`
1. `[ ]` Write an assert statement that the appropiate error message is in `output`
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-11.7.py
:linenos:
:lineno-match:
:start-at: "def test_do_drop_missing_item"
:end-before: def
:class: full-width
:caption: test_game.py

```

`````


#### C. Write `test_do_drop()`

This test will successfully drop something, then make sure that it was added to
the place and removed from inventory.

1. `[ ]` Add the function `test_do_drop()` with the parameter `capsys`
1. `[ ]` Call the `inventory_change()` function with the key of your choice to
         add a fake item to inventory
1. `[ ]` Call `do_drop()` with a list containing an the key as an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that the appropiate debug message is in `output`
1. `[ ]` Write an assert statement that the appropiate message is in `output`
1. `[ ]` Write an assert statement that calls the `place_has()` function with
         the key to make sure the item was added to the place.
1. `[ ]` Write an assert statement that calls the `player_has()` function with
         the key to make sure the item is not in inventory.
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-11.7.py
:linenos:
:lineno-match:
:start-at: "def test_do_drop("
:class: full-width
:caption: test_game.py

```

`````

### And the rest

We've held off on writing tests until now because I felt you needed more
experience coding before adding another potentially confusing component.
Ideally though, you want to write your tests at the same time you write the
cooresponding code. As you can see, back-filling can be a drudge.

Unless you're excited about writing all of your tests now, I'd recommend adding
a test at the beginning of each coding session and whenever something breaks.

Going forward we'll be writing tests for all of our new code, and running them
regularly.

Part 12: Read things
--------------------

In this section we'll add the read command, which the player can use to read a
clue from the book item.

In this section we'll also start following an approach to coding called
{term}`TDD`, or {term}`Test-Driven Development`. When following this process,
you write your test first, then write the code that makes it pass.

This technique has many advantages. You are forced to be very deliberate about
exactly what you are trying to accomplish, which tends to lead to clearer
thinking and cleaner code. You can be more confident that your code is working
as intended and that it won't break in the future without you noticing.

### Part 12.1: Add command

{{ sources.format("12.1") }}

{{ clear }}

In this section we'll be adding the read command.

#### A. in `test_game.py`

{{ left }}

First we'll write the test, which we expect to fail.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.1.A.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Import the `do_read` function
1. `[ ]` Add `test_do_read()` function with one parameter `capsys`
1. `[ ]` Call `do_read()` with an empty list as an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that checks that the debug message
         `"Trying to read: []"` is in `output`
1. `[ ]` Run your tests, either at the command line or in VS Code. Since we
         haven't written `do_read()` yet, you will get an error.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.1.py
:linenos:
:lineno-match:
:end-before: PLAYER
:class: full-width
:emphasize-lines: "9"

```

```{literalinclude} ../../pythonclass/adventure/test_game-12.1.py
:linenos:
:lineno-match:
:start-at: "def test_do_read("
:class: full-width
:caption: test_game.py

```

`````

#### B. in `adventure.py` add `do_read()`

{{ left }}

Now we'll write the code to make it work.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.1.B.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

{{ left }}

1. `[ ]` Add a `do_read()` function with one parameter `args`
1. `[ ]` In it, use the `debug()` function to print something like {samp}`"Trying to read {args}."`.
1. `[ ]` Run your test again. It should now pass.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.1.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:class: full-width
:caption: adventure.py

```

`````

{{ endcols }}

#### C. in `adventure.py` in `main()`

{{ left }}

Finally, we'll add the code to make the command work in the game.

1. `[ ]` Add an `elif` that checks if `command` is `"read"`.
   * `[ ]` if so, call `do_read()` and pass `args`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.1.cast
:poster: npt:0:02
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.1.py
:class: full-width
:linenos:
:lineno-match:
:start-at: def main()
:end-before: 'if __name__'
:emphasize-lines: "37-38"
```

`````

### Part 12.2: Ensure item

{{ sources.format("12.2") }}

{{ clear }}

{{ left }}

In this section we'll make sure that the player entered the item that they want
to read.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.2.cast
:poster: npt:0:02
:speed: 0.75
:rows: 16
```

`````

{{ endcols }}

#### A. in `test_game.py`

{{ left }}

Now we'll add an assertion to check the output for an error message.

1. `[ ]` Change the name of `test_do_read()` to `test_do_read_no_args()`
1. `[ ]` Add an assertion that checks if `"Error What do you want to read?"` is
         in `output`
1. `[ ]` Run your test. It should fail.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.2.A.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.2.py
:linenos:
:lineno-match:
:start-at: "def test_do_read_no_args"
:class: full-width
:caption: test_game.py
:emphasize-lines: "9-"

```

`````

#### B. in `adventure.py` in `do_read()`

{{ left }}

Now we'll write the code to make our test pass.

1. `[ ]` Check if `args` is falsy. If it is, use the `error()` function to
         print an error that says: `"What do you want to read?"` then `return`
1. `[ ]` Run your test again. It should pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.2.B.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.2.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:class: full-width
:caption: test_game.py
:emphasize-lines: "6-"

```

`````

### Part 12.3: Ensure item is here

{{ sources.format("12.3") }}

{{ clear }}

{{ left }}

In this section we'll make sure the item that the player typed is either in
this place or in inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.3.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

#### A. In `test_game.py`

{{ left }}

In this section we'll write a new test to make sure that the item is either in
this place or in inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.3.A.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add `test_do_read_missing_item()` function with the parameter `capsys`
1. `[ ]` Call `do_read()` with a list and a any string that is not an item key for an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that checks that the debug message
         `"Trying to read: []"` is in `output`
1. `[ ]` Write an assert statement that checks that the message
         `"Sorry, I don't know what this is'"` is in `output`
1. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.3.py
:linenos:
:lineno-match:
:start-at: "def test_do_read_missing_item"
:class: full-width
:caption: test_game.py

```

`````

#### B. In `adventure.py` in `do_read()`

{{ left }}

Now we'll add the code to make the test pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.3.B.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` assign the first item of the `args` list to the variable `name` and make it lowercase
1. `[ ]` Write an if statement that checks if either the place or player has the item. If not:
   * `[ ]` Use the `error()` function to print a message like: {samp}`"Sorry, I don't know what this is: {name}'"`
   * `[ ]` return
1. `[ ]` Run your test again. It should pass.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.3.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:class: full-width
:caption: adventure.py
:emphasize-lines: "11-"

```

`````

### Part 12.4: Ensure item is readable

{{ sources.format("12.4") }}

{{ clear }}

{{ left }}

In this section we'll make sure that the item the player wants to be read can,
in fact, be read.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.4.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

#### A. In `test_game.py` write `test_do_read_unreadable_item()`

{{ left }}

In this section we'll be adding a test for when the player tries to read an
item that cannot be read. It should:

* `[ ]` Add a fake unreadable item dictionary to the current place. An item is
  readable if it has a `"message"` key, so for a fake item all we really need
  is an empty dictionary.
* `[ ]` Call `do_read()` with the arguments that would be passed to it if the player
  had typed {samp}`"read {FAKE_THING}"`.
* `[ ]` Check the output for the appropriate error message


{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.4.A.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` import the `place_add` function
1. `[ ]` Add `test_do_read_unreadable_item()` function with the parameter `capsys`
1. `[ ]` Add a fake item to `adventure.ITEMS` with the key of your choice
1. `[ ]` Use the `place_add()` function to add your fake item to the current place
1. `[ ]` Call `do_read()` with a list containing your new key as the argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that checks that the message
         {samp}`"Sorry, I don't can't read '{key}'"` is in `output`
1. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.4.py
:linenos:
:lineno-match:
:start-at: "def test_do_read_unreadable_item"
:class: full-width
:caption: test_game.py

```

`````

#### B. In `adventure.py` in `do_read()`

{{ left }}

Now we'll write the code to make the test pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.4.B.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Use the `get_item()` function to get the item dictionary and assign it to the variable `item`
1. `[ ]` Check if the `"message"` key is in the item dictionary. If not:
   * `[ ]` Use the `error()` function to print an error message like: {samp}`"Sorry, I can't read '{name}'"`
   * `[ ]` return
1. `[ ]` Run your test again. It should pass.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.4.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:class: full-width
:caption: adventure.py
:emphasize-lines: "19-"

```

`````

### Part 12.5: Read things

{{ sources.format("12.5") }}

{{ clear }}

In this section we'll finally provide a readable item and the `read` command
will read it.

#### A. In `test_game.py` write `test_do_read_in_place()`

{{ left }}

In this section we'll write a new test where we'll set up a fake item with 
`"message"` and `"title"` keys containing the text to be read and add it to the
current place. Then we'll call `do_read()`and check for the expected output.


{{ right }}

`````{dropdown} Demo

```{screencast} assets/adventure-12.5.A.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add a function `test_do_read_in_place()`
1. `[ ]` Create a dictionary representing a fake item item with the keys
         `"title"` and `"message"` and whatever text you'd like for the values.
1. `[ ]` Use the `place_add()` function to add it to the current place
1. `[ ]` Call `do_read()` with the the key for your fake item
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that the title is in `output`
1. `[ ]` Write an assert statement that the message is in `output`
1. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.5.py
:linenos:
:lineno-match:
:start-at: "def test_do_read_in_place"
:class: full-width
:caption: test_game.py
:end-before: def

```

`````

#### B. In `adventure.py` in `do_read()`

{{ left }}

Now we'll write the code to actually read the item.

{{ right }}

`````{dropdown} Demo

```{screencast} assets/adventure-12.5.B.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` If the `"title"` key exists in the `item` dictionary, Use the
         `header()` function to print that value. Otherwise print something
         like `"It reads..."`.
1. `[ ]` Use the `wrap()` function to print the `"message"` value from the
         `item` dictionary.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.5.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:emphasize-lines: "27-"
:class: full-width
:caption: adventure.py

```

`````

#### C. Add to `"book"` in `ITEMS`

{{ left }}

Now we'll finally give the player something to read.

1. `[ ]` In the `"book"` dictionary in `ITEMS`, add the key `"title"` with
         whatever text you'd like
1. `[ ]` In the `"book"` dictionary in `ITEMS`, add the key `"message"` with
         whatever text you'd like

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.5.cast
:poster: npt:0:03
:rows: 18
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.5.py
:linenos:
:lineno-match:
:start-at: '"book": {'
:end-before: '"gems": {'
:emphasize-lines: "8-"
:class: full-width
:caption: adventure.py

```

`````

#### D. In `test_game.py` write `test_do_read_in_inventory()`

Can you write a `test_do_read_in_inventory()` function on your own, to test that
you can read a book if it is in your inventory but not in the current place?

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.5.py
:linenos:
:lineno-match:
:start-at: 'def test_do_read_in_inventory'
:class: full-width
:caption: test_game.py

```

`````

### Part 12.6: Indent message

{{ sources.format("12.6") }}

{{ clear }}

{{ left }}

In this section we're going to indent the message part of the text an extra
level.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.cast
:rows: 18
:poster: npt:0:02
```

`````

{{ endcols }}

#### A. In `test_game.py` modify `test_do_read_in_inventory()`

{{ left }}

In this section we're going to modify our `test_do_read_in_inventory()`
function to test that the message has been indented an extra level.

1. `[ ]` Call `.splitlines()` on `output` and assign it to the variable `lines`
1. `[ ]` Write an `assert` statement that checks if the last item in `lines`
         equals your fake items message with 4 spaces at the beginning.
         (Assuming your message is short enough.)
1. `[ ]` Run your test. It should fail.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.A.cast
:poster: npt:0:14
:rows: 16
```

`````

{{ endcols }}

:::{tip}

When you run `pytest` at the command line, you can run a single test by adding
{samp}`::{test_name}` after the filename. For example, here I used `pytest
test_game.py::test_do_read_in_inventory`.

:::

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.6.py
:linenos:
:lineno-match:
:start-at: 'def test_do_read_in_inventory'
:class: full-width
:caption: test_game.py
:emphasize-lines: "17, 22-23"

```

`````

#### B. In `test_game.py` write `test_wrap()`

{{ left }}

Before we change any code in `do_read()`, we're actually going to modify the
`wrap()` function to optionally add indentation. And since we don't have any
tests for `wrap()` yet, we'll one before we change it.

Since we're testing pre-existing behavior here, this is one we'll expect to
pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.B.cast
:poster: npt:0:07
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add a function `test_wrap()` that takes one parameter `capsys`
1. `[ ]` Call `wrap()` with a string that is longer than the `WIDTH` in your game.
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Call `.splitlines()` on `output` and assign it to the variable `lines`
1. `[ ]` Write an `assert` statement that tests that the length of `lines` is greater than `1`
1. `[ ]` Write an `assert` statement that tests that `output` contains the
         first few words of the text argument.
1. `[ ]` Write an `assert` statement that tests that `output` ends with the
         last few words of the text argument, followed by a newline.
1. `[ ]` Make sure that each string in `lines` starts with two, and no more than two, spaces.
1. `[ ]` Run your test. It should pass.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.6.py
:linenos:
:lineno-match:
:start-at: 'def test_wrap'
:end-before: def
:class: full-width
:caption: test_game.py

```

`````

#### C. In `test_game.py` write `test_wrap_with_indent()`

{{ left }}

Now that we have the normal `wrap()` behavior tested, we'll add a (failing)
test for the new behavior with the optional `indent` parameter we will be
adding.

This is going to be nearly identical to the `test_wrap()` function, except
we'll be adding the keyword argument `indent=2` when we call `wrap()`, then
testing that the lines are indented to `4` spaces instead of `2`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.C.cast
:poster: npt:0:08
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add a function `test_wrap_with_indent()` that takes one parameter `capsys`
1. `[ ]` Call `wrap()` with a string that is longer than the `WIDTH` in your
         game, followed by a keyword argument `indent` with a value of `2`.
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Call `.splitlines()` on `output` and assign it to the variable `lines`
1. `[ ]` Write an `assert` statement that tests that the length of `lines` is greater than `1`
1. `[ ]` Write an `assert` statement that tests that `output` contains the
         first few words of the text argument.
1. `[ ]` Write an `assert` statement that tests that `output` ends with the
         last few words of the text argument, followed by a newline.
1. `[ ]` Make sure that each string in `lines` starts with four, and no more than four, spaces.
1. `[ ]` Run your test. (Or however many extra spaces you would like.)  It should fail.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.6.py
:linenos:
:lineno-match:
:start-at: 'def test_wrap_with_indent'
:end-before: def
:class: full-width
:caption: test_game.py

```

`````

#### D. In `adventure.py` modify `wrap()`

{{ left }}

We're finally ready to modify the `wrap()` function to handle indention for us.

1. `[ ]` Add an optional `indent` parameter to `wrap` with a default value of `1`
1. `[ ]` When calculating `margin`, multiply the existing value by `indent`
1. `[ ]` Run your `test_wrap_with_indent()` test. It should pass.
1. `[ ]` Run your `test_wrap()` test. It should pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.D.cast
:poster: npt:0:07
:rows: 16
```

`````

{{ endcols }}

:::{tip}

When you run `pytest` at the command line, you can use the
{samp}`-k {KEYWORD}` flag to run all tests with names that contain
`KEYWORD`. For example, here I use `pytest test_game.py -k test_wrap` to
run both `test_wrap()` and `test_wrap_with_indent()`, but no other tests.

:::

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.6.py
:linenos:
:lineno-match:
:start-at: 'def wrap'
:end-before: def
:class: full-width
:caption: test_game.py
:emphasize-lines: "1-5"

```

`````

#### E. In `adventure.py` modify `do_read()`

{{ left }}

Now we're finally ready to modify our `do_read()` function to use the new
`indent` keyword argument in `wrap()`.

1. `[ ]` When you print the item message by calling `wrap()` add a keyword
         argument `indent` with a value of `2`. (Or more, to your taste. Just be
         sure you update your test.)
1. `[ ]` Run your `test_do_read_in_inventory` test. It should pass.
1. `[ ]` Run all your tests. They should pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.E.cast
:poster: npt:0:13
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.6.py
:linenos:
:lineno-match:
:start-at: 'def do_read'
:end-before: def
:class: full-width
:caption: test_game.py
:emphasize-lines: "34"

```

`````

### Part 12.7: Allow for stanzas

{{ sources.format("12.7") }}

{{ clear }}

{{ left }}

In this section we'll add functionality to break up a long message (in
particular, our `book` message) into multiple stanzas.

To accomplish this, we'll modify `wrap()` so that for its `text` argument it can
take either a string or an iterable (a tuple or a list) of strings. If `text`
is a string, it should print just the same as it does now. If `text` is a
`tuple` or a `list`, each item should be wrapped seperately and printed with a
blank line between each one.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.7.cast
:rows: 22
:poster: npt:0:02
```

`````

{{ endcols }}

#### A. In `test_game.py` modify `test_do_read_in_place()`

{{ left }}

In this section we'll modify the `test_do_read_in_place()` test so that the
`"message"` in our fake item is either a tuple or a list, where each item
represents a stanza. Then we'll add an assert statement to check that there are
two `"\n"` before one of our stanzas.

We'll leave the `test_do_read_in_inventory()` test alone, which will make sure
that it still works if message is a string.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.7.A.cast
:poster: npt:0:10
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Modify the value cooresponding to the `"message"` key in your fake
         item dictionary to be either a tuple or a list of strings with
         multiple items.
1. `[ ]` Add an `assert` statement that checks to make sure that output
         contains two blank lines, followed by the number of indentation
         spaces, followed by the first few words of one of your message items.
1. `[ ]` Run the test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.7.py
:linenos:
:lineno-match:
:start-at: 'def test_do_read_in_place'
:end-before: def
:class: full-width
:caption: test_game.py
:emphasize-lines: "3-9, 30,31"

```

`````

#### B. In `test_game.py` write `test_wrap_with_iterable()`

{{ left }}

Once again, the real heavy lifting will be done in the `wrap()` function. So
before we write any code we'll write a new `wrap()` test for when `text` is an
iterable.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.7.B.cast
:poster: npt:0:09
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add a function `test_wrap_with_iterable()` with one parameter `capsys`
1. `[ ]` Set the variable `message` to a list or a tuple of strings.
         (Consider using a few lyrics of a short song or rhyme.)
1. `[ ]` Call the `wrap()` function with the argument `message`
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an `assert` statement that makes sure part of one of our
         `message` items is in `output`
1. `[ ]` Write an `assert` statement to make sure that a parenthesis is
         not in `output` if message is a `tuple`, or that a square bracket is not
         in `output` if `message` is a list. This is to make sure that we
         are not mistakenly printing the entire iterable instead of each
         string in the iterable.
1. `[ ]` Add an `assert` statement that checks to make sure that output
         contains two blank lines, followed by the number of indentation
         spaces, followed by the first few words of one of your `message` items.
1. `[ ]` Run the test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-12.7.py
:linenos:
:lineno-match:
:start-at: 'def test_wrap_with_iterable'
:end-before: def
:class: full-width
:caption: test_game.py

```

`````

#### C. In `adventure.py` modify `wrap()`

{{ left }}

Now we are ready to change the `wrap()` function.

First we'll turn `text` into a one-item iterable if it was a string, that way
we always have something that we can safely iterate over.

Then we'll iterate over each string in our new `text` iterable, wrap it the
same way we already do, and append it to a list called `blocks`.

Finally, we'll print the `blocks` list with two `"\n"` between each one.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.7.C.cast
:poster: npt:0:35
:rows: 16
```

`````

{{ endcols }}

:::{note}

We don't need to make any changes to `do_read()` for this feature, since it
already calls `wrap()` with whatever was in the item dictionary for
`"message"`. So once you're done with this, all your tests should pass.

:::

1. `[ ]` Write an `if` statement to check if `text` is a string using the `isinstance()` function.
   * `[ ]` If so, make a list or tuple containing `text` and assign it to the same variable, `text`.
1. `[ ]` Make an empty list and assign it to the variable `blocks`
1. `[ ]` Use a `for` loop to iterate over `text` using the variable name `stanza`
   * `[ ]` Indent the line(s) where you assign `paragraph` to be inside your
           `for` loop
   * `[ ]` In your call to `textwrap.fill()`, instead of use `stanza` for the
           first argument instead of `text`.
   * `[ ]` Append `paragraph` to `blocks`
1. `[ ]` You can either:
   * `[ ]` Use [argument unpacking][unpacking] to send all of the items in the
           `blocks` list as seperate arguments to the `print()` function, and the
           keyword argument `sep` to print two newlines between each argument.
   * `[ ]` [Join][join] the `blocks` list using two newlines as the delimiter,
           then print the result.
1. `[ ]` Run your `test_wrap_with_iterable()` test. It should pass.
1. `[ ]` Run your `test_do_read_in_place()` test. It should pass.
1. `[ ]` Run all your tests. They should pass.

[unpacking]: ../lessons/in-depth/functions.html?#part-3-unpacking-arguments
[join]: ../lessons/data-types/strings.html?highlight=join#part-2-splitting-and-joining

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.7.py
:linenos:
:lineno-match:
:start-at: 'def wrap'
:end-before: def
:class: full-width
:caption: adventure.py
:emphasize-lines: "7-15, 25-28"

```

`````

#### D. In `adventure.py` modify `ITEMS`

Finally, change the `"message"` in your `"book"` item to be a list or a tuple
of strings.

And now that we're all liteate, feel free to scatter scrolls, signs and sticky
notes all over your game!

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-12.7.py
:linenos:
:lineno-match:
:start-at: '"book": {'
:end-before: '"gems": {'
:class: full-width
:caption: adventure.py
:emphasize-lines: "14, 17, 20, 22"

```

`````

Part 13: Health
----------------

In this section we'll add the health.

The `health_change()` function will work very much like the
`inventory_change()` function.

* it will take one `int` argument, `amount`
* it will add the `amount` to `PLAYER["health"]` (to subtract, use a negative number)
* it will check to make sure that `PLAYER["health"]` is not over `100`. if it is, set health to `100`
* it will check to make sure that `PLAYER["health"]` is not under `0`. if it is, set health to `0`

### Part 13.1: Add `health_change()`

{{ sources.format("13.1") }}

{{ clear }}

In this function we'll add the simple version of the `health_change()`
function, to simply add to the `PLAYER["health"]`.

#### A. in `test_game.py` write `test_health_change()`

Write the failing `test_health_change()`. The test at this point should just
test that the `amount` argument is added to the players current health.

`````{dropdown} Need help?
1. `[ ]` Import `health_change`
2. `[ ]` Add the function `test_health_change()`
3. `[ ]` Set `PLAYER["health"]` to a positive number between `1` - `100`
4. `[ ]` Call `health_change()` with an argument of a positive number
5. `[ ]` assert that `PLAYER["health"]` is now correct
6. `[ ]` Run your test. It should fail.

`````

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-13.1.py
:linenos:
:lineno-match:
:start-at: "from adventure import"
:end-at: ")"
:class: full-width
:emphasize-lines: "7"
:caption: test_game.py

```

```{literalinclude} ../../pythonclass/adventure/test_game-13.1.py
:linenos:
:lineno-match:
:start-at: "def test_health_change("
:end-before: def
:class: full-width
:caption: test_game.py

```
`````

#### B. in `adventure.py` write `health_change()`

Write the simple `health_change()` function. It should take one argument
`amount` and add that value to `PLAYER["health"]`.

`````{dropdown} Need help?
1. `[ ]` Add the function `health_change()` with one argument `amount`
2. `[ ]` Add `amount` to `PLAYER["health"]`
3. `[ ]` Run your tests. They should now pass.

`````

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-13.1.py
:linenos:
:lineno-match:
:start-at: "def health_change("
:end-before: "def"
:class: full-width
:caption: adventure.py

```

`````

### Part 13.2: Parameratize the test

{{ sources.format("13.2") }}

{{ clear }}

In this section we'll modify the `test_health_change()` function to use
parametrization. This allows us to use the same test for several different
cases by changing a few values in the test to variables.

### A. Parameratize test_health_change()

1. `[ ]` Make the starting `PLAYER["health"]` value (in the GIVEN section) a variable `start`.
2. `[ ]` Make the argument passed to `health_change()` (in the WHEN section) a variable `amount`
3. `[ ]` Make the final `PLAYER["health"]` value (in the THEN section) a variable `result`
4. `[ ]` Make (or add) the assert message (in the THEN section) a variable `message`
    * `[ ]` If you didn't already have an assert message, it should be
            similar to what was in your `THEN` description. ie:
            `"a positive number should be added to player health"`
5. `[ ]` Add the names of all four variables in order as parameters to the
         `test_health_change()` function
6. `[ ]` Immediately above `def` line call `@pytest.mark.parametrize()` with the following arguments:
    * `[ ]` The first argument should be a string containing the name of all four variables in the same order as above0
    * `[ ]` The second argument should be a list of tuples (put each tuple on its own line)
    * `[ ]` The first tuple should contain all of the values that were in
            your test before you changed them to variables, in the same order as above.
7. `[ ]` Run your test. It should pass.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-13.2.py
:linenos:
:lineno-match:
:start-at: "@pytest.mark.parametrize"
:end-before: "a negative number"
:class: full-width
:caption: test_game.py

```

```{literalinclude} ../../pythonclass/adventure/test_game-13.2.py
:linenos:
:lineno-match:
:start-after: "a negative number should be subtracted"
:end-before: "def test_is_for_sale"
:class: full-width
:caption: test_game.py

```

`````

### B. Add another set of test parameters

Where we would usually write a new test like `test_health_change_subtract()` to
ensure a negative number subtracts from `PLAYER["health"]`, now we are just
going to add a new tuple to the list passed to `@pytest.mark.parametrize()`.

1. `[ ]` Add a new tuple to your `@pytest.mark.parametrize()` list that contains the values:
   * `[ ]` A positive number for `start`
   * `[ ]` A negative number for `amount`
   * `[ ]` The result of subtracting `amount` from `start` for `result`
   * `[ ]` A string describing the test case for `message` like:
           `"a negative number should be subtractracted from player health"`
1. `[ ]` Run your test. It should pass.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-13.2.py
:linenos:
:lineno-match:
:start-at: "@pytest.mark.parametrize"
:end-before: "def test_is_for_sale"
:emphasize-lines: "4"
:class: full-width
:caption: test_game.py

```

`````

Part 13.3: Add health limits
----------------------------

In this section we're going to change the `health_change()` function so that
`PLAYER["health"]` is always between `0` and `100`.

### A. Add test case for health <= 0

1. `[ ]` Add a new tuple to your `@pytest.mark.parametrize()` list that contains the values:
   * `[ ]` A positive number for `start`
   * `[ ]` A negative number for `amount` where the absolute value is greater than `start`
   * `[ ]` The number `0` for `amount`
   * `[ ]` A string describing the test case for `message` like:
           `"the min health should be 0"`
1. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-13.3.py
:linenos:
:lineno-match:
:start-at: "@pytest.mark.parametrize"
:end-at: "the min health should be 0"
:emphasize-lines: "5"
:class: full-width
:caption: test_game.py

```

`````

### B. Modify `health_change()`

1. `[ ]` Check if `PLAYER["health"]` is less than zero
    * `[ ]` if so, set `PLAYER["health"]` to zero
2. `[ ]` Run your tests. They should pass

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-13.3.py
:linenos:
:lineno-match:
:start-at: "def health_change"
:end-before: "cap health at 100"
:emphasize-lines: "5-7"
:class: full-width
:caption: adventure.py

```

`````

### C. Add test case for health >= 100

1. `[ ]` Add a new tuple to your `@pytest.mark.parametrize()` list that contains the values:
   * `[ ]` A positive number for `start`
   * `[ ]` A positive number for `amount` that, when added to `start` will be greater than `100`
   * `[ ]` The number `100` for `amount`
   * `[ ]` A string describing the test case for `message` like:
           `"the max health should be 100"`
1. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-13.3.py
:linenos:
:lineno-match:
:start-at: "@pytest.mark.parametrize"
:end-at: "def test_"
:emphasize-lines: "6"
:class: full-width
:caption: test_game.py

```

`````

### D. Modify `health_change()`

1. `[ ]` Check if `PLAYER["health"]` is greater than `100`
    * `[ ]` if so, set `PLAYER["health"]` to `100`
2. `[ ]` Run your tests. They should pass

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/adventure-13.3.py
:linenos:
:lineno-match:
:start-at: "def health_change"
:end-before: "def"
:emphasize-lines: "9-11"
:class: full-width
:caption: adventure.py

```

`````



Reference
---------

### Glossary

```{glossary} adventure-game

refactoring
  Making changes to existing code for the sake of improving the code quality
  without changing what the software does. Refactoring is done to improve
  things like readability, maintainability and reliability.

DRY
Don't repeat yourself
   A principle of software development aimed at reducing repetition of software
   patterns, replacing it with abstractions or using data normalization to
   avoid redundancy.

TDD
Test-Driven Development
  A process for writing code that involves writing a test for how you want the
  code to work before writing the code itself.

```

### TODO

- `[ ]` Add cave to `PLACES`, dragon to `ITEMS`
- `[ ]` Add `do_pet()` in cave
- `[ ]` Add `do_help()`
- `[ ]` Add item aliases
- `[ ]` Aliases for `east`, `e` and other directions
- `[ ]` Add items to items, so the book will only be seen when you look at the desk
- `[ ]` Add place inventory so there can be more than one of an item in a place
- `[ ]` Change `ITEMS` {samp}`"can_take": {str}` to {samp}`"can": {list}`
- `[ ]` Add player health, item health points and `do_drink()`

#### Other ideas

- `[ ]` Add saved games, ask the player's name
- `[ ]` Run multiple commands at once or load from a file
- `[ ]` Add something you have to fight in the forest
- `[ ]` Add a bakery with things you can eat which may also heal
- `[ ]` Add a wizards tower with a puzzle to solve
- `[ ]` Items you can open, close, lift, throw, light, turn off
- `[ ]` Places you can go in, out, up, down
- `[ ]` People you can talk to, give things to, ask about things
- `[ ]` Draw a map as the player goes from place to place
- `[ ]` Add a (secret?) jump command to go straight to a place
- `[ ]` Add search command (ie, search rubble)
- `[ ]` Add mushrooms in the forest that you can eat

