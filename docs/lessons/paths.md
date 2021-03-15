Paths
=====

When you open a file on your computer you may use the Finder or File Explorer
to click through to each folder and eventually find the file you want. When
we want to do the same thing through code we use file paths.

A {term}`path` is a way to represent the location of a file or folder using
text. Not only are they used in pretty much all programming languages, but
paths are also used to on the command line.

Exploring files on the command line
-----------------------------------

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

### Directory separators

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

### The working directory

So far all of these examples have been {term}`relative <relative path>`
meaning that they start from the working directory.

You can explicitly specify the working directory with a `.`.

```{code-block} console
:caption: command line
$ ls ./pythonclass/template.py
./pythonclass/template.py
```

### Parent directory

You can use `..` to indicate the parent directory. For example, I have an
{file}`arduino` directory in the same directory as my working directory
`python-class`. Here's how I would list its contents.

```{code-block} console
:caption: command line
$ ls ../arduino
config  docs  examples  sketchbook  tools
```

### Absolute paths

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

### The home directory

Operating systems designed to support multiple users usually keep each users
files in their own directory not accessible to other users. This is called
the {term}`home directory` and on most operating systems the tilde (`~`) is a
shortcut to the home directory for the current user.

```{code-block} console
:caption: command line
$ ls ~/Documents
Adobe Autodesk
```

### Exercise

```{exercise} command-line-paths
:class: notitles
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

Paths in Python
---------------

### Path strings in `open()`

The first argument to the `open()` function in Python is the path to a file.
So far we've been using a simple filename. In the following example, a file
named {file}`contacts.txt` in the working directory is opened.

```{code-block} python
:caption: python example
fh = open("contacts.txt")
contents = fh.read()
fh.close()
print(fh)
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
print(fh)
```


Reference
---------

### Path examples

| Example                                         | Description                                                 |
|-------------------------------------------------|-------------------------------------------------------------|
| `groceries.txt`                                 | a file in the working directory                             |
| `./groceries.txt`                               | same as above                                               |
| `Documents/groceries.txt`                       | a file in the Documents folder in the working directory     |
| `/Users/pythonclass/Documents/groceries.txt`    | absolute path to the `pythonclass` user's Documents folder  |
| `/home/pythonclass/Documents/groceries.txt`     |                                                             |
| `C:\Documents\groceries.txt`                    |                                                             |
|                                                 |                                                             |

### Special directories

| Directory  | CLI Symbol   |
|------------|--------|
| home       | `~`    |
| working    | `.`    |
| parent     | `..`   |

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
