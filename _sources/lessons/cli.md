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
CLI
===

In this class we've been writing {abbr}`CLI (command line interface)`
programs, as opposed to a {abbr}`GUI (graphical user interface)`. While most
of the programs an average person interacts with on a day-to-day basis
are most likely GUIs, text-based programs have their advantages.

They can often be faster, as they take up fewer resources needing to load and
render graphics. The interface can be more precise and less error prone to
interact with, as typed commands are less ambiguous than clicking on regions.
And they can be powerful, making it possible to accomplish a lot by stringing
together just a few commands. Plus, they're a lot easier to write.

In this lesson we'll learn about writing programs intended to be run in a
command line environment.

```{contents} Table of Contents
:backlinks: top
:local:
```

Arguments
---------

Just like functions can take arguments, so can programs. This is done on the
command line, typically seperated by spaces, with multi-word arguments
surrounded by single or double quotes.

In Python, those arguments can be accessed at `sys.argv` which stores a list of
strings.  The first list item is the name of the program being executed
followed by one argument per list item.

Note all arguments are stored as strings, so as in the following example, type
conversion is often necessary.

```{code-block} python
:caption: "example: program.py"
:class: full-width
:linenos:

import sys
print(sys.argv)
```

```{code-block} console
:caption: command line
:class: full-width
$ python program.py arg1 arg2 arg3
['cli.py', 'arg1', 'arg2', 'arg3']

$ python program.py "multi-word argument 1" arg2
['cli.py', 'multi-word argument 1', 'arg2']
```

This can be used to control program behavior, in major or minor ways. Here for
example is a simple program {file}`randnums.py` which prints `3` random numbers
by default, or the number specified by the first argument if one exists.

```{code-block} python
:caption: "example: randnums.py"
:class: full-width
:linenos:

import sys
import random

count = 3

if len(sys.argv) >= 2:
  count = int(sys.argv[1])

for _ in range(count):
  print(random.randint(0, 100))
```

```{code-block} console
:caption: command line
:class: full-width

$ python randnums.py
50
62
76

$ python randnums.py 2
15
46
```

### Exercise

`````{exercise} Countdown With Args Exercise
:label: argv-exercise

Write a program which counts down from `3` by default, or from the number
passed by the first argument if present. Use `time.sleep()` to pause for a
second between printing each number.

```{dropdown} Need help?
1. Import the `sys` and `time` modules.
2. Assign the value `3` to the `count` variable.
3. If there are at least `2` values in the `sys.argv` list, set count to be the
   second item in the list, converted to an `int`.
4. Use a `for` loop with a variable name of `num` to iterate over a `range`
   with a `start` value of `count`, a `stop` value of `0`, and a `step` value
   of `-1.`

   *Hint: Use `help(range)` for more information on `range` objects.*

   - Print `num` followed by `...`
   - Call `time.sleep()` with an argument of `1`
```

**Example output**:

```{code-block} console
$ python countdown.py
3...
2...
1...

$ python countdown.py 5
5...
4...
3...
2...
1...
```

`````

`````{solution} argv-exercise
:class: dropdown

```{literalinclude} ../../pythonclass/exercises/countdown.py
:caption: Countdown With Args Exercise
:class: full-width
:linenos:
```

```{code-block} console
$ python countdown.py
3...
2...
1...

$ python countdown.py 5
5...
4...
3...
2...
1...
```

`````

Environment Variables
---------------------

Just like we can set variables in our programs, we can also set variables on
the command line. There are known as {term}`environment variables`, and they
are typically stored as all caps. For example, most systems set the variables
`SHELL`, `TERM`, `HOME` and `TMPDIR`.

To reference a variable on the command line, prefix it with a `$`.

```{code-block} console
:caption: command line
:class: full-width
$ echo $SHELL
/bin/zsh

$ echo $TERM
xterm-256color

$ echo $HOME
/Users/pythonclass

$ echo $TMPDIR
/var/folders/mn/qt2cdhdn5md6hrwjrz5sp60m0000gn/T/
```

To set an environment variable, use the `typeset` or `export` command as in the
following example. (Note: The variable only exists only for the duration of
your current terminal sesson.)

