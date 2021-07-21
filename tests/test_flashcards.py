import pytest

from pythonclass.exercises.flashcards import parse_line

def say(*args, **kwargs):
    vals = [f"{k}: {v!r}" for k, v in kwargs.items()]
    print(*args, "; ".join(vals))

@pytest.mark.parametrize("message, line, cells", [
    (
        "single quoted cells",
        """'open file "todo.txt" in write mode', 'open("todo.txt", "w")'""",
        ['open file "todo.txt" in write mode', 'open("todo.txt", "w")']
    ),
    (
        "unquoted cells",
        'condition that returns True if current file is being executed rather than imported, __name__ == "__main__"',
        [
            'condition that returns True if current file is being executed rather than imported',
            '__name__ == "__main__"'
        ]
    ),

    (
        "only one cell single quoted",
        """open file "scores.txt" in append mode, 'open("scores.txt", "a")'""",
        [
            'open file "scores.txt" in append mode',
            'open("scores.txt", "a")'
        ]
    ),
    (
        "first cell double quoted",
        '"from a function definition, exit the function", return',
        [
            "from a function definition, exit the function",
            "return"
        ]
    ),
    (
        "escaped commas",
        "list dict and range object are all examples of: "
            r"(a) iterables\, (b) iterators\, (c) loops, iterables",
        [
            "list dict and range object are all examples of: "
                r"(a) iterables\, (b) iterators\, (c) loops",
            "iterables"
        ]
    ),
])
def test_parse_line(message, line, cells):
    try:
        actual = parse_line(line)
    except BaseException as err:
        breakpoint()
        ...

    if not actual == cells:
        breakpoint()

    assert actual == cells, message


