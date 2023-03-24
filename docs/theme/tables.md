Tables
======

## Pipe tables

{{ left }}

Tables can be written using the standard [Github Flavoured Markdown
syntax](https://github.github.com/gfm/#tables-extension-).

{{ right }}

| Letter | Type           | Presentation | Example        |
|--------|----------------|--------------|----------------|
| `s`    | `str`          | string       | `"hello"`      |
| `d`    | `int`          | decimal      | `"1000"`       |
| `f`    | `float`, `int` | float        | `"1.000000"`   |
| `%`    | `float`, `int` | percent      | `"20.000000%"` |

{{ endcols }}

## Alignment

{{ left }}

Cells in a column can be aligned using the `:` character.

{{ right }}

| Type    | Name    | Example   |
|:--------|:-------:|----------:|
| `bool`  | Boolean | `False`   |
| `str`   | String  | `"hello"` |
| `int`   | Integer | `1`       |
| `float` | Float   | `1.5`     |

{{ endcols }}


## Captions

The `table` directive can be used to create a table with a caption.

```{table} Comparison operators

| operator    | meaning                   | examples                |                               |
|-------------|---------------------------|-------------------------|-------------------------------|
| `==`        | equivalent values         | `choice == "a"`         | `5.0 == 5`                    |
| `!=`        | not equivalent values     | `a != b`                |                               |
| `<`         | less than                 | `"a" < "c"`             | `balance < price`             |
| `<=`        | less than or equal to     | `a <= b`                |                               |
| `>`         | greater than              | `"z" > "d"`             | `price > balance`             |
| `>=`        | greater than or equal to  | `a >= b`                |                               |
| `in`        | is member of              | `"h" in "hello"`        | `5 in [1, 3, 5, 7, 9]`        |
| `not in`    | is not a member of        | `"a" not in "hello  "`  | `2 not in [1, 3, 5, 7, 9]`    |
```

## Widths

You can set both the width of the entire table as well as the widths of columns
using the `table` directive.

```{table} Multiplication Table
:widths: grid
:width: 50%

|      |     |      |     |    |
|-----:|----:|-----:|----:|---:|
|    1 |   2 |   3  |  4  |  5 |
|    2 |   4 |   6  |  8  | 10 |
|    3 |   6 |   9  | 12  | 15 |
|    4 |   8 |  12  | 16  | 20 |
|    5 |  10 |  15  | 20  | 25 |
```

## No headers

Markdown tables must have a header row, but it can be blank.

{{ leftcol }}

:::{table} .notitle class
:class: notitle

|          |                                                                          |
|----------|--------------------------------------------------------------------------|
| `VALUE`  | the value to format                                                      |
| `SPEC`   | the formatting specification                                             |

:::

{{ rightcol }}

````{table} .no-headers class
:class: no-headers

|                                               |                         |
|-----------------------------------------------|-------------------------|
| {menuselection}`Workbench --> Startup Editor` | `none`                  |
| {menuselection}`Appearance --> Tips: Enabled` | <input type="checkbox"> |
| {menuselection}`Python --> Show Start Page`   | <input type="checkbox"> |

````

{{ endcols }}

## List tables

{{ left }}

The `list-table` directive is used to create a table from data in a uniform two-level bullet list.
"Uniform" means that each sublist (second-level list) must contain the same number of list items.

{{ right }}

```{list-table}
:header-rows: 1

* - Sign
  - Meaning
  - Example
* - `+`
  - addition
  - `1+2`
* - `-`
  - subtraction
  - `2-1`
* - `*`
  - multiplication
  - `2*2`
* - `/`
  - division
  - `4/2`
* - `%`
  - remainder
  - `5%2`
* - `**`
  - power
  - `2**4`
* - `//`
  - quotient
  - `5//2`
```

{{ endcols }}

## CSV tables

The `csv-table` directive is used to create a table from Comma-Separated-Values data.

```{csv-table}
:header: >
:    "Sign", "Meaning", "Operation"
:widths: 10, 15, 30
:width: 75%
:align: left

"`&`",       "AND",           "logical conjunction "
"`|`",       "OR",            "logical disjunction"
"`^`",       "XOR",           "exclusive disjunction"
"`~`",       "NOT",           "logical negation"
"`<<`",      "left shift",    "multiplication by pow(2, n)"
"`>>`",      "right shift",   "floor division by pow(2, n)"
```
