Documentation
=============

envvar
------

* [Sphinx > The Standard Role > envvar](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#directive-envvar)

The `{envvar}` directive describes an environment variable.

```{envvar} SHELL
The shell of the current user.
```

program & option
----------------

* [Sphinx > The Standard Role > program](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#directive-program)
* [Sphinx > The Standard Role > option](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#directive-option)

The `{program}` and `{option}` directives, used together, document the options
for a given program.

```{program} rm
```

```{option} -r
Recursive.
```

object
------

* [Sphinx > The Standard Role > object](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#directive-object)

The `{object}` or `{describe}` directive formats the identifier and body the
same as other documentation without creating index enteries or cross-reference
targets.

```{object} PAPER
You can provide this value to select a paper size.
```

productionlist
--------------

* [Sphinx > Directives > Grammar production displays](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#grammar-production-displays)
* [Production Lists](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-productionlist)

The `{productionlist}` directive is for displaying the productions of a formal grammar.

```{eval-rst}
.. productionlist::
    try_stmt: try1_stmt | try2_stmt
    try1_stmt: "try" ":" `suite`
             : ("except" [`expression` ["," `target`]] ":" `suite`)+
             : ["else" ":" `suite`]
             : ["finally" ":" `suite`]
    try2_stmt: "try" ":" `suite`
             : "finally" ":" `suite`
             : "this-is-intentionally-very-stupidly-long-to-make-sure-that-this-has-a-proper-scrollbar"

```

Bibliography
------------

* [Jupyter Book > Get started with references > Bibliography](https://jupyterbook.org/en/stable/tutorials/references.html#bibliography)
* [BibTeX Format Description](http://www.bibtex.org/Format/)
* [Jupyter Book > Citations and bibliographies](https://jupyterbook.org/en/stable/content/citations.html)
* [sphinxcontrib-bibtex extension](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/)

The `{bibliography}` directive will generate the bibliography of all citations
in your book.

```{rubric} Bibliography
```

```{bibliography}
:all:
:style: unsrt
:list: enumerated
:enumtype: lowerroman
```
