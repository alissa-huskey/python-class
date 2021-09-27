---
substitutions:
  label: '<div class="text-right">Syntax:</div>'

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
String formatting: Part 2
=========================

In [part 1](string-formatting-part-1.md) we learned about formatting strings,
sometimes called the formatting spec (short for specification), which are used
to tell Python how a value should be displayed. And we learned how to use them
in the `format()` function.

Today we are going to learn some of the other ways to use formatting strings.

The `format()` function
-----------------------

{{ leftcol }}

First lets do a quick review of the `format()` function.

{{ label }}

{{ rightcol }}

{samp}`format({VALUE}, {SPEC})`

:::{table}
:class: notitle

|          |                                                                          |
|----------|--------------------------------------------------------------------------|
| `VALUE`  | the value to format                                                      |
| `SPEC`   | the formatting specification                                             |

:::

{{ newrow }}

In this example, the `VALUE` is `"Monday"`.

The `SPEC` is `".3s"` which means:

* a precision of `3` should be used
* with a `string` presentation

{{ rightcol }}

```{code-cell} python
:class: full-width
format("Monday", ".3s")
```

{{ endcols }}

The `str.format()` method
-------------------------

{{ leftcol }}

The `.format()` method on `str` objects also uses formatting strings. Here is
how we would do the same thing with the `.format()` method.

{{ rightcol }}

```{code-cell} python
:class: full-width

"{0:.3s}".format("Monday")
```

{{ newrow }}

<div class="text-right">The syntax is:</div>

{{ rightcol }}

{samp}`\{{POSITION}:{SPEC}\}.format(VALUE)`

|            |                                                                          |
|------------|--------------------------------------------------------------------------|
| `{}`       | curly braces placeholders which indicate where the value should go       |
| `POSITION` | argument position                                                        |
| `:`        | a colon is used to indicate that the `SPEC` follows                      |
| `SPEC`     | the formatting specification                                             |
| `VALUE`    | the value to format                                                      |

{{ newrow }}

You might be wondering where that `0` for `POSITION` come from.

Well you see, one of the advantages to using `.format()` is that you can pass
it multiple values. When you do that, each argument has its own position.

{{ rightcol }}

```{code-cell} python
:class: full-width

"{0:.3s} {1:.2f}".format("Monday", 5.2423)
```

{{ newrow }}

If you don't provide a position, each argument will be substituted in the same
order that the placeholders (`{}`) appear.

{{ rightcol }}

```{code-cell} python
:class: full-width

"{:.3s} {:.2f}".format("Monday", 5.2423)
```

{{ newrow }}

Or you can include the position to change the order in which they appear.

{{ rightcol }}

```{code-cell} python
:class: full-width

"{1:.2f} {0:.3s}".format("Monday", 5.2423)
```

{{ newrow }}

Another advantage of `.format()` is that anything not in curley braces is
interpreted literally.

{{ rightcol }}

```{code-cell} python
:class: full-width

"The price on {:.3s} is: ${:.2f}".format("Monday", 5.2423)
```

{{ endcols }}


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
