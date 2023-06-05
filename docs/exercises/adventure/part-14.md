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

`````{dropdown} do_pet()

```{literalinclude} ../../../pythonclass/adventure/adventure-14.1.py
:linenos:
:lineno-match:
:pyobject: "do_pet"
:caption: adventure.py

```
`````

{{ endcols }}

### C. In `adventure.py` modify `main()`: add delay

Finally, add the code in `main()` so that when the player types `"pet"`, the
`do_pet()` function will be called.


{{ left }}

`````{dropdown} Need help?

1. `[ ]` Add an elif that checks if command is `"pet"`.
   * `[ ]` if so, call `do_pet()` and pass `args`.

`````

{{ right }}

`````{dropdown} main()

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
    * `[ ]` Add a matching fake place dictionary to `PLACES`. The `"can"` key
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

`````{dropdown} test_do_pet_cant_pet()

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

`````{dropdown} do_pet()

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

`````{dropdown} PLACES

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
    * `[ ]` Add a matching fake place dictionary to `PLACES`. The `"can"` key
            should be a list containing the string `"pet"`
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

`````{dropdown} test_do_pet_no_args()

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

`````{dropdown} do_pet()

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
    * `[ ]` Add a matching fake place dictionary to `PLACES`. The `"can"` key
            should be a list containing the string `"pet"`
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

`````{dropdown} test_do_pet_no_color()

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

`````{dropdown} do_pet()

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
    * `[ ]` Add a matching fake place dictionary to `PLACES`. The `"can"` key
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

`````{dropdown} test_do_pet_invalid_color()

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

`````{dropdown} COLORS

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
    * `[ ]` Print an error message like: `"I don't see a dragon head that looks like that."`
    * `[ ]` return

`````

`````{dropdown} do_pet()

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

{{ left }}

In this section we'll randomly pick a dragon mood and print a debug message
about it.

We'll make a global list `DRAGONS` to store information about each dragon in
dictionaries. We'll add more to this later, but for now each dictionary just
needs a single key `"mood"` with a string for the dragon's mood, for example
`"cheerful"`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.5.cast
:poster: npt:0:10
```

`````

{{ endcols }}

Then when the player pets one of the dragon's heads, randomly select one of the
dragon dictionaries and print a debug message that says which dragon was
selected.

### A. In `test_game.py` define `test_do_pet_cheerful_dragon()`

In this section we'll start a test for when the player pets a cheerful dragon
head and simply assert that a debug message was printed.

In order to make sure we always get the cheerful dragon in the test, we'll set
`COLORS` and `DRAGONS` to only contain one color and dragon dictionary
respectively.

`````{dropdown} Need help?

{{ left }}

1\. *GIVEN: The player is in a place where they can pet a dragon*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Change `PLAYER` to put the player in a fake place
    * `[ ]` Add a matching fake place dictionary to `PLACES`. The `"can"` key
            should be a list containing the string `"pet"`
   ```

{{ newrow }}

2\. *AND: There is one color of dragon heads*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assign `adventure.COLORS` to a list containing one color
   ```

{{ newrow }}

3\. *AND: There is one dragon*

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
    * `[ ]` assert that an debug message like `"You picked the dragon's cheerful red head."` is in `output`
   ```

{{ endcols }}

6\. Run your tests. They should fail.

`````

`````{dropdown} test_do_pet_cheerful_dragon()

```{literalinclude} ../../../pythonclass/adventure/test_game-14.5.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_cheerful_dragon"
:caption: test_game.py

```

`````

### B. At the top of `adventure.py`: import `random`

In order to randomly select a dragon dictionary from `DRAGONS` we'll need to
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

### C. At the top of `adventure.py`: add `DRAGONS`

Add the global variable `DRAGONS` and assign it to a list where each item is a
dictionary containing information about each of the dragon's heads. For now each
dictionary will only have one key `"mood"`.

Add three dragon dictionaries for the moods `"cheerful"`, `"grumpy"` and
`"lonely"`.

`````{dropdown} Need help?

1. `[ ]` Create global variable `DRAGONS` and assign it to a list. The list should contain:
    * `[ ]` Three dictionaries. Each dictionary should contain:
      * `[ ]` The key `"mood"` and string with the mood of that dragon, ie `"cheerful"`

