"""
2021-12-15 In-Depth: Datetime Objects

Attendees
---------
- Brian
- Fiona
"""

from datetime import datetime

# getting todays date

today = datetime.now()

# printing the date or time

print(str(today))
print(str(today.date()))
print(str(today.time()))

# printing a specific format

# Format Codes: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

print(today.strftime('%Y-%m-%d %H:%M:%S'))

# getting a specifc date

created_at = datetime.strptime("6/5/20", "%m/%d/%y")

# relative dates

from datetime import timedelta

week = timedelta(days=7)
last_week = today - week

print("last week:", last_week)

tomorrow = today + timedelta(days=1)

print("tomorrow:", tomorrow)

# difference between dates

age = today - created_at
print("age:", age)


