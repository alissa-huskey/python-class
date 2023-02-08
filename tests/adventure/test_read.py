"""Test the read command"""

from pythonclass.adventure.adventure import (
    do_read,
    inventory_change,
)

from tests.adventure import read, move_to


def test_do_read_no_args(capsys):
    do_read([])
    output = read(capsys)

    assert "Trying to read: []" in output, \
        "Debug message should be in output"
    assert "Error What do you want to read?" in output, \
        "User error should be in output"


def test_do_read_missing_item(capsys):
    do_read(["nothing"])
    output = read(capsys)

    assert "Trying to read: ['nothing']" in output, \
        "Debug message should be in output"

    assert "Sorry, I don't know what this is: 'nothing'" in output, \
        "User error should be in output"


def test_do_read_unreadable_item(capsys):
    do_read(["desk"])
    output = read(capsys)

    assert "Trying to read: ['desk']" in output, \
        "Debug message should be in output"

    assert "Sorry, I can't read this desk." in output, \
        "User error should be in output"


def test_do_read_place_item(capsys):
    do_read(["book"])
    output = read(capsys)

    assert "Trying to read: ['book']" in output, \
        "Debug message should be in output"

    assert "The book is open to a page that reads" in output, \
        "Preface should be in output"

    assert "    At the edge of the woods" in output, \
        "Indented message should be in output"

    assert "with a different temperament.\n\n" in output, \
        "There should be two lines between each message part."

    assert output.endswith("\n\n"), "Output should end in two blank lines."

    assert "Error" not in output, \
        "There should not be an error message in output"


def test_do_read_inventory_item(capsys):
    move_to("town-square")
    inventory_change("book")

    do_read(["book"])
    output = read(capsys)

    assert "Trying to read: ['book']" in output, \
        "Debug message should be in output"

    assert "The book is open to a page that reads" in output, \
        "Preface should be in output"

    assert "Error" not in output, \
        "There should not be an error message in output"