`````

`````{dropdown} COLORS

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

In this section we'll randomly select one of the dragons from `DRAGONS` using the
`random.choice()` function. We'll add the `"color"` that the player selected to
that dictionary, then print a debug message with information about the dragon.

`````{dropdown} Need help?

1. `[ ]` Call `random.choice()` with the argument `DRAGONS` and assign it to the
         variable `dragon`.
1. `[ ]` Set `dragon["color"]` to `color`
1. `[ ]` Print a debug message like {samp}`"You picked the dragon's {MOOD} {COLOR} head."`

`````

`````{dropdown} do_pet()

```{literalinclude} ../../../pythonclass/adventure/adventure-14.5.py
:linenos:
:lineno-match:
:pyobject: do_pet
:emphasize-lines: "28-"
:caption: adventure.py

```

`````

Part 14.6: Treasure
-------------------

{{ sources.format("14.6") }}

{{ left }}

In this section we're going to write the code so that some of the dragons will
give the player gems.

In order to do this we'll add a `"treasure"` key to some of the dragon
dictionaries `DRAGONS`. The value will be a tuple containing the minimum and
maximum possible gems that a particular dragon might give.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.6.cast
:poster: npt:0:12
```

`````

{{ endcols }}

Then in the `do_pet()` function we'll retrieve the range of possible treasure
from the dragon dictionary, randomly pick a number in that range, then add that
amount the player gems and print a message to tell the player what happened.

### A. In `test_game.py` modify `test_do_pet_cheerful_dragon()`

In this section we'll modify the `test_do_pet_cheerful_dragon()` test to add
the `"treasure"` key to the single dictionary in `DRAGONS`, and a tuple
containing two numbers (the minimum and maximum possible treasure) as the value.

Then we'll need to check that the number if gems in the player's inventory was
increased.

`````{dropdown} Need help?

{{ left }}

1\. Modify *AND: There is one dragon*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Add a `"treasure"` key to the dragon dictionary in `DRAGONS` for
      * `[ ]` The key should be `"treasure"`
      * `[ ]` The value should a tuple with two numbers representing the
              minimum and maximum possible treasure. ie `(10, 20)`.

    :::{tip}

    If we want to know the exact treasure amount you can use the same
    number for the minimum and maximum, for example: `(10, 10)`.

    :::

   ```

{{ newrow }}

2\. After *WHEN* add *AND: The player has some gems*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Set the `"gems"` in `PLAYER` inventory to a number
   ```

{{ newrow }}

3\. After *THEN* add *AND: The player should get treasure*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that the gems in `PLAYER` inventory is more than it was before
   ```

{{ newrow }}

4\. After *THEN* add *AND: The player should see a message about what happened*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert a message like {samp}`"gave you {GEMS} gems"` is in `output`
   ```

{{ endcols }}

5\. Run your tests. They should fail.

`````

`````{dropdown} test_do_pet_cheerful_dragon()

```{literalinclude} ../../../pythonclass/adventure/test_game-14.6.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_cheerful_dragon"
:emphasize-lines: "15, 18-19, 28-"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `DRAGONS`

Modify the dragon dictionaries in the `DRAGONS` list to add `"treasure"` tuples
for the `"cheerful"` and `"lonely"` dragons.

`````{dropdown} Need help?

* `[ ]` Add a `"treasure"` key to the single dictionary in `DRAGONS` list for the
       `"cheerful"` and `"lonely"` dragons
  * `[ ]` The key should be `"treasure"`
  * `[ ]` The value should a tuple with two numbers representing the
          minimum and maximum amount of treasure. ie `(10, 20)`.

`````

`````{dropdown} DRAGONS

```{literalinclude} ../../../pythonclass/adventure/adventure-14.6.py
:linenos:
:lineno-match:
:start-at: "DRAGONS ="
:end-at: "]"
:emphasize-lines: "4, 11"
:caption: adventure.py

```

`````

### B. In `adventure.py` modify `do_pet()`

