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
Part 12: Read things
====================

In this section we'll add the read command, which the player can use to read a
clue from the book item.

In this section we'll also start following an approach to coding called
{term}`TDD`, or {term}`Test-Driven Development`. When following this process,
you write your test first, then write the code that makes it pass.

This technique has many advantages. You are forced to be very deliberate about
exactly what you are trying to accomplish, which tends to lead to clearer
thinking and cleaner code. You can be more confident that your code is working
as intended and that it won't break in the future without you noticing.

Part 12.1: Add command
----------------------

{{ sources.format("12.1") }}

In this section we'll be adding the read command.

### A. In `test_game.py` define `test_do_read()`

{{ left }}

First we'll write the test, which we expect to fail.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.1.A.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Import the `do_read` function
1. `[ ]` Add `test_do_read()` function with one parameter `capsys`
1. `[ ]` Call `do_read()` with an empty list as an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that checks that the debug message
         `"Trying to read: []"` is in `output`
1. `[ ]` Run your tests, either at the command line or in VS Code. Since we
         haven't written `do_read()` yet, you will get an error.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.1.py
:linenos:
:lineno-match:
:end-before: PLAYER
:emphasize-lines: "9"

```

```{literalinclude} ../../../pythonclass/adventure/test_game-12.1.py
:linenos:
:lineno-match:
:start-at: "def test_do_read("
:caption: test_game.py

```

`````

### B. In `adventure.py` define `do_read()`

{{ left }}

Now we'll write the code to make it work.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.1.B.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

{{ left }}

1. `[ ]` Add a `do_read()` function with one parameter `args`
1. `[ ]` In it, use the `debug()` function to print something like {samp}`"Trying to read {args}."`.
1. `[ ]` Run your test again. It should now pass.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.1.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:caption: adventure.py

```

`````

{{ endcols }}

### C. In `adventure.py` modify `main()`

{{ left }}

Finally, we'll add the code to make the command work in the game.

1. `[ ]` Add an `elif` that checks if `command` is `"read"`.
   * `[ ]` if so, call `do_read()` and pass `args`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.1.cast
:poster: npt:0:02
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.1.py
:linenos:
:lineno-match:
:start-at: def main()
:end-before: 'if __name__'
:emphasize-lines: "37-38"
```

`````

Part 12.2: Ensure item
----------------------

{{ sources.format("12.2") }}

{{ left }}

In this section we'll make sure that the player entered the item that they want
to read.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.2.cast
:poster: npt:0:02
:speed: 0.75
:rows: 16
```

`````

{{ endcols }}

### A. In `test_game.py` modify `test_do_read()`

{{ left }}

Now we'll add an assertion to check the output for an error message.

1. `[ ]` Change the name of `test_do_read()` to `test_do_read_no_args()`
1. `[ ]` Add an assertion that checks if `"Error What do you want to read?"` is
         in `output`
1. `[ ]` Run your test. It should fail.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.2.A.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.2.py
:linenos:
:lineno-match:
:start-at: "def test_do_read_no_args"
:caption: test_game.py
:emphasize-lines: "9-"

```

`````

### B. In `adventure.py` modify `do_read()`

{{ left }}

Now we'll write the code to make our test pass.

1. `[ ]` Check if `args` is falsy. If it is, use the `error()` function to
         print an error that says: `"What do you want to read?"` then `return`
1. `[ ]` Run your test again. It should pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.2.B.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.2.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:caption: test_game.py
:emphasize-lines: "6-"

```

`````

Part 12.3: Ensure item is here
------------------------------

{{ sources.format("12.3") }}

{{ left }}

In this section we'll make sure the item that the player typed is either in
this place or in inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.3.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

### A. In `test_game.py` define `test_do_read_missing_item()`

{{ left }}

In this section we'll write a new test to make sure that the item is either in
this place or in inventory.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.3.A.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add `test_do_read_missing_item()` function with the parameter `capsys`
1. `[ ]` Call `do_read()` with a list and a any string that is not an item key for an argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that checks that the debug message
         `"Trying to read: []"` is in `output`
