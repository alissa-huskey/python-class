File System Operations
======================

This lesson will go over how to use `Path` objects to preform common
operations on files and directories.

This part of the lesson is about the ways to get a list of files on your
local computer.

Listing files
-------------

### Directory contents

`Path` objects provide an `iterdir()` method for iterating through the
contents of a directory. Here's a simple example that prints contents of the
working directory.

```{code-block} python
:linenos:
from pathlib import Path

cwd = Path.cwd()
for f in cwd.iterdir():
    print(f)
```

Each of the elements yielded by `iterdir()` is a `Path` object, so we have
access to all of its methods and properties. For example, the following code
iterates through the contents of the working directory and uses
{samp}`{path}.name` and {samp}`{path}.is_dir()` to print just the directory
names.

```{code-block} python
:linenos:
from pathlib import Path

cwd = Path.cwd()

for f in cwd.iterdir():
    if f.is_dir():
        print(f.name)
```

Here's another example that iterates through the contents of the working
directory and prints any files with `"recipe"` in the name that are either
text or markdown.

```{code-block} python
:linenos:
from pathlib import Path

cwd = Path.cwd()

for f in cwd.iterdir():
    if f.suffix in (".md", ".txt") and "recipe" in f.name:
        print(f.name)
```

```{exercise} Print the contents of the working directory.
:label: print-working-dir

Iterate over the contents of the working directory and:

* skip over files or directories with names that begin with `.` or `__`
* print the name of any directories followed by a `/`
* print the name of everything else

```

`````{solution} print-working-dir
:class: dropdown

```{code-block} python
from pathlib import Path

cwd = Path.cwd()

for f in cwd.iterdir():
     if f.name.startswith(".") or f.name.startswith("__"):
         continue
     if f.is_dir():
         print(f"{f.name}/")
     else:
         print(f.name)
```
`````

### Searching files

`Path` objects provides a `glob()` method for simple, albeit limited, file
searching. The `glob()` method uses a set of wildcard characters adopted from
the command line called {term}`glob patterns`, the most common of which is
`*` meaning "any or no text".

The following example uses the glob pattern `*.py` to search for any files
ending in `.py`.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("data")
for f in path.glob("*.py"):
    print(f.name)
```

The `rglob()` method works the same way, but {term}`recursively <recursive>`
includes the contents of all subdirectories in the search.

```{code-block} python
:linenos:
from pathlib import Path

path = Path.cwd()
for f in path.rglob("*.py"):
    print(f)
```

```{exercise} Search for files
:label: list-text-files-exercise

Print the names of all files in your working directory or recursively in any
subdirectories that end with `*.txt`.

```

`````{solution} list-text-files-exercise
:class: dropdown

```{code-block} python
:linenos:
from pathlib import Path

cwd = Path.cwd()
for f in cwd.rglob("*.txt"):
    print(f.name)
```

`````

```{seealso}

