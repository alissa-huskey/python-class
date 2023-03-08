---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'
  icon: '{opticon}`file-code`'

  # green "source code" badge linking to my github
  # usage: {{ source | format("filename.py") }}
  source: |
    ```{div} float-right
      {bdg-link-info-line}`source code <https://github.com/alissa-huskey/python-class/blob/master/pythonclass/adventure/%s>`
    ```
  # two green badges, one for adventure-VERSION.py and one for test_game-VERSION.py
  # usage: {{ sources.format("VERSION") }}
  # note: double curley braces make one literal brace (for .format())
  sources: |
    ```{{div}} float-right
    {{{{ code.format("adventure.py", "adventure/adventure-{0}.py") }}}} {{{{ code.format("test_game.py", "adventure/test_game-{0}.py") }}}}
    ```


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
Part 10: Buy things
===================

In this section we'll add the buy command, add the market, make sure that the
buy and shop commands only work in the market, and make add information to the
buy shop and examine commands.

{{ source | format("adventure-10.1.py") }}

Part 10.1: Add market
---------------------

{{ clear }}

{{ left }}

First we'll need to add the market to our `PLACES` dictionary so we can
navigate to and from there.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-10.1.cast
:poster: npt:0:04
:speed: 0.5
:rows: 16
```

`````

{{ endcols }}

### A. Add market to `PLACES`

{{ left }}

1. `[ ]` Add a `"market"` dictionary to your `PLACES` dictionary.
   * `[ ]` Be sure to add the relevant directions. For example, since I have it just north of `"town-square"`
           I have `"south": "town-square"`.  But you can put it somewhere else if
           it suits you.
   * `[ ]` Also add the `"items"` list with a list of keys of the items that
           are for sale in the market. For example, I have `"book"` and
           `"dagger"` in mine.
1. `[ ]` Add the direction values to the other adjacent place dictionaries. For
         example, in my `"town-square"` dictionary I have `"north": "market"`.
1. `[ ]` Test this by making sure you can get to and from the market.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.1.py
:linenos:
:lineno-match:
:start-at: 'PLACES = {'
:end-before: 'ITEMS ='
:emphasize-lines: "13, 19-28"
```

`````
{{ endcols }}

### B. In `do_shop()` get items from the market

Now that we have a legit market, we can get our items from the market rather
than going through all items.

1. `[ ]` At the beginning of the `do_shop()` function, get the market
         dictionary by calling `get_place()` and assign it to the variable `place`.
1. `[ ]` Change your for loop, instead of iterating over `ITEMS.values()`, use the
         `.get()` method on `place` with the arguments `"items"` and an empty list, and
         iterate over that instead. Also rename the variable from `item` to `key`.
1. `[ ]` Inside the for loop at the beginning, call `get_item()` with the
         argument `key` and assign it to the variable `item`.

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.1.py
:linenos:
:lineno-match:
:pyobject: do_shop
:emphasize-lines: "4, 8-9"
```

`````

{{ source | format("adventure-10.2.py") }}

Part 10.2: Add `place_can()`
----------------------------

{{ clear }}

{{ left }}

Some commands can only happen when you are in a particular place. The way we
initially wrote the `do_shop()` function, you can shop from anywhere. Now we're
going to store some extra information on place dictionaries to let us know if
the action is restricted to certain places.

Similar to place `"items"`, we'll store this information as a list of strings,
this time with the key `"can"`.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-10.2.cast
:poster: npt:0:02
:speed: 0.5
:rows: 16
```

`````

{{ endcols }}


### A: In `PLACES` add `"can"` list to market

In the next section we'll write a function to use that information.

{{ left }}

1. `[ ]` In your `market` place dictionary, add the key `"can"`; and for the
         value a list with one item, `"shop"`.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.2.py
:linenos:
:lineno-match:
:start-at: '"market": {'
:end-at: '},'
:emphasize-lines: "6"
```

`````

{{ endcols }}

### B: Define `place_can()`

The `place_can()` function will let us know if a place supports a particular
action. This function will be very similar to the `place_has()` function, but
for actions instead of items.

1. `[ ]` Add the `place_can()` function that takes one argument, `action`.
1. `[ ]` Get the current place by calling `get_place()` and assign it to the variable `place`
1. `[ ]` Check if `action` is not in the list of place items by calling
         `.get()` on `place` with the key `"can"` and an empty list for the default
         argument.
   * `[ ]` If so, return `True`
   * `[ ]` Otherwise, return `False`

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.2.py
:linenos:
:lineno-match:
:pyobject: place_can
```

`````

### C: Call `place_can()` from `do_shop()`

{{ left }}

1. `[ ]` In `do_shop()` at the very beginning of the function check if shopping
         is supported in the current place by calling `place_can()` with the
         argument `"shop"`.
   * `[ ]` If not, print an error message like {samp}`Sorry, you can't {action} here.` then return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.2.py
:linenos:
:lineno-match:
:pyobject: do_shop
:emphasize-lines: "4-6"
```

`````

{{ endcols }}

{{ source | format("adventure-10.3.py") }}

