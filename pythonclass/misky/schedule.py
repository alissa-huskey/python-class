#!/usr/bin/env python
"""
Parse CSV results from google form "Python Class Schedule Survey":
https://docs.google.com/forms/d/1iLeT_ucQj1-3CR1o9zwL3J3ZG66sLbN-swczFEpop4I/edit
"""

from datetime import datetime
from dateutil.parser import parse, parserinfo
from pathlib import Path
from pprint import pprint
import pytz
import time

from blessed import Terminal
import pandas
import click

WEEKDAY_ABBR = dict(parserinfo.WEEKDAYS)
WEEKDAYS = WEEKDAY_ABBR.values()
VALID_WEEKDAYS = list(WEEKDAYS) + list(WEEKDAY_ABBR.keys())

class Schedule():
    DATADIR = Path(__file__).parent.parent.parent / "data"

    TERM = Terminal()

    PER_HOUR = pandas.offsets.Hour(1)

    AVAILABILITY = {
        "Preferred":    click.style("\u2605", fg="green"),    # ★
        "Workable":     click.style("\u2714", fg="green"),    # ✔
        "Last resort":  click.style("\u2714", fg="red"),      # ✔
        "Not doable":   click.style("\u2716", fg="red"),      # ✖
    }

    HEADERS = [
        ("timestamp", ""),
        ("name", ""),
        ("timezone", ""),
        *pandas.MultiIndex.from_product(
            [
                WEEKDAYS,
                [
                    "start",
                    "end",
                    "preference",
                    "comments",
                ]
            ],
            names=["day", "value"]
        ),
        ("upcoming", ""),
        ("notes", ""),

    ]

    def __init__(self, timezone="Mountain", days=WEEKDAYS, students=[]):
        """Initializer"""
        self.filepath = self.DATADIR / "schedule.csv"
        self.timezone = pytz.timezone(f"US/{timezone}")
        self.students = students
        self.days = days
        self.data = None
        self.hourly = {}

    def has_period(self, row, period):
        """Return True if period is between start and end time"""
        if row[["start_time", "end_time"]].isnull().any():
            return False

        available_hours = pandas.date_range(
            start=row["start_time"],
            end=row["end_time"],
            freq=self.PER_HOUR,
        ).floor(self.PER_HOUR)

        time = self.timezone.localize(period.to_timestamp())

        return time in available_hours

    def normalize_time(self, time_str, tz_str):
        """Return a datetime object converted to Mountain time"""
        if pandas.isna(time_str):
            return time_str

        tz = pytz.timezone(f"US/{tz_str}")
        dt = tz.localize(parse(time_str))
        return dt.astimezone(self.timezone)

    @property
    def people(self):
        """Return a list of first names, lowercased from the name column of
           self.data"""
        return self.data["name"].str.lower().str.extract(
            r"^([a-zA-Z]*)", expand=False)

    def load(self):
        """Load and parse csv file, then generate hourly dataframes"""
        return self.from_csv().parse().mkhourly()

    def from_csv(self):
        """Set self.data to DataFrame loaded from csv file at self.filepath"""
        self.data = pandas.read_csv(self.filepath, index_col=1)
        self.data.columns = pandas.MultiIndex.from_tuples(
            self.HEADERS, names=["header", "subheader"])
        self.data.index = self.people
        return self

    def parse(self):
        """Cleanup and filter self.data"""
        idx = pandas.IndexSlice

        for day in WEEKDAYS:
            col = self.data.xs(day, axis=1, level="header")

            # add available column with symbol
            self.data[(day, "available")] = col["preference"].apply(
                lambda x: self.AVAILABILITY[x])

            # fill any missing end values where start is not empty
            mask = self.data.loc[:, idx[day, "start"]].notna()
            self.data.loc[mask, (day, "end")] = self.data.loc[
                mask,
                idx[day, "end"]
            ].fillna("23:59")

            # add start_time column with time adjusted to MST
            self.data[(day, "start_time")] = self.data.apply(
                lambda row: self.normalize_time(
                    row[(day, "start")],
                    row[("timezone", "")],
                ),
                axis=1)

            # add end_time column with time adjusted to MST
            self.data[(day, "end_time")] = self.data.apply(
                lambda row: self.normalize_time(
                    row[(day, "end")],
                    row[("timezone", "")],
                ),
                axis=1)

        # filter to selected students
        if self.students:
            self.data = self.data.loc[list(self.students)]

        # filter to selected days
        if self.days != WEEKDAYS:
            self.data = self.data[self.days]

        return self

    def mkhourly(self):
        """Set self.hourly to a dict of day: df, where df is a DataFrame
           containing per-hour boolean values reflecting availability"""
        for day in self.days:
            start_range = self.data[(day, "start_time")].min()
            end_range = self.data[(day, "end_time")].max()

            # generate a period range index covering every hour
            # that people have availability for
            periods = pandas.period_range(
                    start_range,
                    end_range,
                    freq=self.PER_HOUR)

            # pretty hour strings
            hours = periods.map(lambda x: x.start_time.strftime("%I:%M%p"))

            # generate a matrix of boolean values for availability in each period
            matrix = self.data[day].apply(
                periods.map(
                    lambda period: lambda row: self.has_period(row, period)
                ), axis=1
            ).to_numpy()

            # create dataframe
            df = pandas.DataFrame(matrix, index=self.data.index, columns=hours)

            # add availbility symbol to index
            width = df.index.map(len).max()
            df.index = self.data[day].apply(lambda x: f"{x.name:>{width}} {x['available']}", axis=1)

            # add to dict
            self.hourly[day] = df

        return self

    def visualize(self, day, table):
        """Print a bar graph for dataframe"""

        margin = 3                         # screen safety margin
        idx_padding = 2                    # padding between index label and values
        nonprinting_length = 11            # number of nonprinting chars in index

        max_width = self.TERM.width - margin    # maximum screen width
        col_width = len("HH:MMAP")         # width of each column

        # number of printable characters in the index
        idx_width = table.index.map(len).max() - nonprinting_length + idx_padding

        bar = " " * col_width              # spaces to fill each cell with

        # return ascii colored string associated with boolean is_true
        bool_to_color = lambda is_true: (self.TERM.on_black(bar),
                                            self.TERM.on_green(bar))[int(is_true)]

        # convert all True/False values to ascii colored strings
        table = table.applymap(bool_to_color)

        # print the day title
        title = f"{day} ".ljust(max_width, "=")
        print(title, "\n")

        # print the header row
        tz = datetime.now(self.timezone).tzname()
        timezone = f"({tz})  ".rjust(idx_width)
        headers = " ".join(table.columns.to_list())
        print(timezone, headers, "\n", sep="")

        # print the name and availbility bars for each person
        for row in table.iterrows():
            name = row[0]
            padding = " " * idx_padding
            bars = " ".join(row[1])
            print( name, padding, bars, "\n", sep="")

        print()


    def show(self):
        """Print visualizations for all hourly dataframes"""
        for day, df in self.hourly.items():
            self.visualize(day, df)


