Lists
=====

Bullet Lists
------------

- Lists can start with `-` or `*`
  * My other, nested
  * bullet point list!

Enumerated Lists
----------------

1. My numbered list
2. has two points

Inline lists
------------

From bootstrap

Hlists
------

* [Sphinx > rst Directives > hlist](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-hlist)

:::::{div} inline

:::{hlist}
:columns: 2

- First item
- Second item
- Third item
- Forth item
- Fifth item
- Sixths item
:::

:::::

{{ clear }}

### With Images

:::{hlist}
:columns: 3

- ![](https://source.unsplash.com/150x150/daily?mossy+forest)
- ![](https://source.unsplash.com/150x150/daily?glow)
- ![](https://source.unsplash.com/150x150/daily?cherry+blossom)

:::

{{ clear }}

### With Figures

`````{hlist}
:columns: 3

- ```{figure} https://source.unsplash.com/150x150/daily?breakfast
  :width: 150
  :height: 150

     Breakfast
  ```
- ```{figure} https://source.unsplash.com/150x150/daily?lunch+sandwich
  :width: 150
  :height: 150

     A delicious sandwich for lunch
  ```
- ```{figure} https://source.unsplash.com/150x150/daily?dinner+beef
  :width: 150
  :height: 150

     A hearty dinner. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     Donec porttitor dolor in odio posuere, vitae ornare libero mattis. In lobortis justo vestibulum nibh aliquet, non.
  ```

`````

{{ clear }}

Field list
----------

* [Sphinx > rst > Field Lists](https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html)

:::{fieldlist}

:State:       Mutable
:Position:    Ordered
:Composition: varies
:Diversity:   Repeatable
:Access:      Subscriptable
:Value:       Hashable

:::

Definition Lists
----------------

* [Jupyter Book > Definition Lists](https://jupyterbook.org/en/stable/content/content-blocks.html#definition-lists)

Term *with Markdown*
: Definition [with reference](#definition-lists)

  A second paragraph
: A second definition

Term 2
  ~ Definition 2a
  ~ Definition 2b

Term 3
:     A code block
: > A quote
: A final definition, that can even include images:

  ![](https://source.unsplash.com/200x200/daily?dress)

Glossary
--------

* [Sphinx > rst Directives > glossary](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-glossary)
* [Jupyter Book > Glossaries](https://jupyterbook.org/en/stable/content/content-blocks.html#definition-lists)
* [markdown-it-py deflist plugin](https://mdit-py-plugins.readthedocs.io/en/latest/#definition-lists)
* [pandoc definition_lists spec](https://jupyterbook.org/en/stable/content/content-blocks.html#definition-lists)

This is a glossary with definition terms for thing like {term}`Writing`:

```{glossary} example-glossary
Documentation
  Provides users with the knowledge they need to use something.

Reading
  The process of taking information into ones mind through the use of eyes.

Writing
  The process of putting thoughts into a medium for other people to {term}`read <Reading>`.
```

Examples
--------

### Nested list

- A simple list.
- There are no margins between list items.
- Simple lists do not contain multiple paragraphs. That's a complex list.
- In the case of a nested list

  - There are no margins between elements

    - Still no margins

      - Still no margins

### Complex

- A bullet list

  + Nested bullet list.
  + Nested item 2.

- Item 2.

  Paragraph 2 of item 2.

  * Nested bullet list.
  * Nested item 2.

    - Third level.
    - Item 2.

  * Nested item 3.

- ``inline literall``
- ``inline literall``
- ``inline literall``
- This item has multiple paragraphs.

  This item has multiple paragraphs.
- This item has multiple paragraphs.

  This item has multiple paragraphs.


### Second list level

- here is a list in a second-level section.
- `yahoo <http://www.yahoo.com>`_
- `yahoo <http://www.yahoo.com>`_

  - `yahoo <http://www.yahoo.com>`_
  - here is an inner bullet ``oh``

    - one more ``with an inline literally``. `yahoo <http://www.yahoo.com>`_

      heh heh. child. try to beat this embed:

      .. literalinclude:: ../_ext/lexicon.py
          :caption: "Literal includes can also have captions."
          :linenos:
          :lines: 138-140

  - and another. `yahoo <http://www.yahoo.com>`_
  - `yahoo <http://www.yahoo.com>`_
  - ``hi``
- how about an admonition?

  .. note::
      This is a note nested in a list.

- and hehe

#### But deeper down the rabbit hole

- I kept saying that, "deeper down the rabbit hole". `yahoo <http://www.yahoo.com>`_

  - I cackle at night `yahoo <http://www.yahoo.com>`_.
- I'm so lonely here in GZ ``guangzhou``
- A man of python destiny, hopes and dreams. `yahoo <http://www.yahoo.com>`_

  - `yahoo <http://www.yahoo.com>`_

    - `yahoo <http://www.yahoo.com>`_ ``hi``
    - ``destiny``

See Also
--------

:::{seealso}

* [Bootstrap > Components > List Group](https://getbootstrap.com/docs/5.0/components/list-group/)
* [Bootstrap > Typography > Lists](https://getbootstrap.com/docs/5.0/content/typography/#lists)

:::

TODO
----

* [Task Lists](https://mdit-py-plugins.readthedocs.io/en/latest/#task-lists)
