Data Types
==========

Just like any other tool, understanding what kind of data you are dealing with
at any given time means understanding what it can do and where it can go.

Think about vehicles. A pickup truck has a flatbed that is good for moving
things, whereas a minivan is better for ferrying a group of people around. A
bicycle might be a good way to get to places close to home, but you be in
trouble if you tried to take a bicycle out sailing when what you need is a
boat.

So it is with data. Every piece of data has a type and that type dictates
things like what methods and attributes it has, what functions it can be passed
to, and what other types of data it can play nicely with.

Classes
-------

In modern Python the terms {term}`type` and {term}`class` are more or less
synonymous.

A class is like a blueprint for that type. You can call a class the same way
you call a function. When you do an empty object of that type will be returned.

Lets look at what happens when we call some of the built in type classes that
we are already familiar with.

```{code-block} python
:caption: Python shell
>>> float()
0.0
>>> int()
0
>>> str()
''
>>> list()
[]
```

Classes may also take arguments. For example, most of the built in type classes
can be used to convert a value to its type. This is called {term}`typecasting`.

```{code-block} python
:caption: Python shell
>>> str(5.0)
'5.0'

>>> float(5)
5.0

>>> int(5.25)
5

>>> list("hello")
['h', 'e', 'l', 'l', 'o']
```

Not all types can be converted to all other types though.

```{code-block} python
:caption: Python shell
>>> dict(5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-2e3c53b6b812> in <module>
----> 1 dict(5)

TypeError: 'int' object is not iterable
```

Sometimes you may need to convert to another type first to get the desired
results. For example, lets say we want a list with all of the digits in
`32562`. An `int` cannot be converted to a `list`. Instead, convert it to a
`str` first, then convert each of the digits back to an `int`.

```{code-block} python
:caption: Python shell
>>> list(32562)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-46-947a2aee1ed3> in <module>
----> 1 list(32562)

TypeError: 'int' object is not iterable

>>> str(32562)
'32562'

>>> list(str(32562))
['3', '2', '5', '6', '2']

>>> digits = list(str(32562))
>>> for i, num in enumerate(digits):
        digits[i] = int(digits[i])

>>> digits
[3, 2, 5, 6, 2]
```

### Exercise

```{exercise} classes
:label: classes-exercise

Do each of the following in a Python shell.

1. Use the type classes to create new empty objects for each of the following:
   - `bool`
   - `int`
   - `float`
   - `str`
   - `dict`
   - `list`
   - `tuple`
2. Convert data types of one type to another. Here are some
   to start with, but feel free to come up with your own
   combinations.
   - `"5"` to `int`
   - `5` to `str`
   - `5` to `bool`
   - `5` to `float`
   - `5.0` to `int`
   - `5.25` to `int`
   - `"5.25"` to `int`
   - `5` to `list`
   - `[1, 2, 3]` to `tuple`
   - `(1, 2, 3)` to `dict`
   - `{'a': '1', 'b': '2', 'c': '3'}` to `list`

```

`````{solution} classes-exercise
:class: dropdown

```{code-block} python
:caption: "#1"
>>> bool()
False

>>> int()
0

>>> float()
0.0

>>> str()
''

>>> dict()
{}

>>> list()
[]

>>> tuple()
()
```

```{code-block} python
:caption: "#2"
>>> int("5")
5

>>> str(5)
'5'

>>> bool(5)
True

>>> float(5)
5.0

>>> int(5.0)
5

>>> int(5.25)
5

>>> int("5.25")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-63-12a4bd2b0343> in <module>
----> 1 int("5.25")

ValueError: invalid literal for int() with base 10: '5.25'

>>> int(float("5.25"))
5

>>> list(5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-64-0c7f5cd48ec1> in <module>
----> 1 list(5)

TypeError: 'int' object is not iterable

>>> tuple([1, 2, 3])
(1, 2, 3)

>>> dict((1, 2, 3))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-66-237d7a195025> in <module>
----> 1 dict((1, 2, 3))

TypeError: cannot convert dictionary update sequence element #0 to a sequence

>>> list({'a': '1', 'b': '2', 'c': '3'})
['a', 'b', 'c']
```

`````

Finding out the type
--------------------

We can find out the type of any value by using the `type()` function.

```{code-block} python
:caption: Python shell
>>> type(5)
<class 'int'>

>>> type(2.5)
<class 'float'>

>>> type("hello")
<class 'str'>
```

You can also check if a value is a particular type by using the `isinstance()`
function. The first argument is the value you want to check, and the second
argument is a type, or tuple of types, that you want to check it against.

```{code-block} python
:caption: Python shell
>>> isinstance("5", int)
False

>>> isinstance(5.0, float)
True

>>> isinstance(5, (int, float))
True
```

### Exercise

```{exercise} classes
:label: type-checking-exercise

Do each of the following in a Python shell.

1. Use the `type()` function on the following values, then come up with some of your own.
   - `False`
   - `None`
   - `"1"`
   - `5.0`
   - `[1, 2, 3]`
2. Use the `isinstance()` function to check the following, then come up with
   some of your own.
   - is `"5"` a `str`
   - is `5` an `int`
   - is `[1, 2, 3]` a `list` or a `tuple`
   - is `0` a `bool`

```

`````{solution} classes-exercise
:class: dropdown

```{code-block} python
:caption: "#1"
>>> type(False)
bool

>>> type(None)
NoneType

>>> type("1")
str

>>> type(5.0)
float

>>> type([1, 2, 3])
list
```

```{code-block} python
:caption: "#2"
>>> isinstance("5", str)
True

>>> isinstance(5, int)
True

>>> isinstance([1, 2, 3], (list, tuple))
True

>>> isinstance(0, bool)
False
```

`````

