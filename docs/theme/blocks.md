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

Block quotes consist text indented 4 spaces or a tab.

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Epigraph
--------

<https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph>

:::{epigraph}

My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
as follows and begins now.  All brontosauruses are thin at one
end, much much thicker in the middle and then thin again at the
far end.  That is my theory, it is mine, and belongs to me and I
own it, and what it is too.

-- Anne Elk (Miss)
:::

Pull quotes
-----------

<https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote>

```{pull-quote}

My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
as follows and begins now.  All brontosauruses are thin at one
end, much much thicker in the middle and then thin again at the
far end.  That is my theory, it is mine, and belongs to me and I
own it, and what it is too.

-- Anne Elk (Miss)
```


Highlights
----------

<https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights>

```{highlights}

My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
as follows and begins now.  All brontosauruses are thin at one
end, much much thicker in the middle and then thin again at the
far end.  That is my theory, it is mine, and belongs to me and I
own it, and what it is too.

-- Anne Elk (Miss)
```

Literal Blocks
--------------

<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#literal-blocks>

Contains a block of text where line breaks and whitespace are significant and
must be preserved.

This is a normal text paragraph. The next paragraph is a code sample:

    It is not processed in any way, except
    that the indentation is removed.

    It can span multiple lines.

This is a normal text paragraph again.

They can be quoted without indentation:

Quoted Text
-----------

> Great idea!
>
> Why didn't I think of that?

Parsed Literals
---------------

<https://docutils.sourceforge.io/docs/ref/rst/directives.html#parsed-literal-block>

It is equivalent to a line block with different rendering: typically in a
typewriter/monospaced typeface, like an ordinary literal block. Parsed literal
blocks are useful for adding hyperlinks to code examples.

```{parsed-literal}
Download at [http://someurl/release-0.1.0.tar-gz](http://someurl/release-0.1.0.tar-gz).
```
