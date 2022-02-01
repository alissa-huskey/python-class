"""
2022-01-31 -- datetime review and exercise

Agenda
------
* Expression exercise
* Review datetimes
* Problem solving exercise


Attendees
---------
- Nila

"""

from workshops import section, div, stop, evaluate, exercise

section("A", "Expression Exercises")

# order of operation rules
#
# - replace variables with values
# - */ before +-
# - inside to out
# - left to right
# - and before or
#

div("A.1", "Exercise")

from pathlib import Path

DEFAULT_CONFIG_DIR = Path.home() / "python_class_config"

options = {
    "url": "https://github.com/alissa-huskey/python-class"
}

options.get("config_dir", DEFAULT_CONFIG_DIR).name.replace("_", " ").title()
# options.get("config_dir", Path.home() / "python_class_config").name.replace("_", " ").title()
# options.get("config_dir", Path("/Users/alissa") / "python_class_config").name.replace("_", " ").title()
# options.get("config_dir", Path("/Users/alissa/python_class_config")).name.replace("_", " ").title()
# Path("/Users/alissa/python_class_config").name.replace("_", " ").title()
# "python_class_config".replace("_", " ").title()
# "python class config".title()
answer = "Python Class Config"

evaluate(
    'options.get("config_dir", DEFAULT_CONFIG_DIR).name.replace("_", " ").title()',
    answer,
    globals(),
)

# ----------------------------------------------------------

section("B", "Review datetimes")

div("B.1", "get the current date and time")

from datetime import datetime
present = datetime.today()
print(present)

div("B.2", "add or subtract a timedelta to/from that datetime object")

from datetime import timedelta
hour = timedelta(hours=1)
future = present + hour
print(future)


div("B.3", "get a property from a datetime object")

print(future.day)

section("3", "Exercise")

exercise("3.1", "Print the schedule for today", 
         """
            Print every hour of the day in 12 hour format with AM/PM
            If there is an activity for that hour on your schedule dictionary,
                print the activity after the hour.

            Use datetime and time delta objects, and iterate using a for loop. Use the
            datetime.replace() method to change the values in a particular datetime
            object.
         """,
         context = """
            schedule = {
                12: "Lunch",
                17: "Coding Class",
                20: "Date night",
            }
         """,
         example="""
                 8 AM  Breakfast
                 9 AM
                10 AM
                11 AM
                12 PM  Lunch
                 1 PM
                 2 PM
                 3 PM
                 4 PM
                 5 PM
                 6 PM  Dinner
         """,
)


