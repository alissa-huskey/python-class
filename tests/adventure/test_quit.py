"""Test the quit command"""

import pytest

from pythonclass.adventure.adventure import do_quit


def test_do_quit():
    with pytest.raises(SystemExit):
        do_quit()
