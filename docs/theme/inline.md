Inline Markdown
===============

Text formatting
---------------

```{role} python(code)
:language: python
```

| Rendered                       | Name                   |
|--------------------------------|------------------------|
| `a=1`                          | literal                |
| **strong**                     | bold                   |
| *emphasis*                     | italic                 |
| ~~strike~~                     | strikethrough          |
| $z=\sqrt{x^2+y^2}$             | math equation          |
| {sub}`subscript`               | subscript role         |
| {sup}`subscript`               | superscript role       |
| {samp}`text {variable}`        | sample role            |
| {guilabel}`this label`         | guilabel role          |
| {kbd}`⌘M`                      | kbd role               |
| {menuselection}`Menu --> item` | menuselection role     |
| {abbr}`abbr (explanation)`     | abbr role              |
| {python}`print("abc")`         | user-defined code role |
| <mark>highlighted</mark>       | mark tag               |
| <del>deleted</del>             | del tag                |
| <ins>inserted</ins>            | ins tag                |
| <small>small</small>           | small tag              |
| {term}`Variable`               | term                   |
| {term}`Missing Term`           | missing term           |
% |                                |                        |


Links & References
------------------

| Rendered                    | Name                 | Links To            |
|-----------------------------|----------------------|---------------------|
| [hyperlink](#)              | hyperlink            | hyperlink           |
| [^f] footnote               | footnote             | footnote            |
| {term}`text <anchor>`       | term role            | glossary definition |
| {PEP}`288`                  | PEP role             | PEP                 |
| {rfc}`2282`                 | RFC role             | RFC                 |
| {download}`inline.md`       | download role        | download file       |
| {eq}`math-example`          | eq  role             | math equation       |
| {title-reference}`title`    | title-reference role | internal title      |
| {manpage}`program(section)` | manpage              | external manpage    |
% |                             |                      |                     |

[^f]: #

Semantic Roles
--------------

| Rendered                      | Role       | Description                         |
|-------------------------------|------------|-------------------------------------|
| {command}`rm`                 | command    | os level command                    |
| {dfn}`label`                  | dfn        | term without index entry            |
| {file}`/bin/{$SHELL}`         | file       | file or directory                   |
| {mailheader}`Content-Type`    | mailheader | RFC 822-style mail header           |
| {makevar}`help`               | makevar    | make variable                       |
| {mimetype}`text/plain`        | mimetype   | MIME type name                      |
| {newsgroup}`comp.lang.python` | newsgroup  | Usenet newsgroup                    |
| {program}`curl`               | program    | executable program                  |
| {regexp}`([abc])+`            | regexp     | regular expression                  |
|                               |            |                                     |

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
* [Sphinx > Roles > Standard Roles](https://docutils.sourceforge.io/docs/ref/rst/roles.html#standard-roles)

:::