def process_weekdays(ctx, values):
    """Convert all weekdays to titlecase, convert abbreviations to full day
       names, and sort chronologicly. (click option callback)"""
    days = []

    for v in values:
        day = v.title()
        if day not in WEEKDAYS:
            day = WEEKDAY_ABBR[day]
        days.append(day)

    chrono = lambda d: [i for i, wd in enumerate(parserinfo.WEEKDAYS)
                        if d in wd ][0]
    return sorted(days, key=chrono)


# load the csv to get a list of names to use for --student choice options
DOC = Schedule().from_csv()


@click.command()
@click.option("-t", "--timezone",
              default="Mountain", show_default=True,
              type=click.Choice(
                  [ t[3:] for t in pytz.all_timezones if t.startswith("US") ],
                  case_sensitive=False
              ),
              callback=lambda ctx, value: value.title(),
              help="convert all times to this timezone")
@click.option("-d", "--day", "days",
              default=WEEKDAYS, show_default="all",
              multiple=True,
              type=click.Choice(VALID_WEEKDAYS, case_sensitive=False),
              callback=process_weekdays,
              help="filter to listed days (multiple ok)")
@click.option("-s", "--student", "students",
              multiple=True,
              default=[], show_default="all",
              type=click.Choice(DOC.people, case_sensitive=False),
              callback = lambda ctx, values: [v.lower() for v in values],
              help="filter to listed students (multiple ok)")
def cli(**kwargs):
    """print visualization of schedule.csv"""
    doc = Schedule(**kwargs).load()
    doc.show()

if __name__ == "__main__":
    cli()
