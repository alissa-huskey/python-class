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
Part 15: Eat & Drink
====================

In this section we will add the eat and drink commands, which may effect the player's health.

Part 15.1: Add command
----------------------

{{ sources.format("15.1") }}

{{ left }}

In this section we'll add the eat and drink commands.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-15.1.cast
:poster: npt:0:03
```

`````

{{ endcols }}

### A. In `test_game.py` define `test_do_consume_no_args()`

We're going to use the `do_consume()` function for both the eat and drink
commands. This means that later when we define the `do_consume()` function, it
will take two arguments: the `action` (either `"eat"`, or `"drink"`), and
`args` (the usual list of words typed by the user).

First we'll write a parametrized test which we expect to fail. It will have one
parameter `action` with the two cases `"eat"` and `"drink"`.

It should test that when you call `do_consume(action, [])` a debug and error
message is printed.

`````{dropdown} Need help?

1. `[ ]` Import the `do_consume` function.
1. `[ ]` Add `test_do_consume()` function with two parameters: `capsys` and `action`
1. `[ ]` Immediately above the `def` line call `@pytest.mark.parametrize()` with the
   following arguments:
    * A list containing the string `"action"`
    * A list containing the strings: `"eat"` and `"drink"`
1. `[ ]` Call `do_consume()` with two arguments: `action` and an empty list.
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that checks that the debug message
    {samp}`"Trying to {ACTION}: []"` is in `output`
1. `[ ]` Write an assert statement that checks that an error message like
    {samp}`"What do you want to {ACTION}?"` is in `output`
1. `[ ]` Run your tests. They should fail.


`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-15.1.py
:linenos:
:lineno-match:
:start-at: "from adventure import"
:end-at: ")"
:emphasize-lines: "4"
:caption: test_game.py

```

```{literalinclude} ../../../pythonclass/adventure/test_game-15.1.py
:linenos:
:lineno-match:
:pyobject: "test_do_consume_no_args"
:caption: test_game.py

```

`````

### B. In `adventure.py` define `do_consume()`

Now we'll add the `do_consume()` function to our game. Unlike our other `do_`
functions it will take two arguments: the `action` (either `"eat"`, or
`"drink"`), and `args` (the usual list of words typed by the user).

It should print a debug message, then it should check if `args` is empty and if
so print an error message then return.

{{ left }}

`````{dropdown} Need help?

1. `[ ]` Add a `do_consume()` function with two parameters: `action` and `args`.
1. `[ ]` In it, use the `debug()` function to print something like {samp}`"Trying to {ACTION}: args."`.
1. `[ ]` Check if `args` is falsy. If so, print an error message and return.
1. `[ ]` Run your tests again. They should now pass.

`````

{{ right }}

`````{dropdown} do_consume()

```{literalinclude} ../../../pythonclass/adventure/adventure-15.1.py
:linenos:
:lineno-match:
:pyobject: "do_consume"
:caption: adventure.py

```
`````

{{ endcols }}

### C. In `adventure.py` modify `main()`: add eat and drink

Finally, add the code in `main()` so that when the player types `"eat"` or
`"drink"`, the `do_consume()` function is called.

`````{dropdown} Need help?

1. `[ ]` Add an elif that checks if command is `"eat"` or `"drink"`.
   * `[ ]` if so, call `do_consume()` and pass the `command` and `args`.

`````

`````{dropdown} main()

```{literalinclude} ../../../pythonclass/adventure/adventure-15.1.py
:linenos:
:lineno-match:
:start-at: "if command in"
:end-at: "continue"
:caption: adventure.py in `main()`
:emphasize-lines: "34-35"

```

`````

Part 15.2: Is the item in inventory?
------------------------------------

{{ sources.format("15.2") }}

{{ left }}

In this section we'll check to make sure the item is in the player's inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-15.2.cast
:poster: npt:0:03
```

`````

{{ endcols }}


### A. In `test_game.py` define `test_do_consume_not_in_inventory()`

In this section we'll write a parametrized test which we expect to fail. It will have one
parameter `action` with the two cases `"eat"` and `"drink"`.

The function should test that if the player tries to eat or drink something
that is not in inventory an error message will be printed.

`````{dropdown} Need help?

{{ left }}

1\. Define a parametrized `test_do_consume_not_in_inventory()` function

{{ br }}

{{ right }}

   ```{dropdown} ...
    1. `[ ]` Add `test_do_consume_not_in_inventory()` function with two parameters: `capsys` and `action`.
    1. `[ ]` Immediately above the `def` line call `@pytest.mark.parametrize()` with the
      following arguments:
        * The string `"action"`
        * A list that contains the strings `"eat"` and `"drink"`
   ```

{{ newrow }}

2\. *GIVEN: The player does not have an item in inventory*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Set `adventure.PLAYER["inventory"]` to an empty dictionary
   ```

{{ newrow }}

3\. *WHEN: You call do_consume() with that item*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_consume()` two arguments: `action`, and a list containing a string like `"something tasty"`
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

4\. *THEN: An error message should be printed*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an error message like {samp}`"Sorry, you don't have any 'something tasty' to {ACTION}."` is in `output`
   ```

{{ endcols }}

4\. Run your tests. They should fail.

`````

`````{dropdown} test_do_consume_not_in_inventory()

```{literalinclude} ../../../pythonclass/adventure/test_game-15.2.py
:linenos:
:lineno-match:
:pyobject: "test_do_consume_not_in_inventory"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `do_consume()`: check inventory

Now we'll modify `do_consume()` function to check that the player has the
current item in inventory. If not an error message will be printed and the
function will return.

`````{dropdown} Need help?

1. `[ ]` Join all items in `args` into a single string seperated by spaces, and make it lowercase. Assign it to the variable `name`.
1. `[ ]` Write an if statement that checks if the player has the item. If not:
    * `[ ]` Use the `error()` function to print a message like: \
      {samp}`"Sorry, you don't have any {name} to {action}."`
    * `[ ]` return

`````

`````{dropdown} do_consume()

```{literalinclude} ../../../pythonclass/adventure/adventure-15.2.py
:linenos:
:lineno-match:
:pyobject: "do_consume"
:emphasize-lines: "9-"
:caption: adventure.py

```

`````
