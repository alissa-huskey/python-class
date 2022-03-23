"""Tests for the text based adventure game"""

from pythonclass.adventure import adventure

__all__ = ["read", "move_to"]


def read(capsys):
    """Return stdout from capsys fixture"""
    return capsys.readouterr().out


def move_to(name):
    """Change the current place to name"""
    adventure.PLAYER["place"] = name
