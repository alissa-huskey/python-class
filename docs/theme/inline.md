Inline Markdown
===============

Text formatting
---------------

% this is the user-defined python role used below
```{role} python(code)
:language: python
```

| Rendered                             | Name                                |
|--------------------------------------|-------------------------------------|
| `a=1`                                | literal                             |
| **strong**                           | bold                                |
| *emphasis*                           | italic                              |
| ~~strike~~                           | strikethrough                       |
| $z=\sqrt{x^2+y^2}$                   | math equation                       |
| {sub}`subscript`                     | [subscript][], sub role             |
| {sup}`subscript`                     | [superscript][], sup role           |
| {samp}`text {variable}`              | [sample][] role                     |
| <mark>highlighted</mark>             | mark tag                            |
| <del>deleted</del>                   | del tag                             |
| <ins>inserted</ins>                  | ins tag                             |
| <small>small</small>                 | small tag                           |
| {span}`Target <pst-color-bg-target>` | target                              |
| {python}`print("abc")`               | user-defined [code][] language role |
| {math}`z=\sqrt{x^2+y^2}`             | [math][] role                       |
% |                                      |                                     |

[subscript]: https://docutils.sourceforge.io/docs/ref/rst/roles.html#superscript
[superscript]: https://docutils.sourceforge.io/docs/ref/rst/roles.html#subscript
[sample]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-samp
[math]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-math
[code]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-code

Semantic Roles
--------------

The following roles format the text in a style specific to what the content of
the text signifies.

| Rendered                       | Role                   | Description               |
|--------------------------------|------------------------|---------------------------|
| {command}`rm`                  | [command][]            | os level command          |
| {dfn}`label`                   | [dfn][]                | term without index entry  |
| {file}`/bin/{$SHELL}`          | [file][]               | file or directory         |
| {mailheader}`Content-Type`     | [mailheader][]         | RFC 822-style mail header |
| {makevar}`HELP`                | [makevar][]            | make variable             |
| {mimetype}`text/plain`         | [mimetype][]           | MIME type name            |
| {newsgroup}`comp.lang.python`  | [newsgroup][]          | Usenet newsgroup          |
| {program}`curl`                | [program][]            | executable program        |
| {regexp}`([abc])+`             | [regexp][]             | regular expression        |
| {guilabel}`this label`         | [guilabel][]           | label from a user interface |
| {kbd}`⌘M`                      | [kbd][]                | sequence of keystrokes    |
| {menuselection}`Menu --> item` | [menuselection][]      | sequence of menu selections |
| {abbr}`abbr (explanation)`     | [abbreviation][], abbr | an abbreviation           |
| {acronym}`DTF`                 | [acronym][]            | an acronym                |
% |                                |                        |                           |

[abbreviation]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-abbr
[acronym]: https://docutils.sourceforge.io/docs/ref/rst/roles.html#acronym
[command]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-command
[dfn]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-dfn
[file]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-file
[mailheader]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-mailheader
[makevar]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-makevar
[mimetype]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-mimetype
[newsgroup]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-newsgroup
[program]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-program
[regexp]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-regexp
[guilabel]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-guilabel
[kbd]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-kbd
[menuselection]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-menuselection

Links & References
------------------

| Rendered                                           | Name                     | Links To                     |
|----------------------------------------------------|--------------------------|------------------------------|
|                                                    |                          |                              |
| [hyperlink](inline)                                | hyperlink                | hyperlink                    |
| [^f] footnote                                      | footnote]                | footnote                     |
| {term}`Variable <variable>`                        | [term][] role            | glossary definition          |
| {term}`Missing Term`                               | [unresolved term][]      | nothing                      |
| {PEP}`288`                                         | [PEP][] role             | PEP Specification            |
| {rfc}`2282`                                        | [RFC][] role             | RFC Specification            |
| {download}`inline.md`                              | [download][] role        | download file                |
| {eq}`math-example-a`                               | [eq][] role              | math directive target        | % links to math-example on directives page
| {title-reference}`Dune`                            | [title-reference][] role | book title from bibliography |
| {cite}`dune`                                       | [cite][] role            | internal title               |
| {manpage}`program(section)`                        | [manpage][] role         | external manpage             |
| {doc}`index`                                       | [doc][] role             | local document               |
| {envvar}`SHELL`                                    | [envvar][] role          | envvar directive target      |
| {keyword}`return`                                  | [keyword][] role         | python keyword               |
| {option}`rm -r`                                    | [option][] role          | option directive target      |
| {token}`try_stmt`                                  | [token][] role           | productionlist token target  |
|                                                    |                          |                              |
| [https://github.com/pydata/pydata-sphinx-theme/][] | [github][] link          | github url                   |
| [https://gitlab.com/gitlab-org/gitlab][]           | [gitlab][] link          | gitlab url                   |


[^f]: This is a footnote target

[term]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-term
[unresolved term]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-term
[PEP]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-pep
[RFC]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-rfc
[download]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-download
[eq]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-eq
[title-reference]: https://docutils.sourceforge.io/docs/ref/rst/roles.html#title-reference
[manpage]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-manpage
[doc]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-doc
[envvar]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-envvar
[keyword]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-keyword
[option]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-option
[token]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-token
[cite]: https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#role-cite
[https://github.com/pydata/pydata-sphinx-theme/]: https://github.com/pydata/pydata-sphinx-theme/
[https://gitlab.com/gitlab-org/gitlab]: https://gitlab.com/gitlab-org/gitlab
[github]: https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/theme-elements.html#link-shortening-for-git-repository-services
[gitlab]: https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/theme-elements.html#link-shortening-for-git-repository-services

See Also
--------

:::{seealso}

* [Myst Parser > Inline Tokens](https://myst-parser.readthedocs.io/en/latest/syntax/reference.html#span-inline-tokens)
* [Myst Parser > Extended Inline Tokens](https://myst-parser.readthedocs.io/en/latest/syntax/reference.html#extended-span-tokens)
* [Myst Parser > Commonmark Inline Tokens](https://myst-parser.readthedocs.io/en/latest/syntax/reference.html#commonmark-inline-tokens)
* [Bootstrap > Typography > Inline text elements](https://getbootstrap.com/docs/5.0/content/typography/#lead)
* [Bootstrap > Typography > Abbreviations](https://getbootstrap.com/docs/5.0/content/typography/#abbreviations)
* [Bootstrap > Reboot > Inline Code](https://getbootstrap.com/docs/5.0/content/reboot/#inline-code)
* [Bootstrap > Reboot > Variables](https://getbootstrap.com/docs/5.0/content/reboot/#variables)
* [Bootstrap > Reboot > User Input](https://getbootstrap.com/docs/5.0/content/reboot/#user-input)
* [Bootstrap > Reboot > Sample Output](https://getbootstrap.com/docs/5.0/content/reboot/#sample-output)
* [Bootstrap > Reboot > Inline Elements > abbr](https://getbootstrap.com/docs/5.0/content/reboot/#inline-elements)
* [Sphinx > The Standard Domain](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-standard-domain)
* [Sphinx > Roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html)
* [reStructuredText Interpreted Text Roles](https://docutils.sourceforge.io/docs/ref/rst/roles.html#standard-roles)

:::

TODO
----

* [token role](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-token)
