"""Test the buy command"""

from pythonclass.adventure import adventure
from pythonclass.adventure.adventure import (
    do_buy,
    player_has,
    place_has,
    place_add,
    inventory_change,
)

from tests.adventure import read, move_to


def test_do_buy_wrong_place(capsys):
    do_buy(["something"])
    output = read(capsys)

    assert "Trying to buy: ['something']" in output, \
        "Debug message should be in output"

    assert "Sorry, you can't buy things here" in output, \
        "User error should be in output"


def test_do_buy_no_args(capsys):
    move_to("market")
    do_buy([])
    output = read(capsys)

    assert "Trying to buy: []" in output, \
        "Debug message should be in output"
    assert "Error What do you want to buy?" in output, \
        "User error should be in output"


def test_do_buy_missing_item(capsys):
    move_to("market")
    do_buy(["nothing"])
    output = read(capsys)

    assert "Trying to buy: ['nothing']" in output, \
        "Debug message should be in output"

    assert "Error Sorry, I don't see a 'nothing' here." in output, \
        "User error should be in output"


def test_do_buy_not_for_sale(capsys):
    move_to("market")
    place_add("book")

    do_buy(["book"])
    output = read(capsys)

    assert "Trying to buy: ['book']" in output, \
        "Debug message should be in output"

    assert "Sorry, a book is not for sale." in output, \
        "User error should be in output"

    assert place_has("book"), \
        "The not for sale item should still be in the place"

    assert not player_has("book"), \
        "The not for sale item should not be in inventory"


def test_do_buy_cannot_afford(capsys):
    move_to("market")
    inventory_change("gems", -40)

    do_buy(["dagger"])
    output = read(capsys)

    assert "Trying to buy: ['dagger']" in output, \
        "Debug message should be in output"

    assert "Sorry, you can't afford" in output, \
        "User error should be in output"

    assert place_has("dagger"), \
        "The too expensive item should still be in the place"

    assert not player_has("dagger"), \
        "The too expensive item should not be in inventory"


def test_do_buy_can_afford(capsys):
    move_to("market")

    do_buy(["elixr"])
    output = read(capsys)

    assert "Trying to buy: ['elixr']" in output, \
        "Debug message should be in output"

    assert "You bought healing elixr" in output, \
        "User message should be in output"

    assert not place_has("elixr"), \
        "The item should not be in the place"

    assert player_has("elixr"), \
        "The item should be in inventory"

    assert adventure.PLAYER["inventory"]["gems"] == 40, \
        "The cost of the item should be subtracted from gem quantity"
