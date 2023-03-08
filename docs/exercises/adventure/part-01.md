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
Part 1: The game loop
=====================

In this section we'll be writing the game loop--the main interface that allows
the player to enter commands, do something, print messages to the player, and
continue with the game.

We'll write a `main()` function to be the core of this interface. In it we'll
use an infinite `while` loop to run the game. Every time the loop runs it will
ask the player for input, then do something based on their response.

We will eventually write a function to correspond to each of the commands
available in the game, which will be called from `main()` when the player enters
the relevant command.

For now though, we're just setting up the basic framework.

Part 1.1: Setup
---------------

1. `[ ]` Create a new file called `adventure.py`. (You might consider creating a new
repo for it, if you're comfortable with git.)
2. `[ ]` Give the file a docstring that includes the link to this page.

{{ source | format("adventure-1.2.py") }}

Part 1.2: The main() function
-----------------------------

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

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-1.2.py
:linenos:
```

`````

{{ clear }}

{{ source | format("adventure-1.3.py") }}

Part 1.3: Your first command: quit
----------------------------------

{{ clear }}

In this section we will actually look at what the player says, and make our first
command: the `quit` command.

### A. Make do_quit()

{{ left }}

1. `[ ]` Make a `do_quit()` function.
1. `[ ]` In it, print `"Goodbye."`
1. `[ ]` Then call `quit()`

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-1.3.cast
:poster: npt:0:03
:rows: 15
```

`````

{{ endcols }}

### B. In main(), in the while loop:

1. `[ ]` After getting `reply`, check if `reply` is equal to `q` or `quit`.
1. `[ ]` If so, call `do_quit()`
1. `[ ]` Otherwise, print a message like: `"No such command."` then `continue`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-1.3.py
:linenos:
:emphasize-lines: "5-9, 16-21"

```

`````

{{ source | format("adventure-1.4.py") }}

Part 1.4 Create `ITEMS`
-----------------------

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

```{literalinclude} ../../../pythonclass/adventure/adventure-1.4.py
:linenos:
:emphasize-lines: "6-19"

```

`````

{{ source | format("adventure-1.5.py") }}

Part 1.5: Make `do_shop()` function
-----------------------------------

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

### A. Define a do_shop() function

1. `[ ]` Define a `do_shop()` function.
1. `[ ]` Have it print `"Items for sale."`
1. `[ ]` Iterate over the `ITEMS` dictionary. Print the `name` and `description` of each.

### B. In main()

1. `[ ]` In between your `if` and `else`, add an `elif` clause that checks if `reply`
   is equal to `shop`.
1. `[ ]` If so, call `do_shop()`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-1.5.py
:linenos:
:emphasize-lines: "21-28, 43-44"
```

`````
