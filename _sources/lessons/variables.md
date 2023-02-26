Variables
=========

A {term}`variable` is a container for storing data.

Variables are made up of an {term}`identifier` and a {term}`value`. The
identifier is the name, and the value is the data that is holds.

To create a variable simply *assign* a value to it it, using the `=` operator.

```{code-block} python
---
caption: The identifiers are `x` and `name`.
---
x = 5
name = "John"
```

To {term}`reference` a variable, or retrieve the data you stored, use the variable name.

```{code-block} python
y = x + 3
print("Hello", name)
```

