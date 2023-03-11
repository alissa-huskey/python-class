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

Part 14.1: Add command
----------------------

{{ sources.format("14.1") }}

{{ left }}

In this section we'll add the pet command.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.1.cast
:poster: npt:0:03
```

`````

{{ endcols }}

### A. In `test_game.py` define `test_do_pet()`

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

### B. In `adventure.py` define `do_pet()`

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

### C. In `adventure.py` modify `main()`

Finally, add the code in `main()` so that when the player types `"pet"`, the
`do_pet()` function will be called.


{{ left }}

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

Part 14.2: Is petting allowed?
------------------------------

{{ sources.format("14.2") }}

{{ left }}

In this section we'll check to make sure petting is allowed in the current place.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.2.cast
:poster: npt:0:05
```

`````

{{ endcols }}


### A. In `test_game.py` define `test_do_pet_cant_pet()`

In this section we'll write a `test_do_pet_cant_pet()` function. It should
check that if the player tries to pet something when in a place where they
aren't allowed (as defined by the place dictionary `"can"` list), they'll see
an error message.

`````{dropdown} Need help?

{{ left }}

1\. *GIVEN: The player is in a place where they can't pet anything*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Change `PLAYER` to put the player in a fake place
    * `[ ]` Add a matching fake places dictionary to `PLACES`. The `"can"` key
            should be an empty list.
   ```

{{ newrow }}

2\. *WHEN: They try to pet something*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_pet()` with a list containing any string
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

3\. *THEN: An error message should be printed*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an error message like `"You can't do that"` is in `output`
   ```

{{ endcols }}

4\. Run your tests. They should fail.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-14.2.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_cant_pet"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `do_pet()`: can pet

Now we'll modify `do_pet()` function to check that if the current place is not
able to use the pet command (as defined by the place dictionary `"can"` list)
an error message will be printed and the function will return.

{{ left }}

`````{dropdown} Need help?

1. `[ ]` Use the `place_can()` function to check if the place can `"pet"`. If not:
    * `[ ]` Print an error message like `"You can't do that here."`
    * `[ ]` return

`````

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.2.py
:linenos:
:lineno-match:
:pyobject: "do_pet"
:emphasize-lines: "6-9"
:caption: adventure.py

```

`````

{{ endcols }}

### C. In `adventure.py` modify `PLACES`

Now update the `PLACES` dictionary to add a cave where you can pet a dragon,
and modify your other places so that you can get to it.

`````{dropdown} Need help?

1. `[ ]` Add a place called `cave` with the `"can"` key set to a list that
         includes the string `"pet"`
2. `[ ]` Modify the `"east"`, `"west"`, `"north"`, and `"south"` key(s) of your
         other places so that the player can get to the cave.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.2.py
:linenos:
:lineno-match:
:start-at: "PLACES ="
:end-before: "ITEMS ="
:emphasize-lines: "13, 31-76"
:caption: adventure.py

```

`````

Part 14.3: Ensure args
----------------------

{{ sources.format("14.3") }}

{{ left }}

In this section we'll make sure that the player typed what they want to pet, or
print an error if they didn't.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.3.cast
:poster: npt:0:10
```

`````

{{ endcols }}

### A. In `test_game.py` define `test_do_pet_no_args()`

In this section we'll write a `test_do_pet_no_args()` function. It should check
that if the player does not type anything after `"pet"`, they'll see an error
message.

`````{dropdown} Need help?

{{ left }}

1\. *GIVEN: The player is in a place where they can pet things*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Change `PLAYER` to put the player in a fake place
    * `[ ]` Add a matching fake places dictionary to `PLACES`. The `"can"` key
            should be an empty list.
   ```

{{ newrow }}

2\. *WHEN: the player types "pet" with no arguments*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_pet()` with an empty list
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

3\. *THEN: an error message should be printed*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an error message like `"What do you want to pet"` is in `output`
   ```

{{ endcols }}

4\. Run your tests. They should fail.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-14.3.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_no_args"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `do_pet()`: ensure args

{{ left }}

`````{dropdown} Need help?

1. `[ ]` Check if `args` is empty. If so:
    * `[ ]` Print an error message like `"What do you want to pet?"`
    * `[ ]` return

