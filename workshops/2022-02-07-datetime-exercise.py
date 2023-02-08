"""
2022-02-07 -- Fundamentals: Date and Time Exercise

Attendees
---------
- Nila


"""

from workshops import section, div, stop, evaluate, exercise

from datetime import datetime
today = datetime.today()
print("today:", today)
# breakpoint()

first_of_month = today.replace(day=1)
print("first of the month:", first_of_month)

# get 8am today using .replace()
morning = today.replace(hour=8, minute=0, second=0, microsecond=0)
# breakpoint()
print("morning:", repr(morning), morning)
from datetime import timedelta
minutes = timedelta(minutes=13)
new_time = morning + minutes
print("The new time is: ", new_time)

exercise("2.1", "Print the schedule for today",
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

# step 1: print a list of the hours in 24 hour format
#           make a list of each 24 hour
#         - hour = timedelta(hour=24)
#           iterate over the 24 hour list
#           for x in hour:
#           replace each 24 hour in the list with a corresponding 12 hour
#               twelve_hour =
#
start_time = today.replace(hour=0, minute=0, second=0, microsecond=0)
hour = timedelta(hours=1)
for _ in range(25):
    print(start_time + hour)

# step 2: convert to 12 hour format
# step 3: fill in the any scheduled activities
