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
Pytest Tests
============

Pytest is a testing framework for Python. In this document we'll discuss how to
write tests that can be run with Pytest as well as how to use some of the extra
features that Pytest provides for use in our test code.

For installation and other usage information, see the [Pytest tool guide](../../tools/pytest).

```{contents}
:backlinks: top
:local:
:depth: 2
```

Part 1: Writing tests
---------------------

In this section we'll discuss how to write tests to be run with Pytest.

### Part 1.1: Hello World

Pytest expects our tests to be located in files whose names begin with `test_`
or end with `_test.py`.

Individual tests are written in functions that begins with `test_` and contain
one or more `assert` statements which determine if it passes or fails.

Say you have a file named `test_hello_world.py` that contains the single test
function `test_truth()`. This test in turn contains a single assert statement
which will always pass.

```{code-block} python
:linenos:
:caption: test_hello_world.py

def test_truth():
    assert True
```

```{important}

Do not duplicate test names. If you do, only the first test will be run and
any duplicates will be ignored by Pytest.

```

To run the test use the command line to type `pytest` followed by the filename.

```{code-block} console
:caption: command line
$ pytest test_hello_world.py
```

The result will look something like this.

```{code-block} pytest
:caption: command line output
===================== test session starts ======================
platform darwin -- Python 3.9.1, pytest-7.0.1, pluggy-1.0.0
cachedir: .pytest_cache
rootdir: ~/python-class, configfile: pyproject.toml
plugins: pylama-8.3.7, typeguard-2.13.3
collected 1 item

test_hello_world.py .                                    [100%]

====================== 1 passed in 0.00s =======================
```

Congratulations, you've run your first Pytest test!

### Part 1.2: Test failures

Let's look at an example of a failing tests. In the following `test_lies()`
function the assert statement fails, which will in turn cause that test to
fail.

```{code-block} python
:linenos:
:caption: test_hello_world.py

def test_truth():
    assert True

def test_lies():
    assert False
```

Here is what your test output looks like now.

```{code-block} pytest
:caption: command line output
$ pytest test_hello_world.py
===================== test session starts ======================
platform darwin -- Python 3.9.1, pytest-7.0.1, pluggy-1.0.0
cachedir: .pytest_cache
rootdir: ~/python-class, configfile: pyproject.toml
plugins: pylama-8.3.7, typeguard-2.13.3
collected 2 items

test_hello_world.py .F                                   [100%]

=========================== FAILURES ===========================
__________________________ test_lies ___________________________

    def test_lies():
>       assert False
E       assert False

test_hello_world.py:5: AssertionError
=================== short test summary info ====================
FAILED test_hello_world.py::test_lies - assert False
================= 1 failed, 1 passed in 0.05s ==================
```

### Part 1.3: Reading test output

Let's take a closer look at that test output.

```{code-block} pytest
:caption: command line output
test_hello_world.py .F                                   [100%]
```

This line indicates the progress of each test file and each test in the file is
represented by a single character following the filename.

* the green `.` indicates the first passing test
* the red `F` indicates the second failing test
* `[100%]` means that all of the test found in the file were run

```{code-block} pytest
:caption: command line output
=========================== FAILURES ===========================
__________________________ test_lies ___________________________

    def test_lies():
>       assert False
E       assert False

```

This section of the output shows you detailed information about each failing
test.

* The `_____ test_lies _____` line indicates that this is the beginning  of the
  information about the `test_lies()` test.
* This is followed by a sample of the code where failure took place with the
  specific line that caused the failure indicated with a `>`.
* The red lines that start with `E` give you more detailed information about
  the failure or error. In this case, there's no additional information so it
  looks the same as the original line.

```{code-cell}
:tags: [remove-input]
print("\x1b[31mtest_hello_world.py:5:\x1b[0m AssertionError")
```

This line is probably the most useful of all. It tells you the three most
important pieces of information:

* the filename and line number where the failure took place
* what kind of exception was encountered

```{code-block} pytest
:caption: command line output
=================== short test summary info ====================
FAILED test_hello_world.py::test_lies - assert False
================= 1 failed, 1 passed in 0.05s ==================
```

Finally, this line shows a summary of all the failures.

### Part 1.4: Testing functions

Let's take a look at what a test for a piece of code might look like.

Below we add to the {file}`test_hello_world.py` file a `increment()` function
which returns `number` incremented by one.

