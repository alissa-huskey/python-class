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

Part 15.3: Is the item consumable?
----------------------------------

{{ sources.format("15.3") }}

{{ left }}

In this section we'll check to make sure the item can be eaten or drunk, based
on if it has a `"eat-message"` or `"drink-message"` key.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-15.3.cast
:poster: npt:0:06
```

`````

{{ endcols }}


### A. In `test_game.py` define `test_do_consume_cant_consume()`

In this section we'll write a parametrized test which we expect to fail. It
will have one parameter `action` with the two cases `"eat"` and `"drink"`.

The function should test that if the player tries to eat or drink an item that
does not have a {samp}`"{action}-message"` key an error message will be printed.

`````{dropdown} Need help?

{{ left }}

1\. Define a parametrized `test_do_consume_cant_consume()` function

{{ br }}

{{ right }}

   ```{dropdown} ...
    1. `[ ]` Add `test_do_consume_cant_consume()` function with two parameters: `capsys` and `action`.
    1. `[ ]` Immediately above the `def` line call `@pytest.mark.parametrize()` with the
      following arguments:
        * The string `"action"`
        * A list that contains the strings `"eat"` and `"drink"`
   ```

{{ newrow }}

2\. *GIVEN: An item exists with no eat-message or drink-message key*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Create a fake item in `adventure.ITEMS` with a key like `"something tasty"`. The value should be a dictionary containing:
      - `[ ]` the key `"name"` and a value like `"something tasty"`
   ```

{{ newrow }}

3\. *AND: That item is in the player's inventory*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Add the item to the player's inventory
   ```

{{ newrow }}

4\. *WHEN: You call do_consume() with that item*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_consume()` with two arguments: `action`, and a list containing the key to your fake item, ie `"something tasty"`
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

4\. *THEN: An error message should be printed*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an error message like {samp}`"Sorry, you can't {action} 'something tasty'."` is in `output`
   ```

{{ endcols }}

4\. Run your tests. They should fail.

`````

`````{dropdown} test_do_consume_cant_consume()

```{literalinclude} ../../../pythonclass/adventure/test_game-15.3.py
:linenos:
:lineno-match:
:pyobject: "test_do_consume_cant_consume"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `do_consume()`: check item

Now we'll modify `do_consume()` function to check to make sure the item can be
eaten or drunk, based on if it has a `"eat-message"` or `"drink-message"` key.
If not an error message will be printed and the function will return.

`````{dropdown} Need help?

1. `[ ]` Get the item using by calling `get_item()` with the argument `name` and assign the result to the variable `item`.
1. `[ ]` Write an if statement that checks if the key {samp}`"{action}-message"` is in the `item` dictionary. If not:
    * `[ ]` Use the `error()` function to print a message like: \
      {samp}`"Sorry, you can't {action} '{name}'.'"`
    * `[ ]` return
1. `[ ]` Run your tests. They should pass.

`````

`````{dropdown} do_consume()

```{literalinclude} ../../../pythonclass/adventure/adventure-15.3.py
:linenos:
:lineno-match:
:pyobject: "do_consume"
:emphasize-lines: "17-"
:caption: adventure.py

```

`````

Part 15.4: Modify `health_change()`
----------------------------------

{{ sources.format("15.4") }}

In this section we're going to modify the `health_change()` function so that it
returns the amount that health was actually changed, which may be different
than the `amount` argument.

This is so that if, for example, the player's health is at `90` and they
drink a potion that is `+20` health, we can tell the player that they
gained `10` health points.

### A. In `test_game.py` modify `test_health_change()`

In this section, we'll add a parameter `diff` to the parametrization of the
`test_health_change()` function. Then we'll need to save the result of calling
`health_change()` and assert that it is equal to `diff`.

(You may also want to rename `result` to `health`, so we can use the variable
name `result` for the returned value.)

`````{dropdown} Need help?

1. `[ ]` Change the name `result` to `health` in:
  - The first argument to `@pytest.mark.parametrize`
  - The parameters to the `test_health_change()` function
  - The assert statement
1. `[ ]` Add a parameter `diff` to:
  - The first argument to `@pytest.mark.parametrize`
  - The parameters to the `test_health_change()` function
1. `[ ]` Add a number for `diff` to each of the parametrization tuples, which
    should be the difference between their start health and end health.
1. `[ ]` Assign the value returned from of `health_change()` to the variable `result`
1. `[ ]` In the `THEN` section, add: *AND: The value returned should be the difference in points* \
  - assert that `result` is equal to `diff`
1. Run your tests. They should fail.

`````

