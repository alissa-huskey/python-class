Python Shell
============

The Python Shell is a way to play around with Python code without needing to
save a new file.  It can be useful when you're trying to figure things out.
Think of it like a chalkboard -- what you type will only be saved as long as
the shell is open.

You can access it from a few places but here I want to show you how to use it
from repl.it.


Part 1. Open the Python Shell
-----------------------------

1. Open repl.it
2. In the right pane, you will see the following and your prompt will be an orange '>'.

```
Python 3.8.2 (default, Feb 26 2020, 02:56:10)
>
```

Now type `python` and hit enter. The prompt will change to three `>>>`.
That means you're in the Python Shell.

```
Python 3.8.2 (default, Feb 26 2020, 02:56:10)
> python
Python 2.7.17 (default, Apr 15 2020, 17:20:14)
[GCC 7.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


Part 2. Simple expressions
--------------------------

Here you can type simple expressions to see what they will do. Here are a few things to try.


```python3
>>> age = 28
>>> age * 365

>>> name = "Jayson"
>>> clothing = "hat"
>>> print("Hello " + name + ". What a nice " + clothing + " you are wearing!")
```

Type some expressions of your own.


Part 3. The semicolon shorthand
-------------------------------

You can put two lines of code on the same line putting a `;` where the line
break would be. This is not recommended in your scripts but it can be a useful
shorthand in the Python Shell.

For example, we could change the above to:

```python3
>>> name = "Jayson" ; clothing = "hat"
>>> print("Hello " + name + ". What a nice " + clothing + " you are wearing!")
```


Part 4. Use Up-arrow and Down-arrow to repeat history
-----------------------------------------------------

You can use the up arrow to fill in previously typed lines in your history.
Imagine we made a mistake.

```python3
>>> print("Hello world)
  File "<stdin>", line 1
    print("Hello world)
                      ^
SyntaxError: EOL while scanning string literal
```

We can hit the up-arrow once to bring the last line back, then fix the misake
and press enter.

```python3
>>> print("Hello world")
Hello world
```

Pressing the up-arrow more than once will bring back lines from further back in
the history. The down arrow will bring us to more recent lines.

For example, we could use the up-arrow to bring back the line where we define
the `name` and `clothing` variables and change their values. After pressing
enter, we could use the up-arrow again to bring back the `print` line to repeat
it with the new values.

```python3
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
***tab-completion***. For identifiers that are either built-in or ones that we
define, it we can type out just the first few characters then hit the Tab key,
and it will attempt to guess the rest.

Try typing `pri` and then hit the tab key.

```python3
>>> print(
```

If there are multiple possible identifiers that could match those characters,
tab-completion will fill in up to the place where they are different, then show
a list of the matches. For example, if we had `favorite_color` and
`favorite_season` defined, and then we typed `fav` followed by the tab key we
would see:

```python3
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

```python3
>>> five = 5
>>> type(five)
<class 'int'>
>>> five = 5.0
>>> type(five)
<class 'float'>
>>> five = "5"
>>> type(five)
<class 'str'>
>>> type(print)
<class 'builtin_function_or_method'>
```

The `callable()` function will tell you if an object is a function or not.

```python3
>>> callable(five)
False
>>> callable(print)
True
```

Part 7. Get help
----------------

The Python Shell includes a handy `help()` function that you can use to get
more information about all sorts of things.

You can pass it a string with the name of a funciton you would like more information about.

(You may find it helpful to expand the right pane by clicking the middle of the
bar between the right and left panes, and dragging to the left.)

```python3
>>> help("print")
>>> help("input")
>>> help("if")
```

You can also call `help()` without arguments to get Python's Interactive Help.
This will change the prompt to `help>`.

```python3
>>> help()

Welcome to Python 3.8's help utility!

...
help>
```

You can type anything you would have passed as an argument to the `help()`
function. For example, typing `print` at the `help>` prompt is the same as
typing `help("print")` at the Python prompt.


```python3
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
- `modules` - A list of available modules. (Don't worry about this for now,
  since we haven't learned about modules yet. Also, it's a little buggy in
  repl.it.)


```python3
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
...
```

To get back to the normal Python shell type `quit` or press `Ctrl-D`.
