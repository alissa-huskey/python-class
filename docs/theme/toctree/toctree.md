toctree directive
=================

* [Sphinx > Directives > toctree](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree)

The `{toctree}` directive inserts a recursive list of the specified documents
and headings using the document title as the entry name (unless otherwise
specified). The listed top-level documents are added as sub-headings to the
current page in the navigation.

Unlike the `{contents}` and `{tableofcontents}` directives, a `{toctree}` will
only include the documents listed, in the order they are listed. That is to
say, the top-level list of documents is not generated.

The `{toctree}` directive may have unexpected results when Jupyter Book builds
your book's contents. You cannot have a page listed in both a `{toctree}` and
the {file}`_toc.yml` file.

```{rubric} toctree
```

```{toctree}
:numbered:
page-a
page-e
Page Dee <page-d>
page-b
```
