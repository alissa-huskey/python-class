"""
2022-02-21 -- Fundamentals: List Review & Fav Movie Exercise

Attendees
---------
- Nila
- Sean
"""

from workshops import section, div, stop, evaluate, exercise

section("A", "Lists Review")

div("A.1", "Create a list")

holidays = ["christmas", "thanksgiving", "valintines", "4th of July", "Halloween"]

print(holidays)

div("A.2", "Add to the end of a list")

holidays.append("Nila's Birthday")

print(holidays)

div("A.3", "Add to anywhere else in a list")

holidays.insert(2, "New Year's")

print(holidays)

div("A.4", "Change something in the list")

holidays[3] = "Valentine's Day"

print(holidays)

div("A.5", "Remove something from the list by index number")

del holidays[-1]

print(holidays)

div("A.6A", "Remove something from the list by index number and have the value that was removed returned")

print("before:", holidays)

removed = holidays.pop(0)
print(f"Holiday known as {removed} no longer exists bc economy")
print("after:", holidays)

div("A.6B", "Sidebar on returning")

def something():
    print("abc")
    return 50
    print("def")

value = something()
print(value)

div("A.7", "Remove an item by value")

holidays.remove("thanksgiving")

print(holidays)

div("A.8", "Get an item from a list by index number")
print(holidays[2])

div("A.9", "Check if a value is in a list")

if "St. Patrick's Day" in holidays:
    print("yes")
else:
    print("no")

if "Guy Fawks's Day" not in holidays:
    print("Guess who's a fancy American!")

div("A.10", "Iterate over a list")

for item in holidays:
    print(item)

div("A.11", "Iterate over a list with index number")

for i, item in enumerate(holidays, 1):
    print(i, item)


exercise(
    "B",
    "List of favorite movies",
    """Given a list of movies, interactively ask the user to reorder them
    sorted by their most to least favorites."""
)

div("B.1", "Print out the list of movies")

