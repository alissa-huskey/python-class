"""
People files

This exercise is to generate files for a list of people that you can use to
keep track of notes, birthday info, gift ideas etc.

At the end of the exercise you should have a folder containing a file for each
person that contains something related to that person.

1. Make a list of people's names that you'd like to keep track of information about.
2. Create a new directory called something like `people` if it does not exist.
3. Iterate over the list of people.
    - Create a blank file called `{name}.txt` in the `people` directory if it doesn't exist.
    - Write something to the file about that person
"""

from pathlib import Path


def main():
    datadir = Path.cwd() / "data" / "students"
    datadir.mkdir(exist_ok=True)

    students = {
        "jayson": "Tuesday",
        "sean": "Monday",
        "brian": "Tuesday",
        "nila": "Monday"
    }

    for name in students:
        filepath = datadir / f"{name}.md"
        print(f"Writing file for student '{name}' to: {filepath}")

        text = ""
        text += f"{name.title()}\n"
        text += (len(name) * "=") + "\n\n"
        text += f"Class: {students[name]}\n"

        with open(filepath, "w") as fp:
            fp.write(text)

main()
