Objects
=======

Python has a special type `object` which is the ancestor to all types in
Python.

```{contents} Table of Contents
:backlinks: top
:local:
```

The object type by itself is not terribly useful. You can see that `object` is
a type and you can create an object instance just like you would with any
other type. But you can't really do much with an object instance.

```{code-block} python
:caption: Python shell
:class: full-width
>>> type(object)
type

>>> object()
<object at 0x1069a2540>
```

The reason it is interesting to talk about is that all data in Python is an
object, which you can test for yourself using the `isinstance()` function.
Just like cars, boats and bicycles are all vehicles, so are lists, strings, and
integers all objects. All data in Python is an object.

```{code-block} python
:caption: Python shell
:class: full-width
>>> isinstance("hello", object)
True

>>> isinstance(False, object)
True

>>> isinstance(100, object)
True
```

As such, the object type defines the characteristics shared by all classes and
instances, which is what we will be talking about in this lesson.

Shared traits
-------------

% TODO
% - [ ] mutability
% - [x] members
%       - [x] attributes
%       - [x] methods

### Members

Objects can have {term}`members <member>` which are accessed using
{term}`dot notation`.

You can think of {term}`dot notation` as reaching into an object using a dot.
Use a `.` after the object followed by the member name:
{samp}`{object}.{member}`. It is the same syntax used to access something
imported from a module, for example: `random.randint()`.

There are two kinds of members: attributes and methods.

#### Attributes

{term}`Attributes <attribute>`, sometimes called {term}`properties <property>`,
are just like variables but they are attached to an object and accessed using
{term}`dot notation`.

For example:

* both `int` and `float` objects have a `.real` property
* file objects have a `.mode` property

```{code-block} python
:caption: Python shell
>>> a_float = 1.0
>>> a_float.real
1.0

>>> a_int = 1
>>> a_int.real
1

>>> fh = open("hello.txt")
>>> fh.mode
'r'
```

If we try to access an attribute on an object that doesn't have it, we'll get
an `AttributeError`.

```{code-block} python
:caption: Python shell
>>> a_string = "1"
>>> a_string.real
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-27-a01766284dc5> in <module>
----> 1 a_string.real

AttributeError: 'str' object has no attribute 'real'
```

#### Methods

A method is a just like a function, but one that is attached to an object and
accessed through {term}`dot notation`.

For example:

* `str` objects have a method `.isnumeric()` which returns `True` if
  all its characters are numbers and `False` otherwise.
* `float` objects have a method `.is_integer()` which returns `True` if it is a
  whole number and `False` otherwise.
* `int` objects have a method `.bit_length()` which returns length of the
  number in binary.
* file objects have a `.read()` method which returns a string containing the
  text from the file

```{code-block} python
:caption: Python shell
>>> a_string = "1"
>>> a_string.isnumeric()
True

>>> a_float = 1.0
>>> a_float.is_integer()
True

>>> a_int = 1
>>> a_int.bit_length()
1

>>> fh.read()
'Hello python class!\n'
```

Just like with attributes, if we try to call a method on an object that doesn't
have it we'll get an `AttributeError`.

```{code-block} python
:caption: Python shell
:class: full-width
>>> a_int.isnumeric()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-50-789c44c0b36c> in <module>
----> 1 a_int.isnumeric()

AttributeError: 'int' object has no attribute 'isnumeric'
```

```{tip}
Methods are technically just attributes that can be called. That is why, for
example, we see an `AttributeError` when trying to call a method on an object
that doesn't have it.

For clarity I use the term {term}`property` when referring to attributes that
are not callable.
```

% TODO
% [ ] accessing attributes on raw values or any kind of expression

#### Listing members

You can use the `dir()` function to see a list of the members an object has.
(The ones that start and end with double underscores (`__`) are special
internal methods that are used by Python under the hood, so you can disregard
those for now.)

```{code-block} python
:caption: Python shell
>>> dir(a_int)
['__abs__',
 '__add__',
 '__and__',
 ...
 'as_integer_ratio',
 'bit_length',
 'conjugate',
 'denominator',
 'from_bytes',
 'imag',
 'numerator',
 'real',
 'to_bytes']
```

In a Python shell you can also use the `help()` function on a type to get
detailed help on that type. You can also usually pass a value to `help()` to
get the help page for that type.

Long help documents will be opened in pager mode where you can use the arrow
keys to scroll. To exit the help document and return to your normal Python
shell press {kbd}`Q` or just scroll to the end of the document.

```{code-block} python
:caption: Python shell
>>> help(int)
Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 ...

>>> help(1)
Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 ...

```

In VS Code, you can hit {kbd}`⌃Space`, {kbd}`Alt+Escape`, or {kbd}`⌘I` after a
variable followed by a `.` to get a list of available members. Then you can use
the {kbd}`UP` and {kbd}`DOWN` arrows to navigate between the options and hit
{kbd}`ENTER` to fill in the selected name.