1. `[ ]` Write an assert statement that checks that the message
         `"Sorry, I don't know what this is'"` is in `output`
1. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.3.py
:linenos:
:lineno-match:
:start-at: "def test_do_read_missing_item"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `do_read()`

{{ left }}

Now we'll add the code to make the test pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.3.B.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` assign the first item of the `args` list to the variable `name` and make it lowercase
1. `[ ]` Write an if statement that checks if either the place or player has the item. If not:
   * `[ ]` Use the `error()` function to print a message like: {samp}`"Sorry, I don't know what this is: {name}'"`
   * `[ ]` return
1. `[ ]` Run your test again. It should pass.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.3.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:caption: adventure.py
:emphasize-lines: "11-"

```

`````

Part 12.4: Ensure item is readable
----------------------------------

{{ sources.format("12.4") }}

{{ left }}

In this section we'll make sure that the item the player wants to be read can,
in fact, be read.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.4.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

### A. In `test_game.py` define `test_do_read_unreadable_item()`

{{ left }}

In this section we'll be adding a test for when the player tries to read an
item that cannot be read. It should:

* `[ ]` Add a fake unreadable item dictionary to the current place. An item is
  readable if it has a `"message"` key, so for a fake item all we really need
  is an empty dictionary.
* `[ ]` Call `do_read()` with the arguments that would be passed to it if the player
  had typed {samp}`"read {FAKE_THING}"`.
* `[ ]` Check the output for the appropriate error message


