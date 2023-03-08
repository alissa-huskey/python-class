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
Part 14: Dragons
================

In this section we will add a cave with a three headed dragon and the command to pet them.

{{ sources.format("14.1") }}

Part 14.1: Add command
----------------------

{{ clear }}

In this section we'll add the pet command.

### A. In `test_game.py` write `test_do_pet()`

First we'll write the test which we expect to fail. It will just test that when
you call `do_pet()` a debug message is printed.

`````{dropdown} Need help?

1. `[ ]` Import the `do_read` function
2. `[ ]` Add `test_do_pet()` function with one parameter `capsys`
3. `[ ]` Call `do_pet()` with an empty list as an argument
4. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
5. `[ ]` Write an assert statement that checks that the debug message
         `"Trying to pet: []"` is in `output`
6. `[ ]` Run your tests. They should fail.


`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-14.1.py
:linenos:
:lineno-match:
:start-at: "from adventure import"
:end-at: ")"
:emphasize-lines: "5"
:caption: test_game.py

```

```{literalinclude} ../../../pythonclass/adventure/test_game-14.1.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet"
:caption: test_game.py

```

`````

### B. In `adventure.py` write `do_pet()`

Now we'll add the `do_pet()` function to our game. It should print a debug
message like {samp}`Trying to pet: `

{{ left }}

`````{dropdown} Need help?

1. `[ ]` Add a `do_pet()` function with one parameter `args`
1. `[ ]` In it, use the `debug()` function to print something like `"Trying to read args."`.
1. `[ ]` Run your tests again. They should now pass.

`````

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.1.py
:linenos:
:lineno-match:
:pyobject: "do_pet"
:caption: adventure.py

```
`````

{{ endcols }}

### C. In `adventure.py` in `main()`

{{ left }}

Finally, add the code in `main()` so that when the player types `"pet"`, the
`do_pet()` function will be called.

`````{dropdown} Need help?

1. `[ ]` Add an elif that checks if command is `"pet"`.
   * `[ ]` if so, call `do_pet()` and pass `args`.

`````

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.1.py
:linenos:
:lineno-match:
:start-at: "if command in"
:end-at: "continue"
:caption: adventure.py in `main()`
:emphasize-lines: "31-32"

```

`````

{{ endcols }}
