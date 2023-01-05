from copy import deepcopy

import pytest
from parametrization import Parametrization

import adventure
from adventure import (
    health_bar,
    debug,
    do_drink,
    do_drop,
    do_eat,
    do_read,
    error,
    header,
    health_change,
    inventory_change,
    is_for_sale,
    place_has,
    player_has,
    place_add,
    wrap,
    write,
)

def setup_module(module):
    """Initialize global state variables. Should be run once."""
    global PLAYER_STATE, PLACES_STATE, ITEMS_STATE, DEBUG_STATE

    PLAYER_STATE = deepcopy(adventure.PLAYER)
    PLACES_STATE = deepcopy(adventure.PLACES)
    ITEMS_STATE = deepcopy(adventure.ITEMS)
    DEBUG_STATE = True

def teardown_function(function):
    """Revert game data to its original state."""
    adventure.PLAYER = deepcopy(PLAYER_STATE)
    adventure.PLACES = deepcopy(PLACES_STATE)
    adventure.ITEMS = deepcopy(ITEMS_STATE)
    adventure.DEBUG = DEBUG_STATE

def test_is_for_sale():
    # GIVEN: a fake item with a price key
    fake_item = {
        "name": "An Expensive Thing",
        "price": "a lot",
    }

    # when: is_for_sale() is called
    result = is_for_sale(fake_item)

    # then: it should return True
    assert result, "is_for_sale() should return True if the item has a price"

def test_is_for_sale_without_price():
    # GIVEN: a fake item without a price key
    fake_item = {
        "name": "A Priceless Thing",
    }

    # WHEN: is_for_sale() is called
    result = is_for_sale(fake_item)

    # THEN: it should return False
    assert not result, \
        "is_for_sale() should return False if the item doesn't have a price"

def test_error(capsys):
    # WHEN: error() is called
    error("You ruined everything.")

    # THEN: the error message should be printed
    output = capsys.readouterr().out

    assert "You ruined everything" in output, \
        "The formatted error message should be printed."

def test_debug(capsys):
    # GIVEN: that debug mode is enabled
    adventure.DEBUG = True

    # WHEN: debug() is called
    debug("Have some cake.")

    # THEN: the debug message should be printed
    output = capsys.readouterr().out
    assert "Have some cake." in output, \
        "The formatted debug message should be printed."

def test_debug_false(capsys):
    """
      GIVEN: debug mode is disabled
      WHEN: debug() is called
      THEN: the debug message should be printed
    """
    # GIVEN: debug mode is disabled
    adventure.DEBUG = False

    # WHEN: debug() is called
    debug("Have some cake.")

    # THEN: the debug message should be printed
    output = capsys.readouterr().out
    assert output == "", \
        "No debug message should be printed if not in debug mode."


def test_header(capsys):
    # WHEN: header() is called
    header("Headline")

    # THEN: the formatted header should be printed
    output = capsys.readouterr().out
    assert "Headline" in output, \
        "The formatted header should be printed."


def test_write(capsys):
    # when write() is called
    write("oh hai")

    # THEN: the indented message should be printed followed by a new line
    output = capsys.readouterr().out
    assert output == "  oh hai\n", \
        "write() should print the indented text followed by a new line"


def test_wrap(capsys):
    # WHEN: wrap() is called
    wrap(
        "I pass through many Me's in the course of my day, "
        "each one selfish with his time. The Lying-in-Bed "
        "me and the Enjoying-the-Hot-Shower Me are particularly "
        "selfish. The Late Me loathes the pair of them."
    )

    # THEN: wrap() should print the indented, wrapped text
    output = capsys.readouterr().out
    lines = output.splitlines()

    # AND: the message should be printed
    assert "I pass through" in output, \
        "wrap() should print the text indented."

    # AND: the end of the message should be printed followed by a newline
    assert output.endswith("pair of them.\n"), \
        "wrap() should print the text"

    # AND: the long message should be broken up onto mulitple lines
    assert len(lines) > 1, "wrap() should break long text onto multiple lines"

    # AND: all lines should be indented
    assert all([line.startswith("  ") for line in lines]), \
        "wrap() should indent all lines"

    # AND: all lines should be indented 2 spaces
    assert all([line[2] != " " for line in lines]), \
        "wrap() should indent all lines 2 spaces"

