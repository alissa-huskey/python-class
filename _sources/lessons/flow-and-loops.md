Flow Control
============

If-Statements
-------------

* if
* elif
* else
* conditions
* logical operators


```{image} assets/breath-of-fire-skills.png
---
alt: skills
align: left
---
```

### Truthy and Falsy

* bool
* True
* False

```
 | type     | name         | False value | True example |
 |----------|--------------|-------------|--------------|
 | `str`    | string       | `""`        | `"a"`        |
 | `int`    | integer      | `0`         | `1`          |
 | `float`  | float        | `0.0`       | `0.5`        |
 | `dict`   | dictionary   | `{}`        | `{"a"=1}`    |
 | `list`   | list         | `[]`        | `[1]`        |
 | `tuple`  | tuple        | `()`        | `(1)`        |
 | `bool`   | boolean      | `False      | `True`       |
 | `None`   | none         | `None`      |              |
```

### Comparison Operators

* sorting

```
 | operator  | meaning                         | example                 | example                                   |
 |-----------|---------------------------------|-------------------------|-------------------------------------------|
 | `==`      | equivalent values               | `choice == "a"`         | `5.0 == 5`                                |
 | `!=`      | not equivalent values           | `a != b`                |                                           |
 | `<`       | less than                       | `"a" < "c"              | `balance < price`                         |
 | `<=`      | less than or equal to           | `a <= b`                |                                           |
 | `>`       | greater than                    | `"z" > "d"`             | `price > balance`                         |
 | `>=`      | greater than or equal to        | `a >= b`                |                                           |
 | `in`      | RHV contains LHV                | `"h" in "hello"`        | `choice in ["red", "green", "blue"]`      |
 | `not in`  | RHV does not contain LHV        | `"a" not in "hello"`    | `choice not in ["red", "green", "blue"]`  |
```

### Comparison Operators

```
 | `and` | both conditions are true  | `choice > min and choice < max`            |
 | `or`  | either condition is true  | `choice < min or choice > max`             |
 | `not` |                           | `not `                                     |
```

Loops
-----

* break
* continue
* pass
