"""Test the go command"""

from pythonclass.adventure import adventure
from pythonclass.adventure.adventure import do_go

from tests.adventure import read


def test_do_go_no_args(capsys):
    do_go([])
    output = read(capsys)

    assert "Trying to go: []" in output, \
        "Debug message should be in output"

    assert "Error Which way do you want to go?" in output, \
        "User error should be in output"


def test_do_go_invalid_direction(capsys):
    do_go(["to hell"])
    output = read(capsys)

    assert "Trying to go: ['to hell']" in output, \
        "Debug message should be in output"

    assert "Error Sorry, I don't know how to go: to hell" in output, \
        "User error should be in output"


def test_do_go_nowhere(capsys):
    do_go(["west"])
    output = read(capsys)

    assert "Trying to go: ['west']" in output, \
        "Debug message should be in output"

    assert "Sorry, you can't go west from here" in output, \
        "User error should be in output"


def test_do_go_somewhere(capsys):
    do_go(["east"])
    output = read(capsys)

    assert "east" in output, \
        "Debug message should be in output"

    assert "The Town Square" in output, \
        "The new place name should be in the output"

    assert adventure.PLAYER["place"] == "town-square", \
        "The player should be in the new place"