`````

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.3.py
:linenos:
:lineno-match:
:pyobject: "do_pet"
:emphasize-lines: "11-"
:caption: adventure.py

```

`````

Part 14.4: Ensure color
-----------------------

{{ sources.format("14.4") }}

This command is a little different from previous commands, because we want the
player to be able to type a few different things.

{{ left }}

We expect the player to type something like:

`pet red dragon`

But we would also accept:

`pet red dragon head`

Or:

`pet red head`

Or even:

`pet red`

{{ right }}


`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.4.cast
:poster: npt:0:10
```

`````

{{ endcols }}


So we'll need to make sure that the player typed something in addition to
`"dragon"` and `"head"` and that it is a valid color.

### A. In `test_game.py` define `test_do_pet_no_color()`

In this section we'll write a `test_do_pet_no_color()` test. It should
check that the player typed something in addition to `"dragon"` and/or
`"head"`.

`````{dropdown} Need help?

{{ left }}

1\. *GIVEN: The player is in a place where they can pet things*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Change `PLAYER` to put the player in a fake place
    * `[ ]` Add a matching fake places dictionary to `PLACES`. The `"can"` key
            should be an empty list.
   ```

{{ newrow }}

2\. *WHEN: the player types "pet" without typing a color*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_pet()` with a list containing the words `"dragon"` and/or `"head"`
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

3\. *THEN: an error message should be printed*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an error message like `"What do you want to pet"` is in `output`
   ```

{{ endcols }}

4\. Run your tests. They should fail.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-14.4.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_no_color"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `do_pet()`: remove ignored args

To support extra words like `"dragon"` and `"head"`, we're simply going to
remove them from `args`.

If we do this *before* we check to make sure that `args` is not empty, then
we'll get the same error message if they type `pet` as when they type `pet
dragon`.

`````{dropdown} Need help?

Do this *before* the line with `if not args:`

1. `[ ]` Make a list of allowed words like `["dragon", "head"]` and iterate
         over it. For each one:
    * `[ ]` Check if the word is in `args`. If so:
      * `[ ]` Remove it from `args`
1. `[ ]` Run your tests. They should pass.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.4.py
:linenos:
:lineno-match:
:start-at: "def do_pet"
:end-before: "color ="
:emphasize-lines: "11-14"
:caption: adventure.py

```

`````

### C. In `test_game.py` define `test_do_pet_invalid_color()`

We'll add a new test `test_do_pet_invalid_color()` to make sure the color is
valid. We'll use a global variable `adventure.COLORS` to store the list of
valid colors.

`````{dropdown} Need help?

{{ left }}

1\. *GIVEN: There are three colors of dragon heads*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assign `adventure.COLORS` to a list of colors
   ```

{{ newrow }}

1\. *AND: The player is in a place where they can pet things*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Change `PLAYER` to put the player in a fake place
    * `[ ]` Add a matching fake places dictionary to `PLACES`. The `"can"` key
            should be an empty list.
   ```

{{ newrow }}

2\. *WHEN: They try to pet a dragon with a color that doesn't exist*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_pet()` with a list containing the a word that is not a color
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

3\. *THEN: an error message should be printed*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an error message like `"I don't see that dragon"` is in `output`
   ```

{{ endcols }}

4\. Run your tests. They should fail.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-14.4.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_invalid_color"
:caption: test_game.py

```

`````

### D. In `adventure.py` add `COLORS`

{{ left }}

At the top of your script where your other global variables are, add a new
global variable `COLORS` and set it to a list with three colors in it.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.4.py
:linenos:
:lineno-match:
:start-at: "import"
:end-before: "PLAYER = "
:emphasize-lines: "22"
:caption: adventure.py

```

`````

{{ endcols }}

### E. In `adventure.py` modify `do_pet()`: ensure valid color

We can now assume that anything left in the `args` list is the color. We'll
check that it is in the `COLORS` list, or print an error message if it is not.

`````{dropdown} Need help?

