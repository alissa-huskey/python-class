Richter scale
=============

Write a `quake_desc` function that takes one argument: `magnitude`, a number.
return the description associated with the magnitude, as shown in the table
below.

| Min       | Max  | Description           |
|-----------|------|-----------------------|
| 0         | `>` 2  | micro               |
| 2         | `>` 3  | very minor          |
| 3         | `>` 4  | minor               |
| 4         | `>` 5  | light               |
| 5         | `>` 6  | moderate            |
| 6         | `>` 7  | strong              |
| 7         | `>` 8  | major               |
| 8         | `>` 10 | great               |
| 10        | `*`    | meteroic            |


```python
def quake_desc(magnitude):
    """Return the description for a magnitude

    >>> quake_desc(0.2)
    'micro'

    >>> quake_desc(2.5)
    'very minor'

    >>> quake_desc(5)
    'moderate'

    >>> quake_desc(11)
    'meteroic'
    """
```

Running with doctest
--------------------

You can test that the examples in your docstrings to ensure that the function
returns the expected results using the doctest module.

Run it at the command line with the syntax

```console
$ python -m doctest -v FILEPATH
```

Replace FILEPATH with the path to your python file.

Here are a couple of examples:

```console
$ python -m doctest -v funcs.py
$ python -m doctest -v myproject/funcs.py
```


