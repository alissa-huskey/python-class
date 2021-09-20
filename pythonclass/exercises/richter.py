"""Richter Scale exercise"""
# Richter scale
#

# Write a `quake_desc` function that takes one argument: `magnitude`, a number.
# return the description associated for the magnitude, as shown in the table
# below.

# | Min       | Max  | Description           |
# |-----------|------|-----------------------|
# | 0         | < 2  | micro                 |
# | 2         | < 3  | very minor            |
# | 3         | < 4  | minor                 |
# | 4         | < 5  | light                 |
# | 5         | < 6  | moderate              |
# | 6         | < 7  | strong                |
# | 7         | < 8  | major                 |
# | 8         | < 10 | great                 |
# | 10        | *    | meteroic              |

# For example:


# under_magnitude -> label
# >>> quake_desc(0.2)
# 'micro'

# >>> quake_desc(2.5)
# 'very minor'

# >>> quake_desc(5)
# 'moderate'

# >>> quake_desc(11)
# 'meteroic'

SCALE = {
    2: "micro",
    3: "very minor",
    4: "minor",
    5: "light",
    6: "moderate",
    7: "strong",
    8: "major",
    10: "great",
    "max": "meteroic",
}

def quake_desc(magnitude):
    """Return the description for a earthquake_desc magnitude

    >>> quake_desc(0.2)
    'micro'

    >>> quake_desc(2.5)
    'very minor'

    >>> quake_desc(5)
    'moderate'

    >>> quake_desc(11)
    'meteroic'
    """
    for ceiling, phrase in SCALE.items():
        if ceiling == "max":
            return phrase
        elif magnitude < ceiling:
            return phrase

