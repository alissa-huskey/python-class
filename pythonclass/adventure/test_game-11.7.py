from copy import deepcopy

import pytest

import adventure
from adventure import (
    debug,
    do_drop,
    error,
    header,
    inventory_change,
    is_for_sale,
    place_has,
    player_has,
    write,
)


PLAYER_STATE = deepcopy(adventure.PLAYER)
PLACES_STATE = deepcopy(adventure.PLACES)
ITEMS_STATE = deepcopy(adventure.ITEMS)
DEBUG_STATE = True


def revert():
    """Revert game data to its original state."""
    adventure.PLAYER = deepcopy(PLAYER_STATE)
    adventure.PLACES = deepcopy(PLACES_STATE)
    adventure.ITEMS = deepcopy(ITEMS_STATE)
    adventure.DEBUG = DEBUG_STATE


@pytest.fixture(autouse=True)
def teardown(request):
    """Auto-add teardown method to all tests."""
    request.addfinalizer(revert)

def test_is_for_sale():
    fake_item = {
        "name": "An Expensive Thing",
        "price": "a lot",
    }

    result = is_for_sale(fake_item)

    assert result, "is_for_sale() should return True if the item has a price"

def test_is_for_sale_without_price():
    fake_item = {
        "name": "A Priceless Thing",
    }

    result = is_for_sale(fake_item)

    assert not result, \
        "is_for_sale() should return False if the item doesn't have a price"

def test_error(capsys):
    error("You ruined everything.")
    output = capsys.readouterr().out

    assert output == "! Error You ruined everything.\n\n", \
        "The formatted error message should be printed."

def test_debug(capsys):
    debug("Have some cake.")

    output = capsys.readouterr().out
    assert output == "# Have some cake.\n", \
        "The formatted debug message should be printed."


def test_header(capsys):
    header("Headline")

    output = capsys.readouterr().out
    assert output == "\n  Headline\n\n", \
        "The formatted header should be printed."


def test_write(capsys):
    write("oh hai")

    output = capsys.readouterr().out
    assert output == "  oh hai\n", \
        "write() should print the indented text followed by a new line"


def test_inventory_change():
    adventure.PLAYER["inventory"]["problems"] = 99
    inventory_change("problems")

    assert adventure.PLAYER["inventory"]["problems"] == 100, \
        "inventory_change() with no quantity argument should add 1."

def test_teardown():
    assert "problems" not in adventure.PLAYER["inventory"], \
        "Each test should start with a fresh data set."


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


def test_do_drop_no_args(capsys):
    do_drop([])
    output = capsys.readouterr().out

    assert "Trying to drop: []" in output, \
        "Debug message should be in output"
    assert "Error What do you want to drop?" in output, \
        "User error should be in output"


def test_do_drop_missing_item(capsys):
    adventure.PLAYER["inventory"] = {}
    do_drop(["anything"])

    output = capsys.readouterr().out

    assert "Trying to drop: ['anything']" in output, \
        "Debug message should be in output"

    assert "You don't have any 'anything'" in output, \
        "User error should be in output"


def test_do_drop(capsys):
    inventory_change("mic")

    do_drop(["mic"])
    output = capsys.readouterr().out

    assert "Trying to drop: ['mic']" in output, \
        "Debug message should be in output"

    assert "You set down the mic" in output, \
        "User message should be in output"

    assert place_has("mic"), \
        "The dropped item should be in the place"

    assert not player_has("mic"), \
        "The dropped item should not be in inventory"
