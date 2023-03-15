Paths
=====

When you open a file on your computer you may use the Finder or File Explorer
to click through to each folder and eventually find the file you want. When
we want to do the same thing through code we use file paths.

A {term}`path` is a way to represent the location of a file or folder using
text. You can think of it like an address; where a street address points to a
physical location in the real world, a path points to a location on a
computer.

Paths are used in pretty much all programming languages as well as on the
command line, which we'll be learning about today.

```{include} ../toc.md
```

Part 1: Exploring files on the command line
-------------------------------------------

For this lesson, open a terminal. We'll use the `ls` command which lists
files to experiment with different paths. (On Windows you may need to use
`dir` instead.) With no arguments it lists the files in the
{term}`working directory` which is the directory (or folder) that you are
currently in.

```{code-block} console
:caption: command line
$ ls
README.md  contacts.py  hello.txt    pyproject.toml  tests  tools
bin        docs         poetry.lock  pythonclass     tmp    vendor
```

The `ls` command takes paths as arguments. When passed, it will list only the
matching files.

:::{tip}

Commands on the command line can take arguments but there are some
differences from Python. Arguments are separated by spaces, no parenthesis or
commas. Single or double quotes are only required if the argument contains
special characters, like a filename with spaces.

:::

The simplest path is just a filename.

```{code-block} console
:caption: command line
$ ls README.md
README.md
```

### Part 1.1: Directory separators