def test_wrap_with_indent(capsys):
    wrap(
        "To the absolutist in every craftsman, "
        "each imperfection is a failure; "
        "to the practitioner, obsession with "
        "perfection seems a perception for failure.",
        indent=2,
    )
    output = capsys.readouterr().out
    lines = output.splitlines()

    assert "To the absolutist" in output, \
        "wrap() should print the text."

    assert output.endswith("perception for failure.\n"), \
        "wrap() should print the text"

    assert len(lines) > 1, "wrap() should break long text onto multiple lines"

    assert all([line.startswith("    ") for line in lines]), \
        "wrap() should indent all lines"

    assert all([line[4] != " " for line in lines]), \
        "wrap() should indent all lines 4 spaces"

def test_wrap_with_delay(capsys):
    message = (
        "A Dark time comes.",
        "My time.",
        "If it offends you.",
        "Stop Me.",
    )
    wrap(message, delay=0.01)

    output = capsys.readouterr().out

    assert "(" not in output, \
        "output should not contain parenthesis representing a tuple"

    assert "A Dark time comes" in output, \
        "wrap() should print the text."

    assert "\n\n  My time." in output, \
        "There should be two newlines between each printed message item"

def test_wrap_with_iterable(capsys):
    message = (
        "The exercise for centering oneself is a simple one.",

        "Stop thinking of what you intend to do. Stop thinking of what you "
        "have just done. Then stop thinking that you have stopped thinking of "
        "those things.",

        "Then you will find the now. The time that stretches eternal, and is "
        "really the only time there is.",
    )
    wrap(message)

    output = capsys.readouterr().out

    assert "The exercise for centering oneself" in output, \
        "wrap() should print the text."

    assert "(" not in output, \
        "wrap() should not contain parenthesis representing a tuple"

    assert "\n\n  Stop thinking" in output, \
        "There should be two newlines between each printed message item"

def test_health_change_add():
    adventure.PLAYER["health"] = 50
    impact = health_change(10)

    assert impact == 10, \
        "health_change() should return the amount added to health"

    assert adventure.PLAYER["health"] == 60, \
        "health_change() should add the quantity to player health"

def test_health_change_subtract():
    adventure.PLAYER["health"] = 50
    impact = health_change(-10)

    assert impact == -10, \
        "health_change() should return the amount subtracted from health"

    assert adventure.PLAYER["health"] == 40, \
        "health_change() should add the quantity to player health"

def test_health_gt_max():
    adventure.PLAYER["health"] = adventure.MAX_HEALTH
    impact = health_change(10)

    assert impact == 0, \
        "health_change() should return the amount actually added to health"

    assert adventure.PLAYER["health"] == adventure.MAX_HEALTH, \
        "health_change() should not allow health to go above MAX_HEALTH"

def test_health_lt_zero():
    adventure.PLAYER["health"] = 5
    impact = health_change(-10)

    assert adventure.PLAYER["health"] == 0, \
        "health_change() should not allow health to go below zero"

    assert impact == -5, \
        "health_change() should return the amount actually subtracted from health"

def test_inventory_change():
    adventure.PLAYER["inventory"]["problems"] = 99
    inventory_change("problems")

    assert adventure.PLAYER["inventory"]["problems"] == 100, \
        "inventory_change() with no quantity argument should add 1."

def test_teardown():
    assert "problems" not in adventure.PLAYER["inventory"], \
        "Each test should start with a fresh data set."


def test_inventory_change_missing_key():
    # GIVEN: players inventory without the desired key
    adventure.PLAYER["inventory"] = {}

    # WHEN: inventory_change() is called with a key and no quantity argument
    inventory_change("brain")

    # THEN: the key should be added to players inventory
    assert "brain" in adventure.PLAYER["inventory"], \
        "inventory_change() should add missing keys to the inventory"

    # AND: the quantity in inventory should be 1
    assert adventure.PLAYER["inventory"]["brain"] == 1, \
        "inventory_change() should add to zero if key was missing"


def test_inventory_change_subtract():
    # GIVEN: a player inventory that contains the desired key
    adventure.PLAYER["inventory"]["bottles of beer"] = 99

    # WHEN: inventory_change() is called with a negative number
    inventory_change("bottles of beer", -1)

    # THEN: the quantity in inventory should be reduced
    assert adventure.PLAYER["inventory"]["bottles of beer"] == 98, \
        "inventory_change() should reduce inventory when qty is negative"


def test_inventory_change_remove():
    # GIVEN: a player inventory that contains the desired key
    adventure.PLAYER["inventory"]["chances"] = 1

    # WHEN: inventory_change() is called with a negaive number that will result
    #       in a quantity of zero
    inventory_change("chances", -1)

    # THEN: the key should be removed from player inventory
    assert "chances" not in adventure.PLAYER["inventory"], \
        "inventory_change() should remove the item when there are none left"


