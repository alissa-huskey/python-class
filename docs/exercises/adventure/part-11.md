---
substitutions:
  testsource: '{{{{ source | format("test_game-{0}") }}}}'

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
Part 11: Test things
====================

```{margin}

:::{seealso}

[][testing]
:::

```

In this section we'll add a read command, which the player will use to read a
clue from the book.

Since our program is starting to get complicated, we'll also start writing
tests. This will help us find out if we break something, even if we don't
happen to play the part of the game that triggers it. Be sure to do the
[Testing Lesson][testing] if you haven't already.

Part 11.1: Setup
----------------

{{ testsource.format("11.1.py") }}

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

### A. Install `pytest`

1. `[ ]` Install `pytest` using the instructions
         [here](/practices/testing.html#part-3-pytest).
1. `[ ]` To make sure it works, type `pytest --help` in the terminal.

### B. Configure VS Code

1. `[ ]` Configure VS Code by following the first two steps
         [here](/practices/testing.html#part-6-testing-in-vs-code). When you are
         prompted to select the directory containing the tests, choose
         {guilabel}`. Root directory`.
1. `[ ]` Install the extension [Python Test Explorer for Visual Studio Code][test-explorer].
         either from the marketplace or by typing the following into the terminal.

   ```console
   code --install-extension littlefoxteam.vscode-python-test-adapter
   ```
1. `[ ]` You may need to restart vscode.

[test-explorer]: https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter

### C. Prepare for import

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


### D. Create and run tests

{{ left }}

1. `[ ]` Create a new file named `test_game.py`
1. `[ ]` In it, import your module with something like `import adventure`
1. `[ ]` Write a function called `test_truth()`
   * `[ ]` In it, write a simple assert statement `assert True`
1. `[ ]` Run your test by typing `pytest -v test_game.py` in the terminal.

{{ right }}

`````{dropdown} Code
:open:

```{literalinclude} ../../../pythonclass/adventure/test_game-11.1.py
:linenos:
:caption: test_game.py
```

`````

{{ endcols }}

You can add the following to your `pyproject.toml` to always run `pytest` in verbose mode.

```{code-block} toml
:caption: pyproject.toml

[tool.pytest.ini_options]
addopts = "-v"
```

### E. Run tests in vscode

```{margin}

:::{seealso}
Testing > [Running Tests](/practices/testing/intro.html#part-6-2-running-tests)
:::

```

1. `[ ]` Click the {guilabel}`Testing` icon (that looks like a test beaker)
1. `[ ]` You may need to click the {guilabel}`Refresh Tests` icon (that looks
         like a arrow in a circle) to find your tests.
1. `[ ]` Click the {guilabel}`Run Tests` icon (that looks like a play button).


Part 11.2: Test `is_for_sale()`
-------------------------------

{{ testsource.format("11.2.py") }}

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

### A. Define `test_is_for_sale()`

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.2.py
:linenos:
:caption: test_game.py
:end-before: 'def test_is_for_sale_without_price'
```

`````

### B. Define `test_is_for_sale_without_price()`

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.2.py
:linenos:
:caption: test_game.py
```

`````

Part 11.3: Test `error()`
-------------------------

{{ testsource.format("11.3.py") }}

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

### A. Define `test_error()`

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.3.py
:linenos:
:lineno-match:
:emphasize-lines: "1, 23-"
:caption: test_game.py
```

`````

Part 11.4: Test `debug()`
-------------------------

{{ testsource.format("11.4.py") }}

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

### A. Define `test_debug()`

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.4.py
:linenos:
:lineno-match:
:end-before: def
```

```{literalinclude} ../../../pythonclass/adventure/test_game-11.4.py
:linenos:
:lineno-match:
:start-at: 'def test_debug'
:caption: test_game.py
```

`````

Part 11.5: Test `header()` and `write()`
----------------------------------------

{{ testsource.format("11.5.py") }}

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.5.py
:linenos:
:lineno-match:
:start-at: 'def test_header'
:end-before: 'def'
:caption: test_game.py
```

`````


`````{dropdown} write()

```{literalinclude} ../../../pythonclass/adventure/test_game-11.5.py
:linenos:
:lineno-match:
:start-at: 'def test_write'
:caption: test_game.py
:caption: test_game.py
```

`````

Part 11.6: Test `inventory_change()`
------------------------------------

{{ testsource.format("11.6.py") }}

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

### A. Add teardown

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:end-before: "def test_"
:emphasize-lines: "1-5, 15-"
:caption: test_game.py
```

### B. Define `test_inventory_change()`

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change"
:end-before: def
:caption: test_game.py
```

`````

### C. Define `test_teardown()`

In this test we'll make sure that the teardown code from
[part A](#a-add-teardown) is working.

1. `[ ]` Add a `test_teardown()` function
1. `[ ]` Add an `assert` statement that the key you added in the previous test
         is not in `PLAYER["inventory"]` with a failure message like:

   `"Each test should start with a fresh data set."`
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change()"
:end-before: "def test_inventory_change_"
:emphasize-lines: "8-"
:caption: test_game.py
```

`````

### D. Define `test_inventory_change_missing_key()`

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change_missing_key()"
:end-before: def
:caption: test_game.py
```

`````

### E. Additional test cases

Can you add the next two tests on your own?

1. `[ ]` `inventory_change_subtract()` should use a negative number for the
         quantity argument and assert that that amount was subtracted from
         inventory
1. `[ ]` `inventory_change_remove()` should use a negative number for the
         quantity argument so that there will be `0` left and assert that the key was
         removed from inventory

`````{dropdown} test_inventory_change_subtract()

```{literalinclude} ../../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change_subtract()"
:end-before: def
:caption: test_game.py
```

`````

`````{dropdown} test_inventory_change_remove()

```{literalinclude} ../../../pythonclass/adventure/test_game-11.6.py
:linenos:
:lineno-match:
:start-at: "def test_inventory_change_remove()"
:caption: test_game.py
```

`````

Part 11.7: Test `do_drop()`
---------------------------

{{ testsource.format("11.7.py") }}

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

### A. Define `test_do_drop_no_args()`

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

```{literalinclude} ../../../pythonclass/adventure/test_game-11.7.py
:linenos:
:lineno-match:
:end-before: PLAYER
:emphasize-lines: "8, 13-14"

```

```{literalinclude} ../../../pythonclass/adventure/test_game-11.7.py
:linenos:
:lineno-match:
:start-at: "def test_do_drop_no_args"
:end-before: def
:caption: test_game.py

```

`````

### B. Define `test_do_drop_missing_item()`

This test will check that if the player tries to drop something they don't have
in inventory, they they get the appropriate error message.

1. `[ ]` Add the function `test_do_drop_missing_item()` with the parameter `capsys`
1. `[ ]` Set `adventure.PLAYER["inventory"]` to an empty dictionary.
1. `[ ]` Call `do_drop()` with a list containing an any string as an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that the appropriate debug message is in `output`
1. `[ ]` Write an assert statement that the appropriate error message is in `output`
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-11.7.py
:linenos:
:lineno-match:
:start-at: "def test_do_drop_missing_item"
:end-before: def
:caption: test_game.py

```

`````


#### C. Define `test_do_drop()`

This test will successfully drop something, then make sure that it was added to
the place and removed from inventory.

1. `[ ]` Add the function `test_do_drop()` with the parameter `capsys`
1. `[ ]` Call the `inventory_change()` function with the key of your choice to
         add a fake item to inventory
1. `[ ]` Call `do_drop()` with a list containing the key as an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that the appropriate debug message is in `output`
1. `[ ]` Write an assert statement that the appropriate message is in `output`
1. `[ ]` Write an assert statement that calls the `place_has()` function with
         the key to make sure the item was added to the place.
1. `[ ]` Write an assert statement that calls the `player_has()` function with
         the key to make sure the item is not in inventory.
1. `[ ]` Run your tests, either at the command line or in VS Code.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-11.7.py
:linenos:
:lineno-match:
:start-at: "def test_do_drop("
:caption: test_game.py

```

`````

### And the rest

We've held off on writing tests until now because I felt you needed more
experience coding before adding another potentially confusing component.
Ideally though, you want to write your tests at the same time you write the
corresponding code. As you can see, back-filling can be a drudge.

Unless you're excited about writing all of your tests now, I'd recommend adding
a test at the beginning of each coding session and whenever something breaks.

Going forward we'll be writing tests for all of our new code, and running them
regularly.

[testing]: /practices/testing/intro
