"""
Test demonstrating how Pytest fixtures request other fixtures.
For Pytest Tests lesson.
"""
from pathlib import Path
import json

import pytest


@pytest.fixture
def fixturesdir():
    """Return the Path object to the directory where fixture files are stored."""
    return Path(__file__).parent / ".data"


@pytest.fixture
def users_file(fixturesdir):
    return fixturesdir / "users.json"


@pytest.fixture
def users(users_file):
    """Return """
    with users_file.open() as fh:
        users = json.load(fh)

    return users


def test_user(users):
    """Test that the first user was loaded from the users.json file."""
    user = users[0]

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
