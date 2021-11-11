# Order of Operation
#
# replace variable names with values
# inner to outter then left to right
# exponents/multiplication/division then addition/subtraction

#######################################################################

# Exercise 1

color = "Yellow"

colors = {
    "white": 39,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
}

color_code = colors[color.lower()]
# color_code = colors["Yellow".lower()]
# color_code = colors["yellow"]
# color_code = 33

#######################################################################

# Exercise 2

import os

dirs = [
    "~",
    "projects",
    "coding-class",
]

path = os.pathsep.join(dirs) + os.pathsep
# path = "/".join(dirs) + "/"
# path = "~/projects/coding-class" + "/"
# path = "~/projects/coding-class/"


#######################################################################

# Exercise 3

def get_weather(x):
    return {}

data = []

assert get_weather(data) == {"temp": "27", "desc": "Partly cloudy"}, \
    "should extract a dict with temp and desc from request data"
# assert get_weather([]) == {"temp": "27", "desc": "Partly cloudy"}, \
#     "should extract a dict with temp and desc from request data"
# assert {} == {"temp": "27", "desc": "Partly cloudy"}, \
#     "should extract a dict with temp and desc from request data"
# assert False, "should extract a dict with temp and desc from request data"
# raise AssertionError("should extract a dict with temp and desc from request data")


#######################################################################

# Exercise 4

from pathlib import Path

srcdir = Path(__file__).parent.parent
outdir = Path(__file__).parent.parent / "_build"

newpath = outdir / path.relative_to(srcdir)

#######################################################################

# Exercise 5

def asciinema_player(opts):
    # opts = {"name": "adventure"}
    return f"<player name={opts['name']}></player>"
    # return f"<player name={'adventure'}></player>"
    # return "<player name=adventure></player>"

options = {"name": "adventure"}

results = [asciinema_player(opts=options)]
# results = [asciinema_player(opts={"name": "adventure"})]
# results = ["<player name=adventure></player>"]

#######################################################################

# Exercise 6

parents = [
    Path('/Users/alissahuskey/Dropbox/projects/python-class'),
    Path('/Users/alissahuskey/Dropbox/projects'),
    Path('/Users/alissahuskey/Dropbox'),
    Path('/Users/alissahuskey'),
    Path('/Users'),
    Path('/')
]

LOGDIR = Path(__file__).parents[2].joinpath("tmp")
# LOGDIR = Path("~/projects/python-class/expressions.py").parents[2].joinpath("tmp")
# LOGDIR = parents[2].joinpath("tmp")
# LOGDIR = Path('/Users/alissahuskey/Dropbox').joinpath("tmp")
# LOGDIR = Path('/Users/alissahuskey/Dropbox/tmp')

# object.method(arguments)

