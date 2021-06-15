Numeric Types
=============

Nearly every program uses numbers at some point, whether you are keeping track
of a game score or doing calculations for graphics.

Numbers are {term}`primitive data types <primitive data type>`, meaning they
are the basic building blocks that make up other types.

Python provides four numeric types:

| Name       | Type       | Description            | Example |
|------------|------------|------------------------|---------|
| Integer    | `int`      | whole numbers          |  `1`    |
| Float      | `float`    | floating point numbers |  `1.0`  |
| Boolean    | `bool`     | `True` or `False`      |  `True` |
| Complex    | `complex`  | imaginary numbers      |  `1+1j` |

More on each of these later, but first lets take a look at how numbers in
Python are alike.

% Numeric objects are immutable, which means when an object is created its value
% cannot be changed.

% numbers.Number

% [ ] immutable

Common traits
-------------

All numeric types are based on the `numbers.Number` class, so they have some
things in common.

They can be positive or negative.

```{code-block} python
:caption: Python shell
:class: full-width
>>> -5
-5

>>> +5.0
5.0

>>> -3+5j
(-3+5j)
```

They almost always play nicely together--they can be compared to one another,
used interchangably with most operators, and converted into one another.

```{code-block} python
:caption: Python shell
:class: full-width
>>> .5 < 5
True

>>> 5 - 0.5
4.5

>>> 1 + True
2

>>> 22 + .5
22.5

>>> 1.25 + 3+2j
(4.25+2j)

>>> int(3.5)
3

>>> float(False)
0.0

>>> bool(2)
True

>>> complex(42)
(42+0j)
```


Underscores (`_`) can be used as a delimiter to group digits for better
readability.[^python3.6] This is usually used to indicate thousands, but in
fact underscores can be used anywhere between digits.

```{code-block} python
:caption: Python shell
:class: full-width
>>> 1_000_000
1000000

>>> 0.001_001
0.001001

>>> 1_1_1_1
1111

>>>  3.14_15_93j
3.141593j
```

[^python3.6]: Python 3.6+

### Operators

The following operators are available to all numeric types.

#### Unary sign operators

| Sign | Meaning                | Example |
|------|------------------------|---------|
| `-`  | negative               | `-1`    |
| `+`  | positive or unchanged  | `+1`    |

#### Arithmetic operators

| Sign | Meaning                      | Example           |
|------|------------------------------|-------------------|
| `+`  | addition                     | `1+2`             |
| `-`  | subtraction                  | `2-1`             |
| `*`  | multiplication               | `2*2`             |
| `/`  | division                     | `4/2`             |
| `%`  | modulus (remainder)          | `5%2`             |
| `**` | exponent (power)             | `2**4`            |
| `//` | floor division (quotient)    | `5//2`            |

### Functions

Numeric types can all be used as arguments to the following built-in functions.

* {samp}`abs({x})` -- Return the absolute value of `x`.
  ```{code-block} python
  >>> abs(-100)
  100

  >>> abs(-0.5)
  0.5

  >>> abs(100)
  100

  >>> abs(0.5)
  0.5
  ```
* {samp}`divmod({x}, {y})` -- Return the tuple containing the quotient and
  remainder of `x` divided by `y`. Equivalent to (`x//y`, `x%y`).
  ```{code-block} python
  >>> divmod(9, 2)
  (4, 1)
  ```
* {samp}`pow({base}, {exp}, {mod}=None)` -- Return `base` to the power of `exp`. (Equivalent to `base**exp`.)
  If `mod` is present, return `base` to the power `exp`, modulo `mod`. (Equivalent to `base**exp % mod`.)
  ```{code-block} python
  >>> pow(3, 4)
  81

  >>> pow(3, 4, 10)
  1
  ```
* {samp}`round({number}, {ndigits}=None)` -- Round a number to `ndigits`
  precision, or nearest integer if `ndigits` is `None`.
  ```{code-block} python
  >>> round(3.75)
  4

  >>> math.pi
  3.141592653589793

  >>> round(3.14159, 2)
  3.14
  ```

Integers
--------

An integer is a whole number with no decimal places.

|                 |                    |
|-----------------|--------------------|
| **Type**        | `int`              |
| **Base Class**  | `numbers.Integral` |

