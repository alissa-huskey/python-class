Admonitions
===========

Sphinx provides several different types of admonitions.

admonition
----------

* [Docutils > Directives > Generic Admonition](https://docutils.sourceforge.io/docs/ref/rst/directives.html#generic-admonition)

```{admonition} The one with the custom titles

   It's got a certain charm to it.
```

attention
---------

* [Docutils > Directives > attention](https://docutils.sourceforge.io/docs/ref/rst/directives.html#attention)

```{attention}

   Climate change is real.
```

caution
-------

* [Docutils > Directives > caution](https://docutils.sourceforge.io/docs/ref/rst/directives.html#caution)

```{caution}

   Cliff ahead: Don't drive off it.
```

danger
------

* [Docutils > Directives > danger](https://docutils.sourceforge.io/docs/ref/rst/directives.html#danger)

```{danger}

   Mad scientist at work!
```

error
-----

* [Docutils > Directives > error](https://docutils.sourceforge.io/docs/ref/rst/directives.html#error)

```{error}

   Does not compute.
```

hint
----

* [Docutils > Directives > hint](https://docutils.sourceforge.io/docs/ref/rst/directives.html#hint)

```{hint}

   Insulators insulate, until they are subject to ______ voltage.
```

important
---------

* [Docutils > Directives > important](https://docutils.sourceforge.io/docs/ref/rst/directives.html#important)

```{important}

   Tech is not neutral, nor is it apolitical.
```

note
----

* [Sphinx > rst Directives > note](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-note)
* [Docutils > Directives > note](https://docutils.sourceforge.io/docs/ref/rst/directives.html#note)

```{note}

   This is a note.
```

seealso
-------

* [Sphinx > rst Directives > seealso](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-seealso)

```{seealso}

   Other relevant information.
```

tip
---

* [Docutils > Directives > tip](https://docutils.sourceforge.io/docs/ref/rst/directives.html#tip)

```{tip}

   25% if the service is good.
```

warning
-------

* [Sphinx > rst Directives > warning](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-warning)
* [Docutils > Directives > attention](https://docutils.sourceforge.io/docs/ref/rst/directives.html#warning)

```{warning}

   Reader discretion is strongly advised.
```

versionadded
------------

* [Sphinx > rst Directives > versionadded](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-versionadded)

```{versionadded} v0.1.1

   Here's a version added message.
```

versionchanged
--------------

* [Sphinx > rst Directives > versionchanged](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-versionchanged)

```{versionchanged} v0.1.1

   Here's a version changed message.
```

deprecated
----------

* [Sphinx > rst Directives > deprecated](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated)

```{deprecated} v0.1.1

   Here's a deprecation message.
```

exercise
--------

```{exercise} Write HR Function
:label: exercise-example-for-theme

Write a function called `hr` to print a line of dashes 100 characters wide, like so:

`--------------------------------------------------`


```

`````{solution} exercise-example-for-theme
:class: dropdown

```{code-block} python
:linenos:
def hr():
  print("-" * 100)
```

`````

```{exercise} Nested Annotations
:label: exercise-nested-annotations

:::{admonition} Need help?
:class: hint dropdown

Here's a tip!

:::

:::{tip}

Here's a tip!

:::


```

margin & sidebar
----------------

::::::{margin}

:::{versionadded} Python 3.3+

:::

::::::

Here's an example of an annotation inside a margin.

{{ clear }}

::::::{sidebar}

:::{seealso}

* [Admonitions](https://shibuya.lepture.com/writing/admonition/)

:::

::::::

Here is some general text

{{ clear }}

### Margin with text

`````{margin}
```{seealso}

For how to pass all iterable items as arguments to a function see [Functions >
Unpacking][arg-unpacking].

```

`````

This is an example of an admonition in a margin with more text.

See Also
--------

:::{seealso}

* [Jupyter Book > Notes, warnings, and other admonitions](https://jupyterbook.org/en/stable/content/content-blocks.html#notes-warnings-and-other-admonitions)
* [Jupyter Book > Dropdown admonitions](https://jupyterbook.org/en/stable/content/components.html#dropdown-admonitions)

:::