In this section we'll retrieve the range of possible treasure from the `dragon`
dictionary (if the `"treasure"` key exists) then use the two numbers in the
`random.randint()` function to get the number of gems to give the player.

Then we'll add that number of gems to the player's inventory and print a
message about it.

`````{margin}

```{seealso}

For how to pass all iterable items as arguments to a function see [Functions >
Unpacking][arg-unpacking].

```

`````


`````{dropdown} Need help?

1. `[ ]` Use the `.get()` method on the `dragon` dictionary to get the value
         for the `"treasure"` key and assign the result to `possible_treasure`.
         Since not all dragons will have the `"treasure"` key, use the second
         argument in `.get()` to set the default value to `(0, 0)`.
1. `[ ]` Pass the minimum and maximum numbers from `possible_treasure` as
         arguments to the `random.randint()` function and assign the results to
         `dragon["gems"]`.
1. `[ ]` Use the `inventory_change()` function to add `dragon["gems"]` to the
         players inventory.
1. `[ ]` Print a message like: {samp}`"The dragon's {MOOD} head gave you {GEMS} gems."`

`````

`````{dropdown} do_pet()

```{literalinclude} ../../../pythonclass/adventure/adventure-14.6.py
:linenos:
:lineno-match:
:pyobject: do_pet
:emphasize-lines: "34-"
:caption: adventure.py

```

`````

Part 14.7: Damage
-----------------

{{ sources.format("14.7") }}

{{ left }}

In this section we're going to write the code so that some of the dragons will
cause the player damage.

In order to do this we'll add a `"damage"` key to some of the dragon
dictionaries `DRAGONS`. The value will be a tuple containing the minimum and
maximum possible damage that a particular dragon might cause.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.7.cast
:poster: npt:0:10
```

`````

{{ endcols }}

Then in the `do_pet()` function we'll retrieve the range of possible damage
from the dragon dictionary, randomly pick a number in that range, then subtract
that amount the player health and print a message to tell the player what
happened.

### A. In `test_game.py` modify `test_do_pet_cheerful_dragon()`

In this section we'll modify the `test_do_pet_cheerful_dragon()` test to make
sure that the player's health does not change.

`````{dropdown} Need help?

{{ left }}

1\. After *WHEN* add *AND: The player has a certain amount of health*

{{ br }}

{{ right }}

   ```{dropdown} ...

    * `[ ]` Set "health" value in the `PLAYER` dictionary to a number like `90`

   ```

{{ newrow }}

2\. After *THEN* add *AND: The player's health should be the same*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assert that `PLAYER["health"]` is the same as it was before
   ```

{{ endcols }}

3\. Run your tests. They should pass.

`````

`````{dropdown} test_do_pet_cheerful_dragon()

```{literalinclude} ../../../pythonclass/adventure/test_game-14.7.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_cheerful_dragon"
:emphasize-lines: "21-22, 34-35"
:caption: test_game.py

```

`````

### B. In `test_game.py` define `test_do_pet_cranky_dragon()`

In this section we'll define the `test_do_pet_cranky_dragon()` test. It will be
very similar to `test_do_pet_cheerful_dragon()`, except in the `DRAGONS`
dictionary we'll add a dragon dictionary that has a `"damage"` key with a tuple
of two negative numbers and we'll assert that `PLAYER["health"]` has decreased.

`````{dropdown} Need help?

{{ left }}

1\. *GIVEN: The player is in a place where they can pet a dragon*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Change `PLAYER` to put the player in a fake place
    * `[ ]` Add a matching fake place dictionary to `PLACES`. The `"can"` key
            should be a list containing the string `"pet"`
   ```

{{ newrow }}

2\. *AND: There is one color of dragon heads*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assign `adventure.COLORS` to a list containing one color
   ```

{{ newrow }}

3\. *AND: There is one dragon who causes damage*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assign `adventure.DRAGONS` to a list containing one dictionary that contains:
      * `[ ]` the key `"mood"` and the string `"cranky"` for the value.
      * `[ ]` the key `"damage"` and a tuple with two negative numbers for the value
   ```

{{ newrow }}

4\. *AND: The player has a certain amount of health*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Set `"health"` in the `PLAYER` dictionary to a number greater than `0` and less than `100`
   ```