![](assets/vscode-attrs.png)

And in `ipython` you can hit {kbd}`TAB` after a variable followed by a `.` to
get a list of available members.  Then you can use the {kbd}`UP` and
{kbd}`DOWN` arrows or {kbd}`SHIFT+TAB` and {kbd}`TAB` to navigate between the
options and hit {kbd}`ENTER` to fill in the selected name.

![](assets/ipython-attrs.png)


#### Checking members

You can use the function `hasattr()` to check if an object has a particular
member. The first argument is the value you want to check, the second argument
is the name of the member, a `str`.

```{code-block} python
:caption: Python shell
>>> hasattr(a_float, "is_integer")
True

>>> hasattr(a_float, "real")
True

>>> hasattr(a_str, "real")
False
```

You can then use the `callable()` function to find out if a member is method
(if returns `True`) or a property (if it returns `False`).

```{code-block} python
:caption: Python shell
>>> callable(a_int.to_bytes)
True

>>> callable(a_int.imag)
False
```

#### Exercise

```{exercise} methods and attributes
:label: methods-and-attributes-exercise
1. In a VS Code editor, use the {kbd}`⌘I`, {kbd}`Alt+Escape`, or {kbd}`⌃Space`
   shortcut keys after an `int` variable to find the method that will return an
   integer ratio.
2. If you use `ipython`, use the {kbd}`TAB` key after a `float` variable to find the
   method that will return a hexadecimal representation of the number.
3. In a Python shell use the `dir()` function on a `str` value to find the method
   to right justify the string.
4. In a Python shell use the `help()` function on a `dict` type or value to
   find the method to remove specified key and return the corresponding value.
5. In a Python shell use the `hasattr()` function on a `list` value to find out
   if it has a method or attribute named `clear`.
6. In a Python shell use the `callable()` function on a `dict` value to find out
   if `values` is a method or a property.
```
### Functions

Functions and methods usually expect certian types of arguments, and you'll run
into some kind of error if you try to pass the wrong type.

However, there are some functions that any object can be passed to:

* {samp}`callable({object})` -- return `True` of `object` is callable.
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> callable(dir)
  True

  >>> callable(str)
  True

  >>> fh = open("hello.txt")
  >>> callable(fh.close)
  True

  >>> callable(fh.mode)
  False
  ```
* {samp}`dir({object})` -- return a list of the member names belonging to `object`.
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> dir(1)
  ['__abs__',
   '__add__',
   '__and__',
   ...
   'as_integer_ratio',
   'bit_length',
   'conjugate',
   'denominator',
   'from_bytes',
   'imag',
   'numerator',
   'real',
   'to_bytes']
  ```
* {samp}`hasattr({object}, {name})` -- return `True` if `object` has member `name`.
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> fh = open("hello.txt")
  >>> hasattr(fh, "close")
  True

  >>> hasattr(fh, "size")
  False
  ```
* {samp}`id({object})` -- return the unique identifier of `object`. \
  Used by the `is` operator to test if two values reference the same object in
  memory.
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> a = [1, 2, 3]
  >>> b = a
  >>> c = [1, 2, 3]

  >>> id(a)
  4418273088

  >>> id(b)
  4418273088

  >>> id(c)
  4410044608
  ```
* {samp}`isinstance({object}, {class(es)})`
  -- return `True` if an object is an instance of `class` (or any of a tuple of
  `classes`) or one of its subclasses.
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> isinstance("hello", str)
  True

  >>> isinstance("hello", object)
  True

  >>> isinstance("hello", int)
  False

  >>> isinstance(False, bool)
  True

  >>> isinstance(100, int)
  True

  >>> isinstance("hello", (str, int))
  True

  >>> isinstance("hello", (int, float))
  False
  ```
* {samp}`repr({object})` -- return a string representation of `object`,
  intended as an unambiguous debugging information for developers.  Often the
  string is either verbatim code that will create an equivalent object, or `<`
  `>` (angle brackets) surrounding the class name followed by meaningful
  identifying information. \
  This is used by the Python Shell to display the results of an expression.
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> print(repr("hello"))
  'hello'

  >>> print(repr([1, 2, 3]))
  [1, 2, 3]

  >>> from pathlib import Path
  >>> path = Path("hello.txt")
  >>> print(repr(path))
  PosixPath('hello.txt')

  >>> fh = open("hello.txt")
  >>> print(repr(fh))
  <_io.TextIOWrapper name='hello.txt' mode='r' encoding='UTF-8'>
  ```
