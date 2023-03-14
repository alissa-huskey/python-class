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
Part 9: Refactoring
===================

In this section we are going to work on refactoring our game.
{term}`Refactoring <refactoring>` is when you change code to make the code
better, but without changing what the software does.

It is key to make changes in small, incremental steps which are tested
regularly to ensure the program works properly throughout. Avoid tearing out
and reworking vast swaths of code at a time, which will often leave you with a
hopeless tangle of broken code.

Here we'll be focusing on the {term}`DRY`[^DRY] principle--don't repeat
yourself. This means that when you notice you're repeating the same, or nearly
the same, code over and over again, find a way to put it somewhere it can be
reused. In this case we'll be adding a few functions, then call those functions
in the places where the same code is repeated.

[^DRY]: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

Part 9.1: Add `abort()`
-----------------------

{{ source | format("adventure-9.1.py") }}

The `abort()` function will be similar to the `error()` function, except it
will exit the game immediately. This function will be for errors that only
happen if there is a problem with the code, as opposed to errors that can be
caused by something the user typed in.

(This will actually result in a minor change in behavior. Now, when you
encounter any errors using the `abort()` function, your game will end
immediately instead of continuing on.)

### A. Define `abort()`

The `abort()` function will simply call `error()` to print an error message,
then exit the program.

When `abort()` is called, a `return` statement will no longer be needed since
the program will end immediately.

{{ left }}

1. `[ ]` define an `abort()` function that takes one argument `message`
1. `[ ]` in `abort()`
   * `[ ]` call `error()` with the argument `message`.
   * `[ ]` call the built-in `exit()` function and pass it the argument `1`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.1.py
:linenos:
:lineno-match:
:pyobject: 'abort'
```

`````

{{ endcols }}

### B. Modify `do_take()`

Since we always expect to be able to find an item in the `ITEMS` dictionary for
a key in the `place` items list, if we fail to find one that means that we
messed something up, not the player. This is a perfect place to use `abort()`
instead of `error()`.

Then because `abort()` exits the program immediately, we can remove the `return`.

{{ left }}

1. `[ ]` Call `abort()` instead of `error()` when you check if `item` is {term}`falsy`
1. `[ ]` remove the `return` statement
1. `[ ]` To test, temporarily change the key for `"book"` to something
         else, then type `take book` from home. It should print an error message
         then exit the program. After verifying that it works, change it back.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.1.py
:linenos:
:lineno-match:
:start-at: 'def do_take'
:end-before: 'if not item.get("can_take")'
:emphasize-lines: "28"
```

`````

{{ endcols }}

### C. Modify `do_examine()`

This is nearly exactly the same as the previous section.

{{ left }}

1. `[ ]` Call `abort()` instead of `error()` when you check if `name` is not in `ITEMS`
1. `[ ]` remove the `return` statement
1. `[ ]` To test, temporarily change the key for `"book"` to something
         else, then type `take book` from home. It should print an error message
         then exit the program. After verifying that it works, change it back.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.1.py
:linenos:
:lineno-match:
:start-at: 'def do_examine'
:end-before: '# get the item dictionary'
:emphasize-lines: "25"
```

`````

{{ endcols }}

### D. Modify `do_go()`

Similar to the previous two sections, we always expect to be able to find an
place in the `PLACES` dictionary for a key from another `place` dictionary, so
if we don't it means there's an error somewhere in the code.


{{ left }}

1. `[ ]` Call `abort()` instead of `error()` when you check if `new_place` is {term}`truthy`
1. `[ ]` remove the `return` statement
1. `[ ]` To test, temporarily change the value for `home["east"]` to something
         else, then type `go east` from home. It should print an error message
         then exit the program. After verifying that it works, change it back.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.1.py
:linenos:
:lineno-match:
:start-at: 'def do_go'
:end-before: '# move the player to the new place'
:emphasize-lines: "38"
```

`````

{{ endcols }}

Part 9.2: Add `get_place()`
---------------------------

{{ source | format("adventure-9.2.py") }}

