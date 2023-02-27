---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

File System Operations
======================

This lesson will go over how to use `Path` objects to preform common
operations on files and directories.

This part of the lesson is about the ways to get a list of files on your
local computer.

```{include} ../toc.md
```

Part 1: Listing files
---------------------

### Part 1.2: Directory contents

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

### Part 1.3: Searching files

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

Part 2: Directory operations
----------------------------

### Part 2.1: Creating directories

You can use the `mkdir()` method on a `Path` object to create a new
directory.

First you'll need to create a `Path` object to the directory, then you can
call `mkdir()` on that object.

The following example creates a `tmp` directory.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("tmp")
print(f"Creating directory: {path}")
path.mkdir()
```

The `mkdir()` method will raise an error if the directory already exists, so
you could check the results of the `exists()` and `is_dir()` before calling
it. But there's an easier way. Just pass the optional `exist_ok` keyword
argument, as in the following example.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("tmp")
print(f"Creating directory: {path}")
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
tmp = Path("data") / "tmp"
print(f"Creating directory: '{tmp}'")
tmp.mkdir(exist_ok=True)
```

`````

### Part 2.2: Deleting directories

To delete an empty directory use the `rmdir()` method on a `Path` object.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("tmp")
print(f"Removing directory: '{path}'")
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
print(f"Removing directory: {path}")
path.rmdir()
```

`````

Part 3: File operations
-----------------------

### Part 3.1: Creating empty files

The command line command {command}`touch` will either update a file's
timestamp of the last time it was accessed and modified, or create an empty
file if it does not exist. This makes it an easy way to generate files
without worrying if they already exist.

`Path` objects provide a `touch()` method that does the same thing, as shown below.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("tmp.py")
print(f"Touching file: {path}")
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
tmpdir = Path("data") / "tmp"
tmpdir.mkdir(exist_ok=True)

for i in range(1, 10):
    path = tmpdir / f"file_{i}.txt"
    print(f"Touching file: '{path}'")
    path.touch()
```

`````

### Part 3.2: Removing files

To remove files use the `unlink()` method on a `Path` object. Since this
deletes a file, it's a good to print the path and confirm with the user that
they really want to.

```{code-block} python
:linenos:
:caption: "note: assumes `data/a.txt` exists"
from pathlib import Path

path = Path("data/a.txt")
reply = input(f"Remove file: '{path}'? [y/N] ")
if reply not in ("y", "yes"):
    print("Ok, nevermind then.")
else:
    print("Ok, removing.")
    path.unlink()
```

The `unlink()` method will throw an error if the file does not exist. You can
avoid this by passing the optional `missing_ok` argument like so.

```{code-block} python
:linenos:
from pathlib import Path

path = Path("file-that-doesnt-exist.txt")
path.unlink(missing_ok=True)
```

```{exercise} Remove a file
:label: remove-a-file-exercise

1. Choose one of your generated {samp}`file_{num}.txt` files to delete.
2. Ask the user to confirm they want to delete the file.
3. Use `unlink()` to delete the file.

```

`````{solution} remove-a-file-exercise
:class: dropdown

```{code-block} python
from pathlib import Path
filepath = Path("data") / "tmp" / "file_9.txt"

print(f"Delete the file '{filepath}'?")
reply = input(f"[yN] > ")

if reply in ("y", "yes"):
  filepath.unlink(missing_ok=True)
  print("All done.")
else:
  print("Well, nevermind then.")
```

`````

### Part 3.3: Moving files

`Path` objects provide a `replace()` method which can be used to move files. It
takes a destination path argument which can be either a string or `Path` object
and returns a destination `Path` object.

In the example below the file {file}`a.txt` is moved to the {file}`data`
directory.

```{code-block} python
:linenos:
:caption: "note: assumes `a.txt` exists"
from pathlib import Path

old_path = Path("a.txt")
new_path = old_path.replace("data/a.txt")

print(f"File moved from '{old_path}' to '{new_path}'")
```

If the destination file location already exists the `replace()` method will
silently overwrite it. So it's a good idea to check that there isn't already a
file at the destination.

In the example below a destination `Path` object is created first to check if
it `.exists()`. Then if all is well it is passed to `.replace()`.

```{code-block} python
:linenos:
from pathlib import Path

from_path = Path("a.txt")
to_path = Path("data") / "a.txt"

if to_path.exists():
    print(f"Error: '{to_path}' already exists.")
else:
  from_path.replace(to_path)
  print(f"File moved from '{from_path}' to '{to_path}'")
```

```{exercise} Move file
:label: move-file-exercise

1. Use `.touch()` to make an empty file `xxx.txt`
2. Make a new `Path` object to {file}`data/xxx.txt`
3. Check to make sure `data/xxx.txt` does not exist, and print an error if it does.
4. Print a message {samp}`"Moving '{from}' to '{to}'."`
5. Use `.replace()` to move the file.

```

`````{solution} move-file-exercise
:class: dropdown

```{code-block} python
from pathlib import Path

from_path = Path("xxx.txt")
to_path = Path("data") / "xxx.txt"

from_path.touch()

if to_path.exists():
    print(f"Cannot move to {to_path} as it already exists.")
else:
    print(f"Moving '{from_path}' to '{to_path}'")
    from_path.replace(to_path)
```

`````

```{exercise} Move text files to data directory
:label: move-text-files-exercise

