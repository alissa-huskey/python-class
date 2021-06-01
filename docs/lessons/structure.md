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
    |-- __init__.py
    |-- easy.py
    |-- medium.py
    |-- hard.py
|-- __init__.py
|-- game.py
```

Variables and functions that are defined in your {file}`__init__.py` will be
available as part of your package.

```{code-block} python
:caption: game.py

from . import abort
```

### Relative imports

When importing from within the same package, you can use the shorthand `.`.

```{code-block} python
:caption: main.py

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

The Python Search Path
----------------------

When Python looks for a module or package it checks:

* the built-in modules and packages
* the working directory
* the list of paths stored in `sys.path`

The `sys.path` contains a list of path strings loaded from:

* the environment variable `PYTHONPATH`
* any file ending in `.pth` located in the search path

Executable scripts
------------------

When your code is in a package, it can be a little confusing how to go about
running it in a reliable way. In this part of the lesson we'll walk through
how to create an executable script that imports your own package.

Here's what our file structure will look like when we're done.

```
hangman/
|-- __init__.py
|-- words.py
|-- game.py
|-- main.py
bin/
| -- play
```

### Boil it down

You first want to provide a minimal interface, a single function if possible,
that will be used by your script. So first we'll create a `main.py` file that
contains a single a `main()` function.

```{code-block} python
:caption: main.py

from .words import WORDS
from .game import play

def main():
      play(WORDS)
```

### The script

Traditionally the `bin` directory (or `Scripts` on Windows) is used to store
executable scripts. We'll create the `play` script there.

```{code-block} python
:caption: bin/play
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Executable to play the hangman game"""

from hangman.main import main
main()
```

This will only work when run from the project directory. However, we can
modify the `sys.path` to include the project directory.

```{code-block} python
:caption: bin/play
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Executable to play the hangman game"""

import sys
from pathlib import Path

rootdir = Path(__file__).parent.parent
sys.path.append(str(rootdir))

from hangman.main import main
main()
```

### Making the script executable

Make it executable by running the `chmod` command.

```{code-block} console
:caption: command line
$ chmod +x bin/play
```

### Running the script

To run the script:

```{code-block} console
:caption: command line
$ bin/play
```

Exercise
--------

```{exercise} Hello World package

1. Create a new directory called `helloworld`
2. Create a subdirectory called `helloworld`
3. Create an empty {file}`__init__.py` file in that directory.
3. Create a `hello.py` script in that directory
4. Create a `main` function that prints `"Hello World"`
5. Create an executable `hello` script in a directory named `bin` or `scripts`
    - Add the project root directory to the `sys.path`.
    - Import and call your your `main` function 
6. Make the file executable
7. Run it
8. Bonus: Add the `helloworld/bin` directory to your `PATH`, then run `hello` from a different directory.

```

```{exercise} Goodbye

1. Add a `goodbye` module that contains a function `goodbye()` that prints `"Goodbye cruel world!"`
2. Import the `goodbye()` function in the `hello` module
3. In the `main()` function, after printing `"Hello World"`, call `goodbye()`.

```

```{exercise} Refactor

Refactor your code so that you end up with:

* a `goodbye` module that contains a `goodbye()` function
* a `hello` module that contains a `hello()` function that just prints `"Hello World!"`
* a new `main` module that 
    * imports the `hello()` and `goodbye()` functions from their respective modules
    * contains a `main()` function that calls `hello()` and `goodbye()`
* Modify your `hello` script to import from the `main` module instead of `hello`

```

Directory structure
-------------------

```{seealso}

* [Hitchhiker's Guide > Structuring your Project](https://docs.python-guide.org/writing/structure/)
* [OpenAstronomy Python Packaging Guide](https://packaging-guide.openastronomy.org/en/latest/index.html)

```

``` text
|-- .git/
    |-- config
    |-- ...
|-- .venv/
    |-- bin/
        |-- ipython
        |-- pip
        |-- pytest
        |-- python
        |-- ...
    |-- ...
|-- .vscode/
    |-- settings.json
    |-- ...
|-- bin/
    | -- play
|-- docs/
|-- hangman/
    |-- __init__.py
    |-- words.py
    |-- game.py
    |-- main.py
|-- tests/
    |-- __init__.py
    |-- test_words.py
    |-- test_game.py
    |-- test_main.py
|-- .editorconfig
|-- .env
|-- .gitignore
|-- README.md
|-- LICENSE
```

