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

`````{dropdown} Demo

```{screencast} assets/adventure-1.2.cast
```

`````

{{ br }}

{{ leftcol }}

1. `[ ]` Define a `main()` function, and have it print `"Welcome!"`
2. `[ ]` In `main()` make a `while` loop with the condition `True`.
3. `[ ]` In the loop, call the `input()` function, with the prompt `"> "`. Assign the returned value to the variable `reply`.
4. `[ ]` Outside of `main()`: Use an if statement to check if `__name__ == "__main__"`.
5. `[ ]` In the `if` statement, call `main()`.

{{ rightcol }}

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

`````{dropdown} Demo

```{screencast} assets/adventure-1.3.cast
```

`````

{{ leftcol }}

```{rubric} Make do_quit()
```

1. `[ ]` Make a `do_quit()` function.
1. `[ ]` In it, print `"Goodbye."`
1. `[ ]` Then call `quit()`

```{rubric} In main(), in the while loop:
```

1. `[ ]` After getting `reply`, check if `reply` is equal to `q` or `quit`.
1. `[ ]` If so, call `do_quit()`
1. `[ ]` Otherwise, print a messsage like: `"No such command."` then `continue`

{{ rightcol }}

`````{dropdown} Code

```{literalinclude} adventure/adventure-1.3.py
:class: full-width
:linenos:
:emphasize-lines: "1-4, 11-16"

```

`````

{{ endcols }}

### Part 1.4 Create `ITEMS`

We're going to make our first real command: `shop`. We're skipping ahead a bit
so we can have our program do something interesting.

{{ leftcol }}

Create a dictionary `ITEMS` that is a global variable. This is where you'll
keep the information about the items that are for sale, or objects in any of
the rooms.

{{ br }}

This will be a nested dictionary, where the key is a unique identifier for
each item, and the value is a dictionary with detailed information about
that item. The keys of the child dictionary will be:

* `"key"` -- the same thing as the key
* `"name"` -- a short description
* `"description"` -- a longer description
* `"price"` -- how much it costs

{{ br }}

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

`````{dropdown} Code

```{literalinclude} adventure/adventure-1.4.py
:linenos:
:emphasize-lines: "1-14"

```

`````


{{ endcols }}

### Part 1.5: Make `do_shop()` function

```{rubric} make a do_shop() function
```

1. Define a `do_shop()` function.
1. Have it print `"Items for sale."`
1. Iterate over the `ITEMS` dictionary. Print the `name` and `description` of each.

```{rubric} in main()
```

1. In between your `if` and `else`, add an `elif` clause that checks if `reply`
   is equal to `shop`.
1. If so, call `do_shop()`

`````{dropdown} Code

```{literalinclude} adventure/adventure-1.5.py
:linenos:
:emphasize-lines: "16-23, 38-39"
```

`````



