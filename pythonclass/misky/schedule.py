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
from dateutil.parser import parse

from blessed import Terminal
import pandas

TERM = Terminal()
DATADIR = Path(__file__).parent.parent.parent / "data"
TODAY = datetime.datetime.today()
TZ = pytz.timezone("US/Mountain")
PER_HOUR = pandas.offsets.Hour(1)

WEEKDAYS = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
]

AVAILABILITY = {
    "Preferred":    TERM.green("\u2605"),    # ★
    "Workable":     TERM.green("\u2714"),    # ✔
    "Last resort":  TERM.red("\u2714"),      # ✔
    "Not doable":   TERM.red("\u2716"),      # ✖
}


def parse_csv(filepath):
    """Return DataFrame object for csv file at filepath"""
    idx = pandas.IndexSlice
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
    #  breakpoint()
    #  data.index = data.index.str.extract(r"^([a-zA-Z]*)", expand=False)
    data.index = data["name"].str.lower().str.extract(r"^([a-zA-Z]*)",
                                                      expand=False)

    #  table = data.loc[:, idx[:, "start"]]
    #  print(table.T)

    #  print(col.T)
    #  return data

    for day in WEEKDAYS:
        col = data.xs(day, axis=1, level="header")

        # add available column with symbol
        data[(day, "available")] = col["preference"].apply(
            lambda x: AVAILABILITY[x])

        # fill any missing end values where start is not empty
        mask = data.loc[:, idx[day, "start"]].notna()
        data.loc[mask, (day, "end")] = data.loc[mask, idx[day, "end"]].fillna("23:59")

        # add start_time column with time adjusted to MST
        data[(day, "start_time")] = data.apply(
            lambda row: normalize_time(row[(day, "start")], row[("timezone", "")]),
            axis=1)

        # add end_time column with time adjusted to MST
        data[(day, "end_time")] = data.apply(
            lambda row: normalize_time(row[(day, "end")], row[("timezone", "")]),
            axis=1)

    return data


def has_period(row, period):
    """Return True if period is between start and end time"""
    if row[["start_time", "end_time"]].isnull().any():
        return False

    available_hours = pandas.date_range(
        start=row["start_time"],
        end=row["end_time"],
        freq=PER_HOUR,
    )
    available_hours = available_hours.floor(PER_HOUR)
    time = TZ.localize(period.to_timestamp())

    return time in available_hours

def normalize_time(time_str, tz_str):
    """Return a datetime object converted to Mountain time"""
    if pandas.isna(time_str):
        return time_str

    tz = pytz.timezone(f"US/{tz_str}")
    dt = tz.localize(parse(time_str))
    return dt.astimezone(TZ)

def hourly(data):
    """Generate data frame with per-hour boolean values for availability"""
    frames = []

    for day in WEEKDAYS:
        start_range = data[(day, "start_time")].min()
        end_range = data[(day, "end_time")].max()

        # generate a period range index covering every hour
        # that people have availability for
        periods = pandas.period_range(
                start_range,
                end_range,
                freq=PER_HOUR)

        # pretty printed hour
        hours = periods.map(lambda x: x.start_time.strftime("%I:%M%p"))

        #  df.columns = ts.index.map(
        #      lambda x: x.start_time.strftime("%I:%M%p"))

        # generate a (day, hour) MultiIndex
        cols = pandas.MultiIndex.from_tuples(
            zip([day]*len(hours), hours),
            names=["day", "hour"]
        )

        # generate a matrix of boolean values for availability in period
        matrix = data[day].apply(
            periods.map(
                lambda period: lambda row: has_period(row, period)
            ), axis=1
        ).to_numpy()


        # create dataframe
        df = pandas.DataFrame(matrix, index=data.index, columns=cols)

        # change the index to include the availbility symbol
        width = df.index.map(len).max()
        df.index = data[day].apply(lambda x: f"{x.name:>{width}} {x['available']}", axis=1)

        # append to master dataframe
        #  frame = frame + df
        frames.append(df)

    return frames

def visualize(table):
    """Print a bar graph for dataframe"""

    # get the data for this day
    #  table = hours[day]
    day = table.columns.get_level_values("day")[0]
    table = table[day]

    margin = 5
    idx_padding = 2
    nonprinting_length = 11
    real_idx_width = table.index.map(len).max()
    idx_width = real_idx_width - nonprinting_length + idx_padding
    max_width = TERM.width - margin
    col_width = 7
    #  header_width = col_width  + 3
    space = " " * col_width

    bool_to_color = lambda is_true: (TERM.on_black(space),
                                        TERM.on_green(space))[int(is_true)]

    # convert True/False to ascii colored strings
    table = table.applymap(bool_to_color)

    # print the day title
    title = f"{day} ".ljust(max_width, "=")
    print(title, "\n")

    # print the header row
    left_margin = " " * idx_width
    headers = " ".join(table.columns.to_list())
    print(left_margin, headers, "\n", sep="")

    for row in table.iterrows():
        name = row[0]
        padding = " " * idx_padding
        bars = " ".join(row[1])
        print( name, padding, bars, "\n", sep="")

    #  print( (" " *idx_width), " ".join([f"{c:>{col_width}}" for c in table.columns.values]), sep="")
    #  print(table.to_string(header=False))

    print()

def show(frames):
    """Print all days"""
    for df in frames:
        visualize(df)

def main():
    filepath = DATADIR / "schedule.csv"
    data = parse_csv(filepath)
    frames = hourly(data)
    show(frames)
    return data, frames


if __name__ == "__main__":
    main()
