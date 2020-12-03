Lists
=====


Table of Contents
-----------------

* [Creating](#creating)
* [Accessing Elements](#accessing-elements)
* [Changing Elements](#changing-elements)
* [Checking Membership](#checking-membership)
* [Iteration](#iteration)
* [Ordering](#ordering)
* [List Information](#list-information)
* [Copying](#copying)
* [Transformation](#transformation)
* [Convert To List](#convert-to-list)
* [Convert From List](#convert-from-list)


Creating
--------

```python
mylist = list()                           # create an empty list
mylist = []                               # create an empty list
mylist = [1, 2, 3]                        # create a list with elements 1, 2 and 3
```

Accessing Elements
------------------

```python
# by index address
mylist[0]                                 # first element value
mylist[1]                                 # second element value
mylist[-1]                                # last element value
# by slice
mylist[1:3]                               # slice of the list, starting at
mylist[1:]                                # slice of the list except for the first element
mylist[:-1]                               # slice of the list except for the last element
mylist[3:6:2]                             # slice with every other element between mylist[3] and mylist[6]
# by value
mylist.index("bacon")                     # get the index number of value "bacon"
```

Changing Elements
-----------------

```python
# set value
mylist[0] = "eggs"                        # set value by index
mylist[2:4] = [ "eggs", "bread" ]         # set value by slice

# add element(s)
mylist.insert(0, "pancakes")              # add element at index 0 (the beginning of the list)
mylist.append("tacos")                    # add an element to the end of the list
mylist.extend([4,5,6])                    # add all elements to the end of the list
mylist + [7,8,9]                          # add all elements to the end of the list
mylist * 3                                # a list that contains the contents of mylist repeated three times

# remove element(s)
del mylist[2]                             # remove an element by index
del mylist[2:4]                           # remove element by slice
mylist.remove("bacon")                    # remove element by element
mylist.pop()                              # remove and return the last element
mylist.clear()                            # remove all elements
```

Checking Membership
-------------------

```python
val in mylist                             # check if list contains val
```

Iteration
---------

```python
for elm in mylist:                        # iterate over each element value
for i, elm in enumerate(mylist):          # iterate over each index number and element value
```

Ordering
--------

```python
mylist = [2,4,1,3,5]
mylist.sort()                             # [1,2,3,4,5] sort values in ascending order in-place (returns None)
mylist.sort(reverse=True)                 # [5,4,3,2,1] sort values in decending order in-place (returns None)
mylist.reverse()                          # [5,3,1,4,2] reverse order of values in-place (returns None)
mylist.sort(key=lambda v:len(v))          # sort values by lambda function results in-place (returns None)
sorted(mylist)                            # [1,2,3,4,5] return list with contents of mylist in ascending order
sorted(mylist, reverse=True)              # [5,4,3,2,1] return list with contents of mylist in decending order
list(reversed(mylist))                    # [5,3,1,4,2] return list with contents of mylist in reverse order
sorted(mylist, key=lambda v: len(v))      # return list sorted by lambda function results
```

List Information
----------------

```python
len(mylist)                               # list length
max(mylist)                               # maximum value in list
min(mylist)                               # maximum value in list
mylist.count("purple")                    # number of times value occurs in list

sum(mylist)                               # sum of all list values
```

Copying
-------

```python
mylist = otherlist                        # create a reference to otherlist
mylist = otherlist.copy()                 # create a new list with references to the contents of otherlist
mylist = otherlist[:]                     # create a new list with references to the contents of otherlist
mylist = copy.deepcopy(otherlist)         # create a new list with the contents of otherlist
```

Transformation
--------------

```python
[ int(x) for x in mylist ]                # list comprehension: mapping
[ x for x in mylist if x ]                # list comprehension: filtering
map(int, mylist)                          # mapping
```

Convert To List
---------------

```python
# from string
list("abc")                               # ['a', 'b', 'c']
"list info search".split()                # ['list', 'info', 'search']
re.split(r"[./]", "github.com/git")       # ['github', 'com', 'git']

# from dict
list(mydict)                              # values
list(mydict.values())                     # values
list(mydict.keys())                       # keys
```

Convert From List
-----------------

```python
"".join(mylist)                          # to string
dict([("a", 1), ("b", 2)])               # to dict
```