`````{dropdown} test_health_change()

```{literalinclude} ../../../pythonclass/adventure/test_game-15.4.py
:linenos:
:lineno-match:
:pyobject: "test_health_change"
:caption: test_game.py
:emphasize-lines: "1-9, 14, 17, 19-"

```

`````

### B. In `adventure.py` modify `health_change()`: return difference

Now we'll modify the `health_change()` function to return the difference
between the player's health before and after it is changed.

`````{dropdown} Need help?

1. `[ ]` At the beginning of the function, save the value of `PLAYER["health"]` to the variable `before`.
1. `[ ]` At the end of the function return the result of subtracting `before` from `PLAYER["health"]`

`````

`````{dropdown} health_change()

```{literalinclude} ../../../pythonclass/adventure/adventure-15.4.py
:linenos:
:lineno-match:
:pyobject: "health_change"
:emphasize-lines: "5-6, 19-"
:caption: adventure.py

```

`````

Part 15.5: Print message with delay
-----------------------------------

{{ sources.format("15.5") }}

{{ left }}

In this section we're going to print the eat or drink message.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-15.5.cast
:poster: npt:0:09
```

`````

{{ endcols }}

### A. In `test_game.py` define `test_do_consume()`

In this section we'll write a `test_do_consume()` function.

The function should test that when a player tries to eat or drink a consumable
item, the `"eat-message"` or `"drink-message"` is printed.

We'll parameratize the test with the parameters `action` (`"eat"`" or
`"drink`), and `item` (a dictionary to add to `adventure.ITEMS`).

:::{tip}

You can set `adventure.WIDTH` to extra wide to avoid wrapping. That way when
you assert `"some string" in ouput` you can be sure that all words are on the
same line.

:::

`````{dropdown} Need help?

1\. Define a parametrized `test_do_consume()` function.

{{ br }}

```{dropdown} ...
1. `[ ]` Add `test_do_consume()` function with four parameters: `capsys`, `action`, and `item`.
1. `[ ]` Immediately above the `def` line call `@pytest.mark.parametrize()` with the
  following arguments:
    * The string `"action, item"`
    * A list of tuples with each tuple on its own line, with values for:
      - `action`: `"eat"` or `"drink"`
      - `item`: a dictionary for the fake item to add to `adventure.ITEMS`.
         it should include keys for: `"name"`, `"health"`, and `"eat-message"`
         or `"drink-message"`

1. `[ ]` Make two tuples, one for `"eat"` and one for `"drink"`.
```

2\. *GIVEN: An item exists*

{{ br }}

```{dropdown} ...
* `[ ]` Assign the variable `name` to the value `item["name"]`
* `[ ]` Create a fake item in `adventure.ITEMS` with the key `name`. The
  value should be the `item` dictionary (from params).
```

3\. *AND: The player has the item in their inventory*

```{dropdown} ...
* `[ ]` Call `inventory_change()` with the argument `name`
```

4\. *AND: The width is set wide to avoid wrapping*


```{dropdown} ...
* `[ ]` set `adventure.WIDTH` to a large number like `200`
```

5\. *WHEN: You call do_consume() with that item*


```{dropdown} ...
* `[ ]` call `do_consume` with the arguments `action`, and a list
  containing the item `name`.
* `[ ]` assign the varible `output` to the results of calling `capsys.readouterr().out`
```

6\. *THEN: The message contents should be in output*


```{dropdown} ...
* `[ ]` assign the varible `line` to the first item in the
  `item[f"{action}-message"] tuple`
* `[ ]` assert that `line` is in output
```

7\. Run your tests. They should fail.

`````

`````{dropdown} test_do_consume()

```{literalinclude} ../../../pythonclass/adventure/test_game-15.5.py
:linenos:
:lineno-match:
:pyobject: "test_do_consume"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `do_consume()`, at the end

In this section we'll modify the `do_consume()` function to wrap and print each
item in the `"eat-message"` or `"drink-message"` and then sleep.

`````{dropdown} Need help?

1. `[ ]` print a blank line
1. `[ ]` Iterate over `item[f"{action}-message"]` with the variable `sentence`.
   In the for loop:
   * `[ ]` print `sentence` by calling the `wrap()` function
   * `[ ]` print a blank line
   * `[ ]` sleep for `DELAY` seconds
1. `[ ]` Run your tests. They should pass.

`````

`````{dropdown} do_consume()

```{literalinclude} ../../../pythonclass/adventure/adventure-15.5.py
:linenos:
:lineno-match:
:pyobject: "do_consume"
:caption: adventure.py
:emphasize-lines: "24-"

```

`````

### C. In `adventure.py` modify `ITEMS` and `PLACES`

In this section we'll add or modify items in `ITEMS` to include an
`"eat-message"` or `"drink-message"` key. Then if needed we'll add those items
to `PLACES`.

