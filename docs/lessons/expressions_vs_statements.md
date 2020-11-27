Expressions vs. Statements 
==========================

An expression is any piece of code that evaluates to a value.

A statement is a logical line of code or group of statements that gives
instructions to Python.

The difference can be confusing, especially since in Python there is a fair bit
of overlap.

One way to think of it is:

  * if you can save the the result of the code to a variable, then it is an expression
  * if the result of the code causes something to happen it is a statement

The string `"hello"` on a line by itself is does not cause anything to
happen, therefore it is not a statement. Whereas `message = "hello"` causes the
variable `message` to be assigned the value `"hello"`.

A function call may or may not be an expression. But a function call on a line
by itself is always a valid statement, since it causes the statements inside
the function to be executed.

````{panels}
Expressions
^^^
evaluated

resolves to a value

smallest unit is a single literal value

are sometimes statements

can contain expressions

cannot contain statements

---

Statements
^^^

executed

an instruction to Python

smallest unit is a logical line of code

are sometimes expressions

can contain expressions

contain statements when compound

---

Expressions
^^^

include:
- literal values
- variables
- the result of an operator between values
- subscripting a list or dict using `[` `]`

may include:
- function calls

---

Statements
^^^

include:
- assignments
- function calls
- lines that start with non-operator keywords


---

Expressions
^^^

```python
5
```

```python
random
```

```python
random.randint(1, 10)
```

```python
[1, 2, 3]
```

```python
"Last index:"
len(nums) - 1
```

```python
num % 2 == 0

```

```python
is_even(1)
```
---

Statements
^^^

<div class="break"><br></div>

```python
import random
```

```python
random.randint(1, 10)
```

```python
nums = [1, 2, 3]
```

```python
print("Last index:", len(nums) - 1)

```

```python
def is_even(num):
  return num % 2 == 0
```

```python
is_even(1)
```
````


