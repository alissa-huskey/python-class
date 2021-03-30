Functions
=========

A function is a set of Python instructions or {term}`statements <statement>` that can be
executed later.

Defining functions
------------------

Functions are {term}`compound-statements`, and are made up of an
{term}`identifier` and the group of {term}`statements` it contains.

```{code-block} python
---
caption: the identifer is `hello`
---
def hello():
  print("Hello.")
```

Calling functions
-----------------

To {term}`call` or execute a function, use the function {term}`identifier`
followed by `(``)`.

```{code-block} python
---
caption: executes `print("Hello.")`
---
hello()
```

Parameters and arguments
------------------------

Functions can be written to accept data as one or more {term}`parameters` separated by `,`.

```{code-block} python
---
caption: defined with one parameter, `name`.
---
def hello(name):
  print("Hello", name, ".")
```

```{code-block} python
---
caption: defined with two parameters, `first_name` and `last_name`.
---
def formal_greeting(first_name, last_name):
  print("Dear", first_name, last_name, ",")
```

When calling the function the values passed are called {term}`arguments`.

Put the values you wish to send to the function inside the parenthesis
separated by `,`. When the function is executed the argument(s) will be
assigned to variables with the same names as the parameters in the function
definition.

```{code-block} python
---
---
hello("John")
hello("Mary")

formal_greeting("John", "Smith")
formal_greeting("Jane", "Doe")
```

Returning values
----------------

Functions can {term}`return` a value.

```{code-block} python
---
caption: returns instead of printing
---

def formal_greeting(first_name, last_name):
  return "Dear" + first_name + last_name + ","
```

```{code-block} python
---
caption: Now the return value can be assigned to a variable, or used anywhere else we need an expression.
---

greeting = formal_greeting("John", "Smith")
print(formal_greeting("Jane", "Doe"))
```

% [ ] returning multiple values
% [ ] default arguments
% [ ] keyword arguments
% [ ] arbitrary argument list
% [ ] arbitrary keyword argument list
% [ ] unpacking arguments
% [ ] docstrings
% [ ] annotations