```{code-block} python
:caption: Python shell
:class: full-width
>>> -10
-10

>>> 1_000_000
1000000

>>> int("25")
25
```

### Alternate bases

The decimal is base `10`, which means it uses ten individual digits to
represent all numbers. This is the most commonly used system and the one we use
in our daily lives.

Python also makes it easy to use other bases. In particular, there is built in
syntax and functions for hexadecimal (base-2), octal (base-8), and binary
(base-2).

| System      | Function | Base  | Prefix       | Example  |
|-------------|----------|-------|--------------|----------|
| hexadecimal |  `hex()` |  `16` | `0x` or `0X` | `0x12`   |
| octal       |  `oct()` |  `8`  | `0o` or `0O` | `0o12`   |
| binary      |  `bin()` |  `2`  | `0b` or `0B` | `0b10`   |

```{code-block} python
:caption: Python shell
:class: full-width
>>> 0xff
255

>>> hex(255)
'0xff'

>>> 0o74
60

>>> oct(60)
'0o74'

>>> 0b110110
54

>>> bin(54)
'0b110110'
```

Moreover, the `int()` type takes an optional keyword argument `base` that can be used to convert to any base.

```{code-block} python
:caption: Python shell
:class: full-width
>>> int('C', base=36)
12

>>> int('12', base=6)
8
```

% #### Bitwise operators

% The following preform bit operations on the values after first converting them to
% a series of bits (binary).

% | Sign | Meaning               | Operation                                   |
% |------|-----------------------|---------------------------------------------|
% | `|`  | or                    |                                             |
% | `^`  | exclusive or          |                                             |
% | `&`  | and                   | Returns 1 if both the bits are 1 else 0     |
% | `<<` | shift bits left       | multiplication by pow(2, n)                 |
% | `>>` | shift bits right      | floor division by pow(2, n)                 |
% | `~`  | invert bits           |                                             |