def test_do_drop_no_args(capsys):
    # WHEN: do_drop() is called with an empty list
    do_drop([])
    output = capsys.readouterr().out

    # THEN: the basic debug message should be printed
    assert "Trying to drop: []" in output, \
        "Debug message should be in output"

    # AND: an error message should be printed
    assert "What do you want to drop?" in output, \
        "User error should be in output"


def test_do_drop_missing_item(capsys):
    # GIVEN: the player inventory is missing the desired key
    adventure.PLAYER["inventory"] = {}

    # WHEN: do_drop() is called
    do_drop(["anything"])

    output = capsys.readouterr().out

    # THEN: the debug mesage should be printed
    assert "Trying to drop: ['anything']" in output, \
        "Debug message should be in output"

    # AND: an error message should be printed
    assert "You don't have any 'anything'" in output, \
        "User error should be in output"


def test_do_drop(capsys):
    # GIVEN: player inventory contains the desired key
    inventory_change("mic")

    # WHEN: do_drop() is called
    do_drop(["mic"])

    output = capsys.readouterr().out

    # THEN: a debug message should be printed
    assert "Trying to drop: ['mic']" in output, \
        "Debug message should be in output"

    # AND: a success message should be printed
    assert "You set down the mic" in output, \
        "User message should be in output"

    # AND: the current user should now contain the dropped item
    assert place_has("mic"), \
        "The dropped item should be in the place"

    # AND: the player inventory should not contain the dropped item
    assert not player_has("mic"), \
        "The dropped item should not be in inventory"

def test_do_read_no_args(capsys):
    do_read([])

    output = capsys.readouterr().out

    assert "Trying to read: []" in output, \
        "Debug message should be in output"

    assert "What do you want to read?" in output, \
        "User error should be in output"

def test_do_read_missing_item(capsys):
    do_read(["missing"])

    output = capsys.readouterr().out

    assert "Trying to read: ['missing']" in output, \
        "Debug message should be in output"

    assert "Sorry, I don't know what this is: 'missing'" in output, \
        "User error should be in output"

def test_do_read_unreadable_item(capsys):
    adventure.ITEMS["your mind"] = {"name": "Your mind"}
    place_add("your mind")

    do_read(["your mind"])
    output = capsys.readouterr().out

    assert "Sorry, I can't read 'your mind'" in output, \
        "User error should be in output"


def test_do_read_in_place(capsys):
    # GIVEN: an item title and message exists
    title = "After studying your palm I see..."

    # AND the message is iterable
    message = (
        "The break in your line of fate may indicate "
        "a change in location or career.",

        "You have more than one life line, which may "
        "indicate you are a cat",
    )

    adventure.ITEMS["your palm"] = {
        "name": "Your palm",
        "title": title,
        "message": message,
    }

    # AND: it's in the current place
    place_add("your palm")

    # WHEN: the player tries to read the item
    do_read(["your palm"])
    output = capsys.readouterr().out

    # THEN: the title should be in output
    assert "After studying your palm I see..." in output, \
        "The writing title {title!r} should be in output"

    # AND: the message should be in output
    assert "The break in your line of fate" in output, \
        "The writing message {message!r} should be in output"

    # AND: there should be two lines between each message item
    assert "\n\n      You have more than" in output, \
        "When message is an iterable, there should be two lines between each item"


def test_do_read_in_inventory(capsys):
    title = "After studying the leaves I see..."
    message = "Your future is uncertain."

    adventure.ITEMS["tea leaves"] = {
        "name": "Tea Leaves",
        "title": title,
        "message": message,
    }

    inventory_change("tea leaves")

    do_read(["tea leaves"])
    output = capsys.readouterr().out
    lines = output.splitlines()

    assert "After studying the leaves I see..." in output, \
        "The writing title {title!r} should be in output"

    assert lines[-1] == "      Your future is uncertain.", \
        "The writing message {message!r} should be indented an extra level."

def test_do_drink_no_args(capsys):
    do_drink([])

    output = capsys.readouterr().out

    assert "Trying to drink: []" in output, \
        "Debug message should be in output"

    assert "What do you want to drink?" in output, \
        "User error should be in output"

def test_do_drink_not_in_inventory(capsys):
    adventure.ITEMS["atmosphere"] = {
        "name": "the atmosphere",
        "drink-message": (
            "You drink in the warm and cheerful atmosphere."
        ),
    }
    do_drink(["atmosphere"])

    output = capsys.readouterr().out

    assert "Sorry, you don't have any 'atmosphere' to drink." in output, \
        "User error should be in output"

