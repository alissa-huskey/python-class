"""Test the inventory command"""

from pythonclass.adventure.adventure import (
    do_inventory,
    inventory_change,
)

from tests.adventure import read


def test_do_inventory_empty(capsys):
    inventory_change("gems", -50)

    do_inventory()
    output = read(capsys)

    assert "Inventory" in output, \
        "The title should be in output"

    assert "Empty." in output, \
        "An empty inventory should say so in output"


def test_do_inventory(capsys):
    do_inventory()
    output = read(capsys)

    assert "Inventory" in output, \
        "The title should be in output"

    assert "(x50)  gems" in output, \
        "Inventory items should be listed in output"
