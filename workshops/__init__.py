"""Module for liveshare workshop files"""

__ALL__ = ["header", "section", "div"]

def header(title, char="-"):
    """Print a header"""
    print()
    print(title)
    print(char * len(title))

def section(part, title):
    """Print a section header"""
    header(f"{part}: {title}", char="=")

def div(part, title):
    """Print a subsection header"""
    header(f"{part}: {title}", char="-")

def stop():
    exit()

def exercise(expr, solve=False):
    print(f"Expression  : {expr}")
    if solve:
        solution = eval(expr, globals=globals())
        print(f"Solution    : {solution}")


