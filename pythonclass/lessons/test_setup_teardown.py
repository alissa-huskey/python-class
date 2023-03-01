"""
This is an example of using setup and teardown functions.
For the Pytest Tests lesson
"""
from copy import deepcopy
import json
from pathlib import Path


def setup_module(module):
    """Initialize STATE global variable and load from json testdata."""
    global STATE
    STATE = {}

    for resource in ["users", "todos"]:
        file = Path(__file__).parent / ".data" / f"{resource}.json"
        with file.open() as fh:
            STATE[resource] = json.load(fh)


def setup_function(function):
    """Revert data to its original state before each test."""
    global DATA
    DATA = deepcopy(STATE)


def test_user():
    """Test that the first user was loaded from the users.json file."""
    user = DATA["users"][0]

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"


def test_todo():
    """Test that the first todo was loaded from the todos.json file."""
    todo = DATA["todos"][0]

    assert todo["id"] == 1
    assert todo["title"] == "delectus aut autem"
    assert not todo["completed"]


def test_modify_state():
    """Change the DATA data"""
    todo = DATA["todos"][0]
    todo["completed"] = True

    assert todo["completed"]


def test_check_modified_state():
    """Check the same data that was modified above."""
    todo = DATA["todos"][0]

    assert not todo["completed"]