`````{dropdown} ITEMS

```{literalinclude} ../../../pythonclass/adventure/adventure-15.5.py
:linenos:
:lineno-match:
:start-at: "ITEMS ="
:end-before: "# Message functions"
:caption: adventure.py
:emphasize-lines: "7-16, 24-49"

```

`````

`````{dropdown} PLACES

```{literalinclude} ../../../pythonclass/adventure/adventure-15.5.py
:linenos:
:lineno-match:
:start-at: "PLACES ="
:end-before: "ITEMS ="
:caption: adventure.py
:emphasize-lines: "7, 47"

```

`````

Part 15.6: Consume
------------------

{{ sources.format("15.6") }}

{{ left }}

In this section we'll make sure that when you eat or drink something it is
removed from inventory and your health is changed accordingly.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-15.6.cast
:poster: npt:0:10
```

`````

{{ endcols }}

### A. In `test_game.py` modify `test_do_consume()`

In this section we'll modify the `test_do_consume()` function to test that the
player's health and inventory has changed and that a message is printed to tell
them so.

In order to do so we'll add two parameters to the test: `health` (for the
player's health after consuming) and `message` for the text that will be
printed about the change.

`````{dropdown} Need help?

1\. Modify `test_do_consume()` to add parameters for `health` and `message`.

{{ br }}

````{dropdown} ...
1. `[ ]` In the first argument of `@pytest.mark.parametrize()` add the
parameters `"health, message"` to the end of the string.
1. `[ ]` Add values for each tuple:
   * A number like `55`, for the amount of health the player will have after
     consuming the item
   * A string like `"lost 5"` for part of the text that the player will see
1. `[ ]` In the definition of `test_do_consume()` add the parameters `health`
   and `message`.
````

2\. `[ ]` Under *GIVEN* add : *AND: The player has a certain amount of health*

````{dropdown} ...
`[ ]` Set `adventure.PLAYER["health"]` to a specific number like `50`
````

3\. `[ ]` Under *THEN* add : *The player's health should be changed*

````{dropdown} ...
`[ ]` Assert that `adventure.PLAYER["health"]` equals `health`
````

4\. `[ ]` Under *THEN* add : *The item should be removed from inventory*

````{dropdown} ...
`[ ]` Assert that the player does not have `name`
````

5\. `[ ]` Under *THEN* add : *A message about the action take should be printed*

````{dropdown} ...
`[ ]` Assert that `f"You {message} point"` is not in `output`
````

6\. `[ ]` Run your tests. They should fail.

`````

`````{dropdown} test_do_consume()

```{literalinclude} ../../../pythonclass/adventure/test_game-15.6.py
:linenos:
:lineno-match:
:pyobject: "test_do_consume"
:caption: test_game.py
:emphasize-lines: "2, 13-14, 26-27, 31, 39-41, 55-"

```

`````

### B. In `adventure.py` modify `do_consume()`

In this section we'll modify the `do_consume()` function so that it removes the
item from inventory, modifies the player's health, and prints a message about
what happened.

`````{dropdown} Need help?

1. `[ ]` Call `inventory_change()` with the arguments `name` and `-1`.
1. `[ ]` Call `item.get()` with the arguments `"health"` and `0` and assign the
         returned value to the variable `health`.
1. `[ ]` Call `health_change()` with the argument `health` and assign the
         returned result to the variable `difference`.
1. `[ ]` If `health` is greater than zero:
    * `[ ]` Print a message like: \
    * {samp}`"You lost {POINTS} point(s)."`
1. `[ ]` Otherwise, if `health` is less than zero:
    * {samp}`"You gained {difference} point(s)."`
1. `[ ]` Run your tests. They should pass.

`````

`````{dropdown} do_consume()

```{literalinclude} ../../../pythonclass/adventure/adventure-15.6.py
:linenos:
:lineno-match:
:pyobject: "do_consume"
:caption: adventure.py
:emphasize-lines: "25-27, 35-"

```

`````

### C. In `adventure.py` modify `ITEMS`

In this section we'll modify any of the item dictionaries in `ITEMS` that have
a `"eat-message"` or `"drink-message"` key to add a `"health"` key. The value
should be the number of health points to add or remove.

Play your game and eat or drink the relevant items to test it out!


`````{dropdown} ITEMS

```{literalinclude} ../../../pythonclass/adventure/adventure-15.6.py
:linenos:
:lineno-match:
:start-at: "ITEMS ="
:end-before: "# Message functions"
:caption: adventure.py
:emphasize-lines: "17, 37, 51"

```

`````

Part 15.7: Add health to examine
--------------------------------

