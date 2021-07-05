Expressions
===========

An {term}`expression` is a unit of code that can be solved to a single value.

This process is called {term}`evaluating` the expression.

Take the following simple expression that resolves to `30`.

```python
10 * 3
```

It is comprised of:

* the {term}`left-hand value` ({term}`LHV`)
* an {term}`operator`
* the {term}`right-hand value` ({term}`RHV`)

```python
# LHV    Operator   RHV
10       *          3
```

An {term}`operator` is a symbol with special meaning that tells Python to do
something. Some examples of operators include `+`, `=`, and `==`.

When an expression includes an operator involved in Python, there is always a
{term}`left-hand value` and a {term}`right-hand value`.

Let's take a more complicated example.

```python
2 + 3 * 6
```

In this case we have 2 operators: `+` and `*`. So then which is the left-hand
value, and which the right-hand?

The answer is that Python evaluates this the same way we would solve a math
problem. That is, it breaks it down into multiple expressions.

```python
# Expression 1: (3 * 6)
#   LHV    Operator   RHV
2 + 3      *           6

# Expression 2: (2 + 18)
# LHV    Operator   RHV
2        +          18
```

Here are some examples of expressions

```python
3                        # a stand-alone vaue is the simplest expression
"hello"                  # a stand-alone string value
today                    # a variable (when assigned)
yesterday = today - 1    # two expressions: #1: today - 1, #2: yesterday = 15
input()                  # functions with a return value also evaluate to a value
```

Anywhere that we can use a value, we can also use an expression. Python will
first evaluate the expression, then use the resulting value in its place.

```python
# using stand-alone values
print(3)
print("hello")
print(yesterday)

# first, evaluates today-1
# then sends 15 as an argument to print()
print(today-1)

# first calls the input() function and waits for the user response
# then sends the result to print()
print(input())
```

Self-Quiz
---------

1. What is the operator in this expression?

```python
"hello " * 3
```

2. If the value of `name` is `"Joe"`, what is the argument that is sent to the `print()` function?

```python
print("Hello " + name)
```


3. What does the following expression evaluate to?

```python
1 == 2
```

Reference
---------

### Glossary

```{glossary} expressions

evaluate
  the process of solving an expression to its resulting value

expression
  a unit of code that can be solved to a single value

left-hand value
  the value to the left of an operator

operator
  A symbol with special meaning that tells the computer to do something (for
  example `=`, `+`, or `==`).

right-hand value
  the value to the right of an operator

value
  a piece of data or information {term}`strings`, {term}`integers` and more.

```

### More info

* [The Python Language Reference » Expressions](https://docs.python.org/3/reference/expressions.html)
