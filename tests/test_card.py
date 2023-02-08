
import pytest

from pythonclass.exercises.blackjack import Card, GermanCard

def test_card():
    card = Card("Q", "S")

    assert card.face == "Q"
    assert card.suit == "S"
    assert card.value == 12
    assert str(card) == "QS"
    assert card == Card(face="Q", suit="S")
    assert repr(card) == "Card(face='Q', suit='S')"

def test_invalid_card():
    with pytest.raises(ValueError):
        Card("X", "S")

    with pytest.raises(ValueError):
        Card("2", "X")

def test_german_card():

    with pytest.raises(ValueError):
        GermanCard("Q", "S")

    card = GermanCard("Q", "A")

    assert card.face == "Q"
    assert card.suit == "A"
    assert str(card) == "QA"
    assert card == GermanCard(face="Q", suit="A")
    assert repr(card) == "Card(face='Q', suit='A')"

