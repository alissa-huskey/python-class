import pytest

from pythonclass.adventure import adventure
from pythonclass.adventure.adventure import (
    abort,
    error,
    debug,
    header,
    inventory_change,
    is_for_sale,
    place_add,
    place_can,
    place_remove,
    place_has,
    player_has,
    wrap,
    write,
    get_item,
    get_place,
)

from tests.adventure import read, move_to


def test_abort():
    with pytest.raises(SystemExit):
        abort("I'm broken on the inside.")


def test_error(capsys):
    error("You ruined everything.")
    output = read(capsys)

    assert output == "! Error You ruined everything.\n\n"


def test_debug(capsys):
    debug("Have some cake.")

    output = read(capsys)
    assert output == "# Have some cake.\n"


def test_header(capsys):
    header("Headline")

    output = read(capsys)
    assert output == "\n  Headline\n\n"


def test_inventory_change():
    adventure.PLAYER["inventory"]["problems"] = 99
    inventory_change("problems")

    assert adventure.PLAYER["inventory"]["problems"] == 100, \
        "Inventory change with no quantity argument should add 1."


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


def test_is_for_sale():
    assert is_for_sale({"price": "a lot"}), \
        "is_for_sale() should return True if a price key exists"


def test_is_for_sale_false():
    assert not is_for_sale({}), \
        "is_for_sale() should return False if no price key exists"


def test_move_to():
    move_to("the moon")

    assert adventure.PLAYER["place"] == "the moon", \
        "move_to() should change the players place"


def test_place_add_preexisting_items():
    place_add("ice cream")

    assert "ice cream" in adventure.PLACES["home"]["items"], \
        "place_add() should update the items in the current place"


def test_place_add():
    move_to("town-square")
    place_add("puppy")

    assert "items" in adventure.PLACES["town-square"], \
        "place_add() should add items to the current place if missing"

    assert "puppy" in adventure.PLACES["town-square"]["items"], \
        "place_add() should update the items in the current place"


def test_place_remove():
    place_remove("book")

    assert "book" not in adventure.PLACES["home"], \
        "place_remove() should update the items in the current place"


def test_place_has_without_item():
    assert not place_has("elixr"), \
        "place_has() should return False if the current place does not have the item"


def test_place_has_without_items():
    move_to("town-square")

    assert not place_has("book"), \
        "place_has() should return False if the current place has no items"


def test_place_has_with_items():
    assert place_has("book"), \
        "place_has() should return True if the item is in the current place"


def test_place_can_without_actions():
    assert not place_can("dance"), \
        "place_can() should be False if the place has no actions"


def test_place_can_without_action():
    move_to("market")

    assert not place_can("dance"), \
        "place_can() should be False if the place does not have the action"


def test_place_can_with_action():
    move_to("market")

    assert place_can("shop"), \
        "place_can() should be True if the place has the action"


def test_player_has_without_key():
    adventure.PLAYER["inventory"] = {}

    assert not player_has("a soul"), \
        "player_has() should be False if the item is not in inventory"


def test_player_has_with_zero():
    adventure.PLAYER["inventory"] = {"fucks to give": 0}

    assert not player_has("fucks to give"), \
        "player_has() should be False if the player has zero"


def test_player_has_without_enough():
    adventure.PLAYER["inventory"] = {"patience": 1}

    assert not player_has("patience", 10), \
        "player_has() should be False if player has less than the quantity"


def test_player_has_with_default():
    adventure.PLAYER["inventory"] = {"brain": 1}

    assert player_has("brain"), \
        "player_has() should be True if player has at least 1 by default"


def test_player_has_with_enough():
    adventure.PLAYER["inventory"] = {"fingers on left hand": 6}

    assert player_has("fingers on left hand", 6), \
        "player_has() should be True if player has at least quantity"


def test_wrap(capsys):
    # spell-checker: disable
    wrap("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    lines = read(capsys).splitlines()

    assert len(lines) > 1, \
        "wrap() should break up long text into multiple lines"

    assert all([line.startswith("  ") for line in lines]), \
        "wrap() should indent each line of wrapped output"


def test_wrap_with_indent(capsys):
    wrap("A drawing is simply a line going for a walk.", indent=2)

    output = read(capsys)

    assert output.startswith("    A drawing is simply a line")


def test_wrap_with_after(capsys):
    wrap("Confidence is 10% hard work and 90% delusion.", after=2)

    output = read(capsys)

    assert output.endswith("delusion.\n\n")


def test_write(capsys):
    write("oh hai")

    output = read(capsys)
    assert output == "  oh hai\n", \
        "write() should print the indented text followed by a new line"


def test_get_item(capsys):
    item = get_item("book")

    assert item and item["key"] == "book", \
        "get_item() should return the item from ITEMS"


def test_get_item_missing(capsys):
    with pytest.raises(SystemExit):
        get_item("clue")


def test_get_place_default(capsys):
    place = get_place()

    assert place and place["key"] == "home", \
        "get_place() should return the current place by default"


def test_get_place_missing(capsys):
    with pytest.raises(SystemExit):
        get_place("your imagination")


def test_get_place(capsys):
    place = get_place("town-square")

    assert place and place["key"] == "town-square", \
        "get_place() should return the place from PLACES"