{{ newrow }}

5\. *AND: The player has some gems*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Set `"gems"` in the `PLAYER["inventory"]` dictionary to a positive number
   ```

{{ newrow }}

6\. *WHEN: The player pets that head*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_pet()` with a list that contains the same color that is in `COLORS`
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

7\. *THEN: A debug message should print*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an debug message like `"You picked the dragon's cranky red head."` is in `output`
   ```

{{ newrow }}

8\. *AND: The player's health should be reduced*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that the `PLAYER["health"]` is less than it was before
   ```

{{ newrow }}

9\. *AND: The player's gems should not be changed*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that the `PLAYER["inventory"]["gems"]` is the same as it was before
   ```

{{ newrow }}

10\. *AND: The player should see a message about what happened*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an debug message like
      {samp}`"caused you {DAMAGE}" damage` is in `output`
   ```


{{ endcols }}

11\. Run your tests. They should fail.

`````

`````{dropdown} test_do_pet_cranky_dragon()

```{literalinclude} ../../../pythonclass/adventure/test_game-14.7.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_cranky_dragon"
:caption: test_game.py

```

`````

### C. In `adventure.py` modify `DRAGONS`

Modify the dragon dictionaries in the `DRAGONS` list to add `"damage"` tuples
for the `"cranky"` and `"lonely"` dragons.

`````{dropdown} Need help?

* `[ ]` Add a `"damage"` key to the single dictionary in `DRAGONS` list for the
       `"cranky"` and `"lonely"` dragons
  * `[ ]` The key should be `"damage"`
  * `[ ]` The value should a tuple with two numbers representing the
          minimum and maximum amount of damage. ie `(-20, -10)`.

`````

`````{dropdown} DRAGONS

```{literalinclude} ../../../pythonclass/adventure/adventure-14.7.py
:linenos:
:lineno-match:
:start-at: "DRAGONS ="
:end-at: "]"
:emphasize-lines: "8, 13"
:caption: adventure.py

```

`````

### D. In `adventure.py` modify `do_pet()`

In this section we'll retrieve the range of possible damage from the `dragon`
dictionary (if the `"damage"` key exists) then use the two numbers in the
`random.randint()` function to get the number of gems to give the player.

Then we'll add that number of gems to the player's inventory and print a
message about it.

`````{dropdown} Need help?

1. `[ ]` Use the `.get()` method on the `dragon` dictionary to get the value
         for the `"damage"` key and assign the result to `possible_damage`.
         Since not all dragons will have the `"damage"` key, use the second
         argument in `.get()` to set the default value to `(0, 0)`.
1. `[ ]` Pass the minimum and maximum numbers from `possible_damage` as
         arguments to the `random.randint()` function and assign the results to
         `dragon["health"]`.
1. `[ ]` Use the `health_change()` function to subtract `dragon["health"]` from the
         players health.
1. `[ ]` Print a message like: {samp}`"The dragon's {MOOD} head caused you {HEALTH} damage."`

`````

`````{dropdown} do_pet()

```{literalinclude} ../../../pythonclass/adventure/adventure-14.7.py
:linenos:
:lineno-match:
:pyobject: do_pet
:emphasize-lines: "38-40, 45-46, 52-"
:caption: adventure.py

```

`````

### E. In `test_game.py` define `test_do_pet_lonely_dragon()`

In this section we'll define the `test_do_pet_lonely_dragon()` test. It will be
just like combining the test for a `"cheerful"` dragon and a `"cranky"` dragon.

That is, the dragon dictionary in `DRAGONS` should have *both* `"treasure"` and
`"damage"`.

`````{dropdown} Need help?

{{ left }}

1\. *GIVEN: The player is in a place where they can pet a dragon*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Change `PLAYER` to put the player in a fake place
    * `[ ]` Add a matching fake place dictionary to `PLACES`. The `"can"` key
            should be a list containing the string `"pet"`
   ```

{{ newrow }}

2\. *AND: There is one color of dragon heads*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assign `adventure.COLORS` to a list containing one color
   ```

{{ newrow }}

