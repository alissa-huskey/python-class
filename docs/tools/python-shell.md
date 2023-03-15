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
Python Shell
============

The Python Shell is a way to play around with Python code without needing to
save a new file.  It can be useful when you're trying to figure things out.
Think of it like a chalkboard -- what you type will only be saved as long as
the shell is open.

You can access it from a few places but here I want to show you how to use it
from repl.it.

```{include} ../toc.md
```

Part 1. Open the Python Shell
-----------------------------

::::::{margin}

:::{admonition} Need help?
:class: hint

For help getting to the command line see [Starting a
Terminal](tools:terminal:starting-a-terminal) in the
[Terminal](tools/terminal.md) tool guide.

:::

::::::

At the {term}`command line` type `python` and hit enter. The prompt will change
to three `>>>`.

That means you're in the Python Shell.

```{code-block} python
:caption: Python shell
Python 2.7.17 (default, Apr 15 2020, 17:20:14)
[GCC 7.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

In these lessons we show Python shell examples in one of the following styles:

{{ leftcol | replace("col", "col align-top") }}

```{code-block} python
:caption: Python shell
>>> print("like this...")
like this...
```

The caption `Python Shell` tells you that this is executed in the Python
Shell. The `>>>` are input lines, and the rest are output.

This should look very similar to what you see in your own Python shell.

{{ rightcol }}

```{code-cell} python
print("...or like that")
```

The green border tells you that this code that you can edit live on this site
(by clicking the ![launch][] icon at the top of the page), or type into your
own Python shell.

The box labeled `In` is input code and the box labeled `Out` is output.

[launch]: ../assets/rocket-icon.png

{{ endcols }}


Part 2. Simple expressions
--------------------------

Here you can type simple expressions to see what they will do. Here are a few things to try.


```{code-cell} python
age = 28
age * 365
```

```{code-cell} python
name = "Jayson"
clothing = "hat"
print("Hello " + name + ". What a nice " + clothing + " you are wearing!")
```

It can be helpful to test out {term}`conditionals` that you would want to put in an {term}`if statement`.

```{code-cell} python
False == 0
```

```{code-cell} python
2.0 == 2
```

```{code-cell} python
2 + 2 == 4
```

```{code-cell} python
2 + 2 + 2 == 2 * 3
```

```{code-cell} python
min_age = 21
age = 28
age >= min_age
```

Type some expressions of your own.


Part 3. The semicolon shorthand
-------------------------------

You can put two lines of code on the same line putting a `;` where the line
break would be. This is not recommended in your scripts but it can be a useful
shorthand in the Python Shell.

For example, we could change the above to:

```{code-cell} python
name = "Jayson" ; clothing = "hat"
print("Hello " + name + ". What a nice " + clothing + " you are wearing!")
```


Part 4. Use Up-arrow and Down-arrow to repeat history
-----------------------------------------------------

You can use the up arrow to fill in previously typed lines in your history.
Imagine we made a mistake.

```{code-block} python
:caption: Python shell
>>> print("Hello world)
  File "<stdin>", line 1
    print("Hello world)
                      ^
SyntaxError: EOL while scanning string literal
```

We can hit the up-arrow once to bring the last line back, then fix the mistake
and press enter.

```{code-block} python
:caption: Python shell
>>> print("Hello world")
Hello world
```

Pressing the up-arrow more than once will bring back lines from further back in
the history. The down arrow will bring us to more recent lines.

For example, we could use the up-arrow to bring back the line where we define
the `name` and `clothing` variables and change their values. After pressing
enter, we could use the up-arrow again to bring back the `print` line to repeat
it with the new values.

```{code-block} python
:caption: Python shell
>>> name = "Cody" ; clothing = "shirt"
>>> print("Hello " + name + ". What a nice " + clothing + " you are wearing!")
Hello Cody. What a nice shirt you are wearing!
>>> name = "Sean" ; clothing = "face"
>>> print("Hello " + name + ". What a nice " + clothing + " you are wearing!")
Hello Sean. What a nice face you are wearing!
```


Part 5. Tab completion
----------------------

To save typing time the Python Shell uses a nifty trick called
{term}`tab completion`. For identifiers that are either built-in or ones that we
define, it we can type out just the first few characters then hit the Tab key,
and it will attempt to guess the rest.

Try typing `pri` and then hit the tab key.

```{code-block} python
:caption: Python shell
>>> print(
```

If there are multiple possible identifiers that could match those characters,
tab-completion will fill in up to the place where they are different, then show
a list of the matches. For example, if we had `favorite_color` and
`favorite_season` defined, and then we typed `fav` followed by the tab key we
would see:

```{code-block} python
:caption: Python shell
>>> favorite_color = "black"
>>> favorite_season = "fall"
>>> fav
favorite_color   favorite_season
>>> favorite_
```

We could then type just the letter `c` then tab to have it fill in
`favorite_color`.


Part 6. Inspect thyself
-----------------------

Python has some helper functions that you can use to figure out more
information about the things you have defined.

The `type()` function will tell you what type a variable is.

```{code-cell} python
:caption: Python shell
five = 5
type(five)
```

```{code-cell} python
five = 5.0
type(five)
```

```{code-cell} python
five = "5"
type(five)
```

```{code-cell} python
type(print)
```

The `callable()` function will tell you if an object is a function or not.

```{code-cell} python
:caption: Python shell
callable(five)
```

```{code-cell} python
callable(print)
```

Part 7. Get help
----------------

The Python Shell includes a handy `help()` function that you can use to get
more information about all sorts of things.

You can pass it a string with the name of a function you would like more information about.

```{code-cell} python
:tags: [output_scroll]

help("print")
```

```{code-cell} python
:tags: [output_scroll]

help("input")
```

```{code-cell} python
:tags: [output_scroll]

help("if")
```

You can also call `help()` without arguments to get Python's Interactive Help.
This will change the prompt to `help>`.

```{code-block} python
:caption: Python shell
>>> help()

Welcome to Python 3.8's help utility!

...
help>
```

You can type anything you would have passed as an argument to the `help()`
function. For example, typing `print` at the `help>` prompt is the same as
typing `help("print")` at the Python prompt.


```{code-block} python
:caption: Python shell
help> print
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
...
```


Additionally you can type:

- `topics` - A list of general topics that you can get more information about,
  where each topic is in all caps. For example `STRINGS`, `FUNCTIONS`, and
  `CALLS`.
- `keywords` - A list of reserved words that have special meanings so that they
  cannot be used as variable or function names. Some examples of keywords in
  python are `for`, `if`, and `def`.
- `symbols` - A list of punctuation symbols that have special meanings. For
  example `=`, `,`, and `+`.
- `modules` - (NOTE: Do not run this in repl.it, as it's buggy and might mess up your
  repl.) A list of available modules.


```{code-block} python
:caption: Python shell
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
...
```

To get back to the normal Python shell type `quit()` or press `Ctrl-D`.

Glossary
--------

```{glossary} python-shell

prompt
  Characters displayed by the interpreter to indicate that it is ready to take
  input from the user.

Python shell
Python interpreter
  a {term}`REPL` for Python code

  an interface where you can type in python code, and it will run it and print
  out the results

read-evaluate-print-loop
REPL
  An interactive tool or environment that takes code input,
  {term}`evaluates` or {term}`executes` it, and displays the
  output or resulting value to the user. {term}`shells` are a subset of
  REPLs. More advanced REPL tools and systems are comprised of an input or
  editor pane, and an output or results pane. Many online REPLs exist such as
  play.golang.org for Go, pythonfiddle.com for Python, try.ruby-lang.org for
  Ruby and repl.it.

tab completion
  A feature in many REPLs where pressing {kbd}`TAB` after a few letters of a
  name (like a command or variable) will attempt to guess the rest.
```