The `test_increment()` test calls the `increment()` function with an argument of
`5` and assigns the result to the variable `answer`. Then it asserts that the
`answer` should be `6`.

```{code-block} python
:linenos:
:caption: test_hello_world.py

def increment(number):
    return number + 1

def test_truth():
    assert True

def test_increment():
    answer = increment(5)
    assert answer == 6
```

### Part 1.5: Importing functions

We typically do not keep our functions in the same file as our tests. This
means in order to test our functions, we'll need to import them into the test
file.

Let's say we have a file called `my_project.py`.

```{code-block} python
:linenos:
:caption: my_project.py
def can_drink(age):
    return age >= 21
```

We would typically name our test file `test_my_project.py`. Then we'd import
the `can_drink` function from the `my_project` module before defining the test
for it.

```{code-block} python
:linenos:
:caption: test_my_project.py

from my_project import can_drink

def test_can_drink():
    is_allowed = can_drink(5)
    assert not is_allowed
```


### Part 1.6: More imports

In larger projects it is common to break things into multiple files and
directories. A common directory structure looks like this:

```text
.
├── README.md
├── my_project
│   ├── __init__.py
│   └── main.py
├── setup.py
└── tests
    └── test_main.py
```

In a setup like this your code would be in the `my_project` directory and your
tests in the `tests` directory.

If we imagine that we renamed the `my_project.py` file to `my_project/main.py`,
then we would need to modify the import statement in our test file.

```{code-block} python
:caption: test_my_project.py
:linenos:

from my_project.main import can_drink

def test_can_drink():
    is_allowed = can_drink(5)
    assert not is_allowed
```

To run the tests you would then run the command

```{code-block} console
:caption: command line
$ pytest tests/test_main.py
```

Or to run all tests in the `tests` directory simply:

```{code-block} console
:caption: command line
$ pytest tests
```


```{important}

You must run `pytest` from the root directory of your project for the imports
to work properly.

```

Part 2: Skipping tests
----------------------

`````{margin}

```{seealso}