### Directories

#### .git

This is the folder that is created when you use the `git init` command and
contains all of your repository data. You will rarely deal with the files in
this directory directly, but the one file that is useful to know about is the
{file}`config` file.

```ini
[core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
    ignorecase = true
    precomposeunicode = true
[remote "origin"]
    url = https://github.com/alissa-huskey/python-class.git
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
    remote = origin
    merge = refs/heads/master
```

#### .venv/

Your virtual environment is stored in this directory if you set up
{command}`poetry` to store your virtual environment in your project
directories, and it is the standard directory for some other virtual
environment tools.

The executable scripts `python`, `pip`, and any installed modules are located
in the `.venv/bin` directory.

This directory also contains a {file}`.venv/bin/activate`. This file which is
used to start your virtual environment shell with the command
`source .venv/bin/activate`, upon which it defines a `deactivate` command.

VS Code will automatically activate source the {file}`.venv/bin/activate`
file in some cases, though not consistently enough to avoid the need to
launch VS Code from a `poetry` shell.

VS Code may also prompt you upon finding a `.venv` directory to select it for
the workspace. This will automatically configure some of the settings in your
per-project {file}`settings.json` file.

##### Poetry setup

To set up `poetry` to store your virtual env in your project directories.

```console
$ poetry config virtualenvs.in-project true
```

You will need to move the existing virtual env directory.

```console
$ mv $(poetry env info -p) ./.venv
```

#### .vscode/

This is the directory where the vscode settings for this project are stored.
Here is an example that that sets the Python interpreter for this project to
your projects `.venv` directory.

```json
{
    "python.venvPath": "${workspaceFolder}/.venv",
    "python.pythonPath": "${workspaceFolder}/.venv/bin/python",
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestEnabled": true,
}
```

#### bin/

As previously mentioned, this is generally where executable scripts are
stored.

#### docs/

This is generally where any project documentation is stored.


#### hangman/

This is the directory for the `hangman` package. Package names should have
short lowercase named without underscores.

The module file should have short all lowercase names with underscores as
needed.

#### tests/

Tests are stored in here. Test files should be named
{samp}`test_{module_or_topic}.py`.

### Files

#### .editorconfig

Used in conjunction with the [EditorConfig VS Code extension][editorconfig],
this file configures code style settings for the project to ensure
consistency amongst different tools, environments and developers. Here is a
comprehensive example for Python files.

```ini
# EditorConfig: https://EditorConfig.org
# Plugins for:
#  - Vim: https://github.com/editorconfig/editorconfig
#  - VS Code: https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true

[*.py]
indent_style = space
indent_size = 4
tab_width = 4
charset = utf-8
insert_final_newline = true
trim_trailing_whitespace = true
max_line_length = 88
quote_type = double
spaces_around_operators = true
```

You can keep a master {file}`.editorconfig` file in your home directory, then
in your per-project file either inherit selective settings by removing the
`root = true` line, or keep it to override all settings.

[editorconfig]: https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig

#### .env

This is a shell script file that allows you to configure environment
variables or run other commands for this project.





* README.md
      * [Make a README](https://www.makeareadme.com/)

* .gitignore
      * [github Python template](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore)
      * [github/gitignore](https://github.com/github/gitignore)
      * [github.io Python template](https://www.toptal.com/developers/gitignore/api/python)
      * [gitignore.io](http://gitignore.io/)
      * [man page](https://git-scm.com/docs/gitignore)
      * [The Git Book > Ignoring Files](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring)

* .vscode-exclude


See also
--------

```{seealso}

* [Python.org Tutorial > Modules & Packages](https://docs.python.org/3/tutorial/modules.html)
* [PEP 8 -- the Style Guide for Python Code > Packages and Modules](https://pep8.org/#package-and-module-names)
* [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)

```

Glossary
--------

```{glossary} structure

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
% [ ] .gitignore
% [ ] .vscode-exclude
% [ ] tests
% [ ] virtual environments
% [ ] installing your package
