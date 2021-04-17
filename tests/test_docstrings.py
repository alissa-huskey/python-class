"""Test docstring exercise."""

from pythonclass.exercises.docstrings import get_file_docstring

import pytest

from pathlib import Path

@pytest.mark.parametrize("message, expected, contents", [
(
"file beginning with a hashbang/encoding/blank line(s)",
"Strings and Lists",
''' #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Strings and Lists"""
''',
),

(
"file beginning with a single-line docstring",
"Demo of saving and opening json files.",
'''"""Demo of saving and opening json files."""

from sys import stderr
from pprint import pprint
from pathlib import Path
'''
),

(
"no docstring",
None,
'''#!/usr/bin/env python

import random

def character_info(character_name, character_title, character_level):
'''
),

(
"multiline docstring",
"""Print the 12 Days of Christmas Song
An exercise from the loops lesson:
https://alissa-huskey.github.io/python-class/lessons/loops.html""",
'''"""Print the 12 Days of Christmas Song

An exercise from the loops lesson:
https://alissa-huskey.github.io/python-class/lessons/loops.html"""
''',
),

(
"Docstring ending in a standaline tripple (double/single-quote",
"""Script to demonstrate dictionary basics
See also: https://www.tutorialspoint.com/python/python_dictionary.htm""",
'''
#!/usr/bin/env python3

"""
Script to demonstrate dictionary basics
See also: https://www.tutorialspoint.com/python/python_dictionary.htm
"""
''',
),

(
"Tripple single-quoted docstring",
"""Display information about a random beer from the PunkAPI
Exercise from the Data Introspection lesson:
https://alissa-huskey.github.io/python-class/lessons/data-introspection.html""",
'''"""Display information about a random beer from the PunkAPI

Exercise from the Data Introspection lesson:
https://alissa-huskey.github.io/python-class/lessons/data-introspection.html"""''',
),

])

def test_get_file_docstring_with_contents(message, expected, contents):
    """Test get_file_docstring(contents=)"""
    assert get_file_docstring(contents=contents) == expected, message

def test_get_file_docstring_with_filepath():
    assert get_file_docstring(Path(__file__)) == "Test docstring exercise.", \
        "Docstring extracted from file located at Path object"

def test_get_file_docstring_without_args():
    with pytest.raises(TypeError):
        get_file_docstring()