* {samp}`type({object})` -- return the `object` type.
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> type(False)
  bool

  >>> type(0)
  int

  >>> type("5.5")
  str
  ```
* {samp}`str({object})` -- return `object` converted to a string, intended as a
  human readable text for the end user. \
  `str` is technically a class rather than a function and calling it
  converts `object` to a `str`, but included here for comparison with the
  `repr()` function. \
  Used by the `print()` function to convert all arguments before printing.
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> print(str("hello"))
  hello

  >>> print(str([1, 2, 3]))
  [1, 2, 3]

  >>> from pathlib import Path
  >>> path = Path("hello.txt")
  >>> print(str(path))
  hello.txt
  ```

Magic methods
-------------

When using the `dir()` function you may have noticed a bunch of members with
names surrounded by double underscores (`__`). These are are special methods
used internally by Python called
{term}`magic <magic method>` or {term}`dunder methods <dunder method>`.
Each one cooresponds some under the hood Python mechanism.

Lets take a look at the members of an object instance.

```{code-block} python
:caption: Python shell
:class: full-width
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

Before you read on, can you guess what any of these coorespond to? I'll wait.

...

...

...

Welcome back.

{term}`Magic methods <magic method>` may coorespond to:

* **Types** -- when named one of the standard built in types, this method is
  called by that type. For example the `.__str__()` method is used by the
  `str()` function.
* **Functions** -- when named one of the built in functions, this method is
  called by that function. For example the `.__dir__()` method is called by the
  `dir()` function.
* **Operators** -- there are magic methods cooresponding to each operator. For
  example the `.__add__()` method is called by the `+` operator.
* **Statements** -- some statements call magic methods. For example when the
* `del` statement is used on an object attribute the `.__del__()` method is
  called.
* **Syntax** -- magic methods are called by some forms of syntax. For example
  `.__getattribute__()` is called when using dot notation.
* **Object information** -- information about the object is stored in
  {term}`special attributes <special attribute>` that are just like magic
  methods, but not callable. For example the `.__class__` attribute contains
  the object type, the same thing returned by the `type()` function.

While magic methods are intended for internal use, there is nothing stopping
you from calling them directly.

```{code-block} python
:caption: Python shell
:class: full-width
>>> a_int = 1
>>> a_int.__str__()
'1'

>>> str(a_int)
'1'

>>> a_int.__add__(2)
3

>>> a_int.__class__
int

>>> type(a_int)
int
```

There are quite a few magic methods and special attributes and they differ
depending on the type.  Don't worry, you don't need to memorize them.  However
it can be useful to understand the general concept, as magic methods and
special attibutes can tell you a lot about an objects capabilities.

```{seealso}

* [Python.org > Special Method Names](https://docs.python.org/3/reference/datamodel.html#specialnames)
* [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/#operators)
* [Python - Dunder or Magic Methods](https://www.alphacodingskills.com/python/pages/python-dunder-methods.php)
* [Python Dunder (Special, Magic) Methods List with Tutorial](https://holycoders.com/python-dunder-special-methods/)

```

Summary
-------

* Objects can have members which are accessed using {term}`dot notation` --
  adding a `.` after the object followed by the member name. Members can either
  be attributes, which are just like variables, or methods which are just like
  functions.
* The `callable()` function will return `True` for things that can be called
  like methods, functions and classes, `False` otherwise.
* You can find out what members a value has:
  - in IPython after a variable followed by a `.` by hitting {kbd}`TAB`
  - in VS Code after a variable followed by a `.` by using the {kbd}`⌘I` or {kbd}`⌃Space` keyboard shortcuts
  - by using the `dir()` or `hasattr()` functions
* There are a number of built in functions that any object can be passed to
  like `repr()` and `type()`.
* Internally Python calls an objects magic methods, those with names surrounded
  by double underscores, to preform many operations. Looking at the magic
  methods using the `dir()` function can tell you how a particular object can be used.

Glossary
--------

```{glossary} data-types
attribute
property
  A variable that is attached to an object and is accessed with a `.` after a
  value followed by the member name. For example, {term}`file handler` objects
  have an attribute `.closed` which is set True if the handler is closed and
  False if it is open.

dot notation
  Accessing an object member using a `.` after the object followed by the
  member name: {samp}`{object}.{member}`. It is the same syntax used to access
  something imported from a module, for example: `random.randint()`.

dunder method
magic method
special method
  An method, beginning and ending with two underscores (`__`) intended to be
  used internally by Python.

member
  An attribute or method attached to an object accessed with a `.` after a
  value followed by the member name

method
  A function that is attached to an object and is accessed with a `.` after a
  value followed by the member name. For example, string objects have a `.lower()`
  method which returns a copy of the string converted to lowercase.

object
  Synonym for {term}`instance`.

  The type that all other Python types are built on.

special attribute
  An attribute beginning and ending with two underscores (`__`) that store
  object information intended to be used internally by Python. (Just like
  {term}`magic methods <magic method>` but not callable.)


```
