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

Dictionaries
============

{{ leftcol | replace("col", "col-8")  }}

A collection of *key: value* pairs.

```{contents} Table of Contents
:backlinks: top
:local:
```

{{ rightcol | replace("col", "col-4 text-right") }}

:::{fieldlist}

:Type:        `dict`
:Synatx:      {samp}`\{{item},...\}`
:Bases:       Mapping
:State:       Mutable
:Position:    Ordered
:Composition: Heterogeneous
:Diversity:   Repeatable
:Access:      Subscriptable
:Value:       Not hashable

:::

{{ endcols }}

Basics
------

A dictionary is a collection of key value pairs. Each key is connected to a
value, which makes them a handy way to look up a particular value.

### Creating

To create a dictionary, enclose comma-seperated key value pairs in curly braces
`{` `}` with a `:` between each key and value.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

book = {
  "title": "Last Chance to See",
  "author": "Douglas Adams",
  "year": 1990,
}
```

### Accessing

Items are accessed via {term}`subscription`, using `[` `]` after the object to
enclose the key.

```{code-cell} python
:class: full-width
print("Title:", book["title"])
print("Author:", book["author"])
print("Published:", book["year"])
```

If you try to access a key that does not exist, you will encounter a
`KeyError`.

```{code-cell} python
:class: full-width
:tags: [raises-exception]

print("Series:", book["series"])
```

However, you can avoid this using the `.get()` method, which two arguments: the
key, and an optional default value.

```{code-cell} python
:class: full-width
:tags: [raises-exception]

series = book.get("series", "NA")
print("Series:", series)
```

### Modifying

Adding or changing elements in the list is done the same way, also using subscription.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

from pprint import pprint

book["genre"] = "Nonfiction"
book["author"] = "Douglas Adams, Mark Carwardine"

pprint(book)
```

You can also change multiple elements at once using the `.update()`
method, which takes one argument, a dictionary. Any keys already present in the
original dictionary will be changed, and any not in the original dictionary
will be added. The remaining elements will be left as they are.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

book.update({"isbn": "0345371984", "genre": "Science", "pages": 256})

pprint(book)
```

### Removing

To remove elements you can use the `del` keyword.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

del book["pages"]

pprint(book)
```

You can also use the `.pop()` method, which returns the deleted element. It has
the added benefit that you can pass it a default value to avoid a `KeyError`
exception.

```{code-cell} python
:class: full-width
:tags: [thebe-init]

format = book.pop("format", "Unknown")
pprint(book)
```

### Exercise

`````{exercise} Word calculator
:label: word-calculator-exercise

Make a dictionary of numbers where the keyword is a word (like `"one"`) and the
value is an integer (like `1`). Assign it to the variable `numbers`.

Write an `add()` function that takes two string arguments, adds together the
value in the `numbers` dictionary associated with those keys, and returns the
result.

**Example Usage**

``` python
>>> add("one", "three")
4
```

**Solution template**

```python
def add(a, b):
  """Add the value of two number strings.

  >>> add("one", "three")
  4
  """
```


`````

`````{solution} word-calculator-exercise
:class: dropdown

```{code-block} python
:caption: Name Exercise
:class: full-width
:linenos:

numbers = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "ten": 10,
}

def add(a, b):
  """Add the value of two number strings.

  >>> add("one", "three")
  4
  """
  return numbers[a] + numbers[b]
`````


% TODO
% [ ] ordered version 3.7+
% [ ] values that can be used as keys
% [ ] no duplicate keys, but duplicate values
% [x] creating
% [x] accessing
%     [x] with key
%     [x] get
% [x] removing
%     [x] pop
%     [x] del
% [ ] values
% [ ] iteration
% [ ] membership
%     [ ] keys
%     [ ] values
% [ ] exercise