Since we're so often needing to get place information from the `PLACES`
dictionary, we'll wrap this functionality into a function called `get_place()`
that we can call from anywhere in our program where we need to get place
information.

### A. Define `get_place()`

The `get_place()` function will take one argument, the `key` to get from the
`PLACES` dictionary. We'll make that argument optional though, and set the
default to `None`.

If the user passes a `key` argument, then we'll get the place information from
`PLACES` for that `key`. If they don't, we'll get the key from the `PLAYER`
dictionary for their current location. That way we can call `get_place()` with
no args to get the current place.

This function will also check to make sure the place is found in the `PLACES`
dictionary, and call `abort()` if it is not. That means that anywhere we call
`get_place()` will not have to do that error handling over and over.


{{ left }}

1. `[ ]` define a `get_place()` function that takes one optional argument `key` with a default value of `None`
1. `[ ]` if `key` is {term}`falsy` then assign `key` to the value of the `PLAYER` dict associated with the `"place"` value
1. `[ ]` get the value from the `PLACES` dictionary associated from the `key` key and assign it to the variable `place`
1. `[ ]` If `place` is {term}`falsy`,
     * `[ ]` Use the `abort()` function to print an error message like:

       {samp}`"Woops! The information about the place {name} seems to be missing."`
1. `[ ]` return `place`