```{code-block} console
:caption: command line
:class: full-width
$ typeset -gx LANGUAGE=en
$ export LANGUAGE=en
```

In Python, we can access this using the `os.environ` dictionary.

```{code-cell} python
:class: full-width

import os
print(os.environ["TERM"])
```

If you're not sure if the environment variable exists, use the `.get()` method,
with an optional second argument that will be the value returned if it is
missing.

```{code-cell} python
:class: full-width

import os
lang = os.environ.get("LANGUAGE", "en")
print(lang)
```

### Exercise

`````{exercise} Environment Variables Exercise
:label: envvar-exercise

Modify your countdown program to check the environment variable `VERBOSE` and the message
{samp}`"Counting down from {COUNT}."` if it is set to a non-blank value.

Test it with the envionment variable not set, set to `""`, and set to a value like `"yes"`.
`````

`````{solution} envvar-exercise
:class: dropdown

```{code-block} python
:caption: Environment Variables Exercise
:class: full-width
:linenos:
:emphasize-lines: "4, 9-12"

"""Countdown exercise for the CLI Lesson
   https://alissa-huskey.github.io/python-class/lessons/cli.html
"""
import os
import sys
import time

count = 3
is_verbose = os.environ.get("VERBOSE", False)

if is_verbose:
  print(f"Counting down from {count}.")

if len(sys.argv) > 2:
  print(f"Warning: extra arguments: {sys.argv[2:]}", file=sys.stderr)

if len(sys.argv) >= 2:
  count = int(sys.argv[1])

for num in range(count, 0, -1):
    print(f"{num}...")
    time.sleep(1)
```

```{code-block} console
:caption: command line
:class: full-width
$ python countdown.py
3...
2...
1...

$ export VERBOSE=""
$ python countdown.py
3...
2...
1...

$ export VERBOSE=yes
$ python countdown.py
Counting down from 3.
3...
2...
1...
```
`````

Input and Output
----------------

In a command line environment, input and output are handled via three special
kinds of files called that serve as data streams: {term}`stdin`, {term}`stdout`
and {term}`stderr`. Each one has an associated {abbr}`FD (file descriptor)`
number, which we'll learn more about later.

| Descriptor     | Name            | FD  | Source / Destination      |
|----------------|-----------------|-----|---------------------------|
| {term}`stdin`  | standard input  | `0` | from the keyboard         |
| {term}`stdout` | standard output | `1` | to the screen             |
| {term}`stderr` | standard error  | `2` | to the screen             |

In Python, these can be accessed in the `sys` module.

When you use the `print()` function, for example it prints to `stdout` by
default. This is the same as:

```{code-cell} python
import sys
print("hello", file=sys.stdout)
```

As I mentioned, these are all special kinds of files, and in Python they are
represented as {term}`file handler` objects. As such, you can interact with
them the same way you would with a normal file object. So yet another way to
accomplish the same thing is:

```{code-cell} python
import sys
sys.stdout.write("hello\n")
```

The most common use of file handlers is to write to `stderr` instead of `stdout`.

```{code-cell} python
import sys
print("Danger, Will Robinson!", file=sys.stderr)
```

This is useful because on those streams can be handled seperately on the
command line. While a complete lesson on {term}`redirection` is outside of the
scope of this lesson, the most common use case is to send a particular stream
to a different destination with the syntax: {samp}`{COMMAND} {FD}> {DESTINATION}`.

The following for example sends the results of the `ls` command to the file
`files.txt`. (The file descriptor defaults to `stdout`.)

```{code-block} console
:caption: command ine
:class: full-width
$ ls > files.txt
```

Or we could send all error messages to `errors.log` or to `/dev/null` (on most
systems) to silence them completely. Here we use the file descriptor number `2`
immediately before the `>` to indicate that we want to redirect `stderr`
instead of `stdout`.

```{code-block} console
:caption: command ine
:class: full-width
$ ls 2> errors.log
file1 file2 file3

$ ls 2> /dev/null
file1 file2 file3
```

Take the following example, which prints some messages to `stderr` and others
to `stdout`.

