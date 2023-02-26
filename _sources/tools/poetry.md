(introduction)=
Poetry
======

Poetry is the go-to dependency management and packaging tool used by Python
developers. It takes the long and complicated toolchain available in the Python
world and wraps it in a few easy to use best practices.

[Poetry](https://python-poetry.org/docs) provides...

```{highlights}
* **Dependency management**: keep track of Python modules that you need for
  a project and easily install them in any environment.
* **Virtual environments**: run your code with an isolated set of dependencies.
* **Standardization**: tools for starting new projects according to
  best practices.
* **Packaging**: building a Python package and publishing it to repositories
  like [PyPi](https://pypi.org/).
```

```{include} ../toc.md
```

:::{attention}
Poetry does not manage installing or switching between Python versions.
It just make sure that the `python` command points to the right version or
prints an error if it cannot be found.
For managing Python versions use [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win).
:::



Quickref
--------

| Command                                     | Description                                                     |
|---------------------------------------------|-----------------------------------------------------------------|
| `poetry new [--name <package-name>] <path>` | generate directory for a new project                            |
| `poetry init`                               | interactively generate pyproject.toml                           |
| `poetry add [--dev] <module>`               | add and install dependency to the virtual env                   |
| `poetry remove [--dev] <module>`            | remove and install dependency to the virtual env                |
| `poetry update [--dev] <module>`            | update virtual env to reflect changes to pyproject.py           |
| `poetry install [--no-root]`                | install the dependencies [and the package] in the virtual env   |
| `poetry shell`                              | start a virtual env shell                                       |
| `poetry run <cmd> [<arg>...]`               | run the command [with args] in the virtual environment          |
| `poetry show [--tree] [<package>]`          | list dependencies for a package                                 |
| `poetry env [info [--path]]`                | display information about the current virtual env               |
| `pip install .`                             | do a system-wide install of your project                        |
| `pip uninstall <package-name>`              | uninstall package from your system                              |
| `poetry help [command]`                     | show poetry help [for command]                                  |

Project Setup
-------------

### New projects

When starting a project from scratch, use the `poetry new` command to create a
directory and generate files.

Usage: `poetry new [--name <package-name>] <path>`

The `--name` flag is optional. If it is not passed, the package name defaults
to the directory name.

For example:

```{code-block} bash
---
caption: command line
---
$ poetry new --name demo poetry-demo
```

Will create the following files:

```
poetry-demo
├── README.rst
├── demo
│   └── __init__.py
├── pyproject.toml
└── tests
    ├── __init__.py
    └── test_demo.py
```

* `README.rst`: an empty README file
* `pyproject.toml`: the Poetry config file for this project
* `demo/`: the directory where your code should go
* `tests/`: the directory where your tests should go
* `tests/test_demo.py`: a test skeleton
* `*/__init__.py`: a special file that indicates that all the files in the same directory are part of a package
* `poetry.lock`: (created later, do not edit) generated based on the contents of `pyproject.toml`. This includes dependency details for the specific versions installed by poetry.

### Existing projects

To start using Poetry on an existing project, use the `poetry init`
command to interactively generate the `pyproject.toml` file.

Project configuration
---------------------

The heart of Poetry is in the `pyproject.toml` file.

Here are the contents of the `pyproject.toml` file from the `python-demo` project:

```{code-block} toml
---
caption: pyproject.toml
---
[tool.poetry]
name = "demo"
version = "0.1.0"
description = ""
authors = ["... <...@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

Here is some information on some of the configuration parameters available.

* `[tool.poetry]`: This section includes details about your project.
  - `readme`: (optional) readme file path
  - `repository`: (optional) repository URL
  - `documentation`: (optional) documentation URL
* `[tool.poetry.dependencies]`:
  - the version of Python to use
  - a list of Python modules that this project depends on. (For example `requests`.)
* `[tool.poetry.dev-dependencies]`: a list of Python modules that this project uses during development. (For example `ipython`.)
* `[build-system]`: details needed by Poetry. (You should rarely if ever need to change this section.)
* `[tool.poetry.scripts]`: (optional) python executable scripts to be generated and installed as part of your package. See [Scripts](#Scripts) below.

:::{seealso}
* [python-poetry.org: The pyproject.toml file](https://python-poetry.org/docs/pyproject/)
  Poetry documentation on the `[tool.poetry]` sections of the `pyproject.toml` file.
:::

Managing Dependencies
---------------------

### Adding, removing and installing

Dependencies in the `[tool.poetry.dependencies]` and
`[tool.poetry.dev-dependencies]` sections of `pyproject.toml` have the format
of:

`<package> = <version>`

You can edit the `pyproject.toml` file directly but it is probably easiest to
use the `poetry add` and `poetry remove` commands. They update the
`pyproject.toml` file and also install or uninstall the modules in the virtual
environment.

For example:

```{code-block} bash
---
caption: command line
---
$ poetry add --dev ipython
$ poetry add requests
$ poetry remove --dev xdoctest
$ poetry remove pandas
```

If you edit the `pyproject.toml` file directly or if you check out a project
on a new computer, use the `poetry install` command to install all modules in
the virtual environment. The optional `--no-root` flag will install only the
dependencies but not your own package.

```{code-block} bash
---
caption: command line
---
$ poetry install --no-root   # install dependencies in the virtual env
$ poetry install             # install dependencies and your package in the virtual env
```

### Versions

Most Python packages use semantic versioning, which has the form of:

`<major>`.`<minor>`.`<patch>`

In `pyproject.toml` versions can have formats like:

* `1.2.3`: only version `1.2.3`
* `^1.2`: at least `1.2` and updates allowed within version `1`
* `~1.2`: at least `1.2` and updates allowed within version `1.2`
* `1.2.*`: at least `1.2` and updates allowed within version `1.2`
* `>= 1.2, < 1.5`: at least `1.2` and less than `1.5`
* `>= 1.2, ! 1.2.5`: at least `1.2` but not `1.2.5`


:::{seealso}
* [Semantic Versioning](https://semver.org/)
  The semantic versioning specification.

* [python-poetry.org: Versions and constraints](https://python-poetry.org/docs/versions/)
  Poetry documentation on specifying dependency version constraints.
:::

Using Poetry
------------

Once you have all of your dependencies installed you will need to run your
code and executables from the virtual environment.

Say I have a file `astros.py` that uses the `requests` module.

```{code-block} python
---
caption: demo/astros.py
---
import requests

def main():
    """Print out the astronauts currently in space using NASAs astros API
    https://api.nasa.gov/
    """

    response = requests.get("http://api.open-notify.org/astros.json")

    if not response.ok:
        print(f"ERROR: Request failed: {response.status_code} {response.reason}")
        return

    data = response.json()

    print(f"There are {data['number']} people in space today.")

    for astro in data['people']:
        print(f"- {astro['name']}")


if __name__ == "__main__":
    main()
```

Here I run the `astros.py` script from normal shell where the `requests`
module is not installed.

```{code-block} bash
---
caption: command line
---
$ python demo/astros.py
Traceback (most recent call last):
  File "demo/astros.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```

Similarly, here I call `xdoctest` which is installed through the `xdoctest`
module. It is not found in the normal shell because that module is only
installed in the virtual environment.

```{code-block} bash
---
caption: command line
---
$ xdoctest --version
zsh: command not found: xdoctest
```

The easiest way to run commands from the virtual environment is to use the
`poetry shell` command. It will update all of your paths so that your
dependencies, executables installed from modules (like `ipython`), and your own
package scripts and code can be found.

```{code-block} bash
---
caption: command line
---
$ poetry shell
Spawning shell within .../virtualenvs/demo-IDGvf4ns-py3.8
(demo-IDGvf4ns-py3.8) $
```

Now if I run the same commands they work as expected until you exit the shell.

```{code-block} bash
---
caption: command line
---
(demo-IDGvf4ns-py3.8) $ python demo/astros.py
There are 7 people in space today.
- Sergey Ryzhikov
- Kate Rubins
- Sergey Kud-Sverchkov
- Mike Hopkins
- Victor Glover
- Shannon Walker
- Soichi Noguchi
```

```{code-block} bash
---
caption: command line
---
(demo-IDGvf4ns-py3.8) $ xdoctest --version
0.15.0
```

Alternately, you can also use the `python run` command from a normal shell to
run any command from the virtual environment.

```{code-block} bash
---
caption: command line
---
$ poetry run xdoctest --version
0.15.0
```

Getting info
------------

To list the currently installed packages use the `poetry show` command.  The
`--tree` flag formats the list as a dependency tree.

```{code-block} bash
---
caption: command line
---
$ poetry show --tree
ipython 7.19.0 IPython: Productive Interactive Computing
├── appnope *
├── backcall *
...
pytest 5.4.3 pytest: simple powerful testing with Python
├── atomicwrites >=1.0
...
requests 2.25.0 Python HTTP for Humans.
├── certifi >=2017.4.17
...
xdoctest 0.15.0 A rewrite of the builtin doctest module
└── six *
```

To get information about the virtual environment for the current project use
the `poetry env info` command.

```{code-block} bash
---
caption: command line
---
$ poetry env info
Virtualenv
Python:         3.8.1
Implementation: CPython
Path:           .../virtualenvs/demo-IDGvf4ns-py3.8
Valid:          True

System
Platform: darwin
OS:       posix
Python:   .../.pyenv/versions/3.8.1
```

The `--path` flag will print just the path to the virtual env.

```{code-block} bash
---
caption: command line
---
$ poetry env info --path
.../virtualenvs/demo-IDGvf4ns-py3.8
```

Executable scripts
------------------

The `[tool.poetry.scripts]` section of `pyproject.toml` lets us specify a list
of executables to be generated and installed as part of the package.

It takes the form of:

`<command> = <python object reference>`

Where `<python object reference>` can take the form of:

- `<package>.<module>`
- `<package>.<module>:<function>`
- `<package>.<module>:<object>.<method>`

Imagine we have the file `demo/hello.py`.

```{code-block} python
---
caption: demo/hello.py
---
def main():
    print("hello world")

if __name__ == "__main__":
  main()
```

We can run this command like usual from the command line:

```{code-block} bash
---
caption: command line
---
$ python demo/hello.py
hello world
```

We can use Poetry to create a `hello` executable by adding it to the
`[tool.poetry.scripts]` section.

```{code-block} toml
---
caption: pyproject.toml
---
[tool.poetry]
name = "demo"
# ...

[tool.poetry.scripts]
hello = "demo.hello:main"
```

Poetry will generate a script that is equivalent to:

```{code-block} python
---
caption: generated script equivalent
---
from demo.hello import main
main()
```

After running `poetry install` we can then run the `hello` command from a
poetry shell or using the `poetry run` command.

```{code-block} bash
---
caption: command line
---
$ poetry install
Installing dependencies from lock file

No dependencies to install or update

  - Installing demo (0.1.0)
```

```{code-block} bash
---
caption: command line -- not in a poetry shell
---
$ poetry run hello
hello world
```

```{code-block} bash
---
caption: command line -- from a poetry shell
---
(demo-IDGvf4ns-py3.8) $ hello
hello world
```


```{seealso}
* [The console_scripts Entry Point](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point)
  From the python-packaging tutorial. Documentation on using Setuptools
  `console_scripts` Entry Point, the mechanism underlying
  `[tool.poetry.scripts]`.

* [setup() args > entry_points > console_scripts](https://packaging.python.org/guides/distributing-packages-using-setuptools/#console-scripts)
  From the Python.org user guide on Packaging and distributing projects.
  Documentation on the `entry_points = {'console_scripts': ...` argument to
  `setup()` function the `setup.py` file.

* [Entry points specification](https://packaging.python.org/specifications/entry-points/)
  From the Python.org user guide on Packaging and distributing projects.
  The specification for defining Entry Points.

* [Entry Points](https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html#entry-points)
  From the setuptools docs. Documentation on Entry Points.
```


Installing your package
-----------------------

To install your package in the virtual environment use the `poetry install`
command as described above.

To install your package system-wide use `pip install` from your project root
directory. The `.` argument tells pip to install the package in the current
directory.

```{code-block} bash
---
caption: command line
---
$ pip install .
Processing .../poetry-demo
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
...
Successfully built demo
Installing collected packages: requests, demo
Successfully installed demo-0.1.0 requests-2.25.0
```

To uninstall it, use the `pip uninstall` command with the name of your package.

```{code-block} bash
---
caption: command line
---
$ pip uninstall demo
Found existing installation: demo 0.1.0
Uninstalling demo-0.1.0:
  Would remove:
    ~/.pyenv/versions/3.8.1/bin/hello
    ~/.pyenv/versions/3.8.1/lib/python3.8/site-packages/demo-0.1.0.dist-info/*
    ~/.pyenv/versions/3.8.1/lib/python3.8/site-packages/demo/*
Proceed (y/n)? y
  Successfully uninstalled demo-0.1.0
```

Using Poetry with VS Code
-------------------------

Get the path where Poetry keeps virtual environments by using the `poetry env`
command.

```{code-block} bash
---
caption: command line
---
$ poetry env info -p
```

Copy the path up to the `virualenvs` dir and add it to the `python.venvPath` in
the `settings.json` file. (From the command palette: `Preferences: Open
Settings (JSON)`.)

```{code-block} json
---
caption: VS Code settings.json
---
{
    "python.venvPath": ".../virtualenvs"
}
```

Start VS Code from a terminal in your project root directory with the `poetry
shell` command.

```{code-block} bash
---
caption: command line
---
$ poetry shell
Spawning shell within .../virtualenvs/demo-IDGvf4ns-py3.8
(demo-IDGvf4ns-py3.8) $ code .
```

You may also need to set the `python.pythonPath` in the workspace
`settings.json`. (From the command palette: `Preferences: Open Workspace
Settings (JSON)`.)

```{code-block} json
---
caption: .vscode/settings.json
---
{
    "python.pythonPath": ".../virtualenvs/demo-IDGvf4ns-py3.8/bin/python3.8"
}
```

:::{seealso}
* [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
  VS Code documentation on Python Environments.

* Python projects with Poetry and VSCode [Part 2](https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2/)
  Article covering starting and setting up VSCode when using Poetry.
:::

Reference
---------

### See also

:::{seealso}
* [Poetry docs](https://python-poetry.org/docs)
  Official Poetry documentation.

* [Getting Started with Python Poetry](https://dev.to/bowmanjd/getting-started-with-python-poetry-3ica)
  Article with a friendly Poetry intro, with both Windows and MacOS commands.

* [Developing Python Projects with poetry](https://ron.sh/developing-python-projects-with-poetry/)
  Article with a friendly Poetry intro, including a section on console scripts.

* [Get started with pyenv & poetry](https://blog.jayway.com/2019/12/28/pyenv-poetry-saviours-in-the-python-chaos/)
  Article with a friendly intro to both Poetry and pyenv.

* Python projects with Poetry and VSCode [Part 1](https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-1/)
  Article covering installing Poetry, starting a project and managing dependencies.
:::
