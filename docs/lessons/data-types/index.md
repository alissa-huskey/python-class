Data Types
==========

Every piece of data in Python has a type. You can think of a data type kind of
like its job title.

![](../assets/hats.jpg)

Knowing the data type of a value will tell you what it has,
what it can do, and where it can be used.

The type controls:

* what methods are available
* what attributes are available
* what operators it has access to and how they behave
* which functions it can be used with

To demonstrate this, lets compare an `int`, a `float` and a `str`.

```{code-block} python
>>> a_int = 1
>>> a_float = 1.0
>>> a_string = "1"
```

Finding out the type
--------------------

We can find out the type of any value by using the `type()` function.

```{code-block} python
>>> type(a_int)
int

>>> type(a_float)
float

>>> type(a_string)
str
```

Methods
-------

A method is a just like a function, but one that is attached to an object.

Calling a method is just like calling a function, except that it goes after the
object that it belongs to with a `.` between the object and the method.

For example:

* `str` objects have a method `.isnumeric()` which returns `True`
  all its characters numbers and `False` otherwise.
* `float` objects have a method `.is_integer()` which returns True if it is a
  whole number and `False` otherwise.
* `int` objects have a method `.bit_length()` which returns the number of bits
  needed to store the number.

```{code-block} python

>>> a_string.isnumeric()
True

>>> a_float.is_integer()
True

>>> a_int.bit_length()
1

```

If we try to call a method on the wrong type, we'll get an error.


```{code-block} python

>>> a_int.isnumeric()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-117-789c44c0b36c> in <module>
----> 1 a_int.isnumeric()

AttributeError: 'int' object has no attribute 'isnumeric'

```

Attributes
----------

Attributes, otherwise known as properties, are just like variables, but they
are attached to an object.

For example, both `int` and `float` objects have a `.real` property.

```{code-block} python

>>> a_float.real
1.0

>>> a_int.real
1

```

Operators
---------

Depending on the type of an object it may have different operators available to
it, those operators may behave in different ways, and there may or may not be
other types that it can play nicely with for a particular operator.

Lets take a look at how the `+` operator works for different types.

In the case of both `int` and `float` objects, the `+` operator adds the two
numbers together. However, in the case of a `str` object, strings are
concatenated.

```{code-block} python

>>> a_int + 1
2

>>> a_float + 1
2.0

>>> a_string + "1"
'11'

```

`int` and `float` objects can be used together with the `+` operator. However,
if we try to use the `+` with a `str` object and either an `int` or a `float`,
we'll get an error.


```{code-block} python

>>> a_int + a_float
2.0

>>> a_int + a_string
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-133-4eab260b045c> in <module>
----> 1 a_int + a_string

TypeError: unsupported operand type(s) for +: 'int' and 'str'


```


```{code-block} python
>>> len(a_int)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-71-8e7674750017> in <module>
----> 1 len(a_int)

TypeError: object of type 'int' has no len()

>>> len(a_float)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-72-8b34fc9d0fe7> in <module>
----> 1 len(a_float)

TypeError: object of type 'float' has no len()

>>> len(a_string)
```

Objects
-------

The Python {term}`object` is the ancestor to all types in Python, and all types
share a few features.

All objects can have:

* methods
* attributes










Classes
-------

A class is like a blueprint for a particular data type and in Python, the
terms "type" and "class" are synonyms.


TODO
----

% what is a type?
% - [ ] class

% what a difference a type makes
% - [x] attributes / properties
% - [x] methods
% - [x] operators
% - [ ] functions

% finding out a type
% - [ ] type
% - [ ] isinstance

% - [ ] ipython
% - [ ] vs code
% - [ ] help
% - [ ] dir


% - [ ] repr
% - [ ] str

% primitive types
% - [ ] None
% - [ ] bool