```{code-block} python
:caption: using-stderr.py
:class: full-width
:linenos:

import sys
print("Welcome!")
print("Danger, Will Robinson!", file=sys.stderr)
print("Farewell.")
```

If we redirect `stdout` to the file `messages.txt` the faux error message will
be printed to the screen and excluded from the `messages.txt` file.

```{code-block} console
:caption: command ine
:class: full-width
$ python using-stderr.py > messages.txt
Danger, Will Robinson!

$ cat messages.txt
Welcome!
Farewell.
```

### Exercise

`````{exercise} Stderr Exercise
:label: stderr-exercise

Modify your countdown function to print a message to `stderr` if there is more
than one argument passed.

Test this on the command line with more than one argument by:
* redirecting stdout to `countdown.txt`
* redirecting stderr to `errors.log`
* redirecting stderr to `/dev/null`

`````

`````{solution} stderr-exercise
:class: dropdown

```{code-block} python
:caption: Stderr Exercise
:class: full-width
:linenos:
:emphasize-lines: "14-15"
"""Countdown exercise for the CLI Lesson
   https://alissa-huskey.github.io/python-class/lessons/cli.html
"""
import os
import sys
import time

count = 3
is_verbose = os.environ.get("VERBOSE", False)

if is_verbose:
  print(f"Counting down from {count}.")

if len(sys.argv) > 2:
  print(f"Warning: extra arguments: {sys.argv[2:]}", file=sys.stderr)

if len(sys.argv) >= 2:
  count = int(sys.argv[1])

for num in range(count, 0, -1):
    print(f"{num}...")
    time.sleep(1)
```

```{code-block} console
:caption: command line
:class: full-width
$ python countdown.py 1
1...

$ python countdown.py 1 2
Warning: extra arguments: ['2']
1...

$ python countdown.py 1 2 > countdown.txt
Warning: extra arguments: ['2']

$ python countdown.py 1 2 2> errors.log
1...

$ python countdown.py 1 2 2> /dev/null
1...
```

`````

Exiting Programs
----------------

When a command line programs ends, it returns an {term}`exit code` to indicate
success or failure. Traditionally an exit code of `0` indicates success and
anything else indicates some kind of failure. Some programs use different exit
codes to let you know why the program failed.

You can see the exit code of the last command with the special variable `$?`.
Lets use the `ls` command as an example.

```{code-block} console
:caption: command line
:class: full-width
$ ls
file1 file2 file3

$ echo $?
0

$ ls x
ls: cannot access 'x': No such file or directory

$ echo $?
2
```

To exit a program in Python use `sys.exit()` with an optional exit code
argument. In the following example we expand the `randnums.py` script to exit
with an exit code of `1`.

```{code-block} python
:caption: "example: randnums.py"
:class: full-width
:linenos:
:emphasize-lines: "6-7"

import sys
import random

count = 3

if len(sys.argv) > 2:
  print(f"Warning: extra arguments: {sys.argv[2:]}", file=sys.stderr)

if len(sys.argv) >= 2:

  if not sys.argv[1].isnumeric():
    print("Count must be a number.")
    sys.exit(1)

  count = int(sys.argv[1])

for _ in range(count):
  print(random.randint(0, 100))
```

### Exercise

`````{exercise} Exiting Exercise
:label: exiting-exercise

Modify your countdown program, so that when an argument is passed that is not a
number, print an error message and exit with an exit code of `1`. Test with
both numeric and non-numeric arguments.

```{dropdown} Need help?
If you already have an if statement checking that `sys.argv` has at least two
items, do the following in it. Otherwise, make one.

1. In an `if` statement, on second item in the `sys.argv` list, check that the
   results of the `.isnumeric()` method is `False`.
  - print an error message
  - call `sys.exit()` with the argument `1`
```

`````

`````{solution} exiting-exercise
:class: dropdown

```{code-block} python
:caption: Exiting Exercise
:class: full-width
:linenos:
:emphasize-lines: "18-20"

"""Countdown exercise for the CLI Lesson
   https://alissa-huskey.github.io/python-class/lessons/cli.html
"""
import os
import sys
import time