3\. *AND: There is one dragon who causes damage and gives treasure*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Assign `adventure.DRAGONS` to a list containing one dictionary that contains:
      * `[ ]` the key `"mood"` and the string `"cranky"` for the value.
      * `[ ]` the key `"treasure"` and a tuple with two positive numbers for the value
      * `[ ]` the key `"damage"` and a tuple with two negative numbers for the value
   ```

{{ newrow }}

4\. *AND: The player has a certain amount of health*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Set `"health"` in the `PLAYER` dictionary to a number greater than `0` and less than `100`
   ```

{{ newrow }}

5\. *AND: The player has some gems*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Set `"gems"` in the `PLAYER["inventory"]` dictionary to a positive number
   ```

{{ newrow }}

6\. *WHEN: The player pets that head*

{{ right }}

   ```{dropdown} ...
    * `[ ]` Call `do_pet()` with a list that contains the same color that is in `COLORS`
    * `[ ]` Assign the results of `capsys.readouterr().out` to the variable `output`
   ```

{{ newrow }}

7\. *THEN: A debug message should print*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an debug message like `"You picked the dragon's lonely red head."` is in `output`
   ```

{{ newrow }}

8\. *AND: The player's health should be reduced*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that the `PLAYER["health"]` is less than it was before
   ```

{{ newrow }}

9\. *AND: The player should get treasure*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that the `PLAYER["inventory"]["gems"]` is more than it was before
   ```

{{ newrow }}

10\. *AND: The player should see a message about what happened*

{{ right }}

   ```{dropdown} ...
    * `[ ]` assert that an debug message like samp`"caused you {HEALTH}" damage` is in `output`
   ```


{{ endcols }}

11\. Run your tests. They should pass.

`````

`````{dropdown} test_do_pet_lonely_dragon()

```{literalinclude} ../../../pythonclass/adventure/test_game-14.7.py
:linenos:
:lineno-match:
:pyobject: "test_do_pet_lonely_dragon"
:caption: test_game.py

```

`````

Part 14.8: Pet the dragon
-------------------------

{{ sources.format("14.8") }}

{{ left }}

In this section we'll add a description of what happens when you pet a dragon's
head, pausing between each line to give it a sense of drama.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.8.cast
:poster: npt:0:15
```

`````

{{ endcols }}

### A. At the top of `adventure.py`: import `sleep` from `time`

In order to add a pause for effect in between lines in the action description,
we'll need to import the `sleep` function from the `time` module.

{{ left }}

`````{dropdown} Need help?

1. `[ ]` import the `sleep` function from the `time` module

`````

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-14.8.py
:linenos:
:lineno-match:
:start-at: "from time"
:end-at: "ProgressBar"
:emphasize-lines: "1"
:caption: adventure.py

```

`````

{{ endcols }}

### B. At the top of `adventure.py`: add `DELAY`

{{ left }}

At the top of your script where your other global variables are, add a new
global variable `DELAY` and set it to a number that will be the number of
seconds to pause for effect.

`````{dropdown} Need help?

1. `[ ]` Set `DELAY` to a number like `1`

`````

{{ right }}

`````{dropdown} DELAY

```{literalinclude} ../../../pythonclass/adventure/adventure-14.8.py
:linenos:
:lineno-match:
:start-at: "WIDTH ="
:end-before: "ProgressBar"
:emphasize-lines: "7"
:caption: adventure.py

```

`````

{{ endcols }}

### C. Modify `do_pet()`: add action description with delay

In this section we're going to add a description of what happens when the player
pets the dragon's head. To make it a little more exciting, we'll split the
description onto multiple strings in a tuple. Something like:

* `"You slowly creep forward..."`
* `"...gingerly reach out your hand..."`
* {samp}`"...and gently pat the dragon's {COLOR} head."`
* `"..."`
* `"He blinks sleepy eyes and peers at you..."`

Before printing the messages about gems and damage, we'll iterate over the
`sentences` tuple. In each iteration we'll print a blank line,
print the string, and call `sleep()` with the argument `DELAY`.

Finally we'll print one blank line at the end.

`````{dropdown} Need help?

1. `[ ]` Create a tuple (or list) assigned to `sentences` that contains the
         three strings from above.
