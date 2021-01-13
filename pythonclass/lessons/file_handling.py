"""Demo of saving and opening json files."""

from sys import stderr
from pprint import pprint
from pathlib import Path
import json

import requests


URL = "http://api.open-notify.org/astros.json"
FILENAME = "astros.json"


def abort(*args):
    """Print error message and exit"""
    print("Error:", *args, file=stderr)
    exit(1)


def say(*args):
    """Print a formatted user message"""
    print("|  ", *args)


def download():
    """download and save JSON file"""
    say("Ok, downloading...")

    response = requests.get(URL)

    # open the file in write mode
    fh = open(FILENAME, "w")

    # basic file handling -- write the raw data to the file
    # fh.write(response.text)

    # fancy json file handling
    # convert the json data to an indented string with newlines
    # and write the resulting string to the file
    json.dump(response.json(), fh, indent=2)

    # close the file handler
    # note: contents may not actually get written until this is called
    fh.close()

    # print the data
    say("Here's your downloaded data:\n")
    data = response.json()
    pprint(data)


def load():
    """load saved json file"""

    say("Ok, loading...")

    # make sure the file exists
    if not Path(FILENAME).exists():
        abort("File does not exist:", FILENAME)

    # open the file in read mode
    fh = open(FILENAME)

    # read the file contents
    text = fh.read()

    # close the file
    fh.close()

    # parse and print the json data
    say("Here's your loaded data:\n")
    data = json.loads(text)
    pprint(data)


def main():
    """Primary UX -- print the menu and act on the response."""

    while True:
        # print the menu
        print()
        for opt in ["load", "download", "quit"]:
            print(f"[{opt[0].upper()}]{opt[1:]}")

        # get the user selection
        choice = input("> ").lower().strip()

        if choice == "d":
            download()
        elif choice == "l":
            load()
        elif choice == "q":
            exit()
        else:
            print("Try again.")


if __name__ == "__main__":
    main()
