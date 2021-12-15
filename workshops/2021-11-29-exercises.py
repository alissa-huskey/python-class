"""2021-11-29 Exercises
"""

def print_season():
    """Make a list of seasons (lowercase). Print the first three characters of
    the 3rd season, title cased."""
    seasons = [
        "spring",
        "summer",
        "fall",
        "winter",
    ]
    print(seasons[2][:3].title())

def get_weekday(day):
    """Make a dictionary where the key is the numbers 1-7 and the value is the
    days of the week: monday - sunday.  Write a function that takes one
    argument, a number, and returns the day of the week associated with that
    number.  """

    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return weekdays[day]

def print_schedule():
# 3. Make a dictionary named schedule where the key is a weekday and the value is another dictionary.
#    - The inner dictionary should be the schedule for the day, where the key is the time in 24 hour format (ie: "14:30")
#      and the value is the thing scheduled
#    - Use a for loop to iterate over each day and print the day name,
#    - then use a nested for loop to iterate over the schedule and print the time and activity
    schedule = {
        "monday": {
            "17:00": "Coding Class: Fundamentals",
        },
        "tuesday": {
            "15:30": "Mom",
            "17:00": "Coding Class: Study Hall",
        },
        "wednesday": {
            "17:00": "Coding Class: Data",
        },
        "thursday": {
            "13:40": "Margit",
        },
        "friday": {
        },
        "saturday": {
        },
        "sunday": {
        },
    }

    for day, appointments in schedule.items():
        print()
        print(day.title())
        print(len(day) * "-")

        if not appointments:
            print("No events.")

        for time, event in appointments.items():
            print(time.rjust(5), event)

def hr():
    """Print a horizontal rule (a line)."""
    print()
    print("*" * 40)
    print()

def main():
    hr()
    print_season()
    hr()
    print(get_weekday(3))
    hr()
    print_schedule()
    hr()

if __name__ == "__main__":
    main()