1. `[ ]` **Above** the messages about gems and damage are printed, use a for
         loop to iterate over `sentences` with the variable `text`.
         In each iteration:
    * `[ ]` Print a blank line.
    * `[ ]` Use the `write()` function to print `text`.
    * `[ ]` Call `sleep()` with the argument `DELAY`.
1. `[ ]` Print a blank line.
1. `[ ]` Play your game and see how it looks!

`````

`````{dropdown} do_pet()

```{literalinclude} ../../../pythonclass/adventure/adventure-14.8.py
:linenos:
:lineno-match:
:start-at: "# get the dragon info"
:end-before: "def main"
:emphasize-lines: "21-32"
:caption: "adventure.py: `do_pet()`"

```

`````

### D. At the top of `test_game.py`: set `adventure.DELAY`

If you were to run your tests now, you would find that all of the
`test_do_pet_*` tests run an awful lot slower. That's because `do_pet()` calls
`sleep()` in the tests just like it does in the game.

To avoid this problem, simply set `adventure.DELAY` to `0` near the top of your
test file. Unlike the changes that we make in a *GIVEN* portion of a test, we
only need to set `adventure.DELAY` once. Put it just under where you assign all
of the `*_STATE` global variables.

{{ left }}

`````{dropdown} Need help?

1. `[ ]` Find where you assign `PLAYER_STATE`, `DEBUG_STATE`, etc. Just under
         that set `adventure.DELAY` to `0`
1. `[ ]` Run your tests. They should pass and be as fast as usual.

`````

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/test_game-14.8.py
:linenos:
:lineno-match:
:pyobject: setup_module
:emphasize-lines: "9"
:caption: test_game.py

```

`````

{{ endcols }}

Part 14.9: Better messages
--------------------------

{{ sources.format("14.9") }}

{{ left }}

In this section we'll make nicer and more detailed messages for when each
dragon causes damage or gives treasure.

To do this we'll add a `"message"` key to each dragon dictionary in `DRAGONS`,
which will have the end of the message for a value.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.9.cast
:poster: npt:0:14
```

`````

{{ endcols }}

For example, say we want the message to be:

`"The happy green dragon thinks you're great and gives you 100 gems!"`

Then the `"message"` value would be:

`"thinks you're great and gives you {gems} gems!"`

It's important to note that value should contain the f-string style variables
`{gems}` and/or `{damage}`, **but it should not actually be an f-string**.

That way we can attach it to the beginning of the message in `do_pet()`, then
call the `.format()` method on the resulting string to fill in all the
variable values.

### A. Modify `test_do_pet_*_dragon()`: add `"message"` to `DRAGONS`

In this section we'll modify the three `test_do_pet_*_dragon()` tests to add
the `"message"` key to the single dictionary in `DRAGONS` with the value bing a
string that contains the f-string style variables `{gems}` and/or `{health}`.

`````{dropdown} Need help?

{{ left }}

1\. Modify *AND: There is one dragon who gives you treasure*

{{ br }}

{{ right }}

   ```{dropdown} ...
    * `[ ]` Add the key `"message"` to the single dictionary in `DRAGONS` with the value:
      * `[ ]` A string that is **not** an f-string but contains the f-string
              style variables `{gems}` and/or `{health}`.

         It should be the part of the message that comes after
         {samp}`"The dragon's {MOOD} {COLOR} head"` and describes what the
         dragon does after the player pets it.

   ```

{{ endcols  }}

2\. Run your tests. They should fail.

`````

`````{dropdown} test_do_pet_cheerful_dragon()

```{literalinclude} ../../../pythonclass/adventure/test_game-14.9.py
:linenos:
:lineno-match:
:start-at: "def test_do_pet_cheerful_dragon"
:end-at: '}]'
:emphasize-lines: "16"
:caption: test_game.py

```

`````

`````{dropdown} test_do_pet_cranky_dragon()

```{literalinclude} ../../../pythonclass/adventure/test_game-14.9.py
:linenos:
:lineno-match:
:start-at: "def test_do_pet_cranky_dragon"
:end-at: '}]'
:emphasize-lines: "16"
:caption: test_game.py

```

`````

`````{dropdown} test_do_pet_lonely_dragon()

