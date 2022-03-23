"""Test the look command"""

from pythonclass.adventure.adventure import (
    do_look,
    place_remove,
    place_add,
)

from tests.adventure import read, move_to


def test_do_look(capsys):
    do_look()
    output = read(capsys)

    assert "Trying to look around" in output, \
        "THe debug message should be in output"

    assert "Your Cottage" in output, \
        "The place name should be in output"

    assert "A cozy stone cottage" in output, \
        "The place description should be in output"

    assert "You see a desk and a book" in output, \
        "The names of the items here should be listed in output."

    assert "To the east is The Town Square" in output, \
        "The surrounding places should be listed in output"


def test_do_look_no_items(capsys):
    move_to("town-square")
    do_look()
    output = read(capsys)

    assert "You see" not in output, \
        "No verbiage about items should be in output when there are no items."


def test_do_look_one_item(capsys):
    place_remove("desk")
    do_look()
    output = read(capsys)

    assert "You see a book." in output, \
        "When there is one item in the place, it should be in output."


def test_do_look_two_items(capsys):
    do_look()
    output = read(capsys)

    assert "You see a desk and a book." in output, (
        "When there are two items in the place, the items should be listed"
        "seperated by the word 'and' in output."
    )


def test_do_look_more_items(capsys):
    place_add("elixr")
    do_look()
    output = read(capsys)

    assert "You see a desk, a book and healing elixr." in output, (
        "When there are three or more items in the place, the items should be"
        "listed seperated by commas, except the last two which should be"
        "seperated by the word 'and' in output."
    )
