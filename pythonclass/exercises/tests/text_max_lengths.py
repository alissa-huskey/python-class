from pprint import pformat
import pytest

@pytest.mark.function("max_lengths")
@pytest.mark.parametrize(
    "matrix,expected", [
        (
            [[628, 4, 82], [140, 59, 23]],
            [3, 2, 2],
        ),
        (
            [
                ['2021-07-13 18:46:39', '4 out of 4'],
                ['2021-07-20 19:17:36', '0 out of 28']
            ],
            [19, 11],

        ),
        (
            [['lend', 'job', 'when'], ['mail', 'walk', 'prove']],
            [4, 4, 5],
        ),
    ])
def test_max_lengths(matrix, expected, func):
    actual = func(matrix)
    assert actual == expected, \
        f"Expected: {expected}; Actual: {actual} for:\n{pformat(matrix)}"

