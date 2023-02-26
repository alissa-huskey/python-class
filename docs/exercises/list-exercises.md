List Exercises
==============

```{include} ../toc.md
```

Hand of Cards
-------------

`````{exercise} Hand of Cards
:label: hand-of-cards-exercise
1. Make a list of cards like: \
    `cards = ["7H", "QC", "2S", "AD", "3C"]`
2. Iterate over the list and print each card symbol with a space after it. \
    Hint: To print without adding a newline use `print(... end="")`

**OUTPUT**
```
    Your hand: 7H QC 2S AD 3C
```

`````

Make a table of contents
------------------------

`````{exercise} Make a table of contents
:label: toc-exercise

1. Make a list of chapters like:
```
  chapters = [
    "The Setup",
    "A Good First Program",
    "Comments And Pound Characters",
    "Numbers And Math"
  ]
```
2. Use the `enumerate()` function to iterate over the list and print each chapter number and title.

**OUTPUT**
```
  Table of Contents

  Chapter 1: The Setup
  Chapter 2: A Good First Program
  Chapter 3: Comments And Pound Characters
  Chapter 4: Numbers And Math
```

`````


Running Calculator
------------------

`````{exercise} Running Calculator
:label: running-calc-exercise

1. Make a list of numbers.
2. Iterate over the list. For each element:
  *  Add the element value to the running total.
  *  Print the value and the balance.

**OUTPUT**
```
            =  0
    + 8     =  8
    + 5     = 13
```

`````

Reformat Contact from CSV
-------------------------

`````{exercise} Reformat Contact from CSV
:label: reformat-contact-exercise

1. Start with the string: `"smith,john,415-555-5555"`
2. Split it into a list on `,` \
    Hint: To split on a different delimiter use `str.split(<delim>)`
3. Print the full name capitalized, then the phone number. \
    Hint: Access list elements with `varname[<index-number>]`

**OUTPUT**
```
    John Smith: 415-555-5555
```

`````

Column lengths
--------------

`````{exercise} Column lengths Exercise
:label: maxlengths-exercise

This exercise is to calculate the length of the longest value in each column.

Write a function that takes one argument `table` that should be a list of
equally sized lists. Each child list is a "row".

It should return a list the same size as the child rows, where each element is
length of the longest value (once converted to a string) in all rows in the
same position.

**Example Usage**

```python
>>> max_lengths([["a", "bb", "ccc"]])
[1, 2, 3]
>>> max_lengths([[628, 4, 82], [140, 59, 23]])
[3, 2, 2]
>>> max_lengths([['lend', 'job', 'when'], ['mail', 'walk', 'prove']])
[4, 4, 5]
```

**Solution template**

```{code-block} python
def max_lengths(table):
    """Return a list of the longest length of columns
       (when converted to strings)

    Arguments:
      table (list): list of equal length lists

    >>> max_lengths([["a", "bb", "ccc"]])
    [1, 2, 3]
    >>> max_lengths([[628, 4, 82], [140, 59, 23]])
    [3, 2, 2]
    >>> max_lengths([['lend', 'job', 'when'], ['mail', 'walk', 'prove']])
    [4, 4, 5]
    """
    pass
```

`````

`````{solution} maxlengths-exercise
:class: dropdown

```{literalinclude} ../../pythonclass/exercises/max_lengths.py
:caption: Column lengths Exercise
:class: full-width
:linenos:

`````

Columnize
---------

`````{exercise} Columnize
:label: columnize-exercise

This exercise is to format align a data into columns.

Write a function that takes one argument `table` that should be a list of
equally sized lists. Each child list is a "row".  It should return a string
where each line contains the text in one row, and the columns are aligned.

Note: This depends on the `max_lengths()` function from the
[Column lengths exercise](#column-lengths).

**Example Usage**

```python
>>> scores = [['Joe', 82], ['Billy', 59], ['Mary', 77]]
>>> text = columnize(scores)
>>> text
'Joe    82\nBilly  59\nMary   77'
>>> print(text)
Joe    82
Billy  59
Mary   77
```

**Solution template**

```{code-block} python
def columnize(table):
    """Return a string of aligned columns of text

    Arguments:
      table (list): list of equal length lists

    >>> columnize([['Joe', 82], ['Billy', 59], ['Mary', 77]])
    'Joe    82\\nBilly  59\\nMary   77'
    """
    # your code here
```

`````

`````{solution} columnize-exercise
:class: dropdown

```{literalinclude} ../../pythonclass/exercises/columnize.py
:caption: Columnize Exercise
:class: full-width
:linenos:

`````