% * [Python Bitwise Operators](https://www.geeksforgeeks.org/python-bitwise-operators/)
% * [Bitwise Operators in Python](https://realpython.com/python-bitwise-operators/)

Boolean
-------

The boolean data type has just two values: `True` and `False`.

|                 |                    |
|-----------------|--------------------|
| **Type**        | `bool`             |
| **Base Class**  | `numbers.Integral` |


```{code-block} python
:caption: Python shell
:class: full-width
>>> True
True

>>> False
False

>>> bool(0)
False
```

While the boolean type is in some ways the simplest, is is also one of the most
fundamental.

It is the type that is returned when we use comparison operators:

```{code-block} python
:caption: Python shell
:class: full-width
>>> 1 == 2
False
```

It is the type that expressions are converted to to determine their truthiness.

```{code-block} python
:caption: Python shell
:class: full-width
>>> bool("")
False

>>> bool("a")
True

>>> bool([])
False
```

Which is what is used when evaluating a conditional statement. For example, the following two are equivalent.

<div class="row"><div class="col">

```{code-block} python
if []:
  # do stuff
```

</div><div class="col">

```{code-block} python
if bool([]):
  # do stuff
```

</div>

Under the hood `True` is equal to `1` and `False` is equal to `0`. Since `1`
and `0` are integers, the `bool` type is just a special kind of integer. That
means that we can usually use booleans as numbers for all intents and purposes.

```{code-block} python
:caption: Python shell
:class: full-width
>>> True + True + True
3

>>> words = ["No", "Yes"]

>>> words[False]
'No'

>>> words[True]
'Yes'
```

Floating point numbers
----------------------

Floating point values are numbers with a decimal point.

|                 |                    |
|-----------------|--------------------|
| **Type**        | `float`            |
| **Base Class**  | `numbers.Real`     |

```{code-block} python
>>> 1.
1.0

>>> .2
0.2

>>> float(1)
1.0
```

### Members

* `.is_integer()` -- Return True if the float is a whole number.
  ```{code-block} python
  >>> f = .25

  >>> f.as_integer_ratio()
  (1, 4)

  >>> f.is_integer()
  False

  >>> f = 5.0

  >>> f.is_integer()
  True
  ```
* `.as_integer_ratio()` -- Return a tuple containing the numerator and denominator.
  ```{code-block} python
  >>> f = .25

  >>> f.as_integer_ratio()
  (1, 4)
  ```

### E notation

Exponent notation or {term}`E notation` is a shorthand to express very large or
very small numbers by using the letter `E` to mean "`10` to the power of".

For example, `8e4` means "`8` times `10` to the power of `4`" (or `8.0 *
10**4`) which can also be expressed as `80000.0`.

Python supports E notation syntax for `float` values using with either a
capital or lowercase `E`. Large or small numbers may also be displayed in E
notation.

```{code-block} python
>>> 3e5
300000.0

>>> 1E-4
0.0001

>>> 10000000000000000.0
1e+16
```

### Limitations

Float values have limitations depending on your system. You can look at
`sys.float_info` to see the limitations of your system.

```{code-block} python
:caption: Python shell
:class: full-width
>>> import sys

>>> sys.float_info.max
1.7976931348623157e+308

>>> sys.float_info.min
2.2250738585072014e-308

>>> sys.float_info.dig
15
```

If you attempt to create a float outside of your systems limitations, you will
get the special float value `inf` for infinity.

```{code-block} python
:caption: Python shell
:class: full-width
>>> 2e400
inf
```

The limitations inherint to the way float values are stored can cause
unexpected results.

```{code-block} python
:caption: Python shell
:class: full-width
>>> 0.1 + 0.2
0.30000000000000004
```

Python does provide ways to do exact decimal point math that behaves as
expected which we'll learn about in a future math lesson. But the simple
answer for now is to use the `round()` function.

```{code-block} python
:caption: Python shell
:class: full-width
>>> round(0.1 + 0.2, 1)
0.3
```


Complex numbers
---------------

Complex numbers provide support for imaginary numbers, primarily used in
scientific, geometry, or calculus calculations.

|                 |                    |
|-----------------|--------------------|
| **Type**        | `complex`          |
| **Base Class**  | `numbers.Complex`  |

They are comprised of a real component combined with a `+` to an imaginary
component indicated with a `j` or `J`.  The most commonly syntax is
{samp}`{real}+{imag}J` but the order of the real and imaginiary parts can be
switched.

```{code-block} python
:caption: Python shell
:class: full-width
>>> x = 3+5j

>>> x
(3+5j)

>>> x.real, x.imag
(3.0, 5.0)

>>> y = 5j+3

>>> y
(3+5j)

>>> y.real, y.imag
(3.0, 5.0)
```

A complex number with a negative imaginary part can be expressed as
{samp}`{real}-{imag}j` which is the same as {samp}`{real}+-{imag}j`.

```{code-block} python
:caption: Python shell
:class: full-width
>>> 3-5j
(3-5j)

>>> 3+-5j
(3-5j)
```

One with a real part of `0` can be expressed as {samp}`{imag}j` which is the
same as {samp}`0+{imag}j`.

```{code-block} python
:caption: Python shell
:class: full-width
>>> x = 5j

>>> x
5j

>>> x.real, x.imag
(0.0, 5.0)

>>> x = 0+5j

>>> x
5j

>>> x.real, x.imag
(0.0, 5.0)
```

Alternately use the `complex()` constructor with the arguments `real` and
`imag`.

```{code-block} python
:caption: Python shell
:class: full-width
>>> a = complex(3, 5)

>>> a
(3+5j)

>>> a.real, a.imag
(3.0, 5.0)
```

### Members

* `.conjugate()` -- Return the complex conjugate
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> x = 3+5j
  >>> x.conjugate()
  (3-5j)
  ```
* `imag` -- the imaginary part of a complex number
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> x = 3+5j
  >>> x.imag
  5.0
  ```
* `real` -- the real part of a complex number
  ```{code-block} python
  :caption: Python shell
  :class: full-width
  >>> x = 3+5j
  >>> x.real
  3.0
  ```


Reference
---------

### Glossary

```{glossary} numeric-types

primitive data type
  A built-in type that where each instance contains a single value not made up
  of any other values. For example `int` is a primitive type, while `list` is
  not.

exponent notation
E notation
  A compact way to represent very large or very small numbers by using an `e`
  to to indicate powers of ten. For example `3e5` indicates `3` times `10` to
  the power of `5` or `300000.0`.

unary operator
  An operator that acts on a single input.

```

### See also

* [python.org > Numeric Types](https://docs.python.org/3/library/stdtypes.html#typesnumeric)
* [python.org > numbers module](https://docs.python.org/3/library/numbers.html)