* [Wikipedia > Glob](https://en.wikipedia.org/wiki/Glob_%28programming%29)
* You can find a details on globbing in Python in the [reference section of this lesson](file-system-operations.html#globbing).

```

Directory operations
--------------------

### Creating directories

You can use the `mkdir()` method on a `Path` object to create a new
directory.

First you'll need to create a `Path` object to the directory, then you can
call `mkdir()` on that object.

The following example creates a `tmp` directory.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("tmp")
path.mkdir()
```

The `mkdir()` method will raise an error if the directory already exists, so
you could check the results of the `exists()` and `is_dir()` before calling
it. But there's an easier way. Just pass the the optional `exist_ok` keyword
argument, as in the following example.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("tmp")
path.mkdir(exist_ok=True)
```

```{exercise} Create a directory
:label: create-a-directory-exercise

Create a `tmp` directory in your `data` directory. If you don't have a `data`
directory, create it first.

```

`````{solution} create-a-directory-exercise
:class: dropdown

```{code-block} python
:linenos:

from pathlib import Path
tmp = Path.cwd() / "data" / "tmp"
tmp.mkdir(exist_ok=True)
```

`````

### Deleting directories

To delete an empty directory use the `rmdir()` method on a `Path` object.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("tmp")
path.rmdir()
```

```{note}
The `rmdir()` method only works on empty directories, so you'll need to
delete any directory contents first. We'll learn how to delete files later in
this lesson.
```

```{exercise} Delete the tmp directory
:label: delete-the-tmp-directory-exercise

Delete the `data/tmp` directory that you created earlier.

```

`````{solution} delete-the-tmp-directory-exercise
:class: dropdown

```{code-block} python
from pathlib import Path
path = Path("data/tmp")
path.rmdir()
```

`````

File operations
---------------

### Creating empty files

The command line command {command}`touch` will either update a file's
timestamp of the last time it was accessed and modified, or create an empty
file if it does not exist. This makes it an easy way to generate files
without worrying if they already exist.

`Path` objects provide a `touch()` method that does the same thing, as shown below.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("tmp.py")
path.touch()
```

```{exercise} Generate files
:label: generate-files-exercise

1. Create the `data/tmp` directory if it does not already exist.
2. Use the `touch()` method to create files `file_1.txt` though `file_9.txt`.

```

`````{solution} generate-files-exercise
:class: dropdown

```{code-block} python
tmpdir = Path.cwd() / "data" / "tmp"
tmpdir.mkdir(exist_ok=True)

for i in range(1, 10):
    path = tmpdir / f"file_{i}.txt"
    path.touch()
```

`````

### Removing files

To remove files use the `unlink()` method on a `Path` object as shown below.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("data/things/a.txt")
path.unlink()
```

The `unlink()` method will throw an error if the file does not exist. You can
avoid this by passing the optional `missing_ok` argument like so.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("data/things/a.txt")
path.unlink(missing_ok=True)
```

```{exercise} Remove a file
:label: remove-a-file-exercise

1. Choose one of your generated files to delete.
2. Ask the user to confirm they want to delete the file.
3. Use `unlink()` to delete the file.

```

`````{solution} remove-a-file-exercise
:class: dropdown

```{code-block} python
from pathlib import Path
tmpdir = Path.cwd() / "data" / "tmp"
filepath = tmpdir / "file_9.txt"

reply = input(f"Delete the file {filepath}? [yN] ")
if reply in ("y", "yes"):
    filepath.unlink(missing_ok=True)
```

`````

### Moving and renaming files

`Path` objects provide a `replace()` method which moves or renames the the
file to the location given in the target argument and returns a new `Path`
object that points to the new location.

In the example below the file {file}`a.txt` is moved to the {file}`data`
directory.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("a.txt")
path = path.replace("data/a.txt")

print("File moved to: {path}")
```

The `replace()` method can take either a string or a `Path` object. The
example below uses a `Path` object.

If the target file location already exists the `replace()` method will
silently overwrite it. So it's important to check that there isn't already
something at the target location before calling `replace()`.

Luckily `replace()` will accept either a string or a `Path` object, so we can
use that to check if it `exists()`.

```{code-block} python
:linenos:
from pathlib import Path

def main():
    path = Path("a.txt")
    target = Path("data") / "a.txt"

    if target.exists():
        print(f"Cannot move to {target} as it already exists.")
        return

    path = path.replace(target)

    print("File moved to: {path}")

main()
```

```{important}
The `replace()` method is relative to whatever the `path` object it was
called on is. That means that if you just rename a relative `data/tmp/a.txt`
to `b.txt` it will be moved to your working directory. Worse if your original
`Path` object was absolute, it will be relative to the root directory.

So it's a good idea to use a `Path` object joined to a known correct parent
directory for the target argument.
```

```{exercise} Rename file
:label: rename-file-exercise

1. Rename the {file}`file_1.txt` that you created earlier to
   {file}`file_01.txt`.
2. Be sure to check first that the target does not already exist.
2. Print the files new name.

```

`````{solution} rename-file-exercise
:class: dropdown

```{code-block} python
from pathlib import Path

TMPDIR = Path("data/tmp")

def main():

    path = TMPDIR / "file_1.txt"
    target = TMPDIR / "file_01.txt"

    if target.exists():
        print(f"Cannot move to {target} as it already exists.")
        return

    path = path.replace(target)
    print(f"Renamed file: {path}")

main()
```

`````

```{exercise} Zero pad filenames
:label: zeropad-filenames-exercise

Sometimes when files are sorted numbers get grouped together so that
`file_1.txt` and `file_11.txt` are before `file_2.txt`. So this exercise is
to add zeros in front of all of the single digit file numbers.

1. Use the `glob()` method to find all of the `file_*.txt` files that you
   created earlier.
2. Check the length of the filename to skip files that are named
   {samp}`file_{xx}.txt`.
3. For any files named {samp}`file_{x}.txt`, use a slice to get the number
   part of the file.
4. Check that the zero-padded version of the file {samp}`file_{xx}.txt` does
   not already exist, otherwise print an error message and skip that file.
5. Rename the file to the zero-padded version.
6. Print the new filename.

```

`````{solution} zeropad-filenames-exercise
:class: dropdown

```{code-block} python
from pathlib import Path

TMPDIR = Path("data/tmp")

for f in TMPDIR.glob("file_*.txt"):
    if len(f.name) > 10:
        print(f"{f.name}               ... SKIPPING: too long")
        continue

    num = f.name[5:6]
    if not num.isnumeric():
        print(f"{f.name}                ... SKIPPING: {num} is not numeric")
        continue

    target = TMPDIR / f"file_0{num}.txt"
    if target.exists():
        print(f"{f.name} -> {target.name} ... ERROR: {target.name} exists")
        continue

    f.replace(target)
    print(f"{f.name} -> {target.name} ... DONE")
```

`````

Reference
---------

### Glossary

```{glossary} something

glob
globbing
glob patterns
filename expansion
    On the command line: A feature available on many command line shells
    where when some characters are not in quotes, they are interpreted as
    filename matching wildcards. For example the command `ls *.txt` will
    first find all files ending with `.txt` in the working directory and send
    them as arguments to {command}`ls`.

    In programming: Some variant of the syntax and behavior of glob patterns
    from the command line have been adopted in many other programs and
    languages when listing files. Some examples include Pythons
    `pathlib.Path.glob` and `glob.glob` and the syntax used in
    {file}`.gitignore` files.


recursive
recursion
    When something uses itself to define itself. Some examples include:
    * [fractals](https://en.wikipedia.org/wiki/Fractal)
    * [infinity mirrors](https://en.wikipedia.org/wiki/Infinity_mirror)
    * the [google search suggestions for recursion](https://www.google.com/search?newwindow=1&q=recursion)

    In programming this happens when a function calls itself, for example to
    traverse a nested data structure or in algorithms to generate the
     [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number#Computer_science).

    When dealing with a file system the term recursive is generally used as
    shorthand to mean, "include the contents of every subdirectory
    recursively", so that the entire file tree is traversed.

```

### Globbing

#### Wildcards

| Symbol           | Matches                                    | Times           |
|------------------|--------------------------------------------|-----------------|
| `**`             | any directory, recursively                 | zero or more    |
| `*`              | any character                              | zero or more    |
| `?`              | any character                              | exactly once    |
| {samp}`[{seq}]`  | any character in {samp}`{seq}`             | exactly once    |
| {samp}`[!{seq}]` | any character not in {samp}`{seq}`         | exactly once    |

#### Character ranges

| Range | Meaning          |
|-------|------------------|
| `a-z` | lowercase letter |
| `A-Z` | uppercase letter |
| `0-9` | number           |

#### Examples

| Pattern            | Matches where the name                           | Located in                                |
|------------------  |--------------------------------------------------|-------------------------------------------|
| `*`                | is anything                                      | this directory                            |
| `*.md`             | ends in `.md`                                    | this directory                            |
| `*circle*.svg`     | includes `circle` and ends in `.svg`             | this directory                            |
| `*[0-9]*`          | includes a number                                | this directory                            |
| `[A-Z]*`           | starts with a uppercase letter                   | this directory                            |
| `file_??.txt`      | is `file_`, then any two characters, then `.txt` | this directory                            |
| `20[0-2][0-9]`     | is `20` followed by `00` through `29`            | this directory                            |
| `*[0-9][0-9].txt`  | ends with two numbers followed by `.txt`         | this directory                            |
| `*[!0-9][0-9].txt` | ends with a non-number, a number, then `.txt`    | this directory                            |
| `[_.0-9]*`         | starts with `_`, `.` or a number                 | this directory                            |
| `*-[hv].svg`       | ends in `-h.svg` or `-v.svg`                     | this directory                            |
| `docs/*`           | is anything                                      | the `docs` child directory                |
| `**/*.doc`         | ends in `.doc`                                   | this directory or any child, recursively  |
| `*/*.jpg`          | ends in `.jpg`                                   | any child directory                       |
| `**/.gitignore`    | is `.gitignore`                                  | this directory or any child, recursively  |
