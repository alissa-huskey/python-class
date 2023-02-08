"""Test the take command"""

from pythonclass.adventure.adventure import do_take, player_has, place_has

from tests.adventure import read


def test_do_take_no_args(capsys):
    do_take([])
    output = read(capsys)

    assert "Trying to take: []" in output, \
        "Debug message should be in output"
    assert "Error What do you want to take?" in output, \
        "User error should be in output"


def test_do_take_missing_item(capsys):
    do_take(["nothing"])
    output = read(capsys)

    assert "Trying to take: ['nothing']" in output, \
        "Debug message should be in output"

    assert "Error Sorry, I don't see a 'nothing' here." in output, \
        "User error should be in output"


def test_do_take_untakable_item(capsys):
    do_take(["desk"])
    output = read(capsys)

    assert "Trying to take: ['desk']" in output, \
        "Debug message should be in output"

    assert "Error You try to pick up 'desk', but" in output, \
        "User error should be in output"

    assert place_has("desk"), \
        "The untakable item should not be removed from the place"

    assert not player_has("desk"), \
        "The untakable item should not be in inventory"


def test_do_take_place_item(capsys):
    do_take(["book"])
    output = read(capsys)

    assert "Trying to take: ['book']" in output, \
        "Debug message should be in output"

    assert "You pick up a book" in output, \
        "User message should be in output"

    assert not place_has("book"), \
        "The taken item should be removed from the place"

    assert player_has("book"), \
        "The taken item should be added to player inventory"
