Pytest
======

Pytest is a tool for writing and running tests.

```{seealso}

On [writing pytest tests](../practices/testing/pytest-tests).

```

Install
-------

:::::{tabbed} Poetry

```{code-block} bash
:caption: command line
poetry add --dev pytest
```

Version `1.2.1` and newer use:

```{code-block} bash
:caption: command line
poetry add --group dev pytest
```

:::::

:::::{tabbed} Pip

```{code-block} bash
:caption: command line
python -m pip install pytest
```

:::::

Usage
-----

### Getting Help

### Running Tests

### Verbose Mode

- [ ] invocation (run)
    - [ ] help
    - [ ] running a single test (`-k` or test_name.py::test_name)
    - [ ] verbose mode
      - [ ] `-v`: verbose
      - [ ] `-x`: fail on first tests
      - [ ] `-k`: expression
      - [ ] `-tb=short`: shorter tracebacks
      - [ ] `--pdb`: start debugger on failures
      - [ ] `--trace`: start debugger with breakpoint at the beginning of each test
      - [ ] `--pdbcls=IPython.terminal.debugger:TerminalPdb`: use the ipython debugger
      - [ ] running single test, filtering to matching names

Quickref
--------

| Flag                  | Description                              |
|-----------------------|------------------------------------------|
| `-h`                  | Help                                     |
| `-x`                  | Exit on first error                      |
| `--pdb`               | start debugger on error                  |
| `--trace`             | add breakpoint to beginning of each test |
| `-s`                  | don't capture stdout and stderr          |
| `-l`, `--show-locals` | show local variable and their values     |
| `--tb=short`          | print shorter tracebacks                 |
|                       |                                          |

See also
--------

```{seealso}

* Pytest [docs](https://doc.pytest.org/en/latest/)
* [Testing Python Applications with Pytest](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)

```

TODO
----

- [x] install
- [ ] setup
    - [ ] pyproject.html: testpaths, addopts
- [ ] conftest.py
- [ ] plugins
    - [ ] pytest-only (add only marker)
    - [ ] pytest-parametrization
    - [ ] pytest-clarity (prettier assert diffs)
  - [ ] adding to `pyproject.toml`
    ```toml
    [tool.pytest.ini_options]
    testpaths = ["tests"]
    addopts = "-vx"
    ```