[Pytest Docs > How to use skip and xfail to deal with tests that cannot succeed](https://docs.pytest.org/en/stable/how-to/skipping.html)

```

`````

In this section we'll discuss how to skip tests.

### Part 2.1: Skipping a test

Sometimes we have a test that is not currently working for some reason--maybe
it's a work in progress or represents something you want to implement at a
later date. Here's an example in our old `test_hello_world.py` file.

First you need to import the `pytest` module in your test. Then above the test
function add the line {samp}`@pytest.mark.skip(reason="{EXPLANATION}")` with a
brief explanation of why it is being skipped.

```{code-block} python
:caption: test_hello_world.py

import pytest

def test_truth():
    assert True

@pytest.mark.skip(reason="an example of a test failure")
def test_lies():
    assert False

def test_increment():
    answer = increment(5)
    assert answer == 6
```

When you run the tests, your output will show a yellow `s` for skipped tests.

```{code-block} pytest
$ pytest test_hello_world.py
===================== test session starts ======================
platform darwin -- Python 3.9.1, pytest-7.0.1, pluggy-1.0.0
rootdir: ~/python-class, configfile: pyproject.toml
plugins: pylama-8.3.7, typeguard-2.13.3
collected 3 items

test_hello_world.py .s.                                  [100%]

================= 2 passed, 1 skipped in 0.00s =================
```

### Part 2.2: Skipping a failure

Another way to do the same thing is to mark it as an expected failure. It is
the same as above, except use `xfail` instead of `skip`.

```{code-block} python
:caption: test_hello_world.py

import pytest

def test_truth():
    assert True

@pytest.mark.xfail(reason="an example of a test failure")
def test_lies():
    assert False

def test_increment():
    answer = increment(5)
    assert answer == 6
```

In the output, the skipped test will be marked with a yellow `x`.

```{code-block} pytest
$ pytest test_hello_world.py
===================== test session starts ======================
platform darwin -- Python 3.9.1, pytest-7.0.1, pluggy-1.0.0
rootdir: ~/python-class, configfile: pyproject.toml
plugins: pylama-8.3.7, typeguard-2.13.3
collected 3 items

test_hello_world.py .x.                                  [100%]

================= 2 passed, 1 xfailed in 0.03s =================
```

### Part 2.3: Skipping sometimes

Sometimes you may want to skip certain tests that only work in certain
environments. For example, based on a developers operating system or the
version of Python they are running.

In these cases the `skipif` decorator is useful. The first argument is the
condition under which to skip the test, then use the `reason` keyword argument
as usual.

```{code-block} python
import sys

import pytest

@pytest.mark.skipif(sys.platform != "darwin", reason="mac-specific testing")
def test_macos():
  ...

```

Part 3: Exception Handling
--------------------------

`````{margin}

```{seealso}

* [Pytest Docs > pytest.raises](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises)
* [Pytest Docs > Assertions about expected exceptions](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions)

```

`````

Sometimes our program may raise exceptions on purpose, in which case we need to
be able to test those exceptions without causing the tests to fail.

### Part 3.1: pytest.raises

To test for a raised exception use `pytest.raises` as a context manager with
the code that is being tested inside of the context manager.

For example, the following code effectively asserts that when you call the
`do_quit()` function a `SystemExit` exception is raised. (Which is how most
Python programs exit, under the hood.)

```{code-block} python
import pytest

from my_game import do_quit

def test_do_quit():
    with pytest.raises(SystemExit):
      # code to test
      do_quit()
```

### Part 3.1: Exception messages

Sometimes just checking the exception class isn't enough -- we have to test for
a specific exception message. For example, our program may raise a `ValueError`
in a function. However `ValueError` exceptions are very common.

In that case you can use the optional `as` part of the `pytest.raises` context
manager to get the exception info, then run the code you wish to test as
before. Then *after* the with statement, you can add an assert statement on
`info.value`.

```{code-block} python
import pytest

from my_game import inventory_remove

def test_inventory_remove_with_invalid_argument():
    with pytest.raises(ValueError) as info:
        # code to test
        inventory_remove(5)

    # check the exception message
    message = str(info.value)
    assert "inventory_remove() expected an item key (str)." in message
```

### Part 3.3: Message patterns

Another way to test the error message is to use the `match` keyword argument in
`pytest.raises()`.

```{code-block} python
import pytest

from my_game import Player

def test_buy():
    player = Player(gems=10)
    sword = Sword(price=90)

    with pytest.raises(ValueError, match="you are 80 gems short") as info:
        # code to test
        player.buy(sword)
```

The `match` argument can be a regular expression, so you could also do.

```{code-block} python
import pytest

from my_game import Player

def test_buy():
    player = Player(gems=10)
    sword = Sword(price=90)

    with pytest.raises(ValueError, match=r"you are \d+ gems short") as info:
        # code to test
        player.buy(sword)
```

Part 4: Testing printed output
------------------------------

`````{margin}

```{seealso}

[Pytest Docs > How to capture stdout/stderr output](https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html)

```

`````

Sometimes we need to test not what is returned, but what is printed to the
screen. To do this we can use the special fixture (more on those later)
`capsys`.

### Part 4.1: Testing stdout

When you call the `print()` function the string that you pass is sent to a
special file called {term}`stdout` that your terminal knows to display to the
end user.

When we are testing something that prints to the screen, add `capsys` to the
function definition to let Pytest know that it should capture the system output
and save it for us.


```{code-block} python
def test_write(capsys):
  write("hello", lines_after=3)
  output = capsys.readouterr().out

  assert output.endswith("\n\n\n")
```

Note that every time you call `readouterr()` it sets the `out` attribute to all
of the content that has been sent to `stdout` since the function started or the
last time `readouterr()` was called.

For example the `output` variable on line `6` contains what was captured from
lines `2` through `4`, while the `output` variable on line `12` contains what
was printed on lines `8` through `10`.

```{code-block} python
:linenos:
:emphasize-lines: "6, 12"
def test_stdout(capsys):
    print("a")
    print("b")
    print("c")

    output_1 = capsys.readouterr().out

    print("x")
    print("y")
    print("z")

    output_2 = capsys.readouterr().out

    assert output_1 == "a\nb\nc\n"
    assert output_2 == "x\ny\nz\n"

```

### Part 4.2: Testing stderr

Many command line programs print errors to a seperate special file called
`stderr`. This allows end users and other programs to do things that involve
handling error messages differently from normal program output. For example to
silence all errors or save a file that contains just the errors.

In Python, to print to `stderr` you simply include the `sys` module, then add
the keyword argument `file=sys.stderr` to your print statement.

Here's an example `error()` function which adds a red `Error` string to the
beginning of the message then prints all arguments to `stderr`.

```{code-block} python
import sys

def error(*args):
    print("\x1b[31mError\x1b[0m", *args, file=sys.stderr)
```

To write a test for this we would use `capsys` just like before, but look for
`err` instead of `out`.

```{code-block} python
def test_error(capsys):
    error("Please reconsider your life choices and try again.")

    output = capsys.readouterr().err

    assert "reconsider" in output
```

### Part 4.3: Testing both

If you need to check what was printed to both `stdout` and `stderr`, you need
to make sure that `readouterr()` is only called once. You can accomplish this
by assigning it to a variable.

Let's say we're testing a function that starts like this:

```{code-block} python
import sys

def do_thing(*args):
    print("debug: Trying to do the thing:", *args)

    if not args:
        print("Which thing should I do?", file=sys.stderr)
        return

    ...
```

In our test, we'll save the result of `readouterr()` to the variable
`captured`, then check `captured.out` and `captured.err` in our assert
statements.

```{code-block} python
def test_do_thing(capsys):
    do_thing()

    captured = capsys.readouterr()

    assert "Trying to do the thing" in captured.out
    assert "Which thing" in captured.err
```

Part 5: Parametrization
-----------------------

`````{margin}

```{seealso}

[Pytest Docs > How to parametrize fixtures and test functions](https://docs.pytest.org/en/stable/how-to/parametrize.html#parametrize-basics)

```

`````

Parametrization is used to combine the multiple test that are *almost* exactly
the same into one test case that takes arguments.

### Part 5.1: parametrize

Remember our `can_drink()` function? Let's say we were very responsible and
wrote tests to cover a whole bunch of cases.

```{code-block} python
:caption: test_my_project.py
:linenos:

from my_project.main import can_drink

def test_can_drink_15():
    is_allowed = can_drink(15)
    assert not is_allowed

def test_can_drink_0():
    is_allowed = can_drink(0)
    assert not is_allowed

def test_can_drink_negative():
    is_allowed = can_drink(-5)
    assert not is_allowed

def test_can_drink_float():
    is_allowed = can_drink(17.5)
    assert not is_allowed

def test_can_drink_21():
    is_allowed = can_drink(21)
    assert is_allowed

def test_can_drink_100():
    is_allowed = can_drink(100)
    assert is_allowed
```

Parametrization allows us to collapse that down into just one test with a few
modifications.

First, we'll refactor our test to add two parameters: `age` and `expected`.
We'll use `age` for the argument to pass to `can_drink()` and `expected` in the
assert statement to indicate if `is_allowed` should be `True` or `False`.

```{code-block} python
:caption: test_my_project.py
:linenos:

from my_project.main import can_drink

def test_can_drink(age, expected):
    is_allowed = can_drink(age)
    assert is_allowed == expected
```

Now we'll import `pytest` and call `@pytest.mark.parametrize()` just above the
test function.

The first argument is a list containing the variable names you use in the test
function. In this case `age` and `expected`.

The second is a list of tuples where each contains the arguments to send to the
test function for run instance.

```{code-block} python
:caption: test_my_project.py
:linenos:

from my_project.main import can_drink

import pytest

@pytest.mark.parametrize(
    ["age", "expected"], [
        (15, False),
        (0, False),
        (-5, False),
        (17.5, False),
        (21, True),
        (100, True),
])
def test_can_drink(age, expected):
    is_allowed = can_drink(age)
    assert is_allowed == expected
```

Pytest will run the test for each tuple. So, for the first tuple `age` will be `15`
and `expected` will be `False`; for the second `age` will be `0` and `expected`
will be `False`; and so on.

If you run your tests in verbose mode with the `-v` flag, you will see a line
for each tuple like so:

```{code-block} pytest
:caption: command line output
$ pytest -v test_my_project.py
===================== test session starts ======================
platform darwin -- Python 3.9.1, pytest-7.0.1, pluggy-1.0.0
cachedir: .pytest_cache
rootdir: ~/python-class, configfile: pyproject.toml
plugins: pylama-8.3.7, typeguard-2.13.3
collected 6 items

test_my_project.py::test_can_drink[15-False] PASSED      [ 16%]
test_my_project.py::test_can_drink[0-False] PASSED       [ 33%]
test_my_project.py::test_can_drink[-5-False] PASSED      [ 50%]
test_my_project.py::test_can_drink[17.5-False] PASSED    [ 66%]
test_my_project.py::test_can_drink[21-True] PASSED       [ 83%]
test_my_project.py::test_can_drink[100-True] PASSED      [100%]

====================== 6 passed in 0.01s =======================
```

### Part 5.2: Skipping instances

You may want to include instances that you know will fail to show that that
usage is unsupported. To do this, make a test instance that calls
`pytest.param()` (instead of a tuple) and include the keyword argument `marks`
to indicate what mark to use.

Below we add a `pytest.param()` instance where `age` is a string `"100"`.
(`expected` is `None`, but it doesn't matter because the exception will happen
on line `17`.) Then we pass the keyword argument `marks=pytest.mark.xfail` to
indicate we expect that instance to fail.

```{code-block} python
:caption: test_my_project.py
:linenos:

from my_project.main import can_drink

import pytest

@pytest.mark.parametrize(
    ["age", "expected"], [
        (15, False),
        (0, False),
        (-5, False),
        (17.5, False),
        (21, True),
        (100, True),
        pytest.param("100", None, marks=pytest.mark.xfail),

])
def test_can_drink(age, expected):
    is_allowed = can_drink(age)
    assert is_allowed == expected
```

When we run the tests in verbose mode Pytest will indicate that that test was
marked as xfail.

```{code-block} pytest
:caption: command line output
$ pytest -v test_my_project.py
===================== test session starts ======================
platform darwin -- Python 3.9.1, pytest-7.0.1, pluggy-1.0.0
cachedir: .pytest_cache
rootdir: ~/python-class, configfile: pyproject.toml
plugins: pylama-8.3.7, typeguard-2.13.3
collected 7 items

test_my_project.py::test_can_drink[15-False] PASSED      [ 14%]
test_my_project.py::test_can_drink[0-False] PASSED       [ 28%]
test_my_project.py::test_can_drink[-5-False] PASSED      [ 42%]
test_my_project.py::test_can_drink[17.5-False] PASSED    [ 57%]
test_my_project.py::test_can_drink[21-True] PASSED       [ 71%]
test_my_project.py::test_can_drink[100-True] PASSED      [ 85%]
test_my_project.py::test_can_drink[100-None] XFAIL       [100%]

================= 6 passed, 1 xfailed in 0.02s =================
```

Part 6: Setup and Teardown
--------------------------

`````{margin}

```{seealso}

[Pytest Docs > classic xunit-style setup](https://docs.pytest.org/en/6.2.x/xunit_setup.html)

```

`````

For tests that need to load data or any other kind of information from the
environment, it is important that each test start with a clean slate. In this
section we'll talk about the different ways to accomplish this.

### Part 6.1: Per-module setup/teardown functions

Some setup or teardown steps only need to be done once per module (or file).
For example, you may need to open and close a connection to a database, create
and delete temporary directories, load the contents of a file, or initialize
global variables.

In Pytest tests you can do this by simply definining a `setup_module()` which
will run once per file before tests and/or a `teardown_module()` which will run
once per file after tests.

Here is an example that loads data files previously downloaded from
`https://jsonplaceholder.typicode.com/` and saved in the directory
`tests/.data` into a `STATE` dictionary.

```{code-block} python
:caption: test_setup_teardown.py
:linenos:
from pathlib import Path
import json

def setup_module(module):
    """Initialize STATE global variable and load from json testdata."""
    global STATE
    STATE = {}

    for resource in ["users", "todos"]:
        file = Path(__file__).parent / ".data" / f"{resource}.json"
        with file.open() as fh:
            STATE[resource] = json.load(fh)

def test_user():
    """Test that the first user was loaded from the users.json file."""
    user = STATE["users"][0]

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"

def test_todo():
    """Test that the first todo was loaded from the todos.json file."""
    todo = STATE["todos"][0]

    assert todo["id"] == 1
    assert todo["title"] == "delectus aut autem"
    assert not todo["completed"]
```

### Part 6.2: Per-test setup/teardown functions

It is important to start each test with a clean slate to avoid test
corruption--that is when you make changes to one test and it unexpectedly
breaks other tests.

Let's add an example to our `test_setup_teardown.py` file.

```{code-block} python
:caption: test_setup_teardown.py
:linenos:
:lineno-start: 28
:emphasize-lines: "4, 12"

def test_modify_state():
    """Change the STATE data"""
    todo = STATE["todos"][0]
    todo["completed"] = True

    assert todo["completed"]

def test_check_modified_state():
    """Check the same data that was modified above."""
    todo = STATE["todos"][0]

    assert not todo["completed"]
```

When we run these tests, `test_check_modified_state()` will fail, because
we changed the data on the previous test.

```{code-block} pytest
:caption: command line output
$ pytest -v test_setup_teardown.py
===================== test session starts ======================
platform darwin -- Python 3.9.1, pytest-7.0.1, pluggy-1.0.0
cachedir: .pytest_cache
rootdir: ~/python-class, configfile: pyproject.toml
plugins: pylama-8.3.7, typeguard-2.13.3
collected 4 items

tests/test_setup_teardown.py ...F                        [100%]

=========================== FAILURES ===========================
__________________ test_check_modified_state ___________________

    def test_check_modified_state():
        """Check the same data that was modified above."""
        todo = STATE["todos"][0]

>       assert not todo["completed"]
E       assert not True

tests/test_setup_teardown.py:41: AssertionError
=================== short test summary info ====================
FAILED tests/test_setup_teardown.py::test_check_modified_state - assert not True
================= 1 failed, 3 passed in 0.05s ==================
```

To avoid this we need to add a `setup_function()` function which will be run
before each test. We'll also add another global variable `DATA` which we'll use
in the tests and reset from `STATE` using `deepcopy()` before each test.

```{code-block} python
:caption: test_setup_teardown.py
:linenos:
:emphasize-lines: "2, 15-18, 22, 29, 37, 44"
from pathlib import Path
from copy import deepcopy
import json

def setup_module(module):
    """Initialize STATE global variable and load from json testdata."""
    global STATE
    STATE = {}

    for resource in ["users", "todos"]:
        file = Path(__file__).parent / ".data" / f"{resource}.json"
        with file.open() as fh:
            STATE[resource] = json.load(fh)

def setup_function(function):
    """Revert data to its original state before each test."""
    global DATA
    DATA = deepcopy(STATE)

def test_user():
    """Test that the first user was loaded from the users.json file."""
    user = DATA["users"][0]

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"

def test_todo():
    """Test that the first todo was loaded from the todos.json file."""
    todo = DATA["todos"][0]

    assert todo["id"] == 1
    assert todo["title"] == "delectus aut autem"
    assert not todo["completed"]

def test_modify_state():
    """Change the DATA data"""
    todo = DATA["todos"][0]
    todo["completed"] = True

    assert todo["completed"]

def test_check_modified_state():
    """Check the same data that was modified above."""
    todo = DATA["todos"][0]

    assert not todo["completed"]
```

Now that each test starts with the same known set of data, all the tests pass.

```{code-block} pytest
:caption: command line output
$ pytest -v test_setup_teardown.py
===================== test session starts ======================
platform darwin -- Python 3.9.1, pytest-7.0.1, pluggy-1.0.0
cachedir: .pytest_cache
rootdir: ~/python-class, configfile: pyproject.toml
plugins: pylama-8.3.7, typeguard-2.13.3
collected 4 items

tests/test_setup_teardown.py ....                        [100%]

====================== 4 passed in 0.01s =======================
```

Part 7: Fixtures
----------------

`````{margin}

```{seealso}

[Pytest Docs > How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

```

`````

In tests we often need to do similar setup in many tests. As a project becomes
larger, it becomes unweildy to create the same data over and over again.

{term}`Fixtures <fixture>` are one way to approach this problem. In general
terms, the fixtures comprise the known state of the test environment. In fact,
you could consider data in setup and teardown functions from
[Part 6](#part-6-setup-and-teardown) to be fixtures.

Different languages and testing frameworks have different systems for
supporting fixtures, usually involving some form of setup/teardown.
Traditionally though, the the term fixture refers to a single record of test
data--from the setup/teardown section, each user or todo dictionary would be
one fixture.

Pytest has a unique and powerful approach to fixtures which can entirely
replace setup and teardown functions. It might take a minute to wrap your head
around it though.

### Part 7.1: Basic Fixture

In Pytest fixtures are set up as functions decorated with the `@pytest.fixture`
decorator. The value that is returned from the function is the fixture data.
are defined as functions and use the `@pytest.fixture` decorator. Then test
functions declare the fixtures that they require as parameters.

Here's an example of the {term}`"hello world" <hello world>` of Pytest fixtures.

```{code-block} python
:caption: test_fixtures.py
:linenos:
import pytest

@pytest.fixture
def true():
    return True

def test_truth(true):
    assert true == True
```

Let's take a closer look.

{{ leftcol }}

1\. First we import `pytest`.

{{ rightcol }}

```{code-block} python
:caption: test_fixtures.py
:linenos:
import pytest

```

{{ newrow }}

2\. The `@pytest.fixture` line is a decorator that tells Pytest to treat the
next function as a fixture.

{{ rightcol }}

```{code-block} python
:caption: test_fixtures.py
:linenos:
:lineno-start: 3
:emphasize-lines: 1

@pytest.fixture
def true():
    return True
```

{{ newrow }}

3\. Now we define the fixture function. The value
returned by the function is what will be used in test
functions.

{{ rightcol }}

```{code-block} python
:caption: test_fixtures.py
:linenos:
:lineno-start: 3
:emphasize-lines: 2-3

@pytest.fixture
def true():
    return True
```

{{ newrow }}

4\. When we define a test function that requires the
fixture, we use the fixture name as a parameter to the
test function.

{{ rightcol }}

```{code-block} python
:caption: test_fixtures.py
:linenos:
:lineno-start: 7
:emphasize-lines: 1
def test_truth(true):
    assert true == True
```

{{ newrow }}

5\. Finally, we use the fixture name in the test
function the same way we would any other variable.

{{ rightcol }}

```{code-block} python
:caption: test_fixtures.py
:linenos:
:lineno-start: 7
:emphasize-lines: 2
def test_truth(true):
    assert true == True
```

{{ endcols }}

### Part 7.2: Example uses

Fixtures can be used to store reusable data such as a dictionary of user
information. It can also be used to return more sophisticated Python
objects--for example, a `pathlib.Path`.

```{code-block} python
:caption: test_fixtures.py
:linenos:
:emphasize-lines: "9-37, 42-47"
from pathlib import Path

import pytest

@pytest.fixture
def true():
    return True

@pytest.fixture
def user_bret():
    return {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  }

@pytest.fixture
def fixturedir():
    return Path(__file__).parent / ".data"

def test_truth(true):
    assert true == True

def test_something_with_a_user(user_bret):
    assert user_bret["id"] == 1

def test_something_from_fixturedir(fixturedir):
    user_file = fixturedir / "users.json"
    assert user_file.exists()
```

### Part 7.3: Auto-use fixtures

You can set up fixtures to be used automatically, so they don't have to be
specified for each test. You can choose what {term}`scope` to use the fixtures
in--that is, at what level functions should share the fixture before it is
destroyed.

| Scope        | Shared with                          | When Fixture is Destroyed |
|--------------|--------------------------------------|---------------------------|
| **function** | a single test function               | end of each test          |
| **class**    | all test methods in a class          | last test in the class    |
| **module**   | all tests in a module (file)         | last test in the module   |
| **package**  | all tests in the package (directory) | last test in the package  |
| **session**  | all tests to be run                  | last test to be run       |


```{code-block} python
:caption: test_fixtures.py
:linenos:
```

See also
--------

```{seealso}

* [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
* [Testing Python Applications with Pytest](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)

```

----

TODO:
-----

- [x] filenames and test names
- [x] skipping tests (`@pytest.mark.skip()`, `pytest.skip()`, `@pytest.mark.xfail()`)
- [x] exceptions
- [x] capsys
- [x] params
- [ ] fixtures
    - [ ] auto-use fixtures: function, module, session
    - [ ] param fixtures
    - [ ] fixture fixtures
    - [ ] `--fixtures` flag
    - [ ] conftest.py
    - [ ] fixture factories
- [-] setup and teardown
- [ ] mocks and stubs
- [ ] temp files/directories
- [ ] vscode
- [ ] testing with debugger
  - [ ] [pdb++](https://github.com/pdbpp/pdbpp)
  - [ ] [pdbr](https://pypi.org/project/pdbr/)
