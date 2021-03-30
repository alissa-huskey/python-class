Structuring Python Projects
===========================

This lesson will discuss how to organize the code in your Python project and
how Python then finds your code.

Modules
-------

A module is a file that contains Python code like that can be {term}`imported <import>`
into other Python files. This can be used to split your code into multiple
files so that your code is more organized.

```{code-block} python
:caption: formatting.md
"""Module of output formatting functions"""

WIDTH = 50

def header(title, width=WIDTH, char="-"):
    underline = len(title) * char
    lines = []
    lines.append(title.center(width))
    lines.append(underline.center(width))
    return "\n".join(lines) + "\n\n"

def div(width=WIDTH):
    return (width * "~") + "\n"

def section(title, contents):
    text = ""
    text += header(title)
    text += contents + "\n\n"
    text += div() + "\n"
    return text
```

This can then be imported into another file.

```{code-block} python
:caption: main.py
import formatting

def main():

    name = input("What's your name? ")
    title = "Welcome."
    contents = f"Well hello there {name.title()}."

    text = formatting.section(title, contents)
    print(f"\n\n{text}")

main()
```

:::{note}

The term "module" is often used to refer to external code installed from the
pipy.org repository. For example, someone might refer to the ["requests module"](https://pypi.org/project/requests/).
This is the broad software engineering usage of the word which refers to an
interchangeable component like a plugin or library.

In the Python lexicon, these are called {term}`packages <package>`.

:::

Packages
--------

A package is a group of modules in the same directory which also contains a
file named {file}`__init__.py`.

For example, imagine we have a hangman package with two modules. The
{file}`words.py` module contains a `WORDS` list, and the {file}`game.py`
module contains the functions to play the game.

```
hangman/
|-- __init__.py
|-- game.py
|-- words.py
```

You could import the whole package like so.

```{code-block} python
import hangman

hangman.play(hangman.words.WORDS)
```

Or import each module from the package separately.

```{code-block} python
from hangman import game
from hangman import words

game.play(words.WORDS)
```

Or import individual variables and functions from the modules.

```{code-block} python
from hangman.game import play
from hangman.words import WORDS

play(WORDS)
```

### Subpackages

You can further divide your code into subpackages, for example:

```
hangman/
|-- words/
    |-- easy.py
    |-- medium.py
    |-- hard.py
|-- game.py
```

### The `__init__.py` file

The `__init__.py` file is executed when the package is imported. This file
can be, and often is, blank. This can also be used to set up variables or
general purpose functions for your module.

```{code-block} python
:caption: __init__.py

__version__ = "0.0.1"

def abort(message):
    print(f"ERROR: {message}")
    exit(1)
```

### Relative imports

When importing from within the same package, you can use the shorthand `.` or
to import from the same package.

```{code-block} python
:caption: main.py

from . import abort
from .words.easy import WORDS
from .game import play

def main():
    play(WORDS)
```

If you're importing from a subpackage you can reference the parent package by
using `..`. For example, from one of the `words` modules we could import
the `abort` function:

```{code-block} python
:caption: easy.py

from .. import abort
```

The Python Search Path
----------------------

When Python looks for a module or package it checks:

* the built-in modules and packages
* the working directory
* the list of paths stored in `sys.path`

The `sys.path` contains a list of path strings loaded from:

* the environment variable `PYTHONPATH`
* any file ending in `.pth` located in the search path

Importing your own package
--------------------------

```
hangman/
|-- words.py
|-- game.py
|-- main.py
|-- bin/
    | -- play
```

```{code-block} python
:caption: main.py

from .words import WORDS
from .game import play

def main():
	play(WORDS)
```

```{code-block} python
:caption: bin/play
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Executable to play the hangman game"""

from hangman.main import main
main()
```

See also
--------

```{seealso}

* [Python.org Tutorial > Modules & Packages](https://docs.python.org/3/tutorial/modules.html)

```

Glossary
--------

```{glossary}

module
    a file containing Python definitions and statements

package
    a directory containing a {file}`__init__.py` file and other Python modules



```

% TODO
% ====
% [x] modules
% [x] packages
% [x] PYTHON_PATH
% [x] relative imports
% [x] __init__.py
% [ ] __main__
% [ ] __all__
