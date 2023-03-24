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

:::{hlist}
:columns: 2
* [reStructuredText Spec > ](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#quoted-literal-blocks)
* [Jupyter Book > Quotations](https://jupyterbook.org/en/stable/content/content-blocks.html?highlight=quote#quotations)
:::

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

:::{epigraph}

Turning and turning in the widening gyre \
The falcon cannot hear the falconer; \
Things fall apart; the centre cannot hold; \
Mere anarchy is loosed upon the world.

:::

Pull-Quotes
-----------

* [reStructuredText Directives > Pull-Quote](https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote)

```{pull-quote}

"Pull-quotes are a great way to add visual interest and excitement to your
layout."

```


Highlights
----------

* [reStructuredText Directives > Highlights](https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights)

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

Rendered like a literal block/block quote, but the markdown is parsed. Parsed
literal blocks are useful for adding hyperlinks to code examples.

```{parsed-literal}
Download at [http://someurl/release-0.1.0.tar-gz](http://someurl/release-0.1.0.tar-gz).
```
