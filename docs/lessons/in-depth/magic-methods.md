Magic methods
=============

When using the `dir()` function you may have noticed a bunch of members with
names surrounded by double underscores (`__`). These are special attributes
used internally by Python called {term}`magic methods <magic method>` or
{term}`special attributes <special attribute>`.

These are special methods used by some Python mechanism under the hood such as:

* **Types** -- some are called when the type of the same name is called. For
* example the `.__str__()` method is used by the
  `str()` function.
* **Functions** -- some are called when the builtin function of the same name
* is called. For example the `.__format__()` method is called by the
  `format()` function.
* **Operators** -- there are magic methods cooresponding to each operator. For
  example the `.__add__()` method is called by the `+` operator.
* **Statements** -- some statements call magic methods. For example when the
  `del` statement is used on an object attribute the `.__del__()` method is
  called.
* **Syntax** -- magic methods are called by some forms of syntax. For example
  `.__getattribute__()` is called when using dot notation.
* **Object information** -- information about the object is stored in
  {term}`special attributes <special attribute>` that are just like magic
  methods, but not callable. For example the `.__doc__` attribute contains the
  help documentation from the type {term}`docstring`. (Which is displayed when
  calling the `help()` function.)

Lets take a look at the members of an `object` instance. These are the magic
methods that are defined for all types.

```{code-block} python
:caption: Python shell
>>> dir(object())
['__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']
```

While magic methods are intended for internal use, there is nothing stopping
you from calling them directly.

Here are a few examples of normal Python code and the same thing via the
cooresponding magic method or special attribute.

{{ leftcol }}

```{code-block} python
>>> value = 1

>>> str(value)
'1'
```

```{code-block} python
>>> value == 2
False
```

```{code-block} python
>>> type(value)
int
```


{{ rightcol }}

```{code-block} python
>>> value = 1

>>> value.__str__()
'1'
```

```{code-block} python
>>> value.__eq__(2)
False
```

```{code-block} python
>>> value.__class__
int
```

{{ endcols }}

Different types have different magic methods and special attributes.

For example `int` and `float` objects have a number of math related magic
methods like `.__add__()` and `.__sub__()` which are called when the `+` and
`-` operators are used. Iterables like `list` and `dict` have a `.__len__()`
method is called by `len()` and a `.__contains__()` method which is called when
you use the `in` or `not in` operators.

While it's not important to understand special attributes until you start
learning [object oriented programming](oop.md), you may come across them from
time to time like when you call the `dir()` or `help()` functions. Python may
feel a lot less alien when you know why they're there.

You'll use magic methods when you start writing your own classes to specify how
Python code behaves with instances of your classes. For example, you can write
a `__mul__` method to define what happens when you use the `*` operator.

```{seealso}

* [Python.org > Special Method Names](https://docs.python.org/3/reference/datamodel.html#specialnames)
* [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/)
* [Python - Dunder or Magic Methods](https://www.alphacodingskills.com/python/pages/python-dunder-methods.php)
* [Python Dunder (Special, Magic) Methods List with Tutorial](https://holycoders.com/python-dunder-special-methods/)

```

Glossary
--------

```{glossary} magic-methods

dunder method
magic method
special method
  An method, beginning and ending with two underscores (`__`) intended to be
  used internally by Python.

special attribute
  An attribute beginning and ending with two underscores (`__`) that store
  object information intended to be used internally by Python. (Just like
  {term}`magic methods <magic method>` but not callable.)

```
