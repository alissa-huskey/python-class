from copy import deepcopy

import pytest

import adventure
from adventure import (
    debug,
    do_drop,
    do_read,
    do_pet,
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
    MAX_HEALTH,
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


########### meta test


def test_teardown():
    assert "problems" not in adventure.PLAYER["inventory"], \
        "Each test should start with a fresh data set."

########### game data test functions


@pytest.mark.parametrize(
    "start, amount, result, message", [
        (50, 10, 60, "a positive number should be added"),
        (50, -10, 40, "a negative number should be subtracted"),
        (20, -30, 0, "the min health should be 0"),
        (90, 20, MAX_HEALTH, f"the max health should be {MAX_HEALTH}"),
    ]
)
def test_health_change(start, amount, result, message):
    # GIVEN: The player has some health
    adventure.PLAYER["health"] = start

    # WHEN: You call health_change()
    health_change(amount)

    # THEN: The player health should be adjusted
    assert adventure.PLAYER["health"] == result, message


def test_is_for_sale():
    # GIVEN: a fake item with a price key
    fake_item = {
        "name": "An Expensive Thing",
        "price": "a lot",
    }

    # WHEN: is_for_sale() is called
    result = is_for_sale(fake_item)

    # THEN: it should return True
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


def test_inventory_change():
    adventure.PLAYER["inventory"]["problems"] = 99
    inventory_change("problems")

    assert adventure.PLAYER["inventory"]["problems"] == 100, \
        "inventory_change() with no quantity argument should add 1."


def test_inventory_change_missing_key():
    adventure.PLAYER["inventory"] = {}
    inventory_change("brain")

    assert "brain" in adventure.PLAYER["inventory"], \
        "inventory_change() should add missing keys to the inventory"

    assert adventure.PLAYER["inventory"]["brain"] == 1, \
        "inventory_change() should add to zero if key was missing"


def test_inventory_change_subtract():
    adventure.PLAYER["inventory"]["bottles of beer"] = 99
    inventory_change("bottles of beer", -1)

    assert adventure.PLAYER["inventory"]["bottles of beer"] == 98, \
        "inventory_change() should reduce inventory when qty is negative"


def test_inventory_change_remove():
    adventure.PLAYER["inventory"]["chances"] = 1
    inventory_change("chances", -1)

    assert "chances" not in adventure.PLAYER["inventory"], \
        "inventory_change() should remove the item when there are none left"


########### printing function tests


def test_error(capsys):
    # WHEN: error() is called
    error("You ruined everything.")

    # THEN: the error message should be printed
    output = capsys.readouterr().out

    assert output == "! Error You ruined everything.\n\n", \
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
    # WHEN: write() is called
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

########### command function tests


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


def test_do_pet(capsys):
    # WHEN: You call do_pet()
    do_pet([])
    output = capsys.readouterr().out

    # THEN: A debug message should be printed
    assert "Trying to pet: []" in output


def test_do_pet_cant_pet(capsys):
    # GIVEN: The player is in a place where they can't pet anything
    adventure.PLAYER["place"] = "nowhere"
    adventure.PLACES["nowhere"] = {
        "name": "The Void",
        "can": [],
    }

    # WHEN: They try to pet something
    do_pet(["red", "dragon"])
    output = capsys.readouterr().out

    # THEN: An error message should be printed
    assert "You can't do that" in output


def test_do_pet_no_args(capsys):
    # GIVEN: The player is in a place where they can pet things
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["pet"],
    }

    # WHEN: the player types "pet" with no arguments
    do_pet([])
    output = capsys.readouterr().out

    # THEN: an error message should be printed
    assert "What do you want to pet" in output


def test_do_pet_no_color(capsys):
    # GIVEN: The player is in a place where they can pet things
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {
        "name": "Somewhere out there",
        "can": ["pet"],
    }

    # WHEN: the player types "pet" with only the words "dragon" and/or "head"
    do_pet(["dragon", "head"])
    output = capsys.readouterr().out

    # THEN: an error message should be printed
    assert "What do you want to pet" in output


def test_do_pet_invalid_color(capsys):
    # GIVEN: There are three colors of dragon heads
    adventure.COLORS = ["red", "green", "blue"]

    # AND: The player is in a place where they can pet dragons
    adventure.PLAYER["place"] = "cave"
    adventure.PLACES["cave"] = {
        "name": "A cave",
        "can": ["pet"],
    }

    # WHEN: They try to pet a dragon with a color that doesn't exist
    do_pet(["purple"])
    output = capsys.readouterr().out

    # THEN: An error message should be printed
    assert "I don't see a dragon" in output


def test_do_pet_cheerful_dragon(capsys):
    # GIVEN: The player is in a place where they can pet a dragon
    adventure.PLAYER["place"] = "cave"
    adventure.PLACES["cave"] = {
        "name": "A cave",
        "can": ["pet"]
    }

    # AND: There is one color of dragon heads
    adventure.COLORS = ["red"]

    # AND: There is one dragon
    adventure.DRAGONS = [
        {"mood": "cheerful"}
    ]

    # WHEN: The player pets that head
    do_pet(["red", "dragon"])
    output = capsys.readouterr().out

    # THEN: A debug message should print
    assert "You picked the cheerful red dragon." in output
