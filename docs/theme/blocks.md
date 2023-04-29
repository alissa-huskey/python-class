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
Text Blocks
===========

Literal Blocks
--------------

:::{admonition} See
:class: docs sidebar

See [Code](theme:code:literal-blocks).

:::

While more often used for code, literal blocks where each line is indented four
spaces, will be rendered as monospaced raw text.

{{ clear }}

    Connecting... OK
    Transmitting data... OK
    Disconnecting... OK

Block Quotes
------------

:::{admonition} Docs
:class: docs margin dropdown

* [CommonMark Tutorial > Block quotes](https://commonmark.org/help/tutorial/05-blockquotes.html)
* [Jupyter Book > Quotations and epigraphs](https://sphinx-book-theme.readthedocs.io/en/stable/content/content-blocks.html#quotations-and-epigraphs)
* [MySt Tools > Typography > Quotations](https://myst-tools.org/docs/mystjs/typography#quotations)
* [Bootstrap > Typography > Blockquotes](https://getbootstrap.com/docs/5.0/content/typography/#blockquotes)

:::

Block quotes are used to visually set a piece of text, traditionally a
quotation, apart from the main body. Each line of a block quote starts with a
greater than (`>`) sign.

> Quotations are one way to highlight information.

Blockquotes can be on multiple lines.

> The first rule about fight club is you don’t talk about fight club.
>
> The second rule about fight club is you don’t talk about fight club.

They can include attribution.

> We've all heard that a million monkeys banging on a million typewriters will
> eventually reproduce the entire works of Shakespeare. Now, thanks to the
> Internet, we know this is not true.
>
> -- Robert Wilensky

Markdown is rendered within a blockquote. They can also be nested by adding one
greater than sign (`>`) for each level of indentation.

> **The quarterly results look great**
>
> - Sales were off the chart!
> - Morale is strong!
> - Poised to go public next spring!
>
> > _Everything_ is going according to **the plan**.

Epigraph
--------

:::{admonition} Docs
:class: docs margin dropdown

* [reStructuredText Directives > Epigraph](https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph)
* [Jupyter Book > Epigraphs](https://jupyterbook.org/en/stable/content/content-blocks.html#epigraphs)
* [Docutils > Directives > epigraph](https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph)

:::

An epigraph is an short inscription, often a quotation or poem, at the
beginning of a document or section. They can be added using the `{epigraph}`
directive.

Epigraphs draw more attention to a quote and highlight its author. You can
provide an attribution to an epigraph by adding -- to the final line, followed
by the quote author.

% Turning and turning in the widening gyre \
% The falcon cannot hear the falconer; \
% Things fall apart; the centre cannot hold; \
% Mere anarchy is loosed upon the world.

:::{epigraph}

There is nothing so useless as doing efficiently that which should not be done at all.

-- Peter Drucker

:::

:::{epigraph}

All that is gold does not glitter, \
Not all those who wander are lost; \
The old that is strong does not wither, \
Deep roots are not reached by the frost.

From the ashes a fire shall be woken, \
A light from the shadows shall spring; \
Renewed shall be blade that was broken, \
The crownless again shall be king.

-- J.R.R. Tolkien, The Fellowship of the Ring

:::

Pull-Quotes
-----------

:::{admonition} Docs
:class: docs margin dropdown

* [reStructuredText Directives > Pull-Quote](https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote)
* [Docutils > Directives > pull-quote](https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote)

:::

```{pull-quote}

Pull-quotes are a great way to add visual interest and excitement to your
layout.

```

A pull-quote is a small selection of text "pulled out and quoted", typically in
a larger typeface. Pull-quotes are used to attract attention, especially in
long articles.

{{ clear }}

Highlights
----------

:::{admonition} Docs
:class: docs margin dropdown

* [reStructuredText Directives > Highlights](https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights)
* [Docutils > Directives > highlights](https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights)

:::

Highlights summarize the main points of a document or section, often consisting
of a list. Use the `{highlights}` directive to add one.

```{highlights}

**What to Know**

* Highlights summarize the main points of a document or section, often in list form.
* Keep the length to no more than five lines.
* Each Highlight should be no more than 85 characters, including spaces.
* Consider the reader - Highlights are the first thing they'll see.

```

Topic
-----

:::{admonition} Docs
:class: docs margin dropdown

* [Docutils > Directives > topic](https://docutils.sourceforge.io/docs/ref/rst/directives.html#topic)

:::

Use the `{topic}` directive to indicate a self-contained idea that is separate
from the flow of the document.

```{topic} By the way

Here is something else to think about.
```

Parsed Literals
---------------

:::{admonition} Docs
:class: docs margin dropdown

* [reStructuredText Directives > Parsed Literal Block](https://docutils.sourceforge.io/docs/ref/rst/directives.html#parsed-literal-block)
* [Docutils > Directives > parsed literal block](https://docutils.sourceforge.io/docs/ref/rst/directives.html#parsed-literal)

:::

Rendered like a literal block/block quote, but the markdown is parsed. Parsed
literal blocks are useful for adding hyperlinks to code examples.

```{parsed-literal}
Download at [http://someurl/release-0.1.0.tar-gz](http://someurl/release-0.1.0.tar-gz).
```

Compound Paragraph
------------------

:::{admonition} Docs
:class: docs margin dropdown

* [Docutils > Directives > Compound Paragraph](https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights)

:::

In the example below, a literal block is embedded within a sentence that begins
in one physical paragraph and ends in another.

***

`````{compound}

The 'rm' command is very dangerous.  If you are logged
in as root and enter:

    cd /
    rm -rf *

you will erase the entire contents of your file system.

`````

***

Line Blocks
-----------

:::{admonition} Docs
:class: docs margin dropdown

* [Docutils > Line Blocks](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#line-blocks)
* [Sphinx > reStructuredText Primer > Lists and Quote-like blocks](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks)
* [Pandoc > Line blocks](https://pandoc.org/MANUAL.html#line-blocks)

:::

Line blocks, where each line is prefaced by a bar (`|`), are useful for address
blocks, verse (poetry, song lyrics), and unadorned lists, where the structure
of lines is significant. They preserve line breaks and indentation in text and
support inline markup.

They are not supported by `myst` and so must be in an `{eval-rst}` directive.

***

```{eval-rst}

| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical

```
