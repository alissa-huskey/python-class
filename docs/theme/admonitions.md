Admonitions
===========

Sphinx provides several different types of admonitions.

topic
-----

```{topic} This is a topic.

   This is what admonitions are a special case of, according to the docutils
   documentation.
```

admonition
----------

```{admonition} The one with the custom titles

   It's got a certain charm to it.
```

attention
---------

```{attention}

   Climate change is real.
```

caution
-------

```{caution}

   Cliff ahead: Don't drive off it.
```

danger
------

```{danger}

   Mad scientist at work!
```

error
-----

```{error}

   Does not compute.
```

hint
----

```{hint}

   Insulators insulate, until they are subject to ______ voltage.
```

important
---------

```{important}

   Tech is not neutral, nor is it apolitical.
```

note
----

```{note}

   This is a note.
```

seealso
-------

```{seealso}

   Other relevant information.
```

tip
---

```{tip}

   25% if the service is good.
```

warning
-------

```{warning}

   Reader discretion is strongly advised.
```

versionadded
------------

```{versionadded} v0.1.1

   Here's a version added message.
```

versionchanged
--------------

```{versionchanged} v0.1.1

   Here's a version changed message.
```

deprecated
----------

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

{{ clear }}

Also here's some general text.
