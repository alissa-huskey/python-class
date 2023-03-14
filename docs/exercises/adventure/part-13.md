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
Part 13: Health
===============

In this section we'll add player health between `1` - `100` with a health
progress bar on the inventory command.

Part 13.1: Add `health_change()`
--------------------------------

{{ sources.format("13.1") }}

In this section we'll start the `health_change()` function which will work very
much like `inventory_change()`. It should:

* Take one `int` argument: `amount`.
* Add the `amount` to `PLAYER["health"]`.

### A. In `test_game.py` define `test_health_change()`

Write the `test_health_change()` function to test `health_change()`.

`````{dropdown} Need help?
1. Import `health_change`
2. Add the function `test_health_change()`
3. *GIVEN: the player has health*

   Set `PLAYER["health"]` to a positive number between `1` - `100`
4. *WHEN: you call `health_change()` with a positive number*
5. *THEN: a positive number should be added to player health

   assert that `PLAYER["health"]` is now correct
6. Run your test. It should fail.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-13.1.py
:linenos:
:lineno-match:
:start-at: "from adventure import"
:end-at: ")"
:emphasize-lines: "7"
:caption: test_game.py

```

```{literalinclude} ../../../pythonclass/adventure/test_game-13.1.py
:linenos:
:lineno-match:
:start-at: "def test_health_change("
:end-before: def
:caption: test_game.py

```
`````

### B. In `adventure.py` define `health_change()`

Write the `health_change()` function.

`````{dropdown} Need help?
1. `[ ]` Add the function `health_change()` with one argument `amount`
2. `[ ]` Add `amount` to `PLAYER["health"]`
3. `[ ]` Run your tests. They should now pass.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.1.py
:linenos:
:lineno-match:
:start-at: "def health_change("
:end-before: "def"
:caption: adventure.py

```

`````

Part 13.2: Parameterize the test
--------------------------------

{{ sources.format("13.2") }}

In this section we'll modify the `test_health_change()` function to use
parametrization. This allows us to use the same test for several different
{term}`test cases` which are stored and run as a list of arguments to a single
test function.

If you're not already familiar with parameterization, see
[Pytest Tests > Parametrization][Parametrization].

[Parametrization]: ../practices/testing/pytest-tests.html#part-5-parametrization

{{ clear }}

### A. In `test_game.py` modify `test_health_change()`: parameterize

```{margin}

:::{seealso}

Pytest Tests > [Parametrization][]

:::

```

In this section we will extract the values that we expect to be different in
new test cases and turn them into four parameters and variables: `start`,
`amount`, `result` and `message`.

At the end of this section we will have a parameratized test with exactly one
test case representing the original test. Functionally, nothing will change but
we'll be set up to more easily add new test cases.

1. Change the following values to variables. (Either keep the original
   line commented out or otherwise make note the original values.)
    ```{code-block-hl} python
    :linenos:
    :caption: test_game.py

    def test_health_change():
        # GIVEN: The player has some health
        adventure.PLAYER["health"] = !!!50!!!

        # WHEN: You call health_change()
        health_change(!!!10!!!)

        # THEN: The player health should be adjusted
        assert adventure.PLAYER["health"] == !!!60!!!, \
          !!!"the player health should be adjusted"!!!
    ```
   * Under *GIVEN*: Change the value assigned to `PLAYER["health"]` to the variable `start`.
   * Under *WHEN*: Change the argument passed to `health_change()` the variable `amount`
   * Under *THEN*: In the assert statement change the value that should equal
     `PLAYER["health"]` to the variable `result`
   * Under *THEN*: Change the assert message to the variable `message`

     If you don't already have an assert message add one that is similar to the
     *THEN* description. ie:

     `"a positive number should be added to player health"`
2. Add the four variables (`start`, `amount`, `result`, `message`) as
   parameters to the `test_health_change()` function
3. Immediately above the `def` line call `@pytest.mark.parametrize()` with the
   following arguments:
    * A list containing the name of all four variables in the same order as above
    * A list of tuples with each tuple on its own line
      * The first tuple should contain the values extracted from step #1 in
        the same order as their cooresponding parameters:
          `start`, `amount`, `result`, `message`.
4. Change your *GIVEN*/*WHEN*/*THEN* comments to be more generic so that they
   can apply to all test cases. For example, change:

   `# THEN: The amount should be added to player health`

   To:

   `# THEN: The player health should be adjusted`
5. Run your test. It should pass.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-13.2.A.py
:linenos:
:lineno-match:
:start-at: "@pytest.mark.parametrize"
:end-at: "assert"
:caption: test_game.py

```

`````

### B. In `test_game.py` above `test_health_change()`: Add another test case

In this section we are going to add a test case for passing a negative value to
`health_change()` to effectively subtract that amount from player health.

