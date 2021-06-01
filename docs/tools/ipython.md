IPython
=======

Table of Contents
-----------------

* [Tip 1: quickref](#tip-1-quickref)
* [Tip 2: history](#tip-2-history)
* [Tip 3: history help](#tip-3-history-help)
* [Tip 4: save](#tip-4-save)


Tip 1: quickref
---------------

You can use the `%quickref` magic command to get a a quick introduction to
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


Tip 2: history
--------------

Use the `%history` magic command to see the all of the commands you typed in
your last ipython session. (Change the `~1` to `~2` go get the second to last,
and so on.) You can also use `%hist` for short.

You can use this to review everything you typed during data inspection
exercise.

```{code-block} ipython
---
caption: ipython shell
---
1>>> %history ~1/
import requests
response = requests.get("http://api.punkapi.com/v2/beers/random")
response.ok
response.status_code
response.reason
response.raise_for_status()
response.headers
...
```
Tip 3: history help
-------------------

You can add a `?` after the `%history` magic command to show detailed help
and usage information.


```{code-block} text
:caption: ipython shell
1>>> %history?
Docstring:
::

  %history [-n] [-o] [-p] [-t] [-f FILENAME] [-g [PATTERN [PATTERN ...]]] [-l [LIMIT]] [-u] [range [range ...]]

Print input history (_i<n> variables), with most recent last.
...
```

Tip 4: save
-----------

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


