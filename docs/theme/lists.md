Lists
=====

Bullet Lists
------------

* [CommonMark Tutoral > Lists](https://commonmark.org/help/tutorial/06-lists.html)
* [CommonMark Spec > List Items](https://spec.commonmark.org/0.30/#list-items)
* [Sphinx > reStructuredText Primer > Lists and Quote-like blocks](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks)
* [reStructuredText Markup Specification > Bullet Lists](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists)

Bulleted lists in commonmark markdown can start with `-` or `*`.

* Apples
* Oranges
* Pears

- Apples
- Oranges
- Pears

+ Apples
+ Oranges
+ Pears

### Nested list

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

- Here is a list in a second-level section.
- [yahoo](http://www.yahoo.com)
- [yahoo](http://www.yahoo.com)

  - [yahoo](http://www.yahoo.com)
  - here is an inner bullet ``oh``

    - one more ``with an inline literally``. [yahoo](http://www.yahoo.com)

      heh heh. child. try to beat this embed:

      ```{literalinclude} ../../pythonclass/lessons/hello_world.py
      :caption: "Literal includes can also have captions."
      :linenos:
      :start-at: "Hello world!"
      ```

  - and another. [yahoo](http://www.yahoo.com)
  - [yahoo](http://www.yahoo.com)
  - ``hi``
- how about an admonition?

  :::{note}

  This is a note nested in a list.

  :::

- and hehe

#### But deeper down the rabbit hole

- I kept saying that, "deeper down the rabbit hole". [yahoo](http://www.yahoo.com)

  - I cackle at night [yahoo](http://www.yahoo.com).
- I'm so lonely here in GZ ``guangzhou``
- A man of python destiny, hopes and dreams. [yahoo](http://www.yahoo.com)

  - [yahoo](http://www.yahoo.com)

    - [yahoo](http://www.yahoo.com) ``hi``
    - ``destiny``

Enumerated Lists
----------------

* [CommonMark Tutoral > Lists](https://commonmark.org/help/tutorial/06-lists.html)
* [CommonMark Spec > List Items](https://spec.commonmark.org/0.30/#list-items)
* [Sphinx > reStructuredText Primer > Lists and Quote-like blocks](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks)
* [reStructuredText Markup Specification > Bullet Lists](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists)

Ordered lists use numbers followed by period `.` or right paren `)`.

1. My numbered list
2. has two points

<!-- break for new list -->

1. Perl
1. Python
1. Ruby

Mixed Lists
-----------

* [CommonMark Tutorial > Nested Lists](https://commonmark.org/help/tutorial/10-nestedLists.html)

<!-- break for new list -->

* Item
    1. First Subitem
    2. Second Subitem
* Item
    - Subitem
    - Subitem
* Item

Hlists
------

* [Sphinx > rst Directives > hlist](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-hlist)

Use the `{hlist}` directive with an optional `:columns:` option to columnize a
bulleted list. For example, the following example uses `3` columns.

:::{hlist}
:columns: 3

- First item
- Second item
- Third item
- Forth item
- Fifth item
- Sixth item
:::

### With Images

You can have images as `hlist` items.

:::{hlist}
:columns: 3

- ![](https://source.unsplash.com/150x150/daily?mossy+forest)
- ![](https://source.unsplash.com/150x150/daily?glow)
- ![](https://source.unsplash.com/150x150/daily?cherry+blossom)

:::

{{ clear }}

### With Figures

Or figures as `hlist` items.

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
* [Python Class fieldlist directive](https://github.com/alissa-huskey/python-class/blob/master/docs/_ext/fieldlist.py)
* [reStructuredText Markup Specification > Field Lists](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists)

Field lists are sequences of fields marked up using the syntax `:fieldname:
Field content`. This syntax is supported natively in `rst` documents, but in
`myst` markdown you'll need the customized `{fieldlist}` directive.

:::{fieldlist}

:State:       Mutable
:Position:    Ordered
:Composition: varies
:Diversity:   Repeatable
:Access:      Subscriptable
:Value:       Hashable

:::

### Advanced

```{admonition} FIXME
:class: error, margin

Broken in `{fieldlist}` directive.

```

Here's a field list with more advanced formatting.

{{ clear }}

{{ br }}

:::{fieldlist}

:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer

:::

Option Lists
------------

* [reStructuredText Markup Specification Option Lists](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#rcs-keywords)

Option lists, a `rst` only syntax, map a program's command-line options to
descriptions documenting them. For example:

```{eval-rst}
-a         Output all.
-b         Output both (this description is
           quite long).
-c arg     Output just arg.
--long     Output all day long.

-p         This option has two paragraphs in the description.
           This is the first.

           This is the second.  Blank lines may be omitted between
           options (as above) or left in (as here and below).

--very-long-option  A VMS-style option.  Note the adjustment for
                    the required two spaces.

--an-even-longer-option
           The description can also start on the next line.

-2, --two  This option has two variants.

-f FILE, --file=FILE  These two options are synonyms; both have
                      arguments.

/V         A VMS/DOS-style option.
```

Definition Lists
----------------

* [Jupyter Book > Definition Lists](https://jupyterbook.org/en/stable/content/content-blocks.html#definition-lists)
* [Pandoc definition list specification](https://pandoc.org/MANUAL.html#definition-lists)

Definition lists are supported using markdown specified by pandoc.

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
* [Jupyter Book > Glossaries](https://jupyterbook.org/en/stable/content/content-blocks.html#glossaries)
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

Term 1 : A
Term 2 : B
  Definition of both terms.

Term 3
  Paragraph 1 \
  Paragraph 2 \
  Paragraph 3

Term 4
  A definition can even include images: \
  ![](https://source.unsplash.com/200x200/daily?dress)
```

See Also
--------

:::{seealso}

* [Bootstrap > Components > List Group](https://getbootstrap.com/docs/5.0/components/list-group/)
* [Bootstrap > Typography > Lists](https://getbootstrap.com/docs/5.0/content/typography/#lists)

:::

TODO
----

* [Task Lists](https://mdit-py-plugins.readthedocs.io/en/latest/#task-lists)
* [Inline Lists](https://getbootstrap.com/docs/5.0/content/typography/#inline)
* [Description list alignment](https://getbootstrap.com/docs/5.0/content/typography/#description-list-alignment)