count = 3
is_verbose = os.environ.get("VERBOSE", False)

if is_verbose:
    print(f"Counting down from {count}.")

if len(sys.argv) > 2:
    print(f"Warning: extra arguments: {sys.argv[2:]}", file=sys.stderr)

if len(sys.argv) >= 2:
    if not sys.argv[1].isnumeric():
        print(f"Error: Countdown count should be a number: {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    count = int(sys.argv[1])

for num in range(count, 0, -1):
    print(f"{num}...")
    time.sleep(1)
```

```{code-block} console
:caption: command line

$ python countdown.py a
Error: Countdown count should be a number: a

$ echo $?
1

$ python countdown.py 2
2...
1...

$ echo $?
0
```

`````

Terminal size
-------------

::::::{margin}

:::{admonition} Python Version
:class: version

3.3+

:::

::::::

If you need to know the size of the terminal, you can use the
`shutil.get_terminal_size()` function.

```{code-cell} python
:class: full-width

import shutil
shutil.get_terminal_size()
```

It returns a `terminal_size` object, which provides the
{term}`properties <property>` `columns` and `lines`.

```{code-cell} python
:class: full-width

import shutil

size = shutil.get_terminal_size()
print("width:", size.columns)
print("height:", size.lines)
```

It is also a special kind of `tuple`, which means you can make use of multiple
assignment.

```{code-cell} python
:class: full-width

import shutil

width, height = shutil.get_terminal_size()
print("width:", width)
print("height:", height)
```

On systems where the size cannot be determined, the defaults `(80, 24)`
will be used. To change the defaults, send an `tuple` argument with
{samp}`({columns}, {lines})`.

```{code-cell} python
:class: full-width

import shutil
width, height = shutil.get_terminal_size((125, 33))
print("width:", width)
print("height:", height)
```

### Exercise

`````{exercise} Terminal Size Exercise
:label: termsize-exercise

In the following example, we use the width from `get_terminal_size()` print
the text `"Hello world!"` centered on the screen.

```{dropdown} Need help?
1. Import the `shutil` module.
2. Set the variable `text` to the value `"Hello world!"`
3. Assign `width` and `height` to the value returned from `shutil.get_terminal_size()`.
4. To get a string with centered text call the `.center()` method on `text`
   with a width argument of `width`. Assign the returned value to `text`.
5. Print `text`.
```

**Example output**:

```
                                  Hello world!                                  
```

`````

`````{solution} termsize-exercise
:class: dropdown

```{code-block} python
:caption: Terminal Size Exercise
:class: full-width
:linenos:

import shutil

text = "Hello world!"
width, height = shutil.get_terminal_size()
text = text.center(width)

print(text.center(width))
```

`````

:::{seealso}

* [python.org > shutil.get_terminal_size()](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size)

:::


Reference
---------

### Glossary

```{glossary} CLI
CLI
command line interface
  A program executed at the {term}`command line` with a text-based user
  interface.

GUI
graphical user interface
  A program where users provide input primarily by manipulating visual
  elements. Examples include ATMs, Windows, MacOS, nearly all smartphones, web
  browsers, and office programs.

stdin
  The standard input file stream.

stdout
  The standard output file stream.

stderr
  The standard error file stream.

FD
file descriptor
  A unique identifier associated with an input/output resource, most often a
  positive number.

environment variables
  A variable is set on the command line and effects how programs are run or behave.

exit code
status code
  A number between `0` and `255` returned by command line programs to indicate
  success or failure.
```

----

% TODO
% [x] file handlers, stdin/stdout/stderr
% [x] sys.environ, environment variables
% [x] arguments
% [x] exit, exit status
% [ ] terminal size
% [ ] catching cancels, SystemExit
% [ ] executable scripts
%     [ ] shabang
%     [ ] chmod
%     [ ] file modes/permissions
% [ ] color
%     [ ] colorama https://k3no.medium.com/command-line-uis-in-python-80af755aa27d
%     [ ] termcolor
% [ ] version, usage, help
% [ ] if __name__ == "__main__"
