---
myst:
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

```{include} ../toc.md
```

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

Another advantage of `.format()` is that anything not in curly braces is
interpreted literally.

{{ rightcol }}

```{code-cell} python
:class: full-width

"The price on {:.3s} is: ${:.2f}".format("Monday", 5.2423)
```

{{ newrow }}

You can also send keyword arguments to `.format()`. Then, instead of using
position numbers, you use variable names.

{{ rightcol }}

```{code-cell} python
:class: full-width

blueprint = "The price on {day:.3s} is: ${cost:.2f}"
blueprint.format(
  day="Monday",
  cost=5.2423,
)
```

{{ endcols }}

### Exercises

`````{exercise} Format Email Address
:label: format-email-exercise

Given the following values:

```python
user = "joe"
domain = "gmail"
extension = "com"
```

Use `.format()` to print the string:

`"joe@gmail.com"`

Bonus: Write a `format_email()` function that takes three arguments, `name`,
`domain`, and `extension` and returns a formatted email address string.

`````

`````{solution} format-email-exercise

:::{dropdown} Click to show

```python
>>> "{user}@{domain}.{extension}".format(user="joe", domain="gmail", extension="com")
'joe@gmail.com'
```
:::

:::{dropdown} Click to show: Bonus

```{code-block} python
:class: full-width

def format_email(user, domain, extension):
  return "{}@{}.{}".format(user, domain, extension)

print(format_email("joe", "gmail", "com"))
```

:::

:::{dropdown} Click to show: Bonus alternate

```{code-block} python
:class: full-width

def format_email(user, domain, extension):
  return "{user}@{domain}.{extension}".format(user=user, domain=domain, extension=extension)

print(format_email("joe", "gmail", "com"))
```

:::

`````

f-strings
---------

{{ leftcol }}

Since we so frequently need to format strings, Python provides a shortcut
called f-strings, which have the letter `f` immediately before the opening
single or double quote.

F-strings works just the same as `.format()`, except variables are used instead
of keyword arguments.


{{ rightcol }}

```{code-cell} python
:class: full-width

day = "Monday"
cost = 5.2423

f"The price on {day:.3s} is: ${cost:.2f}"
```

{{ endcols }}

### Exercise

`````{exercise} Street Address
:label: street-address-exercise

Given the following values:

```python
street = "1600 Pennsylvania Ave NW"
city = "Washington"
state = "DC"
zip = "20500"
```

Use an f-string to print the following:

```text
1600 Pennsylvania Ave NW
Washington, DC 20500
```

Bonus: Write a `format_address()` function that takes the arguments `street`,
`city`, `state` and `zip` and returns a formatted address string.

`````

`````{solution} street-address-exercise

:::{dropdown} Click to show

```{code-block} python
:class: full-width

>>> street = "1600 Pennsylvania Ave NW"
>>> city = "Washington"
>>> state = "DC"
>>> zip = "20500"
>>> print(f"{street}\n{city}, {state} {zip}")
1600 Pennsylvania Ave NW
Washington, DC 20500
```

:::

:::{dropdown} Click to show: Bonus

```{code-block} python
:class: full-width
:linenos:

def format_address(street, city, state, zip):
  return f"{street}\n{city}, {state} {zip}"

print(format_address(
  "1600 Pennsylvania Ave NW",
  "Washington",
  "DC",
  "20500",
))
```

:::



`````
