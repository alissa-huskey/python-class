
% #### Available operators
%
% Remember those pesky `__` members we saw when using the `dir()` function? Those
% are called {term}`magic <magic method>` or
% {term}`dunder methods <dunder method>` and we can look at them to find out what
% operators a value has.
%
% Each operator has a cooresponding magic method. For example the `+` operator
% uses the `.__add__()` method. So if `__add__` is in the list of available
% members, we know that the `+` operator can be used with that value.
%
% ```{code-block} python
% :caption: Python shell
% :emphasize-lines: "3"
% >>> dir(1)
% ['__abs__',
%  '__add__',
%  ...
%  ]
% ```
%
% You can look in the Reference section below to for a list of [Operator dunder
% methods](#operator-dunder-methods) and the operators they coorespond to.
%
% ```{seealso}
%
% * [Python.org > Special Method Names](https://docs.python.org/3/reference/datamodel.html#specialnames)
% * [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/#operators)
% * [Python - Dunder or Magic Methods](https://www.alphacodingskills.com/python/pages/python-dunder-methods.php)
% * [Python Dunder (Special, Magic) Methods List with Tutorial](https://holycoders.com/python-dunder-special-methods/)
%
% ```

### Operator dunder methods

Below are tables matching operators to their cooresponding dunder methods.

#### Arithmetic Operators

| Operator | Meaning                   | Method          | Operator | Method          |
|----------|---------------------------|-----------------|----------|-----------------|
| `+`      | sum                       | `__add__`       | `+=`     | `__iadd__`      |
| `-`      | difference                | `__sub__`       | `-=`     | `__isub__`      |
| `*`      | product                   | `__mul__`       | `*=`     | `__imul__`      |
| `/`      | quotient                  | `__truediv__`   | `/=`     | `__itruediv__`  |
| `//`     | floored quotient          | `__floordiv__`  | `//=`    | `__ifloordiv__` |
| `%`      | remainder                 | `__mod__`       | `%=`     | `__imod__`      |
| `**`     | power of                  | `__pow__`       | `**=`    | `__ipow__`      |

#### Comparison operators

| Operator | Meaning                   | Method          |
|----------|---------------------------|-----------------|
| `<`      | less than                 | `__lt__`        |
| `>`      | greater than              | `__gt__`        |
| `<=`     | less than or equal to     | `__le__`        |
| `>=`     | greater than or equal to  | `__ge__`        |
| `==`     | equals                    | `__eq__`        |
| `!=`     | not equals                | `__nq__`        |
| `in`     | contains                  | `__contains__`  |

### See also

```{seealso}

- [python.org > Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [python.org > The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types)

```

Reference
---------

### Glossary

```{glossary} data-types

dunder method
magic method
special method
  An method, beginning and ending with two underscores (`__`) intended to be
  used internally by Python.

```
