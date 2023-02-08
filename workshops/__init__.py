"""Module for liveshare workshop files"""

import textwrap
import re

from console import fg

__ALL__ = ["header", "section", "div", "evaluate"]

MARKS = {
    True: fg.green("✔"),
    False: fg.red("✘"),
}

def header(title, char="-", indent=""):
    """Print a header"""
    print()
    print(indent, title, sep="")
    print(indent, char * len(title), sep="")

def section(part, title):
    """Print a section header"""
    header(f"{part}: {title}", char="=")

def div(part, title):
    """Print a subsection header"""
    header(f"{part}: {title}", char="-")

def stop():
    exit()

def mark(is_correct):
    return MARKS[is_correct]
    
def evaluate(expr, answer=None, context=None):
    print(f"Expression  : {expr}")
    if answer:
        solution = eval(expr, context)
        symbol = mark(solution == answer)

        print(f"Answer    {symbol} : {solution!r}")
        print(f"Solution    : {solution!r}")


def exercise(part, title, description, example=None, context=None):
    """Print an exercise and instructions"""

    div(part, title)
    margin=" " * 3
    print()

    for line in description.split("\n\n"):
        paragraph = re.sub(r"\s+", " ", line.strip())
        text = textwrap.fill(
            paragraph,
            60,
            initial_indent=margin,
            subsequent_indent=margin,
        )
        print(text, "\n")

    if context:
        header("Context", "~", indent=margin)
        text = textwrap.indent(text=textwrap.dedent(context), prefix=margin)
        print(text)

    if example:
        header("Example", "~", indent=margin)
        text = textwrap.indent(text=textwrap.dedent(example), prefix=margin)
        print(text)