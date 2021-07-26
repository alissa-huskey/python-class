Dictionaries
============

```{contents} Table of Contents
:backlinks: top
:local:
```

Creating
--------

Creating with `{` `}`:

```python
mydict = {'k':"v"}
```

Creating with `dict()`:

```python
mydict = dict('k':"v")
```

Creating with `dict()` using keyword notation:

```python
mydict = dict(k="v")
```

Selecting
---------

Accessing elements:

```python
mydict['k']
```

Accessing elements without missing key errors:

```python
mydict.get('a', None)
```

Modification
------------

### Adding & Changing

Assignment:

```python
mydict['x'] = "y"
```

Bulk appending / modification:

```python
mydict.update({'k':"v"})
```

### Removing

Deleting elements:

```python
del mydict['k']
```

Deleting elements without missing key errors:

```python
mydict.pop('k', "valifmissing")
```

Delete the last item and return `(k, v)`:

```python
mydict.popitem()
```

Membership
----------

Check for key membership using `.has_key()`:

```python
mydict.has_key('k')
```

Check for key membership using in:

```python
'somekey' in mydict
```

Check for value membership:

```python
'someval' in mydict.values()
```

Joining through unpacking:

```python
mydict = {**dict1, **dict2}
```

Iteration
---------

Iterating through values:

```python
for k in mydict:
```

Iterating through keys and values:

```python
for k, v in mydict.items():
```

Sorting
--------

Returns a sorted list of `mydict.keys()`:

```python
sorted(mydict)
```

Sort by value, return a list of tuples:

```python
sorted(mydict.items(), key=lambda x: x[1])
```

Create a new dict sorted by value:

```python
{ k: v for (k, v) in sorted(d.items(), key=lambda x: x[1]) }
```

Printing
--------

Unpack keys from dict:

```python
print("%(first_name) %(last_name)" % person)
```

Aggregation
-----------

Length:

```python
len(mydict)
```

If any value is True:

```python
any(mydict.values())
```

If any key or value is True  (probably not desired):

```python
any(mydict)
```

Misc
----

Using tuples as keys:

```python
mydict = { (5, 10): "a", (3,5): "b" }
```

Creating using dict comprehensions:

```python
{x: x**2 for x in (2, 4, 6)}
```

Creating using `dict()` and `zip()`:

```python
dict(zip("a b c d e f".split(), range(0, 6)))
```

Create a new dict where keys are `upper()`:

```python
dict(map(lambda x: (x[0].upper(), x[1]), mydict.items() ))
```

