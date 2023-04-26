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

Block Quotes
------------

* [CommonMark Spec > 4.4 Indented code blocks](https://spec.commonmark.org/current/#indented-code-blocks)
* [Bootstrap > Typography > Blockquotes](https://getbootstrap.com/docs/5.0/content/typography/#blockquotes)
* [Bootstrap > Reboot > Block Quote](https://getbootstrap.com/docs/5.0/content/reboot/#blockquote)
* [Jupyter Book > Quotations](https://jupyterbook.org/en/stable/content/content-blocks.html#quotations)
* [Sphinx > rst > Literal blocks](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-doctest-blocks)

Block quotes or literal blocks contain a block of text where line breaks and
whitespace are significant and must be preserved. It is not processed in any
way, except that the indentation is removed. It can span multiple lines.

Block quotes consist text indented 4 spaces or a tab.

    -a            command-line option "a"
    -b file       options can have arguments
                  and long descriptions
    --long        options can be long also
    --input=file  long options can also have
                  arguments

    --very-long-option
                  The description can also start on the next line.

                  The description may contain multiple body elements,
                  regardless of where it starts.

    -x, -y, -z    Multiple options are an "option group".
    -v, --verbose  Commonly-seen: short & long options.
    -1 file, --one=file, --two file
                  Multiple options with arguments.
    /V            DOS/VMS-style options too

Quoted Text
-----------

* [reStructuredText Spec > Quoted Literal Blocks](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#quoted-literal-blocks)
* [Jupyter Book > Quotations](https://jupyterbook.org/en/stable/content/content-blocks.html?highlight=quote#quotations)

Regular quotations are controlled with standard Markdown syntax, i.e., by
inserting a caret (>) symbol in front of one or more lines of text.

> “All that is gold does not glitter,
> Not all those who wander are lost;
> The old that is strong does not wither,
> Deep roots are not reached by the frost.
>
> From the ashes a fire shall be woken,
> A light from the shadows shall spring;
> Renewed shall be blade that was broken,
> The crownless again shall be king.”
>
> ― J.R.R. Tolkien, The Fellowship of the Ring

Epigraph
--------

* [reStructuredText Directives > Epigraph](https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph)
* [Jupyter Book > Epigraphs](https://jupyterbook.org/en/stable/content/content-blocks.html#epigraphs)
* [Docutils > Directives > epigraph](https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph)

:::{epigraph}

Turning and turning in the widening gyre \
The falcon cannot hear the falconer; \
Things fall apart; the centre cannot hold; \
Mere anarchy is loosed upon the world.

:::

Pull-Quotes
-----------

* [reStructuredText Directives > Pull-Quote](https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote)
* [Docutils > Directives > pull-quote](https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote)

```{pull-quote}

"Pull-quotes are a great way to add visual interest and excitement to your
layout."

```


Highlights
----------

* [reStructuredText Directives > Highlights](https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights)
* [Docutils > Directives > highlights](https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights)

```{highlights}

**What to Know**

* Highlights summarize the main points of a document or section, often in list form.
* Keep the length to no more than five lines.
* Each Highlight should be no more than 85 characters, including spaces.
* Consider the reader - Highlights are the first thing they'll see.

```

Parsed Literals
---------------

* [reStructuredText Directives > Parsed Literal Block](https://docutils.sourceforge.io/docs/ref/rst/directives.html#parsed-literal-block)
* [Docutils > Directives > parsed literal block](https://docutils.sourceforge.io/docs/ref/rst/directives.html#parsed-literal)

Rendered like a literal block/block quote, but the markdown is parsed. Parsed
literal blocks are useful for adding hyperlinks to code examples.

```{parsed-literal}
Download at [http://someurl/release-0.1.0.tar-gz](http://someurl/release-0.1.0.tar-gz).
```

Compound Paragraph
------------------

* [Docutils > Directives > Compound Paragraph](https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights)

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

* [Docutils > Line Blocks](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#line-blocks)
* [Sphinx > reStructuredText Primer > Lists and Quote-like blocks](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks)
* [Pandoc > Line blocks](https://pandoc.org/MANUAL.html#line-blocks)

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
