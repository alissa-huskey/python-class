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
Graduation
==========

Congratulations, you now have created a game where you can find a clue to a
quest, make your way to a cave to complete a challenge that may either give you
treasure or cause you harm, and purchase or find items that you can eat or
drink to either heal or hurt you.

Now the culmination of this project will be for you to design and write a new
feature, then have someone play your game.

Guidelines
----------

* Your new feature should add at least one new command.
* The new command should serve some purpose towards a new or existing
  objective. For example, the `read` command exists so that the player can
  read the book that gives a clue about petting the dragons; the `buy` command
  exists so that the player has something to do with the treasure they get from
  the dragons.
* You can optionally add enhancements that makes the game nicer to play and /
  or refactor existing code to make it easier to work with.
* This might also be a good time to add more detail or better worded
  descriptions for your items and places, or add new ones to the game.
* Once you are finished, you should start by having other students play your
  game. After you are satisfied that it works well and is not confusing
  for your classmates, ask someone who is not in class to try it out.

:::{tip}

You can use [ChatGPT](https://chat.openai.com/) to generate text descriptions
for inspiration. (You'll need to sign up for an [OpenAI](https://openai.com/)
account first.) For example you could try typing `Describe a RPG-style forest`
or `Give me ten RPG-style game items`.

:::

### Design

As you think about what you would like to add to your game, here are some
questions to ask yourself.

- What is the command you wish to add?
- Does it take any arguments ? If so, is the argument associated with a
  particular item (like `read book`) or specific words (like `go east`)?
- Is the command available everywhere, or is it associated with a particular
  place?
- What information do you need in order to complete the command? For example
  when the player tries to buy an item, we need to know if the item is in the
  current place, if it is for sale, what the price is and if the player has
  enough money to buy it.
- What are all of the reasons that the command might not work? For example, if
  the player tries to drop something when it is not in inventory or tries to
  buy something when they don't have enough money.
- Does the command have an effect on the player, an item, or a place? If so,
  what data will be changed and where is it stored?
- Will you be adding any new types of things to the game? If so, where should
  the data about this new thing be stored?

  For example, the `do_take()` command required that we add the concept of a
  player's inventory which is stored in `PLAYER["inventory"]`;

  The `do_pet()` command required that we add dragons with heads of various
  colors the game, the data about which is stored in the `COLORS` and `DRAGONS`
  global dictionaries.

### Implementation

When you have a pretty clear understanding of how you want your new feature to
work, it will be time to start writing the code.

You should be accustomed to the process of adding new commands to the game at
this point, since they have all followed a pretty similar pattern.

For every step below, you start with writing the test, run your test to see it
fail (in the expected way), then add to or change your game and run the tests
again to see them pass.

1. Add a new `do_` function with a simple debug message.
2. Call the `do_` function from `main()` and pass `args` if needed.
3. Validate the player's input -- that is, make sure that the player can do
   whatever they are trying to do; if not then print an error message and return
   from the function. For example, if the player didn't include any arguments when
   required or if the thing they typed is not an item in the player's inventory
   and it should be.

   (There should be a separate test and corresponding if statement for every
   possible error a player could make.)
4. Get whatever information you need from the game data. (This may be
   interspersed with the validation from step `3`.) For example, you may need
   information about a particular item or the player's current health.
5. Make any needed changes to the data. For example, changing the items in the
  current place or the player's inventory.
6. If the command gives the player information like `examine` or `look`, print
   that information. If an action was taken, print a message about what happened.

Remember to take baby steps! Write a test for the smallest observable change
you can think of, then make the corresponding change to the code and commit
frequently.

Be sure to focus on one thing at a time--if you want to add a command and also
refactor some code and also make some enhancements to the game, don't do them
all at once! Pick either the command, refactoring, or enhancement to start
with, think through the design and finish the code before you start something
else.

Ideas
-----

If you need inspiration for things to add to your game, here are some ideas.

### Commands

- Add a `help` command that lists all commands and gives you additional
  information about what each command does.
- Add a command `debug` (with the argument `on` or `off`) and / or accept
  a command line argument `-d` / `--debug` to enable or disable debug mode.
- Add commands for items like `open` / `close`, `lift`, `throw`, `turn
  off` / `turn on`.
- Add a `fight` command and an enemy that you must defeat, perhaps with a
  particular weapon.
- Add a `jump` command to go straight to a place.
- Add search command (ie, `search rubble`).
- Add `sell` command.
- Add people you can `talk` to, `give` things to, or `ask` about things.

### Enhancements

- Add item aliases. (For example `stick` for `walking stick`.)
- Add direction aliases. (For example `e` for `east`).
- Add new directions like `in` / `out`, `up` / `down`, `over` / `under`
  and places that have those directions.
- Add a `pluralize()` function that can be used when listing items. It
  takes two arguments: `qty` (int) and `word` (str). It should return either
  the singular or plural version of `word`.

  For example: \
  `pluralize(1, "apple") == "apple"` \
  `pluralize(2, "apple") == "apples"`
- Change what happens when you pet the dragon repeatedly. For example,
  perhaps the dragon won't wake up if you try again before leaving and
  reentering the cave and/or until a certain amount of time has passed. And
  perhaps every time you enter the cave, you get a new dragon with three
  different colors of heads.
- Add a `articlize()` function that can be used when listing items in
- prose, for example in `do_look()`. It takes one argument: `word` (str). It
  should return the appropriate article for the word followed by the word.

  For example: \
  `articlize("desk") == "a desk"` \
  `articlize("elixir") == "an elixir"`

  If you have also written a `pluralize()` function, consider including an
  optional argument: `qty` (default: `None`) that will return the plualized
  version of `word` if `qty` is an integer.
-


### Refactoring

- Add validation functions that check for the things that are frequently
  required in various commands. For example, functions for `require_args()`,
  `require_valid_item()`, `require_item_in_place_or_inventory()`, etc.
- Instead of the long if statement in `main()`, store all commands in a
  `COMMANDS` dictionary then use it to look up which function to call by the
  command name or alias.
- Refactor the `wrap()` command to include optional arguments for:
  * `wrap` (default `True`): to determine if the text should be wrapped.
    (Replace all calls to `write()` with `wrap(text, wrap=False)`.)
  * `before` (default `0`): how many blank lines to add before the text.
    (Replace any calls to `print()` before calling `wrap()` with `wrap(text,
    before=1)`.
  * `after` (default `0`): how many blank lines to add after the text.
    (Replace any calls to `print()` after calling `wrap()` with `wrap(text,
    after=1)`.
  * `between` (default `1`): how many blank lines to between each stanza if
    `text` is an iterable. (Use in `do_consume()` and `do_pet()`.)
  * `delay` (default `0`): how many seconds to delay between each stanza if
    `text` is an iterable. (Use in `do_consume()` and `do_pet()`.)
-

### Advanced

- Add items that can have items. For example, the desk can have a book
  which will only be visible after you examine or search the desk.
- Add the ability to save and load a game from a file. This could be as a
  command line option and / or an interactive part of the game using a `save` /
  `load` command or a prompt at the beginning and end of the game.
- Add a `map` command that prints an ASCII rendering of the game world.
  Possibly restrict the map to the places that the player has already visited.
- Add place inventory so there can be more than one of a particular item
  in a place.
- Add a `swim` command that will reduce the player's health if they stay
  underwater too long.
- Add a place with a puzzle to solve.
- Wrap your call to `main()` in a try/except block, catch and ignore the
  following exceptions to avoid seeing error messages:
  - `EOFError`:  Sent when players hit `CTRL-D`.
  - `KeyboardInterrupt`: Sent when players hit `CTRL-C`.
- Alternately, in `main()` use the console library's `raw_mode()` to detect one
  keypress at a time and respond to the following keys. Otherwise, append to
  the command one character at a time until the enter key is detected.
  - `up` / `down`:  move forward or backward in command history
  - `CTRL-C` / `ESC`: clear the current line
  - `CTRL-D`: quit the program
  - `CTRL-S`: save the current game (if implemented)
