#!/usr/bin/env python
"""
Parse CSV results from google form "Python Class Schedule Survey":
https://forms.gle/TzK1MnzoLo5iF1fH9
"""

import datetime
from pathlib import Path
from pprint import pprint
import pytz
import time

from blessed import Terminal
import pandas

TERM = Terminal()
DATADIR = Path(__file__).parent.parent.parent / "data"
TODAY = datetime.datetime.today()
TZ = pytz.timezone("US/Mountain")

WEEKDAYS = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
]

def parse_csv(filepath):
    """Return DataFrame object for csv file at filepath"""
    weekday_headers = pandas.MultiIndex.from_product(
        [
            WEEKDAYS,
        [
            "start",
            "end",
            "preference",
            "comments",
        ]],
        names=["day", "value"]
    )

    headers = [
        ("timestamp", ""),
        ("name", ""),
        ("timezone", ""),
        *weekday_headers,
        ("upcoming", ""),
        ("notes", ""),

    ]

    idx = pandas.IndexSlice
    data = pandas.read_csv(filepath, index_col=1)
    data.columns = pandas.MultiIndex.from_tuples(
        headers, names=["header", "subheader"])

    #  table = data.loc[:, idx[:, "start"]]
    #  print(table.T)

    return data


def between(start_range, end_range, period):
    """Return True if period is between from and to"""
    if pandas.isna(start_range) or pandas.isna(end_range):
        return False

    return (start_range.time() <= period.start_time.time()) and \
        (end_range.time() >= period.end_time.time())

def normalize_time(time_str, tz_str):
    """Return a datetime object converted to Mountain time"""
    if pandas.isna(time_str):
        return time_str

    t_struct = time.strptime(time_str, "%H:%M")
    t = datetime.datetime(*t_struct[:5], tzinfo=pytz.timezone(f"US/{tz_str}"))

    return t.astimezone(TZ)

def main():
    filepath = DATADIR / "schedule.csv"
    data = parse_csv(filepath)
    idx = pandas.IndexSlice

    availability = {
        "Preferred":    TERM.green("\u2605"),    # ★
        "Workable":     TERM.green("\u2714"),    # ✔
        "Last resort":  TERM.red("\u2714"),      # ✔
        "Not doable":   TERM.red("\u2716"),      # ✖
    }

    frequencies = (
        pandas.offsets.Hour(1),
        #  pandas.offsets.Minute(30),
        #  pandas.offsets.Minute(15),
    )

    #  pprint(data.columns)
    #  pprint(data.T)


    for day in WEEKDAYS:
        col = data.xs(day, axis=1, level="header")
        data[(day, "available")] = col["preference"].apply(
            lambda x: availability[x])
        data[(day, "start_time")] = data.apply(
            lambda row: normalize_time(row[(day, "start")], row[("timezone", "")]),
            axis=1)
        data[(day, "end_time")] = data.apply(
            lambda row: normalize_time(row[(day, "end")], row[("timezone", "")]),
            axis=1)

    freq = pandas.offsets.Hour(1)
    for day in WEEKDAYS:
        start_range = data[(day, "start_time")].min()
        end_range = data[(day, "end_time")].max()

        ts = pandas.Series(
            None,
            index=pandas.period_range(
                start_range,
                end_range,
                freq=freq),
            dtype=pandas.BooleanDtype()
        )

        ts = ts.resample(freq).mean()
        df = pandas.DataFrame(columns=ts.index, index=data.index)
        df = data[(day)].apply(
            ts.index.map(
                lambda p: lambda r: between(r["start_time"], r["end_time"], p)
            ), axis=1)
        df.columns = ts.index.map(
            lambda x: x.start_time.strftime("%I:%M%p"))
        df.index = df.index.str.extract(r"^([a-zA-Z]*)", expand=False)

        margin = 5
        idx_width = df.index.map(len).max() + 2
        width = TERM.width - idx_width - margin
        col_width = int(width // len(df.columns)) - 5
        header_width = col_width  + 3
        space = " " * col_width
        #  space = "[{:>{col_width}}]".format(" ", col_width=col_width)

        bool_to_color = lambda is_true: (TERM.on_black(space),
                                            TERM.on_green(space))[int(is_true)]

        print("{:=<{w}}".format(f"{day} ", w=TERM.width-3))
        print()
        print( (" " *idx_width), " ".join([f"{c:>{header_width}}" for c in df.columns.values]), sep="")
        print(df.to_string(
            formatters=[bool_to_color]*len(df.columns),
            header=False
        ))
        print()










if __name__ == "__main__":
    main()
