Dictionaries
============

Creating
--------

```python
mydict = {'k':"v"}                                             # creating with {}
mydict = dict('k':"v")                                         # creating with dict()
mydict = dict(k="v")                                           # creating with dict() using keyword notation
```

Accessing Elements
------------------

```python
mydict['k']                                                    # accessing elements
mydict.get('a', None)                                          # accessing elements without missing key errors
```

Changing Elements
-----------------

```python
mydict['x'] = "y"                                              # assignment
mydict.update({'k':"v"})                                       # bulk appending / modification
del mydict['k']                                                # deleting elements
mydict.pop('k', "valifmissing")                                # deleting elements without missing key errors
mydict.popitem()                                               # delete the last item and return (k, v)
```

Checking Membership
-------------------

mydict.has_key('k')                                            # check for key membership using has_key()
'somekey' in mydict                                            # check for key membership using in
'someval' in mydict.values()                                   # check for value membership

Iteration
---------

```python
for k in mydict:                                               # iterating through values
for k, v in mydict.items():                                    # iterating through keys and values
```

Ordering
--------

```python
sorted(mydict)                                                 # returns a sorted list of mydict.keys()
sorted(mydict.items(), key=lambda x: x[1])                     # sort by value, return a list of tuples
{ k: v for (k, v) in sorted(d.items(), key=lambda x: x[1]) }   # create a new dict sorted by value
```

Printing
--------

```python
print("%(first_name) %(last_name)" % person)                   # unpack keys from dict
```

```python
mydict = {**dict1, **dict2}                                    # joining through unpacking
len(mydict)                                                    # length
any(mydict.values())                                           # if any value is True
any(mydict)                                                    # if any key or value is True  (probably not desired)
mydict = { (5, 10): "a", (3,5): "b" }                          # using tuples as keys
{x: x**2 for x in (2, 4, 6)}                                   # creating using dict comprehensions
dict(zip("a b c d e f".split(), range(0, 6)))                  # creating using dict() and zip()
dict(map(lambda x: (x[0].upper(), x[1]), mydict.items() ))     # create a new dict where keys are upper()
```

