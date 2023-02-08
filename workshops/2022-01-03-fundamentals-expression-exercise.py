"""
2022-01-03 -- Fundamentals: Expression Exercise

Attendees
---------
- Nila

See also
--------
* Format Codes: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

Agenda
------
- Expression exercises
"""


##################################################################################################################
# Expression exercises
# --------------------
#
# Order of operation rules:
# - replace variable names with values
# - left to right
# - inside to outside
# - */ before +-
# - and before or
#
##################################################################################################################

player = {"inventory": {"coins": 8}}

item = "sword"
qty = player.get("inventory", {}).get(item, 0)

print(f"You have {qty} {item}s.")

# player.get("inventory", {}).get(item, 0)
# player.get("inventory", {}).get("sword", 0)
# {"inventory": {"coins": 8}}.get("inventory", {}).get("sword", 0)
# {"coins": 8}.get("sword", 0)
# 0

# syntax meanings for parenthesis:
#   description                                          example                  syntax
# - call functions, methods, types (str, int)            print(...)               callable_name(optional_arguments, args)
# - grouping and order of operation                                               (expression)
# - tuples                                               (1, 2, 3)                (value, value, ...)