If we were to write this as a non-parameratized test it would look something
like:

```{code-block-hl} python
:linenos:
:lineno-start: 64
:caption: test_game.py

def test_health_change_subtract():
    # GIVEN: The player has some health
    adventure.PLAYER["health"] = !!!50!!!

    # WHEN: You call health_change() with a negative value
    health_change(!!!-10!!!)

    # THEN: The amount should be subtracted from player health
    assert adventure.PLAYER["health"] == !!!-40!!!, \
        !!!"a negative number should be subtracted from player health"!!!
```


Instead of writing this test though, we will add a test case tuple that
contains the `start`, `amount`, `result` and `message` values that we would
otherwise put in a `test_health_change_subtract()` test.

1. `[ ]` Add a new tuple to the list of test case tuples that contains values
         for each of the four parameters:

   | Parameter | Value                             |
   |-----------|-----------------------------------|
   | `start`   | a positive `int`                  |
   | `amount`  | a negative `int`                  |
   | `result`  | `start` - `amount`                |
   | `message` | a `str` describing this test case |
1. `[ ]` Run your test. It should pass.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-13.2.py
:linenos:
:lineno-match:
:start-at: "@pytest.mark.parametrize"
:end-at: "assert"
:emphasize-lines: "4"
:caption: test_game.py

```

`````

Part 13.3: Add health limits
----------------------------

In this section we're going to modify the `health_change()` function so that
`PLAYER["health"]` is always between `0` and `100`.

### A. In `test_game.py` above `test_health_change()`: ensure health > 0

In this section we will add a test case to ensure that even if `start` - `amount` is
less than zero, player health is set to zero instead of a negative number

If we were to write this as a non-parameratized test, it would look something like:

`````{dropdown} test_health_change_minimum_health()

```{code-block-hl} python
:linenos:
:lineno-start: 64
:caption: test_game.py

def test_health_change_minimum_health():
    # GIVEN: The player has some health
    adventure.PLAYER["health"] = !!!20!!!

    # WHEN: You call health_change() with a negative number
    #       which would make player health less than zero
    health_change(!!!-30!!!)

    # THEN: The player health should be zero
    assert adventure.PLAYER["health"] == !!!0!!!, \
        !!!"the minimum health should be 0"!!!
```

`````

1. `[ ]` Add a new tuple to the list of test case tuples that contains values
         for each of the four parameters:

   | Parameter | Value                                                        |
   |-----------|--------------------------------------------------------------|
   | `start`   | a positive `int`                                             |
   | `amount`  | a negative `int` that would make player health less than `0` |
   | `result`  | `0`                                                          |
   | `message` | a `str` describing this test case                            |
2. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-13.3.py
:linenos:
:lineno-match:
:start-at: "@pytest.mark.parametrize"
:end-before: "MAX_HEALTH"
:emphasize-lines: "5"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `health_change()`

In this section we will modify `health_change()` to make the above test case
pass.

1. `[ ]` At the end of the function, after `PLAYER["health"]` is changed, check
   if `PLAYER["health"]` is less than zero
    * `[ ]` if so, set `PLAYER["health"]` to zero
2. `[ ]` Run your tests. They should pass

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.3.py
:linenos:
:lineno-match:
:start-at: "def health_change"
:end-before: "cap health"
:emphasize-lines: "5-7"
:caption: adventure.py

```

`````

### C. At the top of `adventure.py`

In this section we'll add a global variable `MAX_HEALTH` to keep track of the
maximum value for `PLAYER["health"]`.

1. `[ ]` Add global variable `MAX_HEALTH` and set it to `100`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.3.py
:linenos:
:lineno-match:
:start-at: "import"
:end-before: "# Game World Data"
:emphasize-lines: 11
:caption: adventure.py

```

`````

### D. In `test_game.py` above `test_health_change()`: ensure `MAX_HEALTH`

In this section we'll add a test case to ensure that even if `start` + `result`
is greater than `MAX_HEALTH`, player health will be set to `MAX_HEALTH`.

If we were to write this as a non-parameratized test it would look something
like:

`````{dropdown} test_health_change_maximum_health()

```{code-block-hl} python
:linenos:
:lineno-start: 64
:caption: test_game.py

def test_health_change_maximum_health():
    # GIVEN: The player has some health
    adventure.PLAYER["health"] = !!!90!!!

    # WHEN: You call health_change() with a positive number
    #       which would make player health more than the maximum
    health_change(!!!20!!!)

    # THEN: The player health should be MAX_HEALTH
    assert adventure.PLAYER["health"] == !!!MAX_HEALTH!!!, \
        !!!f"the maximum health should be {MAX_HEALTH}"!!!
```

`````

