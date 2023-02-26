---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

Dates and Times
===============

Dealing with dates and times is vital to many programming tasks from something
as simple as displaying the current date and time to pulling up all of the
records that were created during a particular period of time.

Dates and times have a surprising amount of complexity, between timezones,
daylight savings times, leap years, and varying month lengths. Luckily modern
Python programmers don't need to figure this all out, but instead can rely on
libraries to handle to package it into a few (relatively) simple types.

```{include} ../toc.md
```

Part 1: Datetime objects
------------------------

The `datetime` module provides types for manipulating dates and times. In this
lesson we'll learn about the `datetime` type.

### Part 1.1: The current date and time

To get the current date and time, first you'll need to import the `datetime`
type from the `datetime` module. Then you can call the `.today()` method, which
will return a `datetime` object with the current date and time.

```{code-cell} python
:class: full-width

from datetime import datetime
now = datetime.today()
```

### Part 1.2: Simple date and time formatting

If you want to display a human-readable date or time, you can convert a
datetime object to a string using the `str` type.

```{code-cell} python
print(str(now))
```

For just the date or time, you can call the `.date()` or `.time()` methods
respectively, then convert the returned value to a string.

```{code-cell} python
print(str(now.date()))
print(str(now.time()))
```

### Part 1.3: Individual values

You can access individual parts of a `datetime` object via the following
properties:

- year
- month
- day
- hour
- minute
- second
- microsecond

```{code-cell} python
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
```

To get the day of the week you can call the `.weekday()` method. It will return
an integer between `0` and `6` representing `Monday` through `Sunday`.

```{code-cell} python
print(now.weekday())
```

For a list-like iterable of day names in the correct order, you can import
`day_name` from the `calendar` module.

```{code-cell} python
from calendar import day_name

print(list(day_name))
```

You can then use the value returned by the `.weekday()` method as the index
value of `day_name` to get the weekday name.

```{code-cell} python
print(day_name[now.weekday()])
```

### Part 1.4: Getting a specific date

To create a `datetime` object with some other date and time, call the
`datetime` type and pass integer arguments for at least the `year`, `month` and
`day`.

In this example, I'm making a `datetime` object for the date of the initial
release of Python[^python-release].

```{code-cell} python
datetime(1991, 2, 20)
```

You can also optionally also pass the `hour`, `minute`, `second` and
`microsecond`.

```{code-cell} python
datetime(1991, 2, 19, 10, 35, 26)
```

[^python-release]: https://groups.google.com/g/alt.sources/c/O2ZSq7DiOwM/m/gcJTvCA27lMJ?pli=1

Part 2: Date formatting
-----------------------

Since there are so many ways to represent a date or time, most programming
languages provide a fairly standard set of {term}`date formatting codes`, where
each code is a character prefixed by a `%` that is used to represent a
particular field and presentation.

These can then be put together in a string to indicate a how a date should be
displayed or interpreted.

For example, the string `"%Y-%m-%d %H:%M:%S"` would represent a date like
`"1991-02-19 10:35:26"`.