{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.4.A.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` import the `place_add` function
1. `[ ]` Add `test_do_read_unreadable_item()` function with the parameter `capsys`
1. `[ ]` Add a fake item to `adventure.ITEMS` with the key of your choice
1. `[ ]` Use the `place_add()` function to add your fake item to the current place
1. `[ ]` Call `do_read()` with a list containing your new key as the argument
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that checks that the message
         {samp}`"Sorry, I don't can't read '{key}'"` is in `output`
1. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.4.py
:linenos:
:lineno-match:
:start-at: "def test_do_read_unreadable_item"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `do_read()`

{{ left }}

Now we'll write the code to make the test pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.4.B.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Use the `get_item()` function to get the item dictionary and assign it to the variable `item`
1. `[ ]` Check if the `"message"` key is in the item dictionary. If not:
   * `[ ]` Use the `error()` function to print an error message like: {samp}`"Sorry, I can't read '{name}'"`
   * `[ ]` return
1. `[ ]` Run your test again. It should pass.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.4.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:caption: adventure.py
:emphasize-lines: "19-"

```

`````

Part 12.5: Read the message
---------------------------

{{ sources.format("12.5") }}

In this section we'll finally provide a readable item and the `read` command
will read it.

### A. In `test_game.py` define `test_do_read_in_place()`

{{ left }}

In this section we'll write a new test where we'll set up a fake item with
`"message"` and `"title"` keys containing the text to be read and add it to the
current place. Then we'll call `do_read()`and check for the expected output.


{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.5.A.cast
:poster: npt:0:04
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add a function `test_do_read_in_place()`
1. `[ ]` Create a dictionary representing a fake item item with the keys
         `"title"` and `"message"` and whatever text you'd like for the values.
1. `[ ]` Use the `place_add()` function to add it to the current place
1. `[ ]` Call `do_read()` with the key for your fake item
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an assert statement that the title is in `output`
1. `[ ]` Write an assert statement that the message is in `output`
1. `[ ]` Run your test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.5.py
:linenos:
:lineno-match:
:start-at: "def test_do_read_in_place"
:caption: test_game.py
:end-before: def

```

`````

### B. In `adventure.py` modify `do_read()`

{{ left }}

Now we'll write the code to actually read the item.

{{ right }}

`````{dropdown} Demo

```{screencast} assets/adventure-12.5.B.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` If the `"title"` key exists in the `item` dictionary, Use the
         `header()` function to print that value. Otherwise print something
         like `"It reads..."`.
1. `[ ]` Use the `wrap()` function to print the `"message"` value from the
         `item` dictionary.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.5.py
:linenos:
:lineno-match:
:start-at: "def do_read"
:end-before: def
:emphasize-lines: "27-"
:caption: adventure.py

```

`````

### C. Modify `ITEMS`: add to `"book"`

{{ left }}

Now we'll finally give the player something to read.

1. `[ ]` In the `"book"` dictionary in `ITEMS`, add the key `"title"` with
         whatever text you'd like
1. `[ ]` In the `"book"` dictionary in `ITEMS`, add the key `"message"` with
         whatever text you'd like

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.5.cast
:poster: npt:0:03
:rows: 18
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.5.py
:linenos:
:lineno-match:
:start-at: '"book": {'
:end-before: '"gems": {'
:emphasize-lines: "8-"
:caption: adventure.py

```

`````

### D. In `test_game.py` define `test_do_read_in_inventory()`

Can you write a `test_do_read_in_inventory()` function on your own, to test that
you can read a book if it is in your inventory but not in the current place?

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.5.py
:linenos:
:lineno-match:
:start-at: 'def test_do_read_in_inventory'
:caption: test_game.py

```

`````

Part 12.6: Indent message
-------------------------

{{ sources.format("12.6") }}

{{ left }}

In this section we're going to indent the message part of the text an extra
level.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.cast
:rows: 18
:poster: npt:0:02
```

`````

{{ endcols }}

### A. In `test_game.py` modify `test_do_read_in_inventory()`

{{ left }}

In this section we're going to modify our `test_do_read_in_inventory()`
function to test that the message has been indented an extra level.

1. `[ ]` Call `.splitlines()` on `output` and assign it to the variable `lines`
1. `[ ]` Write an `assert` statement that checks if the last item in `lines`
         equals your fake items message with 4 spaces at the beginning.
         (Assuming your message is short enough.)
1. `[ ]` Run your test. It should fail.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.A.cast
:poster: npt:0:14
:rows: 16
```

`````

{{ endcols }}

:::{tip}

When you run `pytest` at the command line, you can run a single test by adding
{samp}`::{test_name}` after the filename. For example, here I used `pytest
test_game.py::test_do_read_in_inventory`.

:::

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.6.py
:linenos:
:lineno-match:
:start-at: 'def test_do_read_in_inventory'
:caption: test_game.py
:emphasize-lines: "17, 22-23"

```

`````

### B. In `test_game.py` define `test_wrap()`

{{ left }}

Before we change any code in `do_read()`, we're actually going to modify the
`wrap()` function to optionally add indentation. And since we don't have any
tests for `wrap()` yet, we'll one before we change it.

Since we're testing pre-existing behavior here, this is one we'll expect to
pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.B.cast
:poster: npt:0:07
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add a function `test_wrap()` that takes one parameter `capsys`
1. `[ ]` Call `wrap()` with a string that is longer than the `WIDTH` in your game.
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Call `.splitlines()` on `output` and assign it to the variable `lines`
1. `[ ]` Write an `assert` statement that tests that the length of `lines` is greater than `1`
1. `[ ]` Write an `assert` statement that tests that `output` contains the
         first few words of the text argument.
1. `[ ]` Write an `assert` statement that tests that `output` ends with the
         last few words of the text argument, followed by a newline.
1. `[ ]` Make sure that each string in `lines` starts with two, and no more than two, spaces.
1. `[ ]` Run your test. It should pass.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.6.py
:linenos:
:lineno-match:
:start-at: 'def test_wrap'
:end-before: def
:caption: test_game.py

```

`````

### C. In `test_game.py` define `test_wrap_with_indent()`

{{ left }}

Now that we have the normal `wrap()` behavior tested, we'll add a (failing)
test for the new behavior with the optional `indent` parameter we will be
adding.

This is going to be nearly identical to the `test_wrap()` function, except
we'll be adding the keyword argument `indent=2` when we call `wrap()`, then
testing that the lines are indented to `4` spaces instead of `2`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.C.cast
:poster: npt:0:08
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add a function `test_wrap_with_indent()` that takes one parameter `capsys`
1. `[ ]` Call `wrap()` with a string that is longer than the `WIDTH` in your
         game, followed by a keyword argument `indent` with a value of `2`.
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Call `.splitlines()` on `output` and assign it to the variable `lines`
1. `[ ]` Write an `assert` statement that tests that the length of `lines` is greater than `1`
1. `[ ]` Write an `assert` statement that tests that `output` contains the
         first few words of the text argument.
1. `[ ]` Write an `assert` statement that tests that `output` ends with the
         last few words of the text argument, followed by a newline.
1. `[ ]` Make sure that each string in `lines` starts with four, and no more than four, spaces.
1. `[ ]` Run your test. (Or however many extra spaces you would like.)  It should fail.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.6.py
:linenos:
:lineno-match:
:start-at: 'def test_wrap_with_indent'
:end-before: def
:caption: test_game.py

```

`````

### D. In `adventure.py` modify `wrap()`

{{ left }}

We're finally ready to modify the `wrap()` function to handle indention for us.

1. `[ ]` Add an optional `indent` parameter to `wrap` with a default value of `1`
1. `[ ]` When calculating `margin`, multiply the existing value by `indent`
1. `[ ]` Run your `test_wrap_with_indent()` test. It should pass.
1. `[ ]` Run your `test_wrap()` test. It should pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.D.cast
:poster: npt:0:07
:rows: 16
```

`````

{{ endcols }}

:::{tip}

When you run `pytest` at the command line, you can use the
{samp}`-k {KEYWORD}` flag to run all tests with names that contain
`KEYWORD`. For example, here I use `pytest test_game.py -k test_wrap` to
run both `test_wrap()` and `test_wrap_with_indent()`, but no other tests.

:::

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.6.py
:linenos:
:lineno-match:
:start-at: 'def wrap'
:end-before: def
:caption: test_game.py
:emphasize-lines: "1-5"

```

`````

### E. In `adventure.py` modify `do_read()`

{{ left }}

Now we're finally ready to modify our `do_read()` function to use the new
`indent` keyword argument in `wrap()`.

1. `[ ]` When you print the item message by calling `wrap()` add a keyword
         argument `indent` with a value of `2`. (Or more, to your taste. Just be
         sure you update your test.)
1. `[ ]` Run your `test_do_read_in_inventory` test. It should pass.
1. `[ ]` Run all your tests. They should pass.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.6.E.cast
:poster: npt:0:13
:rows: 16
```

`````

{{ endcols }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.6.py
:linenos:
:lineno-match:
:start-at: 'def do_read'
:end-before: def
:caption: test_game.py
:emphasize-lines: "34"

```

`````

Part 12.7: Allow for stanzas
----------------------------

{{ sources.format("12.7") }}

{{ left }}

In this section we'll add functionality to break up a long message (in
particular, our `book` message) into multiple stanzas.

To accomplish this, we'll modify `wrap()` so that for its `text` argument it can
take either a string or an iterable (a tuple or a list) of strings. If `text`
is a string, it should print just the same as it does now. If `text` is a
`tuple` or a `list`, each item should be wrapped separately and printed with a
blank line between each one.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.7.cast
:rows: 22
:poster: npt:0:02
```

`````

{{ endcols }}

### A. In `test_game.py` modify `test_do_read_in_place()`

{{ left }}

In this section we'll modify the `test_do_read_in_place()` test so that the
`"message"` in our fake item is either a tuple or a list, where each item
represents a stanza. Then we'll add an assert statement to check that there are
two `"\n"` before one of our stanzas.

We'll leave the `test_do_read_in_inventory()` test alone, which will make sure
that it still works if message is a string.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.7.A.cast
:poster: npt:0:10
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Modify the value corresponding to the `"message"` key in your fake
         item dictionary to be either a tuple or a list of strings with
         multiple items.
1. `[ ]` Add an `assert` statement that checks to make sure that output
         contains two blank lines, followed by the number of indentation
         spaces, followed by the first few words of one of your message items.
1. `[ ]` Run the test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.7.py
:linenos:
:lineno-match:
:start-at: 'def test_do_read_in_place'
:end-before: def
:caption: test_game.py
:emphasize-lines: "3-9, 30,31"

```

`````

### B. In `test_game.py` define `test_wrap_with_iterable()`

{{ left }}

Once again, the real heavy lifting will be done in the `wrap()` function. So
before we write any code we'll write a new `wrap()` test for when `text` is an
iterable.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.7.B.cast
:poster: npt:0:09
:rows: 16
```

`````

{{ endcols }}

1. `[ ]` Add a function `test_wrap_with_iterable()` with one parameter `capsys`
1. `[ ]` Set the variable `message` to a list or a tuple of strings.
         (Consider using a few lyrics of a short song or rhyme.)
1. `[ ]` Call the `wrap()` function with the argument `message`
1. `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
1. `[ ]` Write an `assert` statement that makes sure part of one of our
         `message` items is in `output`
1. `[ ]` Write an `assert` statement to make sure that a parenthesis is
         not in `output` if message is a `tuple`, or that a square bracket is not
         in `output` if `message` is a list. This is to make sure that we
         are not mistakenly printing the entire iterable instead of each
         string in the iterable.
1. `[ ]` Add an `assert` statement that checks to make sure that output
         contains two blank lines, followed by the number of indentation
         spaces, followed by the first few words of one of your `message` items.
1. `[ ]` Run the test. It should fail.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-12.7.py
:linenos:
:lineno-match:
:start-at: 'def test_wrap_with_iterable'
:end-before: def
:caption: test_game.py

```

`````

### C. In `adventure.py` modify `wrap()`

{{ left }}

Now we are ready to change the `wrap()` function.

First we'll turn `text` into a one-item iterable if it was a string, that way
we always have something that we can safely iterate over.

Then we'll iterate over each string in our new `text` iterable, wrap it the
same way we already do, and append it to a list called `blocks`.

Finally, we'll print the `blocks` list with two `"\n"` between each one.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-12.7.C.cast
:poster: npt:0:35
:rows: 16
```

`````

{{ endcols }}

:::{note}

We don't need to make any changes to `do_read()` for this feature, since it
already calls `wrap()` with whatever was in the item dictionary for
`"message"`. So once you're done with this, all your tests should pass.

:::

1. `[ ]` Write an `if` statement to check if `text` is a string using the `isinstance()` function.
   * `[ ]` If so, make a list or tuple containing `text` and assign it to the same variable, `text`.
1. `[ ]` Make an empty list and assign it to the variable `blocks`
1. `[ ]` Use a `for` loop to iterate over `text` using the variable name `stanza`
   * `[ ]` Indent the line(s) where you assign `paragraph` to be inside your
           `for` loop
   * `[ ]` In your call to `textwrap.fill()`, instead of use `stanza` for the
           first argument instead of `text`.
   * `[ ]` Append `paragraph` to `blocks`
1. `[ ]` You can either:
   * `[ ]` Use [argument unpacking][unpacking] to send all of the items in the
           `blocks` list as separate arguments to the `print()` function, and the
           keyword argument `sep` to print two newlines between each argument.
   * `[ ]` [Join][join] the `blocks` list using two newlines as the delimiter,
           then print the result.
1. `[ ]` Run your `test_wrap_with_iterable()` test. It should pass.
1. `[ ]` Run your `test_do_read_in_place()` test. It should pass.
1. `[ ]` Run all your tests. They should pass.

[unpacking]: lessons:in-depth:functions:unpacking-arguments
[join]: ../../lessons/data-types/strings

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.7.py
:linenos:
:lineno-match:
:start-at: 'def wrap'
:end-before: def
:caption: adventure.py
:emphasize-lines: "7-15, 25-28"

```

`````

### D. In `adventure.py` modify `ITEMS`

Finally, change the `"message"` in your `"book"` item to be a list or a tuple
of strings.

And now that we're all literate, feel free to scatter scrolls, signs and sticky
notes all over your game!

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-12.7.py
:linenos:
:lineno-match:
:start-at: '"book": {'
:end-before: '"gems": {'
:caption: adventure.py
:emphasize-lines: "14, 17, 20, 22"

```

`````