1. `[ ]` Import `MAX_HEALTH`
2. `[ ]` Add a new tuple to the list of test case tuples that contains values
         for each of the four parameters:

   | Parameter | Value                                                          |
   |-----------|----------------------------------------------------------------|
   | `start`   | a positive `int`                                               |
   | `amount`  | a positive `int` that would make player health more than `100` |
   | `result`  | `MAX_HEALTH`                                                   |
   | `message` | a `str` describing this test case                              |
3. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-13.3.py
:linenos:
:lineno-match:
:start-at: "from adventure import"
:end-at: ")"
:emphasize-lines: "15"
:caption: test_game.py

```

```{literalinclude} ../../../pythonclass/adventure/test_game-13.3.py
:linenos:
:lineno-match:
:start-at: "@pytest.mark.parametrize"
:end-at: "def test_"
:emphasize-lines: "6"
:caption: test_game.py

```

`````

### E. In `adventure.py` modify `health_change()`

In this section we will modify `health_change()` to make the above test case
pass.

1. `[ ]` At the end of the function, check if `PLAYER["health"]` is greater
         than `MAX_HEALTH`
    * `[ ]` if so, set `PLAYER["health"]` to `MAX_HEALTH`
2. `[ ]` Run your tests. They should pass

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.3.py
:linenos:
:lineno-match:
:start-at: "def health_change"
:end-before: "def"
:emphasize-lines: "9-11"
:caption: adventure.py

```

`````

Part 13.4: UX Changes
---------------------

In this section we'll add a few changes to integrate health with the game
itself.

### A. In `adventure.py` modify `PLAYER`

1. `[ ]` Add a `"health"` key to the `PLAYER` dictionary with a value of `100`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.4.py
:linenos:
:lineno-match:
:start-at: "PLAYER ="
:end-before: "PLACES"
:emphasize-lines: "4"
:caption: adventure.py

```

`````

### B. At the top of `adventure.py`: Add ProgressBar

`````{margin}

```{seealso}

* [Console Docs](https://mixmastamyk.bitbucket.io/console/additional.html#progress-bars)

```

`````

We're going to use the progress bar feature of the
[console](https://github.com/mixmastamyk/console) library to add a health bar
to the inventory command.

In this section we'll add a global variable `BAR` which will be set to a
`ProgressBar()` object. We'll use this later to print the progress bar.

1. `[ ]` Import `ProgressBar` from `console.progress`
2. `[ ]` Create a new global variable `BAR` and set it to a new `ProgressBar()`
         object with the following keyword arguments:

   | Keyword      | Value                                 | Why                                                                        |
   |--------------|---------------------------------------|----------------------------------------------------------------------------|
   | `total`      | `MAX_HEALTH + 0.1`                    | prevent dimming of bar at `100%`                                           |
   | `clear_left` | `False`                               | prevent removal of `"Health "` text to left of bar                         |
   | `width`      | `WIDTH - len("Health") - len("100%")` | make bar width `WIDTH` minus the length of the other text on the same line |
   |              |                                       |                                                                            |


:::{note}

From the command line you can run `python -m console.progress` to see a demo of
the various progress bar styles.

Feel free to play around and pick your own style.

:::

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.4.py
:linenos:
:lineno-match:
:start-at: "import"
:end-before: "# Game World Data"
:emphasize-lines: "4, 14-18"
:caption: adventure.py

```

`````

### C. In `adventure.py` define `health_bar()`

In this section we'll add a function `health_bar()` which will print the health bar.

1. `[ ]` Write a function `health_bar()`
2. `[ ]` In use the `write()` command to print:
    * `[ ]` `"Health"`
    * `[ ]` the value returned when you call `BAR()` and pass the argument `PLAYER["health"]`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.4.py
:linenos:
:lineno-match:
:start-at: "def health_bar"
:end-before: "# Data functions"
:caption: adventure.py

```

`````

### D. In `adventure.py` modify `do_inventory()`

In this section we'll call `health_bar()` in the `do_inventory()` function to
print the health bar.

{{ left }}

1. `[ ]` At the beginning of `do_inventory()` call `health_bar()`

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-13.4.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.4.py
:linenos:
:lineno-match:
:start-at: "def do_inventory"
:end-before: "def"
:emphasize-lines: 6
:caption: adventure.py

```

`````


### E. In `adventure.py` modify `main()`

In this section we'll quit the game if player health is out of health.

1. `[ ]` At the very end of the `main()` function, check to make sure that the player still has health
2. `[ ]` If not print something like `"Game over"` and call `quit()`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-13.4.py
:linenos:
:lineno-match:
:start-at: "def main"
:end-before: "if __name__"
:emphasize-lines: "53-"
:caption: adventure.py

```

`````