```{literalinclude} ../../../pythonclass/adventure/test_game-14.9.py
:linenos:
:lineno-match:
:start-at: "def test_do_pet_lonely_dragon"
:end-at: '}]'
:emphasize-lines: "17"
:caption: test_game.py

```

`````

### B. In `adventure.py` modify `DRAGONS`: add `"message"`

Modify the dragon dictionaries in the `DRAGONS` list to add `"message"` string
for all three dragons.

`````{dropdown} Need help?

* `[ ]` Add the key `"message"` to the all three dragon dictionaries in
        `DRAGONS` with the value:
  * `[ ]` A string that is **not** an f-string but contains the f-string
          style variables `{gems}` and/or `{health}`.

      It should be the part of the message that comes after
      {samp}`"The dragon's {MOOD} {COLOR} head "` and describes what the
      dragon does after the player pets it.

`````

`````{dropdown} DRAGONS

```{literalinclude} ../../../pythonclass/adventure/adventure-14.9.py
:linenos:
:lineno-match:
:start-at: "DRAGONS ="
:end-at: "]"
:emphasize-lines: "5, 10-13, 19-23"
:caption: adventure.py

```

`````

### C. Modify `do_pet()`: print the message

`````{margin}

```{seealso}

* [String Formatting > str.format() method][str-format]
* [Functions > Unpacking > Mappings][kwarg-unpacking] -- for how to pass all dictionary key value pairs as keyword arguments to a function see

```

`````

Now we'll combine the beginning of the message
`"The dragon's {mood} {color} head "` with the string from `dragon["message"]`.

Since the `dragon` dictionary already has the information about `mood`,
`color`, and `gems` and/or `health`, we can call `.format()` on the resulting
string and pass the whole dictionary as keyword arguments. That will fill in
all those variables with their corresponding values from the dictionary.

Then we can replace the lines where we print the two old messages with a line
printing the new message, wrapped.

`````{dropdown} Need help?

1. `[ ]` Remove the lines where you print the messages about gems and damage.
1. `[ ]` Concatonate the string `"The dragon's {mood} {color} head "` with
         `dragon["message"]` and assign the result to the variable `tpl`.
1. `[ ]` Call the `.format()` method on `tpl` and pass all key-value pairs from
         the `dragon` dictionary as keyword arguments. Assign the result to `text`.
1. `[ ]` Use the `wrap()` function to print `text`.
1. `[ ]` Run your tests. They should pass.

`````

`````{dropdown} do_pet()

```{literalinclude} ../../../pythonclass/adventure/adventure-14.9.py
:linenos:
:lineno-match:
:start-at: "# get the dragon info"
:end-at: "wrap"
:emphasize-lines: "34-"
:caption: "adventure.py: `do_pet()`"

```

`````

Part 14.10: Add dragon
----------------------

{{ sources.format("14.10") }}

{{ left }}

Finally, we'll add the dragon itself as an item in your cave so the player can
examine it to find out the colors of each dragon head.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.10.cast
:poster: npt:0:12
```

`````

{{ endcols }}

### A. In `adventure.py` modify `ITEMS`

In your `ITEMS` dictionary, add a `"dragon"` key. Use the global variable
`COLORS` in the description to list the colors of the dragon heads.

`````{dropdown} ITEMS

```{literalinclude} ../../../pythonclass/adventure/adventure-14.10.py
:linenos:
:lineno-match:
:start-at: '"dragon": '
:end-at: "   },"
:caption: adventure.py

```

`````

### B. In `adventure.py` modify `PLACES`

{{ left }}


{{ right }}

`````{dropdown} COLORS

```{literalinclude} ../../../pythonclass/adventure/adventure-14.10.py
:linenos:
:lineno-match:
:start-at: '"cave": '
:end-at: '   },'
:emphasize-lines: "12"
:caption: adventure.py

```

`````

{{ endcols }}

[arg-unpacking]: ../../lessons/in-depth/functions.html#part-3-unpacking-arguments
[kwarg-unpacking]: ../../lessons/in-depth/functions.html#part-3-3-mappings
[str-format]: ../../lessons/string-formatting-part-2.html#the-str-format-method
