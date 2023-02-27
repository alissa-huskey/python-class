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
IPython
=======

```{include} ../toc.md
```

Tips
----

### Tip 1: quickref

You can use the `%quickref` magic command to get a quick introduction to
IPythons features.

```{code-block} text
1>>> %quickref

IPython -- An enhanced Interactive Python - Quick Reference Card
================================================================

obj?, obj??      : Get help, or more help for object (also works as
                   ?obj, ??obj).
?foo.*abc*       : List names in 'foo' containing 'abc' in them.
%magic           : Information about IPython's 'magic' % functions.
...
```

### Tip 2: Save history to file

You can save the history from your last session to the file in the directory
you were in when you started `ipython` by using the `%save` magic command.

```{code-block} text
---
caption: ipython shell -- save to a file named session.py
---
1>>> %save session ~1/
The following commands were written to file `session.py`:
import requests
response = requests.get("http://api.punkapi.com/v2/beers/random")
response.ok
response.status_code
response.reason
...
```

Troubleshooting
---------------

### unexpected keyword argument 'column'

:::{dropdown} Error
:open:

This error occurs when attempting tab completion.

```
  File "../venv/lib/python3.8/site-packages/IPython/core/completer.py", line 2029, in _complete
    completions = self._jedi_matches(
  File "../venv/lib/python3.8/site-packages/IPython/core/completer.py", line 1373, in _jedi_matches
    interpreter = jedi.Interpreter(
  File "../venv/lib/python3.8/site-packages/jedi/api/__init__.py", line 725, in __init__
    super().__init__(code, environment=environment,
TypeError: __init__() got an unexpected keyword argument 'column'
```

:::

::::::{dropdown} Solution
:open:

iPython `<=7.19` is incompatible with jedi version `0.18.0`.
To resolve, downgrade `jedi` to version `0.17.2`.

::::{tab-set}

`````{tab-item} poetry

Modify your {file}`pyproject.toml` file and add the following `jedi`
dependency just above the `ipython` dependency.

```{code-block} toml
:caption: pyproject.toml
:emphasize-lines: "3-3"

[tool.poetry.dev-dependencies]
...
jedi = "0.17.2" # ipython <=7.19
ipython = "^7.19.0"
```

Then in a terminal run:

```{code-block} bash
:caption: terminal
poetry update jedi
```

`````

`````{tab-item} pip

In a terminal run:

```{code-block} bash
:caption: terminal
python -m pip install -U jedi~=0.17.2
```

`````

::::

::::::

```{seealso}

* [ipython/ipython#12740](https://github.com/ipython/ipython/issues/12740)

```

### Unhandled exception in event loop

:::{dropdown} Error
:open:

This error occurs intermittently after hitting enter.

```
Unhandled exception in event loop:
  File "...\lib\asyncio\proactor_events.py", line 768, in _loop_self_reading

    f.result()  # may raise
  File "...\lib\asyncio\windows_events.py", line 808, in _poll
    value = callback(transferred, key, ov)
  File "...\lib\asyncio\windows_events.py", line 457, in finish_recv
    raise ConnectionResetError(*exc.args)

Exception [WinError 995] The I/O operation has been aborted because of either a thread exit or an application request
```

:::

::::::{dropdown} Solution
:open:

iPython ~7.13.0 on Windows does not work with a version 3+ of prompt-toolkit.
To resolve, downgrade `prompt-toolkit` to version `2.x`.

:::::{tab-set}

`````{tab-item} poetry

Modify your {file}`pyproject.toml` file and add the following `prompt-toolkit`
dependency just above the `ipython` dependency.

```{code-block} toml
:caption: pyproject.toml
:emphasize-lines: "3-3"

[tool.poetry.dev-dependencies]
...
prompt-toolkit = "^2" # ipython ~7.10
ipython = "^7.13.0"
```

Then in a terminal run:

```{code-block} bash
:caption: terminal
poetry update prompt-toolkit
```

`````

`````{tab-item} pip

In a terminal run:

```{code-block} bash
:caption: terminal
python -m pip install -U prompt-toolkit~=2.0
```

`````

::::::

```{seealso}

* [ipython/ipython#12049](https://github.com/ipython/ipython/issues/12049)
* [StackOverflow: Why do I get an 'Unhandled exception in event loop' error on ipython](https://stackoverflow.com/questions/59355904/why-do-i-get-an-unhandled-exception-in-event-loop-error-on-ipython)

```

