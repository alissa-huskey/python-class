"""
2022-01-17 Fundamentals: Dates and Times

Agenda
------
A. Review
    * truthy and falsy
    * boolean context
    * how and/or operators work
B. Expression exercises
C. Dates and times

Attendees
---------
- Nila
- Sean

"""

def header(title, char="-"):
    print()
    print(title)
    print(char * len(title))

def section(part, title):
    header(f"{part}: {title}", char="=")

def div(part, title):
    header(f"{part}: {title}", char="-")

# truthy and falsy
# ================
#
# truthy - if the value, when converted to a boolean*, is True
# falsy - if the value, when converted to a boolean*, is False
#
# * or: when evaluated in a boolen contexted

section("A", "Review")

div("A.1", "Truthyness and Falsiness")

eyness = {False: "Falsy", True: "Truthy"}

print(f"{5} converted to a bool is {bool(5)} which is {eyness[bool(5)]}.")
print(f"{0.0} converted to a bool is {bool(0.0)} which is {eyness[bool(0.0)]}.")

# to check if something is truthy, do if expression:

quantity = 10
price = 1.25

if quantity * price:
    print(f"You owe: ${quantity*price}.")

# to check if something is falsy, do if not expression:

if not quantity * price:
    print("You owe nothing.")

div("A.2", "Boolean context")

# When something is evaluated in a boolean context it means:
#      the expression is converted to a bool

# So this:

expression = ...

if expression:
    ...

# is the same as

if bool(expression):
    ...
    
# the following statements/operators are evaluated in a boolean context
#
# if
# while
# not
# and 
# or

div("A.3", "and/or operators")

# and -- both things are truthy

True and True        # True
True and False       # False
False and False      # False

# or -- either thing is truthy

True or True         # True
True or False        # False
False or False       # False

# though and/or are evaluated in a boolean context for decision making purposes
# they actually evaluate to one of the values

# and -- evaluates to the first falsy value or the last truthy value

0 and 0.0           # 0
0 and 1             # 1
1 and 0             # 0
1 and 2             # 2


# or -- evalutes to the first truthy value or the last falsy value

1 or 0              # 1
1 or 2              # 2
0 or 1              # 1
0 or 0.0            # 0.0


# you can use and/or as values

# for example, in assignment
# this assigns number to 100 if randint() returns 0

from random import randint
number = randint(0, 1) or 100

################################################################################
# Expression exercises
################################################################################

section("B", "Expression exercises")

# Order of operation rules
#
# - replace variables with values
# - inner to outter
# - left to right
# - */ before +-
# - and before or

div("B.1", '"a" or "b" and "c"')

x = "a" or "b" and "c"
# "a" or "c"
# "a"

print(x)

div("B.2", '("a" or "b") and "c"')

x = ("a" or "b") and "c"
# ("a") and "c"
# "a" and "c"
# "c"

print(x)


div("B.3", 'date.split()[-1]')

date = "Mon Jan 17 17:14:00 MST 2022"
x = date.split()[-1]
# "Mon Jan 17 17:14:00 MST 2022".split()[-1]
# ["Mon", "Jan", "17", "17:14:00", "MST", "2022"][-1]
# "2022"

print(x)

################################################################################
# Dates and Times
################################################################################

div("C.1", "Current date and time")
################################################################################

from datetime import datetime

now = datetime.today()

print(f"It is: {now}")

div("C.2", "Some other date and time")
# ------------------------------------------------------------------------------


date = datetime(1999, 12, 31)                     # year, month, and day are required
date = datetime(1999, 12, 31, 23, 59, 59, 16555)  # you can also pass in hour, minute, second, and microsecond
date = datetime(1999, 12, 31, minute=30)          # you can use keyword args too, the missing values will default to 0

print(f"Party like it's {date}")

div("C.3", "Human readable datetime object string")
# ------------------------------------------------------------------------------

# convert to a string using str(value)
# (print() or fstrings convert to a string automatically)

print(str(date))



# Exercises
# ---------
# 1. get the current date and time and assign it to a variable now then print it
# 2. get a datetime object for your birthday and print it


div("C.3", "Printing just the date or just the time")
# ------------------------------------------------------------------------------

print(f"Today is: {now.date()}")
print(f"It is: {now.time()}")

div("C.4", "Parts of a datetime object")
# ------------------------------------------------------------------------------

print(f"It is {now.hour} o'clock and all is well!")
print(f"Party like it's {now.year}.")


# Exercises
# ---------
# 1. Print just the date of the current datetime object using the .date() method
# 2. Print just the time of the current datetime object using the .time() method
# 3. Print a sentence like:
#    The year of our lord YEAR, on the DAY day of the MONTHth month, something happened!
#    (Using the .year, .day, and .month properties.)

div("C.5", "Durations")

from datetime import timedelta

# days
# seconds
# microseconds
# milliseconds
# minutes
# hours
# weeks


year = timedelta(days=365)
print(year)

# you can do math on timedelta objects with other timedelta objects

num_weeks = year / timedelta(weeks=1)
print(f"There are {num_weeks} in a year.")

# or with numbers

work_day = timedelta(hours=8)
work_week = work_day * 5
work_hours = work_week / timedelta(hours=1)

print(f"There are {work_hours} in a work week.")

# all timedelta objects are stored in days and/or seconds

print(work_week.days)
print(work_week.seconds)



# Exercises
# ---------
# 1. import timedelta type from the datetime module
# 2. make a timedelta for a year
# 3. multiply a year by ten to make a decade


div("C.6", "Relative dates and times")
# ------------------------------------------------------------------------------

# You can use math with datetime and timedelta objects

# For example, to figure out what time it was two hours ago:

time = now - timedelta(hours=2)
print(f"Two hours ago it was: {time}")

# You can also use math with multiple datetime objects

# For example, subtract now from a future datetime object to find out
#     how long it will be until then.

v_day = datetime(2022, 2, 14)

countdown = v_day - now

print(f"There are {countdown.days} days until Valentines Day {v_day.year}.")


# Exercises
# ---------
# 1. Find out the date a week from now
# 2. Look up the date of the last solar eclipse. Print how many days it has been since then.
#    Bonus: Use timedelta objects to calculate how many years, months, and days it has been.
