"""
This is an example of Pytest Parametrization for the Pytest Tests lesson.
"""


def can_drink(age):
    """Return True if age is greater than 21"""
    return age >= 21


import pytest  # noqa


@pytest.mark.parametrize(["age", "expected", "message"], [
    (15, False, "False when age is less than 21"),
    (0, False, "False when age is zero"),
    (-5, True, "False when age is a negative int"),
    (17.5, False, "False when age is a negative float"),
    (21, True, "True when age is exactly 21"),
    (100, True, "True when age is over 21"),
])
def test_can_drink(age, expected, message):
    is_allowed = can_drink(age)
    assert is_allowed == expected, \
        f"can_drink() should return {message}"
