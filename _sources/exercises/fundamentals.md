Program Flow Exercises
======================

Today we're going to write some code for game characters, working with the
concepts of {term}`variables<variable>` and {term}`functions<function>` that we
discussed last week.

Start by making a new file `character.py`. We're going to use the `random`
module today, so start off by importing it at the top of the file.

```{code_block} python
---
caption: character.py
---
import random
```

Variable assignment and reference
---------------------------------

Last week we discussed that...

* A {term}`variable` is like a storage container for data.
* To create a variable, you simply {term}`assign` a value to
  it, using the `=` operator. This is like adding an item to
  your inventory.
* To retrieve the stored information you {term}`reference` it using the
  variable name or {term}`identifier`.


Let's start by assigning two new variables:

* `name` a string (`str`)
* `level` an integer (`int`) that is a random number between `1` and `5`.

```{code_block} python
---
caption: character.py
---
import random

name = "Ash"
level = random.randint(1,5)
```