1. `[ ]` Assign the first item from `args` to the variable `color`
1. `[ ]` Check to make sure that `color` is in the list of `COLORS`. If not:
    * `[ ]` Print an error message like: `"I don't see a dragon that looks like that."`
    * `[ ]` return

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.4.py
:linenos:
:lineno-match:
:pyobject: "do_pet"
:emphasize-lines: "21-"
:caption: adventure.py

```

`````

Part 14.5: Pick a dragon
------------------------

{{ sources.format("14.5") }}

In this section we are going to make a global list `MOODS` to store information
about each dragon in dictionaries. We'll add more to this later, but for now
each dictionary just needs a single key `"mood"` with a string for the dragon's
mood, for example `"cheerful"`.

Then when the player pets one of the dragon heads, randomly select one of the
dragon dictionaries and print a debug message that says which dragon was
selected.

### A. In `test_game.py` define `test_do_pet_cheerful_dragon()`

In this section we'll start a test for when the player pets a cheerful dragon
head and simply assert that a debug message was printed.

In order to make sure we always get the cheerful dragon in the test, we'll set
`COLORS` and `MOODS` to only contain one color and dragon dictionary
respectively.

`````{dropdown} Need help?

{{ left }}

1\. *GIVEN: The player is in a place where they can pet a dragon*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Change `PLAYER` to put the player in a fake place
    * `[ ]` Add a matching fake places dictionary to `PLACES`. The `"can"` key
            should be an empty list.
   ```

{{ newrow }}

2\. *AND: There is one color of dragon heads*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assign `adventure.COLORS` to a list containing one color
   ```

{{ newrow }}

3\. *AND: There is one a dragon*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assign `adventure.DRAGONS` to a list containing one dictionary. The
            dictionary should have the key `"mood"` and the string `"cheerful"` for
            the value.
   ```

{{ newrow }}

4\. *WHEN: The player pets that head*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_pet()` with a list that contains the same color that is in `COLORS`
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

5\. *THEN: A debug message should print*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an debug message like `"You picked the cheerful red dragon."` is in `output`
   ```

{{ endcols }}

6\. Run your tests. They should fail.

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-14.5.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_cheerful_dragon"
:caption: test_game.py

```

`````

### B. At the top of `adventure.py`: import `random`

In order to randomly select a dragon dictionary from `MOODS` we'll need to
import the `random` module.

{{ left }}

`````{dropdown} Need help?

1. `[ ]` import the `random` module

`````

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.5.py
:linenos:
:lineno-match:
:start-at: "import"
:end-before: "clear_line"
:emphasize-lines: "1"
:caption: adventure.py

```

`````

{{ endcols }}

### C. At the top of `adventure.py`: add `MOODS`

Add the global variable `MOODS` and assign it to a list where each item is a
dictionary containing information about each of the dragon heads. For now each
dictionary will only have one key `"mood"`.

Add three dragon dictionaries for the moods `"cheerful"`, `"grumpy"` and
`"lonely"`.

`````{dropdown} Need help?

1. `[ ]` Create global variable `MOODS` and assign it to a list. The list should contain:
    * `[ ]` Three dictionaries. Each dictionary should contain:
      * `[ ]` The key `"mood"` and string with the mood of that dragon, ie `"cheerful"`

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.5.py
:linenos:
:lineno-match:
:start-at: "COLORS ="
:end-before: "PLACES ="
:emphasize-lines: "3-7"
:caption: adventure.py

```

`````

### D. In `adventure.py` modify `do_pet()`

In this section we'll randomly select one of the dragons from `MOODS` using the
`random.choice()` function. We'll add the `"color"` that the player selected to
that dictionary, then print a debug message with information about the dragon.

`````{dropdown} Need help?

1. `[ ]` Call `random.choice()` with the argument `MOODS` and assign it to the
         variable `dragon`.
1. `[ ]` Set `dragon["color"]` to `color`
1. `[ ]` Print a debug message like {samp}`"You picked the {MOOD} {COLOR} dragon."`

`````

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.5.py
:linenos:
:lineno-match:
:pyobject: do_pet
:emphasize-lines: "28-"
:caption: adventure.py

```

`````

---

1. `[ ]`
1. `[ ]`
1. `[ ]`
1. `[ ]`
1. `[ ]`
    * `[ ]`
1. `[ ]`
    * `[ ]`
