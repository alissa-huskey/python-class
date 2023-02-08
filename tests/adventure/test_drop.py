"""Test the drop command"""

from pythonclass.adventure import adventure
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
    output = read(capsys)

    assert "Trying to drop: ['mic']" in output, \
        "Debug message should be in output"

    assert "You set down the mic" in output, \
        "User message should be in output"

    assert place_has("mic"), \
        "The dropped item should be in the place"

    assert not player_has("mic"), \
        "The dropped item should not be in inventory"
