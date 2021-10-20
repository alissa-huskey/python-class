---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'

jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
tocdepth: 2
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
```

Part 1: The game loop
---------------------

In this section we'll be writing the game loop--the main interface that allows
the user to enter commads, do something, print messages to the user, and
continue with the game.

We'll write a `main()` function to be the core of this interface. In it we'll
use an infinite `while` loop to run the game. Every time the loop runs it will
ask the user for input, then do something based on their response.

We will eventually write a function to coorespond to each of the commands
available in the game, which will be called from `main()` when the user enters
the relevant command.

For now though, we're just setting up the basic framework.

### Part 1.1: Setup

1. Create a new file called `adventure.py`. (You might consider creating a new
repo for it, if you're comfortable with git.)
2. Give the file a docstring that includes the link to this page.

### Part 1.2: The main() function

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

In this section we will actually look at what the user says, and make our first
command: the `quit` command.

{{ left }}

```{rubric} A. Make do_quit()
```

1. `[ ]` Make a `do_quit()` function.
1. `[ ]` In it, print `"Goodbye."`
1. `[ ]` Then call `quit()`

```{rubric} B. In main(), in the while loop:
```

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

```{rubric} A. Define a do_shop() function
```

1. Define a `do_shop()` function.
1. Have it print `"Items for sale."`
1. Iterate over the `ITEMS` dictionary. Print the `name` and `description` of each.

```{rubric} B. in main()
```

1. In between your `if` and `else`, add an `elif` clause that checks if `reply`
   is equal to `shop`.
1. If so, call `do_shop()`

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

### Part 2.1: Split reply into command and arguments

{{ left }}

This will be the first command that we've written that takes an argument. That
is, the user needs to type not just `go`, but also which direction to go like
`north`.

That means we need to split the string that is returned from `input()` into a
list. That way we if the user types `go north` we can figure out that `go` is
the command, and `north` is the direction.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-2.1.cast
:rows: 15
```

`````

{{ endcols }}

```{rubric} A. Define do_go
```

1. Define a `do_go()` function that takes one argument: `args`.
2. In `do_go()` print {samp}`Trying to go: {args}`

```{rubric} B. In main(), in the while loop
```

1. Strip the value returned from `input()` using the `.strip()` method.

   This means if a user enters `" quit"` or `"quit "` the program still knows
   to call `do_quit()`.
2. Call `.split()` on `reply` and assign it to the variable `args`.

   Now the `args` variable will contain a list where each word is an item in
   the list.
3. Use an `if` statement to check if `args` is {term}`falsy`. If it is,
   `continue`.

   This means that if a user doesn't enter anything, the program will ignore it
   and start the loop over.
4. Remove the first item from `args` using the `.pop()` method and assign it to
   the variable `command`.

   Now `command` will contain the first word the user entered, and `args` will
   contain a list of the remaining commands. If there were no additional words,
   then `args` will be an empty list.
5. In each clause of the `if` statement where we check the value of `reply`,
   change it to `command`.
6. Add an `elif` clause that checks if `command` is equal to `"g"` or `"go"`.
   If it is, call `do_go()` and pass `args`.

`````{dropdown} Code

```{literalinclude} adventure/adventure-2.1.py
:linenos:
:emphasize-lines: "35-37, 42-50, 53, 56-57"
```

`````

### Part 2.2: Create PLAYER and PLACES

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

```{rubric} at the top of your file
```

1. Create a `PLAYER` dictionary with the key `"place"` and the value `"home"`.
2. Create a `PLACES` dictionary where the key is a unique identifier for each place.
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

### Part 2.3: Write user message functions

{{ left }}

We're going to take a brief interlude here to write a couple of functions for
printing messages to the user.

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

```{rubric} A. At the top of the file
```

1. `[ ]` Import `stderr` from the `sys` module
1. `[ ]` Add a global variable `DEBUG` and set it to `True`


```{rubric} B. Define debug() function
```

1. `[ ]` Write a function named: `debug` with one parameter: `message`
1. `[ ]` In the function, check if `DEBUG` is `True` (or {term}`truthy`)
   * `[ ]` If so, then print `message`
   * `[ ]` Bonus: Print something before it like `"DEBUG: "`, or `"# "`, so you can more
                 easily tell that it is a debug message

```{rubric} C. define error() function
```

1. `[ ]` Write a function named: `error` with one parameter: `message`
1. `[ ]` Print `message` with something before it like `"Error: "`. Send the
         keyword argument `file` with the value `stderr` to print it to
         {term}`stderr`.
         *See [CLI Lesson](../lessons/cli.html#input-and-output) for more information.*

```{rubric} D. in do_go()
```

1. `[ ]` Call `debug()` instead of `print()` for the message {samp}`Trying to go: {args}`

```{rubric} E. in main(), in the while loop
```

1. `[ ]` At the beginning of the `while` loop call `debug()` with the message {samp}`You are at: {PLACE}`.
   Replace `PLACE` with the value in the `PLAYER` dictionary associated with the `"place"` key

   This will print a debug message with your current location every time the loop runs.

1. `[ ]` After assigning `command`, use `debug()` to print `command` and `args`.
1. `[ ]` Call `error()` instead of `print()` for the message {samp}`No such command.`

```{rubric} F. Test debug messages
```

1. `[ ]` Test with `DEBUG` set to `True` as well as with `DEBUG` set to `False`


`````{dropdown} Code

