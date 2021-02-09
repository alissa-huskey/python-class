#!/usr/bin/env python
"""generate reading-code.md"""

from string import Template
from pathlib import Path

from tabulate import tabulate
from more_itertools import padded, always_iterable


CODE = """
total = 0
i = 0
while i < 3:
    print("loop", i)
    total = total + i
    i = i + 1
print("The total is:", total)
"""

SECTION = """
% =====================================
% START $COMMENT_TITLE
% -------------------------------------

% ~~~~~~~~~~~~~
% start sidebar
% ~~~~~~~~~~~~~

`````{sidebar} $TITLE

% start context -----------------------

```{admonition} variables

$VARS

```

% evaluation steps --------------------

```{code-block} python
:caption: steps to evaluate line
:class: full-width
$STEPS
```

% output ------------------------------

```{panels}
:container: m-0 p-0
:body: text-monospace text-white bg-dark
:card: shadow-none m-0 p-0
:footer: text-white-50 bg-secondary

$OUTPUT

++++++++++++++
output
```

`````

% ~~~~~~~~~~~
% end sidebar
% ~~~~~~~~~~~

% code --------------------------------

```{code-block} python
:linenos:
:emphasize-lines: $LINE, $LINE
$CODE
```

{{clear}}

---

% -------------------------------------
% END $COMMENT_TITLE
% =====================================

"""

PAGE = """
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
$TITLE
============

$CONTENTS
"""

def mksteps(steps: list=[]) -> str:
    """
    Return string of ">>> " prefaced lines for for each member of steps

    Examples
    --------
    >>> mksteps(["total = total + i", "total = 0 + 0", "total = 0"])
    '>>> total = total + i\n>>> total = 0 + 0\n>>> total = 0'
    """
    return "\n".join([f">>> {step}" for step in steps])


def mkvars(values: dict={}) -> str:
    """Return generated GHF markdown table for a dictionary of variables or *none*

    Examples
    --------
    >>> mkvars({})
    "*none*"
    >>> print(mkvars({"total": 0, "i": 0}))
    |          |        |
    |----------|--------|
    | `total`  |  `0`   |
    | `i`      |  `0`   |
    """

    if not values:
        return "*none*"

    headers = [""] * len(values)
    table = []

    for key, value in values.items():
        table.append([f"`{key}`", f"`{value!r}`"])

    return tabulate(table, headers, tablefmt="github")

def mktitle(line, loop=None) -> str:
    """."""
    if loop != None:
        return f"loop {loop}, line {line}"
    else:
        return f"line {line}"

def mkoutput(lines: list=[]) -> str:
    """Return the markdown for a list of output lines, with new lines bolded

    Params
    ------
    lines (list[str,tuple[str, bool]]): a list of lines to print
                                       either strings for old liens
                                       or (str, True) for new lines

    Examples
    --------
    >>> mkoutput(["a", "b", "c"])
    'a\n\nb\n\nc'
    >>> mkoutput([("hello", False), ("goodbye", True)])
    'hello\n\n**world**'
    >>> mkoutput(["hello", ("goodbye", True)])
    'hello\n\n**world**'
    """
    if not lines:
        return "&nbsp;"
    args = [list(padded(always_iterable(line), False, 2)) for line in lines]
    text = [f"**{line[0]}**" if line[1] else str(line[0]) for line in args]
    return "\n\n".join(text)

def mksection(line, code, loop=None, output=[], steps=[], variables={}):
    """Generate the markdown for one line of code from a code sample

    Params
    ------
    line (int): the line number to emphaesize
    code (str): the code sample
    output (str): the lines of output to print
    steps (list[str]): the steps to evaluate the line
    variables (dict): the variables when this line is executed
    """

    tpl = Template(SECTION.strip())
    markdown = tpl.substitute(dict(
        LINE=line,
        COMMENT_TITLE=mktitle(line, loop).upper(),
        TITLE=mktitle(line, loop),
        CODE=code,
        OUTPUT=mkoutput(output),
        STEPS=mksteps(steps),
        VARS=mkvars(variables)
    ))
    return markdown + "\n"

