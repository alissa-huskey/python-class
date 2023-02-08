"""Test the shop command"""

from pythonclass.adventure.adventure import do_shop

from tests.adventure import read, move_to


def test_do_shop_wrong_place(capsys):
    do_shop()
    output = read(capsys)

    assert "Sorry, you can't shop here" in output, \
        "User error should be in output"


def test_do_shop(capsys):
    move_to("market")
    do_shop()
    output = read(capsys)

    assert "Items for sale" in output, \
        "Title should be in output"

    assert "healing elixr" in output, "for sale items should be in output"
    assert "a dagger" in output, "for sale items should be in output"