{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'get_place'
```

`````

{{ endcols }}

### B. Modify `do_go()`

{{ left }}

1. `[ ]` Call `get_place()` with no arguments to get the value for `old_place`.
         (This will replace the existing `PLACES[old_place]`.)
1. `[ ]` Remove the line assigning `old_name` since that is taken care of in `get_place()`
1. `[ ]` Call `get_place()` with the argument `new_name` to get the value for `new_place`.
         (This will replace the existing `PLACES.get(new_place)`.)
1. `[ ]` Remove the lines that calls `abort()` if `new_place` is {term}`falsy`.


{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_go'
:emphasize-lines: '20, 31'
```

`````

{{ endcols }}

### C. Modify `do_look()`

1. `[ ]` Replace the existing value for `place` with a call to `get_place()`.
1. `[ ]` Remove the line assigning `place_name` since that is taken care of in `get_place()`
1. `[ ]` Replace the existing value for `destination` with a call to `get_place()` with the argument `name`.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_look'
:emphasize-lines: '7, 51'
```

`````

### D. Modify `do_take()`, `do_examine()` and `do_drop()`

1. `[ ]` Replace the existing value for `place` with a call to `get_place()`.
1. `[ ]` Remove the line assigning `place_name` since that is taken care of in `get_place()`

`````{dropdown} do_take()

```{literalinclude} ../../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_take'
:emphasize-lines: '15'
```

`````

`````{dropdown} do_examine()

```{literalinclude} ../../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_examine'
:emphasize-lines: '12'
```

`````

`````{dropdown} do_drop()

```{literalinclude} ../../../pythonclass/adventure/adventure-9.2.py
:linenos:
:lineno-match:
:pyobject: 'do_drop'
:emphasize-lines: '26'
```

`````

Part 9.3: Add `get_item()`
--------------------------

{{ source | format("adventure-9.3.py") }}

In this section we'll be adding a `get_item()` function which will be very
similar to `get_place()` but for items instead of places.

### A. Define `get_item()`

The `get_item()` function will be almost exactly like `get_place()`. It will
also take one argument, the `key` to get from the `ITEMS` dictionary, but it
will not be optional. We'll call `abort()` if the `key` is not in the `ITEMS`
dictionary and finally return the `item` otherwise.


{{ left }}

1. `[ ]` define a `get_item()` function that takes one argument `key`
1. `[ ]` use the `.get()` method on the `ITEMS` dictionary to get the value associated from the `key` key and assign it to the variable `item`
1. `[ ]` If `item` is {term}`falsy`,
     * `[ ]` Use the `abort()` function to print an error message like:

       {samp}`"Woops! The information about the item {name} seems to be missing."`
1. `[ ]` return `item`


{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'get_item'
```

`````

{{ endcols }}

### B. Modify `do_look()` and `do_inventory()`: call `get_item()`

Throughout the rest of the program, you'll replace anywhere that you get an
item from the `ITEMS` dictionary using {term}`subscription` or the `.get()`
method with a call to `get_item()`.

1. `[ ]` Call `get_item()` with the argument `name` or `key` to get the value
   for `item`. This will replace the existing {samp}`ITEMS.get({key})` or
   {samp}`ITEMS[{key}]`.

`````{dropdown} do_look()

```{literalinclude} ../../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'do_look'
:emphasize-lines: "23"
```

`````

`````{dropdown} do_inventory()

```{literalinclude} ../../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'do_inventory'
:emphasize-lines: "13"
```

`````

### C. Modify `do_examine()` and `do_take()`: call `get_item()`

In these functions we'll do a similar replacement as above. Additionally, we'll
remove error handling that is done in `get_item()`.

1. `[ ]` Call `get_item()` with the argument `name` or `key` to get the value
   for `item`. This will replace the existing {samp}`ITEMS.get({key})` or
   {samp}`ITEMS[{key}]`.
1. `[ ]` Remove the lines that calls `abort()` if `item` is {term}`falsy` or if
   `name` is not in `ITEMS`.


`````{dropdown} do_examine()

```{literalinclude} ../../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'do_examine'
:emphasize-lines: "23"
```

`````

`````{dropdown} do_take()

```{literalinclude} ../../../pythonclass/adventure/adventure-9.3.py
:linenos:
:lineno-match:
:pyobject: 'do_take'
:emphasize-lines: "23"
```

`````

Part 9.4: Validation functions
------------------------------

{{ source | format("adventure-9.4.py") }}

In this section we'll be several functions return `True` or `False` so that
they can be used for things we commonly need to check. Specifically the
functions `player_has()`, `place_has()`, and `is_for_sale()`.

### A. Define `player_has()`

The `player_has()` function will return `True` if the player has a particular
item in inventory.


1. `[ ]` define a `player_has()` function that takes one argument `key`, and an optional argument `qty` with a default value of `1`
1. `[ ]` Check if the `key` is in the players inventory (stored in the `PLAYER`
         dict with the `"inventory"` key), and if so, if the value is greater than or
         equal to `qty`.
    * `[ ]` If so, return `True`
    * `[ ]` If not, return `False`


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: 'player_has'
```

`````

### B. Modify `do_drop()`: call `player_has()`

Now in our if statements where we check the same thing we can replace it with a
call to `player_has()`.


1. `[ ]` Find the if statement where we check to see if the item is in not inventory.
1. `[ ]` Replace the part of the condition that checks with a call to
         `player_has()` and pass the argument `name()`. (Be sure to keep the `not`.)


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_drop
:emphasize-lines: "16"
```

`````

### C. Call `player_has()` from `do_examine()`

1. `[ ]` Find the if statement where we check to see if the item is not in
         either the current place or the inventory.
1. `[ ]` Replace the part of the condition that checks with a call to
         `player_has()` and pass the argument `name()`. (Be sure to keep the
         `not`, as well as the part that checks if the item is in the current
         place.)


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_examine
:emphasize-lines: "18"
```

`````

### D. Define `place_has()`

The `place_has()` function will return `True` if the place has a particular
item.


1. `[ ]` define a `place_has()` function that takes one argument `item`.
1. `[ ]` In the function get the current place by calling `get_place()` assign it to the variable `place`.
1. `[ ]` Check if the `item` is in the list of items in the current place by
         using the `.get()` method on `place` with the key `"items"`.
    * `[ ]` If so, return `True`
    * `[ ]` If not, return `False`


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: 'place_has'
```

`````

### E. Call `place_has()` from `do_take()`

Now in our if statements where we check the same thing we can replace it with a
call to `place_has()`.


1. `[ ]` Find the if statement where we check to see if the item is not in the current place.
1. `[ ]` Replace the part of the condition that checks with a call to
         `place_has()` and pass the argument `name()`. (Be sure to keep the `not`.)


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_take
:emphasize-lines: "18"
```

`````

### F. Call `place_has()` from `do_examine()`

Now in our if statements where we check the same thing we can replace it with a
call to `place_has()`.


1. `[ ]` Find the if statement where we check to see if the item is not in the current place.
1. `[ ]` Replace the part of the condition that checks with a call to
         `place_has()` and pass the argument `name`. (Be sure to keep the
         `not` as well as the part that checks if the player has the item.)


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_examine
:emphasize-lines: "18"
```

`````

### G. Define `is_for_sale()`

The `is_for_sale()` function will return `True` if an item is for sale.

1. `[ ]` Define a `is_for_sale()` function that takes one argument, `item`.
1. `[ ]` Check if the `"price"` key is in the `item` dictionary.
    * `[ ]` If so, return `True`
    * `[ ]` If not, return `False`


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: is_for_sale
```

`````

### H. Call `is_for_sale()` from `do_shop()`

Now in our if statements where we check the same thing we can replace it with a
call to `is_for_sale()`.


1. `[ ]` Find the if statement where we check to see if the `"price"` key is in an `item` dictionary
1. `[ ]` Replace the part of the condition that checks with a call to
         `is_for_sale()` and pass the argument `item`. (Be sure to keep the `not`.)


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.4.py
:linenos:
:lineno-match:
:pyobject: do_shop
:emphasize-lines: "7"
```

`````

Part 9.5: Add `inventory_change()`
----------------------------------

{{ source | format("adventure-9.5.py") }}

In this section we'll be adding an `inventory_change()` function that will add
or remove items from the players inventory.

### A. Define `inventory_change()`

The `inventory_change()` function will handle either adding items to a player's
inventory or removing from it. We'll use an optional argument `quantity` for
the number to add. (If the number is negative, then it the quantity will be
subtracted.)

In this function we'll use the `.setdefault()` method on the inventory
dictionary. This is kind of like the inverse of the `.get()` method--if the `key`
is not currently in the dictionary, it will set it `default` value. Otherwise,
nothing will happen.[^setdefault]

Once we are done changing the quantity in inventory, we'll remove the entire
item from dictionary if there is `0` (or less) of them left. This way items
with a zero quantity won't show up in `do_inventory()`.


1. `[ ]` Define a `inventory_change()` function that takes one argument `key`,
         and an optional argument `quantity` with a default value of `1`
1. `[ ]` Call the `.setdefault()` method on the players inventory (accessed in
         the `PLAYER` dict with the `"inventory"` key) with the arguments `key`
         and `0` for the default.
1. `[ ]` Add `quantity` to the players inventory (accessed in the `PLAYER` dict
         with the `"inventory"` key) for the `key` key.

   *Hint: Use the `+=` operator.*
1. `[ ]` Check if the value associated with `key` in the players inventory is
         {term}`falsy`, or if it is less than or equal to zero.
    * `[ ]` If so, remove that key from the player's inventory by calling the
            `.pop()` method on the inventory dictionary with the `key` argument.

[^setdefault]: See `help(dict.setdefault)` in a python/iPython shell for more information.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.5.py
:linenos:
:lineno-match:
:pyobject: 'inventory_change'
```

`````

### B. Call `inventory_change()` in `do_take()`

Now we can call `inventory_change()` anytime we want to add or remove something
from inventory. Let's start in the `do_take()` function. Since we currently can
only have one of something in a room at a time, we won't pass the `quantity`
argument, so it will default to `1`.

{{ left }}


1. `[ ]` Find where you add the item to the player's inventory. Replace those
         lines with a call to `inventory_change()` and pass the `name` argument.

{{ right }}


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.5.py
:linenos:
:lineno-match:
:pyobject: 'do_take'
:emphasize-lines: 30
```

`````

{{ endcols }}

### C. Call `inventory_change()` in `do_drop()`

Next, we'll call it from `do_drop()`.

Here we'll be subtracting from inventory by passing in a negative value for
quantity by putting a `-` in front of the value. Then when the negative number
is added to the current inventory value in `inventory_change()`, it will be the
same as if we had subtracted a positive number.

We run into a little issue, since we can have more than one of something in the
player's inventory, but only one of something in a place. To account for this,
we'll zero out that item in inventory and only add one item to place. (Someday
we may want to make the place `"items"` a dictionary instead of a list so we
can have more than one of a thing in a particular place, but this will have to
do for now.)

{{ left }}


1. `[ ]` Find where you remove the item from the player's inventory. Right above
         that, get the amount the player has in their inventory (stored in the `PLAYER`
         dict with the `"inventory"` key) using the `name` key and assign it to the
         `qty` variable.
1. `[ ]` Replace the lines where you add to the inventory with a call to
         `inventory_change()` with the arguments `name` and `-qty`.

{{ right }}


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.5.py
:linenos:
:lineno-match:
:pyobject: 'do_drop'
:emphasize-lines: "20-24"
```

`````

{{ endcols }}

Part 9.6: Add `place_add()`
---------------------------

{{ source | format("adventure-9.6.py") }}

In this section we'll be adding an `place_add()` function that will add
an item to the current place.

### A. Define `place_add()`

The `place_add()` function will take care of looking up the current place,
making sure that the places `"items"` dictionary is set to an empty list if
it's missing, making sure that it's not already in the place, and finally
adding the item key to the place list.

1. `[ ]` Define a `place_add()` function that takes one argument `key`.
1. `[ ]` Get the current place by calling `get_place()` and assign it to the
         variable `place`.
1. `[ ]` Call `.setdefault()` on `place` with the arguments `"items"` and an
         empty list.
1. `[ ]` Check if `key` is in the `place["items"]` list
    * `[ ]` If not, append `key` to the `place["items"]` dict

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.6.py
:linenos:
:lineno-match:
:pyobject: 'place_add'
```

`````

### B. Call `place_add()` in `do_drop()`

Now we can call `place_add()` anytime we want to add something to a place.
Right now, this only happens in the `do_drop()` function.

{{ left }}


1. `[ ]` Find where you add the item to the place. Replace those lines with a
         call to `place_add()` and pass the `name` argument.
1. `[ ]` You can also remove the line where you get the current place using the
        `get_place()` function.


{{ right }}


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.6.py
:linenos:
:lineno-match:
:pyobject: 'do_drop'
:emphasize-lines: 27
```

`````

{{ endcols }}

Part 9.7: Add `place_remove()`
------------------------------

{{ source | format("adventure-9.7.py") }}

In this section we'll be adding an `place_remove()` function that will remove
an item from the current place.

### A. Define `place_remove()`

The `place_remove()` function will take care of looking up the current place,
making sure that the item is in the place, and finally removing the item key
from the place list.

1. `[ ]` Define a `place_remove()` function that takes one argument `key`.
1. `[ ]` Get the current place by calling `get_place()` and assign it to the
         variable `place`.
1. `[ ]` Check if `key` is in the current place by calling `.get()` on `place`
         and passing the arguments `key` and an empty list for the default value.
    * `[ ]` If so, call `.remove()` on `place["items"]` with the `key` argument

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.7.py
:linenos:
:lineno-match:
:pyobject: 'place_remove'
```

`````

### B. Call `place_remove()` in `do_take()`

Now we can call `place_remove()` anytime we want to remove something from a
place.  Right now, this only happens in the `do_take()` function.

{{ left }}


1. `[ ]` Find where you remove the item from the place. Replace those lines
    with a call to `place_remove()` and pass the `name` argument.
1. `[ ]` You can also remove the line where you get the current place using the
        `get_place()` function.


{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-9.7.py
:linenos:
:lineno-match:
:pyobject: 'do_take'
:emphasize-lines: 30
```

`````

{{ endcols }}
