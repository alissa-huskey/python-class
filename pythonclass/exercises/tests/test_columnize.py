from pprint import pformat
import pytest

@pytest.mark.function("columnize")
@pytest.mark.parametrize(
    "matrix,expected", [
        (
            [['Joe', 82], ['Billy', 59], ['Mary', 77]],
            "Joe    82\nBilly  59\nMary   77"
        ),
        (
            [
                ["Ender's Game", "Orson Scott Card", 1985],
                ["Flowers for Algernon", "Daniel Keyes", 1959],
                ["Last Chance to See", "Douglas Adams", 1990],
                ["Spin", "Robert Charles Wilson", 2005],
                ["This Alien Shore", "C.S. Friedman", 1998],
                ["Snow Crash", "Neal Stephenson", 1992],
                ["House of Leaves", "Mark Z. Danielewski", 2000]
            ],
            """
Ender's Game          Orson Scott Card       1985
Flowers for Algernon  Daniel Keyes           1959
Last Chance to See    Douglas Adams          1990
Spin                  Robert Charles Wilson  2005
This Alien Shore      C.S. Friedman          1998
Snow Crash            Neal Stephenson        1992
House of Leaves       Mark Z. Danielewski    2000
            """.strip()
        ),
    ])
def test_columnize(matrix, expected, func):
    actual = func(matrix)
    assert actual == expected, \
        f"Expected:\n {expected}; \n\nActual:\n {actual} \n\nInput:\n{pformat(matrix)}"


