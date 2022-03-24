from adventure import (
    debug,
    error,
    header,
    is_for_sale,
    write,
)

def test_is_for_sale():
    fake_item = {
        "name": "An Expensive Thing",
        "price": "a lot",
    }

    result = is_for_sale(fake_item)

    assert result, "is_for_sale() should return True if the item has a price"

def test_is_for_sale_without_price():
    fake_item = {
        "name": "A Priceless Thing",
    }

    result = is_for_sale(fake_item)

    assert not result, \
        "is_for_sale() should return False if the item doesn't have a price"

def test_error(capsys):
    error("You ruined everything.")
    output = capsys.readouterr().out

    assert output == "! Error You ruined everything.\n\n", \
        "The formatted error message should be printed."

def test_debug(capsys):
    debug("Have some cake.")

    output = capsys.readouterr().out
    assert output == "# Have some cake.\n", \
        "The formatted debug message should be printed."
