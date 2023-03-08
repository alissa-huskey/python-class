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

{{ left }}

In this section we'll add the pet command.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.1.cast
:poster: npt:0:03
:rows: 16
```

`````

{{ endcols }}

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

{{ sources.format("14.2") }}

Part 14.2: Is petting allowed?
------------------------------

{{ clear }}

{{ left }}

In this section we'll check to make sure petting is allowed in the current place.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-14.2.cast
:poster: npt:0:05
:rows: 16
```

`````

{{ endcols }}


### A. In `test_game.py` write `test_do_pet_cant_pet()`

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

### B. In `adventure.py` in `do_pet()`

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

### C. In `adventure.py` in `PLACES`

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

{{ sources.format("14.3") }}

Part 14.3: Ensure args
----------------------

{{ clear }}

In this section we'll make sure that the player typed what they want to pet.

### A. In `test_game.py` add `test_do_pet_no_args()`

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


1. `[ ]`
1. `[ ]`
1. `[ ]`
1. `[ ]`
1. `[ ]`
    * `[ ]`
1. `[ ]`
    * `[ ]`
