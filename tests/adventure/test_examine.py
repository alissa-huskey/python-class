"""Test the examine command"""

from pythonclass.adventure.adventure import (
    do_examine,
    inventory_change,
)

from tests.adventure import read, move_to


def test_do_examine_no_args(capsys):
    do_examine([])
    output = read(capsys)

    assert "Trying to examine: []" in output, \
        "Debug message should be in output"
    assert "Error What do you want to examine?" in output, \
        "User error should be in output"


def test_do_examine_missing_item(capsys):
    do_examine(["nothing"])
    output = read(capsys)

    assert "Trying to examine: ['nothing']" in output, \
        "Debug message should be in output"

    assert "Sorry, I don't know what this is: 'nothing'" in output, \
        "User error should be in output"


def test_do_examine_place_item(capsys):
    do_examine(["book"])
    output = read(capsys)

    assert "Trying to examine: ['book']" in output, \
        "Debug message should be in output"

    assert "A Book" in output, \
        "Title of item should be in output"

    assert "A hefty leather-bound tome" in output, \
        "Description of item should be in output"

    assert "Error" not in output, \
        "There should not be an error message in output"


def test_do_examine_inventory_item(capsys):
    inventory_change("elixr")

    do_examine(["elixr"])
    output = read(capsys)

    assert "Trying to examine: ['elixr']" in output, \
        "Debug message should be in output"

    assert "Healing Elixr" in output, \
        "Title of item should be in output"

    assert "(x1)" in output, \
        "Inventory quantity should be in output"

    assert "a magical elixr that will heal what ails ya" in output, \
        "Description of item should be in output"

    assert "Error" not in output, \
        "There should not be an error message in output"


def test_do_examine_for_sale_item(capsys):
    move_to("market")

    do_examine(["dagger"])

    output = read(capsys)

    assert "Trying to examine: ['dagger']" in output, \
        "Debug message should be in output"

    assert "A Dagger" in output, \
        "Title of item should be in output"

    assert "25 gems" in output, \
        "Price should be in output"

    assert "a 14 inch dagger" in output, \
        "Description of item should be in output"

    assert "Error" not in output, \
        "There should not be an error message in output"