def mkpage(filename, code, *sections):
    """."""
    with open(filename) as fp:
        page = fp.read()

    tpl = Template(page.strip())
    sections = [mksection(kwargs.pop("line"), code, **kwargs) for kwargs in sections]
    return tpl.substitute(dict(
        CONTENTS="\n".join(sections),
    ))


def main():
    """."""
    markdown = mkpage(
        "reading-code.tpl.md",
        CODE,
        dict(line=1, steps=["total = 0"]),
        dict(line=2, variables={"total": 0}, steps=["i = 0"]),
        dict(loop=0, line=3, variables={"total": 0, "i": 0}, steps=[
            "i < 3",
            "0 < 3  # True, so go to line 4"
            "True  # True, so go to line 4"
        ]),
        dict(loop=0, line=4, variables={"total": 0, "i": 0},
             steps=[
                'print("loop", i)',
                'print("loop", 0)'
            ],
            output=[ ("loop 0", True) ]
        ),
        dict(loop=0, line=5, variables={"total": 0, "i": 0},
             steps=[
                "total = total + i",
                "total = 0 + 0",
                "total = 0"
            ],
            output=[ "loop 0" ]
        ),
        dict(loop=0, line=6,
             variables={
                "total": 0,
                "i": 0},
            steps=[
                "i = i + 1",
                "i = 0 + 1",
                "i = 1",
                "# end of loop, go to line 3",
            ],
            output=[ "loop 0" ]
        ),
        dict(loop=1, line=3,
             variables={
                "total": 0,
                "i": 1},
            steps=[
                "i < 3",
                "1 < 3  # True, so go to line 4",
                "True  # True, so go to line 4",
            ],
            output=[ "loop 0" ]
        ),
        dict(loop=1, line=4, variables={"total": 0, "i": 1},
             steps=[
                'print("loop", i)',
                'print("loop", 1)'
            ],
            output=[ "loop 0", ("loop 1", True) ]
        ),
        dict(loop=1, line=5,
             variables={
                "total": 0,
                "i": 1},
            steps=[
                "total = total + i",
                "total = 0 + 1",
                "total = 1",
            ],
            output=[ "loop 0", "loop 1" ]
        ),
        dict(loop=1, line=6,
             variables={
                "total": 1,
                "i": 1},
            steps=[
                "i = i + 1",
                "i = 1 + 1",
                "i = 2",
                "# end of loop, go to line 3",
            ],
            output=[ "loop 0", "loop 1" ]
        ),
        dict(loop=2, line=3,
             variables={
                "total": 1,
                "i": 2},
            steps=[
                "i < 3",
                "2 < 3  # True, go to line 4",
                "True  # True, go to line 4",
            ],
            output=[ "loop 0", "loop 1" ]
        ),
        dict(loop=2, line=4, variables={"total": 1, "i": 2},
             steps=[
                'print("loop", i)',
                'print("loop", 2)'
            ],
            output=[ "loop 0", "loop 1", ("loop 2", True) ]
        ),
        dict(loop=2, line=5,
             variables={
                "total": 1,
                "i": 2},
            steps=[
                "total = total + i",
                "total = 1 + 2",
                "total = 3",
            ],
            output=[ "loop 0", "loop 1", "loop 2" ]
        ),
        dict(loop=2, line=6,
             variables={
                "total": 3,
                "i": 2},
            steps=[
                "i = i + 1",
                "i = 2 + 1",
                "i = 3",
                "# end of loop, go to line 3"
            ],
            output=[ "loop 0", "loop 1", "loop 2" ]
        ),
        dict(loop=3, line=3,
             variables={
                "total": 3,
                "i": 3},
            steps=[
                "i < 3",
                "3 < 3",
                "False  # False, so go to line 7",
            ],
            output=[ "loop 0", "loop 1", "loop 2" ]
        ),
        dict(line=7,
             variables={
                "total": 3,
                "i": 3},
            steps=[
                'print("The total is:", total)',
                'print("The total is:", 3)'],
            output=[ "loop 0", "loop 1", "loop 2", ("The total is: 3", True) ]
            ),
    )
    print(markdown)


main()