```{literalinclude} adventure/adventure-2.3.py
:linenos:
:emphasize-lines: "6-8, 47-55, 73, 79, 88, 100"
```

`````


### Part 2.4: Fill in `go` command

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

```{rubric} A. in do_go(): ensure that the user typed a valid direction
```

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
:lines: "71-87"
:lineno-match:
:emphasize-lines: "6-8, 12, 15-17"
```

`````

```{rubric} B. (still) in do_go(): look up where the user is at
```

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
:lines: 89-91
:emphasize-lines: "2-"
```

`````

{{ endcols }}

```{rubric} C. (still) in do_go(): look up what is in that direction from here
```

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
:lines: 93-99
:emphasize-lines: "2, 5-7"
```

`````


```{rubric} D. (still) in do_go(): figure out where we're going
```

Next we'll look up the new place name from the current place dictionary using
the direction (ie. `"east"`) to as a key. If it's missing, that means the
player can't go that direction from where they are.

1. `[ ]` use the `.get()` method on `PLACES` to get the value associated
         with the `new_name` key and assign it to `new_place`
1. `[ ]` Check if `new_place` is falsy. If so:
   * `[ ]` Use the `error()` function to print a message saying:
   `"Woops! The information about {new_name} seems to be missing."`

   This will only happen if you made a mistake somewhere in your code. But just
   in case we do, we want to have a clear error message so we can tell what
   went wrong.
   * `[ ]` return

`````{dropdown} Code

```{literalinclude} adventure/adventure-2.4.py
:linenos:
:lines: 101-109
:lineno-match:
:emphasize-lines: "2, 7-9"
```

`````

```{rubric} E. (still) in do_go(): update the players place and describe it
```

Finally, we can now update the `PLAYER` dictionary to point to the new place
name and print the place information.

{{ leftcol }}

1. `[ ]` In the `PLAYER` dictionary change value associated with the `"player"` key to `new_name`
1. `[ ]` Print the values associated with the `"name"` and `"description"` keys of the `new_place` dictionary

{{ rightcol }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-2.4.py
:linenos:
:lines: 111-116
:lineno-match:
:emphasize-lines: "2, 5-6"
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-2.4.py
:pyobject: do_go
:linenos:
:emphasize-lines: "6-8, 12, 15-17, 20-21, 24, 27-29, 32, 37-39, 42, 45-46"
:lineno-match:
```

`````

Part 3: Colors and wrapping
---------------------------

In this section we'll start making things prettier by wrapping text and adding colors.

Part 3.1: Text wrapping
-----------------------

{{ left }}

In this section we're going to add a `message()` function, which we'll use for
anything that we want to print to the user. We'll put our text wrapping in that
function.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-3.1.cast
:rows: 15
```

`````

{{ endcols }}

```{rubric} A. at the top of your file
```

{{ left }}

1. `[ ]` import the `textwrap` module
1. `[ ]` Add a global variable `WIDTH` and assign it the value `60` (or so, to taste).

{{ right }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-3.1.py
:linenos:
:lines: "6-15"
:lineno-match:
:emphasize-lines: "2, 4"
```

`````

{{ endcols }}


```{rubric} B. Make message()
```

1. `[ ]` Define a `message()` function which takes one argument `text`.
1. `[ ]` For now, just print `message` in the function, so we can make sure it works.

```{rubric} C. In do_go(), at the end
```

1. `[ ]` Instead of printing the new place name and description, call the
         `message()` function you just wrote.


`````{dropdown} Code

```{literalinclude} adventure/adventure-3.1.py
:class: full-width
:linenos:
:lines: "122-126"
:lineno-match:
:emphasize-lines: "3, 5"
```

`````

```{rubric} B. In message()
```

1. `[ ]` Call the `wrap()` function from the `textwrap` module. Pass it the
   `text` and the global variable `WIDTH`. Assign the result to the variable
   `lines`.
1. `[ ]` Iterate over the `lines`, and print each `line`.

`````{dropdown} Code

```{literalinclude} adventure/adventure-3.1.py
:class: full-width
:linenos:
:lines: "50-53"
:lineno-match:
:emphasize-lines: "1-"
```

`````

Part 3.2: Colors
----------------

{{ left }}

In this sction we're going to use the `console` module to make our game more
colorful.

```{rubric} A. install console
```

1. `[ ]` Follow the instructions [here](../lessons/cli.html#installation) to install.


{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-3.2.cast
:rows: 15
```

`````

{{ endcols }}

```{rubric} B. At the top of your file
```

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

```{rubric} B. In error(), debug(), other places...
```

{{ left }}

1. In the places you want it, such as in the `error()` and `debug()` function,
  add colors and styles to your taste.

{{ right }}

`````{dropdown} Code
:open:

```{literalinclude} adventure/adventure-3.2.py
:class: full-width
:linenos:
:lines: "57-65"
:lineno-match:
:emphasize-lines: "3, 9"
```

```{literalinclude} adventure/adventure-3.2.py
:class: full-width
:linenos:
:lines: "130-137"
:lineno-match:
:emphasize-lines: "7"
```

`````

{{ endcols }}