{{ sources.format("15.7") }}

{{ left }}

In this section we'll add health to the examine command.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-15.7.cast
:poster: npt:0:04
```

`````

{{ endcols }}

### A. In `test_game.py` add `test_examine()`

In this section we'll add a test for the `do_examine()` function if it does not
already exist. Then we'll modify the test to make sure that the health is
displayed.

`````{dropdown} Need help? (skip if test_do_examine is defined)

1\. Import `do_examine`

2\. Define the `test_do_examine()` function and include the `capsys` fixture.

{{ br }}

````{dropdown} ...
`[ ]` Define `test_do_examine()` with the parameter `capsys`
````

3\. `[ ]` *GIVEN: An item exists*

````{dropdown} ...
* `[ ]` Create a dictionary for a fake item and assign it to the variable `item`.
      The dictionary should include keys for: `"name"`, `"description"` and
      `"price"`.
* `[ ]` Add the `item` to the `adventure.ITEMS` dictionary
````

4\. `[ ]` *AND: A place has the item*

````{dropdown} ...
`[ ]` Add a fake place to the `adventure.PLACES` dictionary. It should include
      keys for `"name"` and `"items"`. Make sure to add the fake item to the place.
````

5\. `[ ]` *AND: The player is that place*

````{dropdown} ...
`[ ]` Modify `adventure.PLAYER` to put the player in your fake place.
````

6\. `[ ]` *WHEN: do_examine() is called*

````{dropdown} ...
* `[ ]` Call `do_examine()` with a list containing the key to your fake item.
* `[ ]` Assign the variable `output` to the result of calling `capsys.readouterr().out`
````

7\. `[ ]` *THEN: a debug message should be printed*

````{dropdown} ...
`[ ]` Assert that a string like `"Trying to examine: ['cookie']"` is in `output`
````

8\. `[ ]` *AND: The item name should be printed*

````{dropdown} ...
`[ ]` Assert that `item["name"]` is in `output`
````

9\. `[ ]` *AND: The item description should be printed*

````{dropdown} ...
`[ ]` Assert that `item["description"]` is in `output`
````

10\. `[ ]` *AND: The price should be printed*

````{dropdown} ...
`[ ]` Assert that a string like `"5 gems"` is in `output`
````

11\. `[ ]` Run your tests. They should pass.

`````

`````{dropdown} Need help?

1\. `[ ]` Modify: *GIVEN: An item exists* to add `"health"`

{{ br }}

````{dropdown} ...
`[ ]` Modify your fake item dictionary to include a key for `"health"`
````

2\. `[ ]` Under *THEN* add : *AND: The health points should be printed*

````{dropdown} ...
`[ ]` Assert that a string like `"+5 health"` is in `output`
````

3\. `[ ]` Run your tests. They should fail.

`````

`````{dropdown} test_do_examine()

```{literalinclude} ../../../pythonclass/adventure/test_game-15.7.py
:linenos:
:lineno-match:
:pyobject: "test_do_examine"
:caption: test_game.py
:emphasize-lines: "6, 41-"

```

`````

### B. In `adventure.py` modify `do_examine()`

In this section we'll modify the `do_examine()` function to print the health
gained or lost from an item, if any.

In my examine display I have the item price, inventory quantity, and health all
on the same line, right aligned.

To accomplish this I put them all in a list named `stats`, then joined them
with the `|` character, then called `.rjust()` on the result to print it.
Depending how you want to format your examine output, you may or may not want
to do it the same way.

`````{dropdown} Need help?

1. `[ ]` Create an empty list assigned to the variable `stats`.
1. `[ ]` If the place can `"shop"` and the place has the item and the item is for sale:
   * `[ ]` Append a string like {samp}`"Price: {PRICE} gems"` to `stats`.
1. `[ ]` Otherwise, if the item is in the player's inventory:
   * `[ ]` Append a string like {samp}`"(x {QUANTITY})"` to `stats`.
1. `[ ]` If the item has a `"health"` key:
   * `[ ]` Append a string like {samp}`"+{HEALTH} health"` to `stats`
1. `[ ]` If the `stats` list is not empty:
   * `[ ]` Assign the variable `text` to the `stats` list joined by a string like: \
     `" | "`.
   * `[ ]` Call the `.rjust()` method with the argument `WIDTH - MARGIN` and print it.
   * `[ ]` Print a blank line.
1. `[ ]` Run your tests. They should pass.

`````

`````{dropdown} do_examine()

```{literalinclude} ../../../pythonclass/adventure/adventure-15.7.py
:linenos:
:lineno-match:
:pyobject: "do_examine"
:caption: adventure.py
:emphasize-lines: "22-35, 40-44"

```

`````