Directories are separated with a slash (`/`) or backslash (`\`) on
Windows. For example here's how I would list the `template.py` file inside
the `pythonclass` directory.

```{code-block} console
:caption: command line
$ ls pythonclass/template.py
pythonclass/template.py
```

On Windows the {term}`directory separator` is a backslash (`\`). A slash
(`/`) might work too, depending on which version of Windows and terminal
you're using. Otherwise the same command would be:

```{code-block} powershell
:caption: command line
> ls pythonclass\template.py
pythonclass\template.py
```

### Part 1.2: The working directory

So far all of these examples have been {term}`relative <relative path>`
meaning that they start from the working directory.

You can explicitly specify the working directory with a `.`.

```{code-block} console
:caption: command line
$ ls ./pythonclass/template.py
./pythonclass/template.py
```

### Part 1.3: Parent directory

You can use `..` to indicate the parent directory. For example, I have an
{file}`arduino` directory in the same directory as my working directory
`python-class`. Here's how I would list its contents.

```{code-block} console
:caption: command line
$ ls ../arduino
config  docs  examples  sketchbook  tools
```

### Part 1.4: Absolute paths

When a path starts with a `/` or the drive (like `C:`) it is an
{term}`absolute <absolute path>` path. That means that it starts at the
computers root directory and contains all of the information to get from
there to the file.

Sometimes it's easier not to start in the working directory, but instead use
the complete file location. This is called the {term}`absolute path` and
starts from the {term}`root directory`, or top-most directory in the file
system, indicated by a single `/`.

So start absolute paths with a slash (`/`).

```{code-block} console
:caption: command line
$ ls /etc/group
/etc/group
```

On Windows you may need to start with the drive letter.

```{code-block} text
:caption: command line
> ls C:\Windows\system32
C:\Windows\system32
```

### Part 1.5: The home directory

Operating systems designed to support multiple users usually keep each users
files in their own directory not accessible to other users. This is called
the {term}`home directory` and on most operating systems the tilde (`~`) is a
shortcut to the home directory for the current user.

```{code-block} console
:caption: command line
$ ls ~/Documents
Adobe Autodesk
```

### Part 1.6: Exercise

```{exercise} command-line-paths
:class: notitle
:label: command-line-paths

On a Unix-like operating system what is the path for each of the following?

1. A file named `blueberry-muffins.md` in a folder named Recipes` in the working directory?
1. An absolute path to the `Music` directory of the `guest` user located under the `Users` directory.
1. A file named `letter.doc` in the parent directory of the working directory.
1. The `Pictures` directory in the home directory of the current user.

```

```{solution} command-line-paths
:class: dropdown

1. `./Recipes/blueberry-muffins.md`
1. `/Users/guest/Music`
1. `../letter.doc`
1. `~/Pictures`

```

Part 2: Paths in Python
-----------------------

### Part 2.1: Path strings in `open()`

The first argument to the `open()` function in Python is the path to a file.
So far we've been using a simple filename. In the following example, a file
named {file}`contacts.txt` in the working directory is opened.

```{code-block} python
:caption: python example
fh = open("contacts.txt")
contents = fh.read()
fh.close()
print(contents)
```

But what if you want to open a file somewhere other than the working
directory? In that case, you can include the path in the argument. In the
following example the {file}`contacts.txt` file is in a {file}`data`
directory in the working directory.

```{code-block} python
:caption: python example
fh = open("data/contacts.txt")
contents = fh.read()
fh.close()
print(contents)
```

### Part 2.2: `Path` objects

Python provides a `pathlib.Path` object which makes it easier to construct
and manipulate cross-platform paths, provides handy methods for filesystem
operations, and can be used in many of the places that string paths are used.

First import the `Path` class from the `pathlib` module. Then call `Path`
with a string path argument. For example, here's how you create a `Path`
object for the `README.md` file.

```{code-block} python
:caption: python example

from pathlib import Path

path = Path("README.md")
```

### Part 2.3: Using `Path` objects in `open()`

You can use a `Path` object instead of a string for the first argument of the
`open()` function.

```{code-block} python
:caption: python example

from pathlib import Path

path = Path("README.md")
fh = open(path)
contents = fh.read()
fh.close()
print(contents)
```

### Part 2.4: Validation methods

`Path` objects provide some handy boolean methods for checking the status of
a file or directory.

* {samp}`{path}.exists()`
* {samp}`{path}.is_file()`
* {samp}`{path}.is_dir()`

The following example checks to be sure that the {file}`README.md` file
exists and that it is a normal file before trying to read it.

```{code-block} python
:caption: python example

from pathlib import Path

def main():
  path = Path("README.md")
  if not path.exists():
    print("Sorry, no file named README.md")
    return

  if not path.is_file():
    print("Unable to read file: README.md")
    return

  fh = open(path)
  contents = fh.read()
  fh.close()
  print(contents)
```

### Part 2.5: Exercise

```{exercise} Validating paths
:class: notitle
:label: validating-paths

Write a function to print the contents of the {file}`contacts.txt` file.
Before reading it, check to make sure the file exists. If it does not, tell
the user the file does not exist and return.

```

`````{solution} validating-paths
:class: dropdown

```python
from pathlib import Path

FILENAME = "data/contacts.txt"

def show():
  """Print all contacts"""
  path = Path(FILENAME)

  if not path.exists():
    print(f"No such file: {FILENAME}")
    return

  with open(path) as fh:
    contents = fh.read()

  print(contents)
```

`````

### Part 2.6: Canonical path

`Path` objects provide methods for handling absolute versus relative paths as
well as converting symbols for the current operating system.

You can use the `.is_absolute()` method to check if a path is an absolute or relative.

```{code-block} python
:caption: Python Shell
>>> path = Path("file.txt")
PosixPath("file.txt")

>>> path.is_absolute()
False
```

You can use the `.absolute()` method to return an absolute version of a path object.

```{code-block} python
:caption: Python Shell
>>> path.absolute()
PosixPath("/home/pythonclass/Documents/file.txt")
```

Note though, `.absolute()` does not change the value of path. It is still relative.

```{code-block} python
:caption: Python Shell
>>> path
PosixPath("file.txt")
```

To make `path` absolute, you'll need to assign it to the `path` variable using the `=` operator.

```{code-block} python
:caption: Python Shell
>>> path = path.absolute()
>>> path
PosixPath("/home/pythonclass/Documents/file.txt")
```

Finally, you can get the normalized path using the `.resolve()` method. This
will convert shortcuts like `..` or `~` to the path and resolve, or follow,
any symbolic links (like shortcuts).

```{code-block} python
:caption: Python Shell
>>> path = Path("../file.txt")
>>> path
PosixPath("../file.txt")

>>> path.resolve()
PosixPath("/home/pythonclass/file.txt")
```

### Part 2.7: Parts of a path

Python `Path` objects make it easy to access parts of a path without
having to worry about which operating system is being used.

| Property   | Type      | Description                                          |
|------------|-----------|------------------------------------------------------|
| `parent`   | `Path`    | Parent directory.                                    |
| `parts`    | `tuple`   | Sequence of directories and filename if any.         |
| `parents`  | `tuple`   | Sequence of parent directories.                      |
| `name`     | `str`     | Filename.                                            |
| `stem`     | `str`     | Filename without extension.                          |
| `suffix`   | `str`     | Filename extension including `.`                     |

The following example prints the filename minus the extension using the
`stem` property above the file contents.

```{code-block} python
:caption: python example

from pathlib import Path

def main():
  path = Path("README.md")

  with open(path) as fh:
    contents = fh.read()

  print(f"*** {path.stem} ***\n")
  print(contents)
```

### Part 2.8: Constructing paths

One way to construct paths in a way that will work on all operating systems
is to use the `joinpath()` method to add a subdirectory or filename to an
existing path.

In the following example the file {file}`~/Documents/groceries.txt` is
printed to the screen.

```{code-block} python
:caption: python example

from pathlib import Path

def main():
  home = Path.home()
  basedir = home.joinpath("Documents")
  path = basedir.joinpath("groceries.txt")

  with open(path) as fh:
    contents = fh.read()

  print(f"*** {path.stem} ***\n")
  print(contents)
```

You can also chain the method calls together like this:

```{code-block} python
:caption: python example

from pathlib import Path

def main():
  path = Path.home().joinpath("Documents").joinpath("groceries.txt")

  with open(path) as fh:
    contents = fh.read()

  print(f"*** {path.stem} ***\n")
  print(contents)
```

Finally, you can use the `/` operator on `Path` objects as a shorthand for the `joinpath()` method.

```{code-block} python
:caption: python example

from pathlib import Path

def main():
  path = Path.home() / "Documents" / "groceries.txt"

  with open(path) as fh:
    contents = fh.read()

  print(f"*** {path.stem} ***\n")
  print(contents)
```

### Part 2.9: Paths relative to current file

The working directory in Python is the directory the current program was
launched from. This can make using relative paths problematic because if the
user runs the program from a different directory, the location of any
relative paths will change.

Instead you may want to make a path relative to the file that is being run.

Python provides a special variable `__file__` that contains a string with the
path of the current file. When used to create a `Path` object, you can use
the `parent` property to get the directory the file is in.

The following example opens the file {file}`.vscode/launch.json` in the same
directory as the current file.

```{code-block} python
:caption: python example

from pathlib import Path

def main():
  basedir = Path(__file__).parent / ".vscode" / "launch.json"

  with open(path) as fh:
    contents = fh.read()

  print(contents)
```

### Part 2.10: Exercise

```{exercise} Constructing paths
:class: notitle
:label: constructing-paths-exercise

Write a function to print the contents of a different Python script in your project.

```

`````{solution} constructing-paths-exercise
:class: dropdown

```python
from pathlib import Path

def print_script():
  path = Path(__file__).parent / "pythonclass" / "template.py"

  with open(path) as fp:
    contents = fp.read()

  print(f"{path.name}\n")
  print(contents)
```

`````

Reference
---------

### Special directories

| Directory  | CLI   | Python                |
|------------|-------|-----------------------|
| home       | `~`   | `Path.home()`         |
| working    | `.`   | `Path.cwd()`          |
| parent     | `..`  | {samp}`{path}.parent` |

### Path examples

| Example                                         | Description                                                    |
|-------------------------------------------------|----------------------------------------------------------------|
| `groceries.txt`                                 | a file in the working directory                                |
| `./groceries.txt`                               | same as above                                                  |
| `Documents/groceries.txt`                       | a file in the Documents folder in the working directory        |
| `/Users/pythonclass/Documents/`                 | MacOS path to the `pythonclass` user's Documents folder        |
| `/home/pythonclass/Documents/`                  | Unix path to the `pythonclass` user's Documents folder         |
| `C:\Documents\`                                 | Windows path to the `pythonclass` user's Documents folder      |

### Glossary

```{glossary} paths

absolute path
  A complete path starting from the {term}`root directory`.

directory separator
  The symbol used to separate directories in a {term}`path`, either a slash
  `/` or a backslash (`\`) on Windows.

home directory
  On operating systems that support multiple users, the directory created
  for and with access restricted to a given user which is intended to
  contain all of the users files.

  On the command line in most systems the shorthand is the tilde character
  (`~`). It is usually stored in the environment variable `$HOME` or on
  Windows `%USERPROFILE%` or `%HOMEDRIVE%%HOMEPATH%`.

path
  A text representation of a file location.

relative path
  A path starting from the {term}`working directory`.

root directory
  The top-most directory in the file system.

working directory
current working directory
CWD
  On the command line, the current directory. In a Python script or shell,
  the directory that the shell or script was started from.

```

### See also

:::{seealso}

* [LinuxCommand.org > Navigation](https://linuxcommand.org/lc3_lts0020.php)
* [LinuxCommand.org > Looking Around](https://linuxcommand.org/lc3_lts0030.php)

:::