0. If you have no files ending in `.txt` in your working directory, use
   `.touch()` to generate some first.
1. Iterate over text files in your working directory ending in `.txt`
    * [ ] Use a for-loop and `iterdir()` or `glob()` to iterate over the files
    * [ ] If using `iterdir()`, use an if statement to `continue` if the file does
          not end in `.txt`
2. Check if a file with the same name already exists in `data/`
    * [ ] Create a  destination path object
    * [ ] If a file already `.exists()` print an error message and `continue`
3. Move the file
    * [ ] Confirm that the user wants to move the file.
    * [ ] Use .replace() to move the file
    * [ ] Print a confirmation message with the old and new path.
4. Bonus: Instead of skipping files that already exist in `data/`, move the
          file to {samp}`data/{file}-{num}.txt`

```

`````{solution} move-text-files-exercise
:class: dropdown

```{code-block} python
:caption: "version 1: skip files that exist"
from pathlib import Path

for from_path in Path.cwd().iterdir():
  to_path = Path("data") / from_path.name

  if from_path.suffix.lower() != ".txt":
    continue

  if to_path.exists():
      print(f"Skipping: {from_path.name}")
      continue

  print(f"Move '{from_path.name}' to 'data/{to_path.name}'?")
  reply = input("[yN] >")

  if reply.lower() not in ("y", "yes"):
      print(f"Declined: {from_path.name}")
      continue

  from_path.replace(to_path)
  print(f"Moved '{from_path.name}' to '{to_path}'")
```

```{code-block} python
:caption: "version 2: make numbered versions if file exists"
from pathlib import Path

for from_path in Path.cwd().iterdir():
  to_path = Path("data") / from_path.name

  if from_path.suffix.lower() != ".txt":
    continue

  version = 1
  while to_path.exists():
    to_path = Path("data") / f"{from_path.stem}-{version}{from_path.suffix}"
    version += 1

  print(f"Move '{from_path.name}' to 'data/{to_path.name}'?")
  reply = input("[yN] >")

  if reply.lower() not in ("y", "yes"):
      print(f"Declined: {from_path.name}")
      continue

  from_path.replace(to_path)
  print(f"Moved '{from_path.name}' to '{to_path}'")
```

`````

### Part 3.4: Renaming files

Renaming files is the same as moving files except instead of moving to a new
directory, you are moving to the same directory but with a new name. Just like
moving files, use the `.replace()` method, passing the string or path object to
the destination location.


```{code-block} python
:linenos:
:caption: "note: assumes `data/a.txt` exists"
from pathlib import Path

from_path = Path("data") / "a.txt"
to_path = Path("data") / "file_a.txt"

if to_path.exists():
    print(f"Cannot rename '{from_path}' to '{to_path}' as it already exists.")
else:
    from_path.replace(to_path)
    print(f"Renamed to: '{to_path.name}'")
```

The {samp}`{path}.replace()` method is relative to your working directory, just
like when you create a new `Path` object. If you pass `.replace()` _only_ the
the new filename, the file will end up being moved to your working directory.
It's is an easy mistake to make.

:::{highlights}

To rename a file, the string or path object sent to `.replace()` must have
the same directory information as the original path object.

:::

It's a good idea to create a `Path` object to the shared directory that can
then be used for both path objects.

<div class="row"><div class="col">

```{rubric} Bad
```

```{code-block}
:caption: "_Bad_: moves file to ./file_a.txt"
from pathlib import Path

from_path = Path("data") / "a.txt"
to_path = from_path.replace("file_a.txt")
```

</div><div class="col">

```{rubric} Better
```

```{code-block}
:caption: "_Better_: renames file to ./data/file_a.txt"
from pathlib import Path

from_path = Path("data") / "a.txt"
to_path = from_path.replace("data/file_a.txt")
```

</div></div>

```{rubric} Best
```

```{code-block}
:caption: "_Best_: Avoid mistakes with a `folder` variable"
from pathlib import Path

folder = Path("data")
from_path = folder / "a.txt"
to_path = folder / "file_a.txt"

from_path.replace(to_path)
```

```{exercise} Rename file
:label: rename-file-exercise

1. Rename the {file}`file_1.txt` that you created earlier to
   {file}`file_01.txt`.
2. Be sure to check first that the destination does not already exist.
2. Print the files new name.

```

`````{solution} rename-file-exercise
:class: dropdown

```{code-block} python
from pathlib import Path

tmpdir = Path("data/tmp")
from_path = tmpdir / "file_1.txt"
to_path = tmpdir / "file_01.txt"

if to_path.exists():
    print(f"Cannot move to {to_path} as it already exists.")
else:
  from_path.replace(to_path)
  print(f"Renamed file: {to_path.name}")
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

for from_path in TMPDIR.glob("file_*.txt"):
    if len(from_path.name) > 10:
        print(f"{from_path.name}               ... SKIPPING: too long")
        continue

    num = from_path.name[5:6]
    if not num.isnumeric():
        print(f"{from_path.name}                ... SKIPPING: {num} is not numeric")
        continue

    to_path = TMPDIR / f"file_0{num}.txt"
    if to_path.exists():
        print(f"{from_path.name} -> {to_path.name} ... ERROR: {to_path.name} exists")
        continue

    from_path.replace(to_path)
    print(f"{from_path.name} -> {to_path.name} ... DONE")
```

`````

Reference
---------

### Glossary

```{glossary} file-system-operations

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
