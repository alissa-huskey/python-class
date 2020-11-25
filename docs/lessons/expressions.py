# %% [markdown]

# # Fundamentals: Expressions

# An *expression* is a unit of code that can be solved to a single value.

# This process is called *evaluating* the expression.

# Take the following simple expression that resolves to `30`.


# %% 1

10 * 3

# %% [markdown]

# It is comprised of:
#
# * the *left-hand value* (*LHV*)
# * an *operator*
# * the *right-hand value* (*RHV*)

# %% 2
# LHV    Operator   RHV
10       *          3

# %% [markdown]

# An *operator* is a symbol with special meaning that tells Python to do
# something. Some examples of operators include `+`, `=`, and `==`.
#
#  When an expression includes an operator involved in Python, there is always a
#  *left-hand value* and a *right-hand value*.

# Let's take a more complicated example.

# %% 3

2 + 3 * 6

# %% [markdown]

# In this case we have 2 operators: `+` and `*`. So then which is the left-hand
# value, and which the right-hand?

# The answer is that Python evaluates this the same way we would solve a math
# problem. That is, it breaks it down into multiple expressions.

# %% 4

# Expression 1: (3 * 6)
#   LHV    Operator   RHV
2 + 3      *           6

# Expression 2: (2 + 18)
# LHV    Operator   RHV
2        +          18

# %% [markdown]

# Here are some examples of expressions

# %% 5

3                        # a stand-alone vaue is the simplest expression
"hello"                  # a stand-alone string value
today = 16               # evaluates to 16
today                    # a variable
yesterday = today - 1    # two expressions: #1: today - 1, #2: yesterday = 15
input()                  # functions with a return value also evaluate to a value

# %% [markdown]

# Anywhere that we can use a value, we can also use an expression. Python will
# first evaluate the expression, then use the resulting value in its place.

# %% 6

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

# %% [markdown]

# ## Self-Quiz


# %% [markdown]
# 1. What is the operator in this expression?

# %%
"hello " * 3

# %% [markdown]
# 2. If the value of `name` is `"Joe"`, what is the argument that is sent to the `print()` function?

# %%
print("Hello " + name)

# %% [markdown]
# 3. What does the following expression evaluate to?

# %%
1 == 2

# %% [markdown]

## Today we learned

# * **value**: a piece of data or information
# * **expression**: a unit of code that can be solved to a single value
# * **evaluate**: the process of solving an expression to its resulting value
# * **left-hand value**: the value to the left of an operator
# * **right-hand value**: the value to the right of an operator
# * **operator**: a symbol that has special meaning, telling Python to do something with the values on either side
