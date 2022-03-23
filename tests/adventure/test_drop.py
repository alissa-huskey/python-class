"""Test the drop command"""

from pythonclass.adventure.adventure import (
    do_drop,
    player_has,
    place_has,
    inventory_change,
)

from tests.adventure import read


def test_do_drop_no_args(capsys):
    do_drop([])
    output = read(capsys)

    assert "Trying to drop: []" in output, \
        "Debug message should be in output"
    assert "Error What do you want to drop?" in output, \
        "User error should be in output"


def test_do_drop_missing_item(capsys):
    do_drop(["nothing"])
    output = read(capsys)

    assert "Trying to drop: ['nothing']" in output, \
        "Debug message should be in output"

    assert "You don't have any 'nothing'" in output, \
        "User error should be in output"


def test_do_drop(capsys):
    inventory_change("book")

    do_drop(["book"])
    output = read(capsys)

    assert "Trying to drop: ['book']" in output, \
        "Debug message should be in output"

    assert "You set down the book" in output, \
        "User message should be in output"

    assert place_has("book"), \
        "The dropped item should be in the place"

    assert not player_has("book"), \
        "The dropped item should not be in inventory"
