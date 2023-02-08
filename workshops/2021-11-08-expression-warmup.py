"""
2021-11-08 Expressions Warmup Exercises

Fundamentals
------------
- Sean

"""

#######################################################################
# Order of Operation Rules
#
# - inside to outside
# - left to right
# - replace variables with values
# - */ before +-
#
#######################################################################

# Exercise 1

from pathlib import Path

(Path(__file__).parent / "data" / "functions.csv").stem.lower()
# (Path("/Users/alissahuskey/projects/python-class/expressions.py").parent / "data" / "functions.csv").stem.lower()
# (Path("/Users/alissahuskey/projects/python-class") / "data" / "functions.csv").stem.lower()
# (Path("/Users/alissahuskey/projects/python-class/data") / "functions.csv").stem.lower()
# (Path("/Users/alissahuskey/projects/python-class/data/functions.csv")).stem.lower()
# Path("/Users/alissahuskey/projects/python-class/data/functions.csv").stem.lower()
# "functions".lower()
# "functions"

#######################################################################

# Exercise 2

text = "conditional expressions"

text.lower().replace(" ", "_").rstrip("s") + ".xls"

# "conditional expressions".lower().replace(" ", "_").rstrip("s") + ".xls"
# "conditional expressions".replace(" ", "_").rstrip("s") + ".xls"
# "conditional_expressions".rstrip("s") + ".xls"
# "conditional_expression" + ".xls"
# "conditional_expression.xls"

#######################################################################

# bad behavior
#   this is rather excessive

reply = input().strip().lower().split()[0].center(20)

print(repr(reply))