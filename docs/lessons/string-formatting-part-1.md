---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
String formatting
=================

We often want to display text to the end user in a specific way. For example,
we may want to display `25.375` as `$25.38` if it represents an amount of money
but as `25%` if it represents a percentage.

Python provides a number of tools for this, but for this lesson we'll focus on
the built in `format()` function, which takes two arguments: the `value`, and the
`formatting string`.

The formatting string is a combination of specific letters or characters that
controls the format. This is a mini-language with its own syntax, but this
lesson will focus on a few of the most commonly used.

Here's how you would use the `format()` method to print the aformentioned
examples. *Don't worry, this is just a teaser--I don't expect you to understand
this yet.*

```{code-cell} python
:class: full-width
print(format(25.375, '.2f'))

print(format(25.375/100, '.0%'))
```

Presentation
------------

{{ leftcol }}

At the core of a formatting strings is its presentation. Each letter
cooresponds to a specific input value type and output presentation. The most
common are:

{{ rightcol }}

| Letter | Type           | Presentation | Example        |
|--------|----------------|--------------|----------------|
| `s`    | `str`          | string       | `"hello"`      |
| `d`    | `int`          | decimal      | `"1000"`       |
| `f`    | `float`, `int` | float        | `"1.000000"`   |
| `%`    | `float`, `int` | percent      | `"20.000000%"` |

{{ br }}

{{ newrow }}

So here's a simple example that formats an `int` value with a decimal
presentation style.

{{ rightcol }}

```{code-cell} python
:class: full-width
format(5, "f")
```

{{ br }}

{{ newrow }}

If there is no presentation type letter in a formatting string, the default is
`d` for numbers or `s` otherwise.

So technically, these are equivalent.

{{ rightcol }}

```{code-cell} python
:class: full-width
format("hello", "")
format("hello", "s")
```

```{code-cell} python
:class: full-width
format(5, "")
format(5, "d")
```

{{ endcols }}

Precision
---------

{{ leftcol }}

Precison goes before the presentation, with the syntax:

{{ rightcol }}

{samp}`.{NUMBER}`

{{ newrow }}

The `NUMBER` controls how many digits to display after the decimal point for
floating point numbers.

{{ rightcol }}

```{code-cell} python
:class: full-width
format(2.5, '.2f')
```

{{ br }}

{{ newrow }}

Or the maximum number of characters to show for strings.

{{ rightcol }}

```{code-cell} python
:class: full-width
format("Monday", ".3s")
```


{{ endcols }}

Alignment
---------

{{ leftcol }}

The formatting string for alignment goes before precision and consists of at
least two parts:

{{ rightcol }}

{samp}`{ALIGNMENT} {WIDTH}`

{{ newrow }}

With one of these characters for alignment.

{{ rightcol }}

| Character | Alignment           |
|-----------|---------------------|
| `>`       | right               |
| `<`       | left                |
| `^`       | center              |
| `=`       | align numeric signs |

{{ newrow }}

For example, to center a string to a width of `20`:

{{ rightcol }}

```{code-cell} python
:class: full-width
format("hello", "^20")
```

{{ newrow }}

It works the same way for numbers.

{{ rightcol }}

```{code-cell} python
:class: full-width
 format(22, ">5d")
```

{{ newrow }}

But you'll most likely want to use the special number alignment character `=`,
which ensures that signs are aligned.

{{ rightcol }}

```{code-cell} python
:class: full-width
print(format(">", ">5s"), format("=", ">5s"), "\n")
for x in (25, -436, 8, 150, -32, 10):
   print(format(x, ">5d"), format(x, "=5d"), sep="  ")
```

{{ newrow }}

It is important to keep in mind that the width is the number of total
characters in the output string, including any signs or decimal points.

{{ newrow }}

By the way, if we break down that last formatting string: `"=8.2f"`.

{{ rightcol }}

| Formatting string   | Refers to             | Meaning                             |
|---------------------|-----------------------|-------------------------------------|
| `=8`                | alignment             | numeric alignment, total width: `8` |
| `.2`                | precision             | `2` digits after the decimal        |
| `f`                 | presentation          | float                               |


{{ endcols }}

Exercises
---------

`````{exercise} String Formatting
:label: string-formatting-exercise

Use the `format()` function to:

1. Format the number `48.7052` to two decimal points.
1. Format the number `2.5` to two decimal points.
1. Format `.25` to `25%`
1. Truncate the string `"September"` to a width of `3` characters
1. Center the string `"Game Over"` to a width of `80`
1. Left align the text `"8 of 10"` to a width of `80`
1. Left align the string `"Question"` with a fill character of `"="` to a width of `30` characters.

`````


Reference
---------

### Presentations

| Letter   | Type           | Presentation | Details                                             | Example (Input)   | (Output)                   |
|----------|----------------|--------------|-----------------------------------------------------|--------------------------|----------------------------|
| `s`      | `str`          | string       |                                                     | `"hello"`                | `"hello"`                  |
| `d`, `i` | `int`          | decimal      | [^fmt-alias]                                        | `1000`                   | `"1000"`                   |
| `n`      | `int`          | decimal      | with number sepertors                               | `1000`                   | `"1,000"`                  |
| `f`      | `float`, `int` | float        |                                                     | `1.0`                    | `"1.000000"`               |
| `%`      | `float`, `int` | percent      |                                                     | `0.2`                    | `"20.000000%"`             |
| `e`, `E` | `float`, `int` | float        | scientific notation                     [^fmt-case] | `1.5`                    | `"1.500000e+00"`           |
| `g`, `G` | `float`, `int` | float        | normal or scientific depending on size  [^fmt-case] | `1.5` {{ br }} `1000000` | `"1.5"` {{ br }} `"1e+06"` |
| `b`      | `int`          | decimal      | binary                                              | `25`                     | `"1010"`                   |
| `o`      | `int`          | decimal      | octal                                               | `10`                     | `"12"`                     |
| `x`, `X` | `int`          | decimal      | hex                                     [^fmt-case] | `10`                     | `"a"`                      |
| `c`      | `int`          | string       | single character                                    | `65`                     | `"A"`                      |

[^fmt-case]: case of letter indicates case of output
[^fmt-alias]: alias

### See also

:::{seealso}

* [Format String Syntax](https://docs.python.org/3/library/string.html#format-specification-mini-language)

:::



% TODO
% [ ] format() / .format() / % / fstrings
% [ ] `x%`
% [ ] `$x.xx`
% [ ] `(-10)`
% [ ] `5.25378` -> `5.2`
% [ ] center/left/right to width
%     [ ] with alternate character
% [ ] truncate a string

% EXERCISES
% [ ] Remove leading zeros from an IP address