Part 10.3: Add buy command
--------------------------

{{ clear }}

{{ left }}

Now we'll add the buy command.

{{ right }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-10.3.cast
:poster: npt:0:26
:speed: 0.75
:rows: 16
```

`````

{{ endcols }}

### A. Add game info

First we'll need to give the player some gems, add buy to the market `"can"`
list, and add gems to the items list.

{{ left }}

1. `[ ]` For now, let's give the player some free gems so we can test out
         buying things. Add a `"gems"` key to the `PLAYER` inventory dictionary with a
         value of `50` or so.
1. `[ ]` In the `PLACES` dictionary, add a `"buy"` to the `"can"` list to the market dictionary.
1. `[ ]` In `ITEMS` add a `"gems"` item.

{{ right }}

`````{dropdown} PLAYER

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'PLAYER ='
:end-before: 'PLACES ='
:emphasize-lines: 3
```

`````

`````{dropdown} PLACES

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'PLACES ='
:end-before: 'ITEMS ='
:emphasize-lines: 24
```

`````

`````{dropdown} ITEMS

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'ITEMS ='
:end-before: '# Message functions'
:emphasize-lines: "30-36"
```

`````

{{ endcols }}


### B: Define a `do_buy()` function

Here we'll define the function that is called when the player types `"buy"`.

{{ left }}

1. `[ ]` Define a `do_buy()` function that takes one argument, `args`
1. `[ ]` In it, use the `debug()` function to print something like {samp}`Trying to buy {args}.`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-at: 'debug'
```

`````

{{ endcols }}

### C: In `main()`

{{ left }}

1. `[ ]` Add an `elif` that checks if `command` is equal to `buy`
   * `[ ]` If so, call `do_buy()` and pass `args`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:pyobject: main
:emphasize-lines: "40-41"
```

`````

{{ endcols }}

### D: In `do_buy()`, Make sure the place supports buying

{{ left }}

1. `[ ]` Check if you can buy things in the current place buy calling `place_can()` with the argument `"buy"`.
   * `[ ]` If not, print a message like {samp}`Sorry, you can't buy things here.` then return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-at: 'return'
:emphasize-lines: "6-8"
```

`````

{{ endcols }}

### E: Still in `do_buy()`, make sure the player typed in something to buy

{{ left }}

1. `[ ]` Check if `args` is {term}`falsy`
   * `[ ]` If so, print a message with the `error()` function like `What do you want to buy?` then return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-before: '# get the item name'
:emphasize-lines: "10-13"
```

`````

{{ endcols }}

### F: Still in `do_buy()`, make sure the item is in this place

{{ left }}

1. `[ ]` assign the first item of the `args` list to the variable `name` and make it lowercase
1. `[ ]` check if the item is in this place by calling `place_has()` with the argument `name`
   * `[ ]` if not, print an error message `"Sorry, I don't see a {name} here."` then return

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-before: '# get the item info'
:emphasize-lines: "15-22"
```

`````

{{ endcols }}

### G. Still in `do_buy()`, make sure the item is for sale

{{ left }}

1. `[ ]` Get the item dictionary by calling `get_item()` with the
         argument `name` and assign it to the variable `item`.
1. `[ ]` Check if the item is for sale by calling `is_for_sale()` with the argument `item`
   * `[ ]` If not print an error message like {samp}`Sorry, {name} is not for sale` then return
1. `[ ]` To test this, add another item that is not for sale to the `market`,
         or temporarily remove the `"price"` from one of the items in your market.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-before: 'price ='
:emphasize-lines: "24-29"
```

`````

{{ endcols }}

### H. Still in `do_buy()`, make sure the player can afford the item

{{ left }}

1. `[ ]` Get the price from the item dictionary, and make it positive (if
         necessary) by calling `abs()`, then assign it to the variable `price`
1. `[ ]` Check if the player has enough gems by calling `player_has()` with the
         arguments `"gems"` and `price`. If not:
   * `[ ]` Get the number of gems the player currently has from the `PLAYER`
           inventory dictionary by calling the `.get()` method with the arguments
           `"gems"` and `0` for the default value. Assign it to the variable `gems`.
   * `[ ]` Print an error message like {samp}`Sorry, you can't afford {name} because it costs {price} and you only have {gems}.`
   * `[ ]` return
1. `[ ]` To test this, temporarily change the price of one of your items to be more than the amount of gems you have.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:start-at: 'def do_buy'
:end-before: '# remove gems'
:emphasize-lines: "31-35"
```

`````

{{ endcols }}

### I. In `do_buy()`, buy the item

{{ left }}

1. `[ ]` Remove gems from inventory by calling `inventory_change()` with the values `"gems"` and negative `price`.
1. `[ ]` Add the item to inventory by calling `inventory_change()` with the value `name`
1. `[ ]` Remove the item from the current place by calling `place_remove()` with the argument `name`
1. `[ ]` Print a message like {samp}`"You bought {name}."`

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.3.py
:linenos:
:lineno-match:
:pyobject: 'do_buy'
:emphasize-lines: "37-"
```

`````

{{ endcols }}


{{ source | format("adventure-10.4.py") }}

Part 10.4: Clean up the shop
----------------------------

{{ clear }}

{{ leftcol | replace("col", "col-2") }}

In this section we'll make a number of small changes to improve the shop and examine commands.

{{ rightcol | replace("col", "col-10") }}

`````{dropdown} Demo
:open:

```{screencast} assets/adventure-10.4.cast
:poster: npt:0:06
:speed: 0.5
:rows: 16
```

`````

{{ endcols }}

### A: Show price in `do_shop()`

We should add the price to the information we print out about each item. This
is also a good chance to make this look prettier.

{{ left }}

1. `[ ]` Print the `item` `"price"` along with the name and description. If the
         number is negative, call `abs()` to make it a positive number.
1. `[ ]` Use [string formatting](../../lessons/string-formatting-part-1) to align
         the information into columns.

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.4.py
:linenos:
:lineno-match:
:pyobject: do_shop
:emphasize-lines: 17
```

`````

{{ endcols }}

### B. Handle long descriptions

If your item descriptions are too long for a single line, you can do either one
of the following.

#### I. Truncate the description

The simplest way to handle too-long descriptions is to truncate them so that
they are all limited to a specific width. There are a few ways to do this, but
here we'll use the `textwrap.shorten()` function.

1. `[ ]` In your for loop, before you call `write()` to print the line, call
         `textwrap.shorten()` with two arguments: the item description, and the desired
         maximum width. Assign it to the variable `description`.
1. `[ ]` In the argument to your `write()` function, replace
         `item["description"]` with `description`.

`````{dropdown} Code

```{code-block}
:linenos:
:lineno-start: 233
:emphasize-lines: "17-18"

def do_shop():
    """List the items for sale."""

    if not place_can("shop"):
        error(f"Sorry, you can't {action} here.")
        return

    place = get_place()

    header("Items for sale.")

    for key in place.get("items", []):
        item = get_item(key)
        if not is_for_sale(item):
            continue

        description = textwrap.shorten(item["description"], 30)
        write(f'{item["name"]:<13}  {description:<30} {abs(item["price"]):>2} gems')

    print()
```

`````

#### II. Add a short `"summary"` to items dictionary

Another way to deal with the problem is to separate the long `"description"`
from a shorter `"summary"` in the `ITEMS` dictionaries. Then here in
`do_shop()` we'll print the `"summary"`, and in `do_examine()` we'll show the
longer description.

This is fancier, but it will require coming up with more data for each item in
your game.

1. `[ ]` In each dictionary in `ITEMS` add a key `"summary"` with a one-line
         description of the item.
1. `[ ]` In `do_shop` when printing the item information, replace
        `item["description"]` with `item["summary"]`.

`````{dropdown} ITEMS

```{code-block}
:linenos:
:lineno-start: 73
:emphasize-lines: "4-8, 14-18"

    "elixr": {
        "key": "elixr",
        "name": "healing elixr",
        "summary": "a healing elixer",
        "desc": (
            "A small corked bottle filled with a swirling green liquid. "
            "It is said to have magical healing properties."
        ),
        "price": -10,
    },
    "dagger": {
        "key": "dagger",
        "name": "a dagger",
        "summary": "a double-edged 14 inch dagger",
        "description": (
            "A double-edged 14 inch dagger with a crescent shaped hardwood "
            "grip, metal cross guard, and curved studded metal pommel."
        ),
        "price": -25,
    },
```

`````

`````{dropdown} do_shop()

```{code-block}
:linenos:
:lineno-start: 233
:emphasize-lines: "17"

def do_shop():
    """List the items for sale."""

    if not place_can("shop"):
        error(f"Sorry, you can't {action} here.")
        return

    place = get_place()

    header("Items for sale.")

    for key in place.get("items", []):
        item = get_item(key)
        if not is_for_sale(item):
            continue

        write(f'{item["name"]:<13}  {items["summary"]:<30} {abs(item["price"]):>2} gems')

    print()
```

`````

### C. Show price in `do_examine()`

Let's show the price to `do_examine()` if we're in the market (or somewhere else
where we can shop).

1. `[ ]` In `do_examine()` after the header, check if:
   * the place supports shopping by calling `place_can()` with the argument `"shop"` and
   * the place has the item by calling `place_has()` with the argument `name` and
   * the item is for sale by calling `is_for_sale()` with the argument `item`

   If so:
   * `[ ]` print the `item` `"price"`


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.4.py
:linenos:
:lineno-match:
:pyobject: do_examine
:emphasize-lines: "28-31"
```

`````

### D. Show inventory quantity in `do_examine()`

1. `[ ]` Check if the player has the item in inventory by calling `player_has()` with the argument `name`. If so:
   * `[ ]` Print the quantity from the `PLAYER` inventory dictionary for `name`.


`````{dropdown} Code

```{literalinclude} ../../../pythonclass/adventure/adventure-10.4.py
:linenos:
:lineno-match:
:pyobject: do_examine
:emphasize-lines: "33-36"
```

`````
