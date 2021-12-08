---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'
  icon: '{opticon}`file-code`'

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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-1.2.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

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
```

`````

`````{dropdown} Code

```{literalinclude} adventure/adventure-1.2.py
:class: full-width
:linenos:
```

`````

{{ endcols }}


### Part 1.3: Your first command: quit

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-1.3.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

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
:rows: 15
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-1.3.py
:class: full-width
:linenos:
:emphasize-lines: "5-9, 16-21"

```

`````

### Part 1.4 Create `ITEMS`

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-1.4.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

We're going to make our first real command: `shop`. We're skipping ahead a bit
so we can have our program do something interesting.

Create a dictionary `ITEMS` that is a global variable. This is where you'll
keep the information about the items that are for sale, or objects in any of
the rooms.

{{ leftcol }}

This will be a nested dictionary, where the key is a unique identifier for
each item, and the value is a dictionary with detailed information about
that item. The keys of the child dictionary will be:

* `"key"` -- the same thing as the key
* `"name"` -- a short description
* `"description"` -- a longer description
* `"price"` -- how much it costs

Make a few items for your shop.

{{ rightcol }}

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

```{literalinclude} adventure/adventure-1.4.py
:linenos:
:emphasize-lines: "6-19"

```

`````

### Part 1.5: Make `do_shop()` function

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-1.5.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll make a `shop` command that will list the items that we
defined in `ITEMS` above.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-1.5.cast
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

```{literalinclude} adventure/adventure-1.5.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-2.1.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

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

```{literalinclude} adventure/adventure-2.1.py
:linenos:
:emphasize-lines: "35-37, 42-50, 53, 56-57"
```

`````

### Part 2.2: Create PLAYER and PLACES

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-2.2.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

Now we'll make global `PLACES` dictionary which will store information about
the different areas in the game.

Like the `ITEMS` dictionary, `PLACES` will be a nested dictionary, where the
key is a unique identifier for each place, and the value is a dictionary with
detailed information about that place.

{{ leftcol }}

The keys of the child dictionary will be:

* `"key"` -- the same thing as the key
* `"name"` -- a short description
* `"description"` -- a longer description
* `"east"`, `"west"`, `"north"`, `"south"` -- the key to the place in that
  direction. (More on that next.)

{{ rightcol }}

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

{{ leftcol }}

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

{{ rightcol }}

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

{{ leftcol }}

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

{{ rightcol }}

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

{{ leftcol }}

```{code-block-hl} python
:class: full-width
:name: player-to-places

PLAYER = {
    "place": !!!"home"!!!,
}
```

{{ rightcol }}

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

```{literalinclude} adventure/adventure-2.2.py
:linenos:
:emphasize-lines: "6-26"
:end-at: "ITEMS ="
```

`````

### Part 2.3: Write message functions

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-2.3.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

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
:rows: 15
```

`````

{{ endcols }}

#### A. At the top of the file

{{ left }}

1. `[ ]` Add a global variable `DEBUG` and set it to `True`

