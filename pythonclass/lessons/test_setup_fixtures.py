"""
This is an example of writing fixtures to replace setup and teardown functions.
For the Pytest Tests lesson
"""
from copy import deepcopy
import json
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def state():
    """Load state from json testdata."""
    data = {}

    for resource in ["users", "todos"]:
        file = Path(__file__).parent / ".data" / f"{resource}.json"
        with file.open() as fh:
            data[resource] = json.load(fh)

    return data


@pytest.fixture
def users(state):
    """Return a fresh set of data for each function."""
    return deepcopy(state["users"])


@pytest.fixture(scope="function")
def todos(state):
    """Return a fresh set of data for each function."""
    return deepcopy(state["todos"])


def test_user(users):
    """Test that the first user was loaded from the users.json file."""
    user = users[0]

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"


def test_todo(todos):
    """Test that the first todo was loaded from the todos.json file."""
    todo = todos[0]

    assert todo["id"] == 1
    assert todo["title"] == "delectus aut autem"
    assert not todo["completed"]


def test_modify_state(todos):
    """Change the data"""
    todo = todos[0]
    todo["completed"] = True

    assert todo["completed"]


def test_check_modified_state(todos):
    """Check the same data that was modified above."""
    todo = todos[0]

    assert not todo["completed"]
