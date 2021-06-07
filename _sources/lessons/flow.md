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
Program Flow
============

In this lesson we are going to do an exercise seeing code the way that Python
does. We're going to do this by pretending that as Python {term}`executes` each
{term}`statement`, it is playing a video game.


Review
------

* [](variables.md)
* [](functions.md)

If Python was a game
--------------------

### Assigning Variables

```{image} assets/zelda-inventory.jpg
---
alt: inventory
align: left
---
```

If executing Python was like playing a video game, the step of assigning
variables would be like collecting inventory.

Let's walk through the following example code.

```{div} clear
.
```


````{sidebar} Game
---
class: game-info
---
```{admonition} **Your Inventory**
---
class: inventory
---

|            |              |
|-----------:|--------------|
| `character`| `Mario`     |
| `coins`    | `25`         |
| `potions`  | `5`          |
| `objects`  | - `iron key` |
```
````

```{code-block} python
---
linenos:
---
character = "Mario"
coins = 25
potions = 5
objects = [
    "iron key",
]
```

### Defining functions

```{image} assets/breath-of-fire-skills.png
---
alt: skills
align: left
---
```

If executing Python was like playing a video game, the step of defining
functions would be like acquiring skills or abilities.

Let's walk through an example.


```{div} clear
.

```
````{sidebar} Game
---
class: game-info
---
```{admonition} **Your Inventory**
---
class: inventory
---

|            |              |
|-----------:|--------------|
| `character`| `Mario`     |
| `coins`    | `25`         |
| `potions`  | `5`          |
| `objects`  | - `iron key` |
```

```{admonition} **Your Skills**

|                           |
|---------------------------|
| `hide()`                  |
| `pick_up(`*`object`*:` str)`  |
```
````

```{code-block} python
---
linenos:
---
character = "Mario"
coins = 25
potions = 5
objects = [
    "iron key",
]

def hide():
  print("You cast a concealment spell. *poof* Nobody can see you")

def pick_up(name):
  objects.append(name)
  print("You picked up a", name, ".")


```


### Calling functions


If executing Python was like playing a video game, the step of calling
functions would be like using your skills or abilities.

Let's walk through an example.


````{sidebar} Game
---
class: game-info
---
```{admonition} **Your Inventory**
---
class: inventory
---

|            |              |
|-----------:|--------------|
| `character`| `Mario`     |
| `coins`    | `25`         |
| `potions`  | `5`          |
| `objects`  | - `iron key` |
```

```{admonition} **Your Skills**

|                           |
|---------------------------|
| `hide()`                  |
| `pick_up(`*`object`*:` str)`  |
```

```{admonition} **Your activity**

|    |                                                                    |
|----|--------------------------------------------------------------------|
|  1 | You cast a concealment spell. *poof* Nobody can see you            |
```

````

```{code-block} python
---
linenos:
---
character = "Mario"
coins = 25
potions = 5
objects = [
    "iron key",
]

def hide():
  print("You cast a concealment spell. *poof* Nobody can see you")

def pick_up(name):
  objects.append(name)
  print("You picked up a", name, ".")

hide()
```

The `"You cast a spell..."` message doesn't get printed until you {term}`call`
the function on line `15`.

### Calling more functions

````{sidebar} Game
---
class: game-info
---
```{admonition} **Your Inventory**
---
class: inventory
---

|            |              |
|-----------:|--------------|
| `character`| `Mario`     |
| `coins`    | `25`         |
| `potions`  | `5`          |
| `objects`  | - `iron key` |
|            | - `silver key` |
|            | - `spellbook` |
```

```{admonition} **Your Skills**

|                           |
|---------------------------|
| `hide()`                  |
| `pick_up(`*`object`*:` str)`  |
```

```{admonition} **Your activity**

|    |                                                                    |
|----|--------------------------------------------------------------------|
|  1 | You cast a concealment spell. *poof* Nobody can see you            |
|  2 | You picked up a silver key.                                        |
|  3 | You picked up a spellbook.                                         |
```

````

```{code-block} python
---
linenos:
---
character = "Mario"
coins = 25
potions = 5
objects = [
    "iron key",
]

def hide():
  print("You cast a concealment spell. *poof* Nobody can see you")

def pick_up(name):
  objects.append(name)
  print("You picked up a", name, ".")

hide()
pick_up("silver key")
pick_up("spellbook")
```

The `pick_up` function changed the value of the `objects` variable.


### Referencing variables

````{sidebar} Game
---
class: game-info
---
```{admonition} **Your Inventory**
---
class: inventory
---

|            |              |
|-----------:|--------------|
| `character`| `Mario`     |
| `coins`    | `25`         |
| `potions`  | `5`          |
| `objects`  | - `iron key` |
|            | - `silver key` |
|            | - `spellbook` |
```

```{admonition} **Your Skills**

|                           |
|---------------------------|
| `hide()`                  |
| `pick_up(`*`object`*:` str)`  |
```

```{admonition} **Your activity**

|    |                                                                    |
|----|--------------------------------------------------------------------|
|  1 | You cast a concealment spell. *poof* Nobody can see you            |
|  2 | You picked up a silver key.                                        |
|  3 | You picked up a spellbook.                                         |
|  4 | Mario has finished Level One.                                      |
```

````

```{code-block} python
---
linenos:
---
character = "Mario"
coins = 25
potions = 5
objects = [
    "iron key",
]

def hide():
  print("You cast a concealment spell. *poof* Nobody can see you")

def pick_up(name):
  objects.append(name)
  print("You picked up a", name, ".")

hide()
pick_up("silver key")
pick_up("spellbook")

print(character, "has finished Level One.")
```

An action is preformed on a variable when it is referenced. So even though the
`character` variable is assigned on line `1`, it isn't referenced until line `19`.

