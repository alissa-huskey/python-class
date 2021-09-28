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
:open:

```{screencast} assets/adventure-1.cast
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

```{code-block} python
:class: full-width
:linenos:

def main():
    print("Welcome")
    while True:
        reply = input("> ")


if __name__ == "__main__":
    main()

```

`````


{{ endcols }}