{{ right }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-2.3.py
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

```{literalinclude} adventure/adventure-2.3.py
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

```{literalinclude} adventure/adventure-2.3.py
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

```{literalinclude} adventure/adventure-2.3.py
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

```{literalinclude} adventure/adventure-2.3.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-2.4.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

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

```{literalinclude} adventure/adventure-2.4.py
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

{{ leftcol }}

1. `[ ]` get the value from `PLAYER` associated with the `"place"` key and assign it to `old_name`
1. `[ ]` get the value from `PLACES` associated with `old_name` and assign it to `old_place`

{{ rightcol }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-2.4.py
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

```{literalinclude} adventure/adventure-2.4.py
:linenos:
:lineno-match:
:lines: 91-97
:emphasize-lines: "2, 5-7"
```

`````


#### D. (still) in do_go(): figure out where we're going

Next we'll look up the new place name from the current place dictionary using
the direction (ie. `"east"`) to as a key. If it's missing, that means the
player can't go that direction from where they are.

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

```{literalinclude} adventure/adventure-2.4.py
:linenos:
:lines: 99-107
:lineno-match:
:emphasize-lines: "2, 7-9"
```

`````

#### E. (still) in do_go(): update the players place and describe it

Finally, we can now update the `PLAYER` dictionary to point to the new place
name and print the place information.

{{ leftcol }}

1. `[ ]` In the `PLAYER` dictionary change value associated with the `"place"` key to `new_name`
1. `[ ]` Print the values associated with the `"name"` and `"description"` keys of the `new_place` dictionary

{{ rightcol }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-2.4.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-3.1.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we're going to add a `wrap()` function, which we'll use to
print paragraphs of text like place or item descriptions. We'll both indent and
wrap the text so that it looks nice.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-3.1.cast
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

```{literalinclude} adventure/adventure-3.1.py
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

```{literalinclude} adventure/adventure-3.1.py
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

```{literalinclude} adventure/adventure-3.1.py
:class: full-width
:linenos:
:start-at: 'def wrap'
:end-before: 'def'
:lineno-match:
:emphasize-lines: "2-"
```

`````

### Part 3.2: Colors

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-3.2.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

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
:rows: 15
```

`````

{{ endcols }}

#### B. At the top of your file

{{ left }}

1. `[ ]` Import `fg`, `bg`, and `fx` from `console`.

{{ right }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-3.2.py
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

```{literalinclude} adventure/adventure-3.2.py
:class: full-width
:linenos:
:lineno-match:
:emphasize-lines: "3, 9"
:start-at: "def error"
:end-before: "def do_"
```

```{literalinclude} adventure/adventure-3.2.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-3.3.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we're going to write a `header()` function to print pretty
headers and a `write()` function to print all other one-line messsages.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-3.3.cast
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

```{literalinclude} adventure/adventure-3.3.py
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

```{literalinclude} adventure/adventure-3.3.py
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

```{literalinclude} adventure/adventure-3.3.py
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

```{literalinclude} adventure/adventure-3.3.py
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

```{literalinclude} adventure/adventure-3.3.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-4.1.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

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

```{literalinclude} adventure/adventure-4.1.py
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

#### B. In do_shop(), in the for loop:

{{ left }}

1. `[ ]` Before printing each item, check if the item has a `"price"` key.
`continue` if not.

{{ right }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-4.1.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-4.2.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll add an `examine` command.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-4.2.cast
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

```{literalinclude} adventure/adventure-4.2.py
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

```{literalinclude} adventure/adventure-4.2.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-4.3.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

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

```{literalinclude} adventure/adventure-4.3.py
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

```{literalinclude} adventure/adventure-4.3.py
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
1. `[ ]` check if name is in the `items` list by:
   * `[ ]` use an if statement with the condition:
     * `[ ]` check if `name` is not in the list returned by `.get()`
     * `[ ]` use the `.get()` method on `place` to get the `"items"` list and pass
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

```{literalinclude} adventure/adventure-4.3.py
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

```{literalinclude} adventure/adventure-4.3.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-5.1.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll define a `do_look()` function that gets called when the
player types `l` or `look`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-5.1.cast
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

```{literalinclude} adventure/adventure-5.1.py
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

```{literalinclude} adventure/adventure-5.1.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-5.2.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll look up the place info and print the name and description.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-5.2.cast
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

```{literalinclude} adventure/adventure-5.2.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-5.3.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll print the list of items in the current place.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-5.3.cast
:rows: 16
```

`````

{{ endcols }}

#### A: at the end of `do_look()`

In this section you will use each of the items in the current places `"items"`
list to get the item information from `ITEMS` then construct a list of each
items `"name"`.

1. `[ ]` Using the `.get()` method, get the value from `place` associated with
         the `items` dictionary. Use a default value of `[]` and assign it to the
         variable `items`.
1. `[ ]` If `items` is {term}`truthy`:
   1. `[ ]` Make an empty list assigned to the variable `names`
   1. `[ ]` Iterate over the `items` list using the variable name `key` for each item. For each item:
      * `[ ]` Get the value from `ITEMS` associated with the `key` key and assign it to the variable `item`
      * `[ ]` Append the value associated with the `"name"` key from the `items` dictionary to the `names` list

`````{dropdown} Code

```{literalinclude} adventure/adventure-5.3.py
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

```{literalinclude} adventure/adventure-5.3.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "if items"
:end-before: "def"
:emphasize-lines: "10-"
```

`````

### Part 5.4: Print the nearby places

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-5.4.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll print the name of each of any places directly to the
`"north"`, `"south"`, `"east"` or `"west"` of the players current place.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-5.4.cast
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

```{literalinclude} adventure/adventure-5.4.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-6.1.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll define a `do_take()` function that gets called when the
player types `t`, `take`, or `grab`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-6.1.cast
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

```{literalinclude} adventure/adventure-6.1.py
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

```{literalinclude} adventure/adventure-6.1.py
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

{{ left }}

In this section we'll check to make sure that the player entered a valid, takable
item in the current place.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-6.2.cast
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

```{literalinclude} adventure/adventure-6.2.py
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

```{literalinclude} adventure/adventure-6.2.py
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

```{literalinclude} adventure/adventure-6.2.py
:class: full-width
:linenos:
:lineno-match:
:start-at: "def do_take"
:end-before: "def"
:emphasize-lines: "23-"
```

`````

### Part 6.3: Take it

{{ left }}

In this section we'll actually take the item.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-6.3.cast
:rows: 16
```

`````

{{ endcols }}

#### A: in `PLAYER`

{{ left }}

1. `[ ]` Add `"inventory": {}` to the `PLAYER` dictionary.

{{ right }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-6.3.py
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

```{literalinclude} adventure/adventure-6.3.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_take(args):'
:end-at: 'wrap(f"You pick up'
:emphasize-lines: "35-"
```

`````

### Part 6.4: Examine inventory

{{ left }}

In this section we'll modify `do_examine()` so it can be used to look at inventory items.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-6.4.cast
:rows: 16
```

`````

{{ endcols }}

#### A: in `do_examine()`

1. `[ ]` Find the if statement where you check if `name` is not in the `place`
         items list. Modify it so that it shows the error if `name` is not in
         `place` items **and** `name` is not in `PLAYER["inventory"]`.

`````{dropdown} Code

```{literalinclude} adventure/adventure-6.4.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-7.1.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll define a `do_inventory()` function that gets called when the
player types `i`, or `inventory`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-7.1.cast
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

```{literalinclude} adventure/adventure-7.1.py
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

```{literalinclude} adventure/adventure-7.1.py
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

{{ left }}

In this section we'll print the players inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-7.2.cast
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

```{literalinclude} adventure/adventure-7.2.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-8.1.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll define a `do_drop()` function that gets called when the
player types `drop`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-8.1.cast
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

```{literalinclude} adventure/adventure-8.1.py
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

```{literalinclude} adventure/adventure-8.1.py
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

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-8.2.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll check to make sure that the player entered an item they
have in inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-8.2.cast
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

```{literalinclude} adventure/adventure-8.2.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_drop'
:end-before: 'def '
:emphasize-lines: "6-"
```

`````

### Part 8.3: Drop it

{link-badge}`https://github.com/alissa-huskey/python-class/blob/master/docs/exercises/adventure/adventure-8.3.py," source code",cls=badge-info text-white fa fa-file-code float-right font-bold p-2 header-link`

{{ clear }}

{{ left }}

In this section we'll check remove the item from the players inventory and add
it to the place items.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-8.3.cast
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

```{literalinclude} adventure/adventure-8.3.py
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
1. `[ ]` call `.setdefault()` on `place` with the argument `items` and `[]`
1. `[ ]` append `name` to `place["items"]`


`````{dropdown} Code

```{literalinclude} adventure/adventure-8.3.py
:class: full-width
:linenos:
:lineno-match:
:start-at: 'def do_drop'
:end-before: 'def '
:emphasize-lines: "25-"
```

`````