def test_do_drink_not_drinkable(capsys):
    adventure.ITEMS["x"] = {
        "name": "x",
    }
    inventory_change("x")

    do_drink(["x"])

    output = capsys.readouterr().out

    assert "Sorry, you can't drink 'x'." in output, \
        "User error should be in output"

def test_do_drink_empty(capsys):
    adventure.DELAY = 0
    adventure.ITEMS["blood"] = {
        "name": "the blood of your enemies",
        "drink-message": (
            "You greedily drink up the blood of your enemies.",
            "It tastes of sweet revenge.",
        ),
        "empty": True,
    }
    inventory_change("blood")

    do_drink(["blood"])

    output = capsys.readouterr().out

    assert "You try to drink the blood of your enemies" in output, \
        "User error should be in output"


def test_do_drink_emptyable(capsys):
    adventure.DEBUG = True
    adventure.DELAY = 0
    adventure.ITEMS["tears"] = {
        "name": "tears",
        "drink-message": "You drink the delicious tears of your rivals.",
        "empty": False,
    }
    inventory_change("tears")

    do_drink(["tears"])

    output = capsys.readouterr().out

    assert "Trying to drink: ['tears']" in output, \
        "Debug message should be in output"

    assert "(" not in output, \
        "The drink message should be in output"

    assert "You drink the delicious" in output, \
        "The drink message should be in output"

    assert player_has("tears"), \
        "The item should still be in inventory"

    assert adventure.ITEMS["tears"]["empty"], \
        "But should now be empty"


def test_do_eat_with_health(capsys):
    adventure.DELAY = 0
    adventure.PLAYER["health"] = 95
    adventure.ITEMS["lies"] = {
        "name": "lies",
        "eat-message": "You eat up the beautiful lies.",
        "impact": 10,
    }
    inventory_change("lies")

    do_eat(["lies"])

    output = capsys.readouterr().out

    assert "You gain 5 health points." in output, \
        "The player should be informed of the health impact."

    assert adventure.PLAYER["health"] == 100, \
        "The item impact should be applied to the player health."


def test_do_drink(capsys):
    adventure.DELAY = 0
    adventure.ITEMS["praise"] = {
        "name": "praise",
        "drink-message": (
            "You stand back and admire your handwork...",
            "As you drink in the praise of your adoring fans."
        ),
    }
    inventory_change("praise")

    do_drink(["praise"])

    output = capsys.readouterr().out

    assert "Trying to drink: ['praise']" in output, \
        "Debug message should be in output"

    assert "(" not in output, \
        "output should not contain parenthesis representing a tuple"

    assert "You stand back" in output, \
        "The drink message should be in output"

    assert "\n\n  As you drink in" in output, \
        "The drink message should be in output"

    assert not player_has("praise"), \
        "The item should be removed from inventory."


def test_do_eat(capsys):
    adventure.DELAY = 0
    adventure.ITEMS["your feelings"] = {
        "name": "your feelings",
        "eat-message": (
            "It's the wee hours of the morning, and you're eating"
            "your feelings."
        ),
    }
    inventory_change("your feelings")

    do_eat(["your feelings"])

    output = capsys.readouterr().out

    assert "Trying to eat: ['your feelings']" in output, \
        "Debug message should be in output"

    assert "(" not in output, \
        "The eat message should be in output"

    assert "It's the wee hours" in output, \
        "The eat message should be in output"

    assert not player_has("your feelings"), \
        "The item should be removed from inventory."

def test_health_bar_70(capsys):
    health_bar(70)

    output = capsys.readouterr().out

    assert len(output) == adventure.WIDTH + 2, \
        f"The width should be {adventure.WIDTH + 2} but is: {len(output)}"

    assert "Health" in output, \
        "The title should be in output"

    assert "70%" in output, \
        "The correct percentage should be in output"

@Parametrization.autodetect_parameters()
@Parametrization.case("100", position=100)
@Parametrization.case("70", position=70)
@Parametrization.case("0", position=0)
def test_health_bar(position, capsys):
    health_bar(position)

    output = capsys.readouterr().out

    assert len(output) == adventure.WIDTH + 2, \
        f"The width should be {adventure.WIDTH + 2} but is: {len(output)}"

    assert "Health" in output, \
        "The title should be in output"

    assert f"{position}%" in output, \
        "The correct percentage should be in output"

def test_health_bar_100(capsys):
    health_bar(100)

    output = capsys.readouterr().out

    assert "100%" in output, \
        "The total should show even at 100%"

#  def test_health_bar_0(capsys):
#      health_bar(0)

#      output = capsys.readouterr().out

#      assert "0%" in output, \
#          "The total should show even at 0%"
