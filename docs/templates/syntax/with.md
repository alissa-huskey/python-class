`````{parsed-literal}
{samp}`with {EXPN} as {VAR}:`
    {samp}`    {BODY}`
`````

* `with` and `as` are {term}`keywords <keyword>`
* {samp}`{EXPN}` -- an expression that produces a context manager object (ie `open(...)`)
* {samp}`{VAR}` -- variable name for the object (ie `fh`)
* {samp}`{BODY}` -- statements that use {samp}`{VAR}`

