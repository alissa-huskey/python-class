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
|                                |                        |
|                                |                        |


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
|                             |                      |                     |

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