For a full list of format codes see the [format codes table](#format-codes) in
the reference section of this page.

### Part 2.1: Displaying

To display a date in a particular format, use the `.strftime()` method on a
`datetime` object, and pass it a string with the date format you wish to use.

```{code-cell} python
print(now.strftime('%Y-%m-%d %H:%M:%S'))
```

### Part 2.2: Interpreting

If you have a date string that you want to turn into a `datetime` object, use
the `.strptime()` method on the `datetime` type. Pass it two arguments: the
date string and the format string.

```{code-cell} python
datetime.strptime("6/5/20", "%m/%d/%y")
```

Part 3: Relative dates and times
--------------------------------

When working with dates and times we often care about the amount of time since
or until a particular date, or the times between two dates and times.

### Part 3.1: Durations

Python provides the `timedelta` type to represent a duration of time, which you
can import from the `datetime` module.

To construct a `timedelta` object, pass a keyword argument with an integer
value for any of the following:

- days
- seconds
- microseconds
- milliseconds
- minutes
- hours
- weeks

For example, to make a `timedelta` object representing a quarter hour you would
pass `minutes=15`.

```{code-cell} python
from datetime import timedelta

timedelta(minutes=15)
```

You can also do math with `timedelta` objects.

```{code-cell} python
week = timedelta(weeks=1)
fortnight = timedelta(days=14)

fortnight / week
```

While `timedelta` objects can be created in any of the above units of
measurement, they are stored in `days` and `seconds`. For example, here we
create a `moment` timedelta of `1` minute and `30` seconds.

```{code-cell} python
moment = timedelta(minutes=1, seconds=30)
```

This is stored as `90` seconds.

```{code-cell} python
print(moment.seconds)
```


```{code-cell} python
delta = timedelta(days=1, hours=12)
print(delta.days)
print(delta.seconds)
```


### Part 3.2: Adding and subtracting from dates

```{code-cell} python
week = timedelta(days=7)
last_week = now - week

print("last week:", last_week)
```

```{code-cell} python
tomorrow = now + timedelta(days=1)

print("tomorrow:", tomorrow)
```

### Part 3.3: Difference between dates

```{code-cell} python
birthday = datetime(2020, 6, 5)
age = now - birthday

print(age)
```

% ### Part 3 Exercises

% `````{exercise} Name
% :label: label-exercise
% 
% 1. Get the timedelta for a `fortnight` (`2` weeks).

% `````
% 
% `````{solution} label-exercise
% :class: dropdown
% 
% ```{code-block} python
% :caption: "Name Exercise"
% :class: full-width
% :linenos:
% 
% ```
% 
% `````

% Part 4: Timestamps and seconds math
% -----------------------------------

% Another way to represent a date and time is known as an
% {term}`epoch timestamp`.

% ```{code-cell} python
% now.timestamp()
% ```

% ```{code-cell} python
% # first moon walk
% # July 20, 1969
% ```


Reference
---------

### Format Codes

| Code(s) |        | Field         | Example                          | Format details                              |
|---------|--------|---------------|----------------------------------|---------------------------------------------|
| `%a`    |        | Weekday       | `"Sun"`                          | abbreviated name                            |
| `%A`    |        | Weekday       | `"Sunday"`                       | full name                                   |
| `%u`    |        | Weekday       | `"7"`                            | as number, Monday=1 (Solars: Sunday=1)      |
| `%w`    |        | Weekday       | `"0"`                            | as number, Sunday=0                         |
| `%b`    | `%h`   | Month         | `"Sep"`                          | abbreviated name                            |
| `%B`    |        | Month         | `"September"`                    | full name                                   |
| `%m`    |        | Month         | `"09"`                           | as number, zero-padded                      |
| `%d`    |        | Day of Month  | `"08"`                           | as number, zero-padded                      |
| `%e`    | `%-d`  | Day of Month  | `"8"`                            | as number                                   |
| `%y`    | `%g`   | Year          | `"13"`                           | two digit                                   |
| `%Y`    | `%G`   | Year          | `"2013"`                         | four digit                                  |
| `%H`    | `%I`   | Hour          | `"07"`                           | 24-hour clock, zero-padded                  |
| `%-H`   | `%-I`  | Hour          | `"7"`                            | 24-hour clock                               |
| `%M`    |        | Minute        | `"45"`                           | minute                                      |
| `%S`    |        | Second        | `"01"`                           | second                                      |
| `%f`    |        | Microsecond   | `"936048"`                       | zero-padded microsecond                     |
| `%p`    |        | Time Period   | `"AM"`                           | AM or PM                                    |
| `%Z`    |        | Timezone      | `"MTD"`                          | name                                        |
| `%Z`    |        | Timezone      | `"-0600"`                        | abbreviation                                |
| `%s`    |        | Epoch Seconds | `"1632494701"`                   | epoch timestamp                             |
| `%j`    |        | Day of Year   | `"267"`                          | zero-padded number, up to 366               |
| `%C`    |        | Century       | `"20"`                           | number (first two digits of year)           |
| `%W`    |        | Week of Year  | `"01"`                           | year starts at first Monday                 |
| `%U`    |        | Week of Year  | `"38"`                           | year starts at first Sunday                 |
| `%V`    |        | Week of Year  | `"38"`                           | year starts at first Monday with 4+ days    |
| `%c`    |        | Date and Time | `"Fri Sep 24 08:45:01 2021"`     | preferred                                   |
| `%+`    |        | Date and Time | `"Fri Sep 24 08:45:01 MDT 2021"` | national                                    |
| `%F`    |        | Date          | `"2021-09-24"`                   | same as %Y-%m-%d                            |
| `%D`    |        | Date          | `"09/24/21"`                     | same as %m/%d/%y                            |
| `%x`    |        | Date          | `"09/24/2021"`                   | preferred                                   |
| `%r`    |        | Time          | `"08:45:01 AM"`                  | 12 hour notation                            |
| `%T`    |        | Time          | `"08:45:01"`                     | %H:%M:%S                                    |
| `%R`    |        | Time          | `"08:45"`                        | 24 hour notation                            |
| `%X`    |        | Time          | `"08:45:01"`                     | preferred                                   |
| `%n`    |        | Character     | `"\n"`                           | newline                                     |
| `%t`    |        | Character     | `"\t"`                           | tab                                         |
| `%%`    |        | Character     | `"%"`                            | literal %                                   |

### See also

```{seealso}

* [Python.org Docs > datetime Objects](https://docs.python.org/3/library/datetime.html#datetime-objects)
* [Python.org Tutorial > 10.8 Dates and Times](https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)
* [Format Codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
* [Format Codes Specification](https://www.ibm.com/docs/en/zos/2.2.0?topic=services-ceeftdsformat-time-date-into-character-string)

```

### Glossary

```{glossary} Dates

date formatting codes
  A set of characters prefixed by `%` which represent a particular date or time
  field and presentation. For example `"%m"` is for the month as a number `01`-`12`
  while `"%M"` is for the full month name and `"%b"` is for the abbreviated
  month name.

timestamp
epoch timestamp
unix timestamp
  A representation of a particular point in time as an integer, the number of
  seconds since Jan 01 1970 UTC.

```


----

% TODO
% [x] datetime objects
% [x] datetime.today() / datetime.now()
% [ ] epoch / fromtimestamp / t.timestamp()
% [ ] isoformat / from isoformat
% [x] strftime / strptime
% [ ] compare format codes to standard
% [ ] relativedelta
% [ ] timezones
%     - datetime.fold
%     - datetime.tzinfo
