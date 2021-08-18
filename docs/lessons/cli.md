CLI
===

In this class we've been writing {abbr}`CLI [(command line interface)]`
programs, as opposed to a {abbr}`GUI [(graphical user interface)]`. While most
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
```
$ python countdown.py                                                                      3:49PM <main> [ 1 ]
3...
2...
1...

$ python countdown.py 5                                                                    3:50PM <main> [ 0 ]
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

`````

Output
------

Reference
---------

### Glossary

```{glossary}
CLI
command line interface
  A program executed at the {term}`command line` with a text-based user
  interface.

GUI
graphical user interface
  A program where users provide input primarily by manipulating visual
  elements. Examples include ATMs, Windows, MacOS, nearly all smartphones, web
  browsers, and office programs.
```

...

----

% TODO
% [ ] shabang
% [ ] chmod
% [ ] file handlers, stdin/stdout/stderr
% [ ] environment variables
% [ ] arguments
% [ ] terminal size
% [ ] color
%     [ ] colorama https://k3no.medium.com/command-line-uis-in-python-80af755aa27d
%     [ ] termcolor
% [ ] sys.environ
% [ ] exit, exit status
% [ ] version, usage, help
% [ ] file modes/permissions
% [ ] catching cancels, SystemExit
