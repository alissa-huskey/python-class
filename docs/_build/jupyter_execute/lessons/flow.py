#!/usr/bin/env python
# coding: utf-8

# Program Flow
# ============
# 
# In this lesson we are going to do an exercise seeing code the way that Python
# does. We're going to do this by pretending that as Python {term}`executes` each
# {term}`statement`, it is playing a video game.
# 
# 
# Review
# ------
# 
# ### Variables
# 
# A {term}`variable` is a container for storing data.
# 
# Variables are made up of an {term}`identifier` and a {term}`value`. The
# identifer is the name, and the value is the data that is holds.
# 
# To create a variable simply *assign* a value to it it, using the `=` operator.
# 
# ```{code-block} python
# ---
# caption: The identifiers are `x` and `name`.
# ---
# x = 5
# name = "John"
# ```
# 
# To {term}`reference` a variable, or retrieve the data you stored, use the variable name.
# 
# ```{code-block} python
# y = x + 3
# print("Hello", name)
# ```
# 
# ### Functions
# 
# A function is a set of Python instructions or {term}`statements` that can be
# executed later.
# 
# Functions are {term}`compound-statements`, and are made up of an
# {term}`identifier` and the group of {term}`statements` it contains.
# 
# ```{code-block} python
# ---
# caption: the identifer is `hello`
# ---
# def hello():
#   print("Hello.")
# ```
# 
# To {term}`call` or execute a function, use the function identifier (name)
# followed by `(``)`.
# 
# ```{code-block} python
# ---
# caption: executes `print("Hello.")`
# ---
# hello()
# ```
# 
# Functions can be written to accept data as one or more {term}`arguments`, seperated by `,`.
# 
# ```{code-block} python
# ---
# caption: takes one argument, `name`.
# ---
# def hello(name):
#   print("Hello", name, ".")
# ```
# 
# 
# ```{code-block} python
# ---
# caption: takes two arguments, `first_name` and `last_name`.
# ---
# def formal_greeting(first_name, last_name):
#   print("Dear", first_name, last_name, ",")
# ```
# 
# When calling a function that accepts arguments, put the values inside the parenthesis.
# 
# ```{code-block} python
# ---
# ---
# hello("John")
# hello("Mary")
# 
# formal_greeting("John", "Smith")
# formal_greeting("Jane", "Doe")
# ```
# 
# 
# Functions {term}`return` a value, so that it can be used as an expression.
# 
# ```{code-block} python
# ---
# caption: returns instead of printing
# ---
# 
# def formal_greeting(first_name, last_name):
#   return "Dear" + first_name + last_name + ","
# ```
# ```{code-block} python
# ---
# caption: Now the return value can be assigned to a variable, or used anywhere else we need an expression.
# ---
# 
# greeting = formal_greeting("John", "Smith")
# print(formal_greeting("Jane", "Doe"))
# ```
# 
# If-Statements
# -------------
# 
# An {term}`if-statement` is a way to change what happens depending on the
# circumstances.
# 
# If-statements are compound statements, made up of the one or more
# {term}`conditions`, followed by the group of statements that belong to it.
# 
# ```{code-block} python
# ---
# linenos:
# ---
# if choice == "left":
#   print("You decide to take the path to the left.")
# elif choice == "right":
#   print("You decide to take the path to the right.")
# else:
#   print("Invalid choice.")
# ```
# 
# If Python was a game
# --------------------
# 
# ### Assigning Variables
# 
# ```{image} assets/zelda-inventory.jpg
# ---
# alt: inventory
# align: left
# ---
# ```
# 
# If executing Python was like playing a video game, the step of assigning
# variables would be like collecting inventory.
# 
# Let's walk through the following example code.
# 
# ```{div} clear
# .
# ```
# 
# 
# ````{sidebar} Game 
# ---
# class: game-info
# ---
# ```{admonition} **Your Inventory**
# ---
# class: inventory
# ---
# 
# |            |              |
# |-----------:|--------------|
# | `character`| `Mario`     |
# | `coins`    | `25`         |
# | `potions`  | `5`          |
# | `objects`  | - `iron key` |
# ```
# ````
# 
# ```{code-block} python
# ---
# linenos:
# ---
# character = "Mario"
# coins = 25
# potions = 5
# objects = [
#     "iron key",
# ]
# ```
# 
# ### Defining functions
# 
# ```{image} assets/breath-of-fire-skills.png
# ---
# alt: skills
# align: left
# ---
# ```
# 
# If executing Python was like playing a video game, the step of defining 
# functions would be like acquiring skills or abilities.
# 
# Let's walk through an example.
# 
# 
# ```{div} clear
# .
# 
# ```
# ````{sidebar} Game
# ---
# class: game-info
# ---
# ```{admonition} **Your Inventory**
# ---
# class: inventory
# ---
# 
# |            |              |
# |-----------:|--------------|
# | `character`| `Mario`     |
# | `coins`    | `25`         |
# | `potions`  | `5`          |
# | `objects`  | - `iron key` |
# ```
# 
# ```{admonition} **Your Skills**
# 
# |                           |
# |---------------------------|
# | `hide()`                  |
# | `pick_up(`*`object`*:` str)`  |
# ```
# ````
# 
# ```{code-block} python
# ---
# linenos:
# ---
# character = "Mario"
# coins = 25
# potions = 5
# objects = [
#     "iron key",
# ]
# 
# def hide():
#   print("You cast a concealment spell. *poof* Nobody can see you")   
# 
# def pick_up(name):
#   objects.append(name)
#   print("You picked up a", name, ".")   
# 
# 
# ```
# 
# 
# ### Calling functions
# 
# ```{image} assets/breath-of-fire-skills.png
# ---
# alt: skills
# align: left
# ---
# ```
# 
# If executing Python was like playing a video game, the step of calling
# functions would be like using your skills or abilities.
# 
# Let's walk through an example.
# 
# 
# ```{div} clear
# .
# 
# ```
# ````{sidebar} Game
# ---
# class: game-info
# ---
# ```{admonition} **Your Inventory**
# ---
# class: inventory
# ---
# 
# |            |              |
# |-----------:|--------------|
# | `character`| `Mario`     |
# | `coins`    | `25`         |
# | `potions`  | `5`          |
# | `objects`  | - `iron key` |
# ```
# 
# ```{admonition} **Your Skills**
# 
# |                           |
# |---------------------------|
# | `hide()`                  |
# | `pick_up(`*`object`*:` str)`  |
# ```
# 
# ```{admonition} **Your activity**
# 
# |    |                                                                    |
# |----|--------------------------------------------------------------------|
# |  1 | You cast a concealment spell. *poof* Nobody can see you            |
# ```
# 
# ````
# 
# ```{code-block} python
# ---
# linenos:
# ---
# character = "Mario"
# coins = 25
# potions = 5
# objects = [
#     "iron key",
# ]
# 
# def hide():
#   print("You cast a concealment spell. *poof* Nobody can see you")   
# 
# def pick_up(name):
#   objects.append(name)
#   print("You picked up a", name, ".")   
# 
# hide()
# ```
# 
# The `"You cast a spell..."` message doesn't get printed until you {term}`call`
# the function on line `15`.
# 
# ### Calling more functions
# 
# ````{sidebar} Game
# ---
# class: game-info
# ---
# ```{admonition} **Your Inventory**
# ---
# class: inventory
# ---
# 
# |            |              |
# |-----------:|--------------|
# | `character`| `Mario`     |
# | `coins`    | `25`         |
# | `potions`  | `5`          |
# | `objects`  | - `iron key` |
# |            | - `silver key` |
# |            | - `spellbook` |
# ```
# 
# ```{admonition} **Your Skills**
# 
# |                           |
# |---------------------------|
# | `hide()`                  |
# | `pick_up(`*`object`*:` str)`  |
# ```
# 
# ```{admonition} **Your activity**
# 
# |    |                                                                    |
# |----|--------------------------------------------------------------------|
# |  1 | You cast a concealment spell. *poof* Nobody can see you            |
# |  2 | You picked up a silver key.                                        |
# |  3 | You picked up a spellbook.                                         |
# ```
# 
# ````
# 
# ```{code-block} python
# ---
# linenos:
# ---
# character = "Mario"
# coins = 25
# potions = 5
# objects = [
#     "iron key",
# ]
# 
# def hide():
#   print("You cast a concealment spell. *poof* Nobody can see you")   
# 
# def pick_up(name):
#   objects.append(name)
#   print("You picked up a", name, ".")   
# 
# hide()
# pick_up("silver key")
# pick_up("spellbook")
# ```
# 
# The `pick_up` function changed the value of the `objects` variable.
# 
# 
# ### Referencing variables
# 
# ````{sidebar} Game
# ---
# class: game-info
# ---
# ```{admonition} **Your Inventory**
# ---
# class: inventory
# ---
# 
# |            |              |
# |-----------:|--------------|
# | `character`| `Mario`     |
# | `coins`    | `25`         |
# | `potions`  | `5`          |
# | `objects`  | - `iron key` |
# |            | - `silver key` |
# |            | - `spellbook` |
# ```
# 
# ```{admonition} **Your Skills**
# 
# |                           |
# |---------------------------|
# | `hide()`                  |
# | `pick_up(`*`object`*:` str)`  |
# ```
# 
# ```{admonition} **Your activity**
# 
# |    |                                                                    |
# |----|--------------------------------------------------------------------|
# |  1 | You cast a concealment spell. *poof* Nobody can see you            |
# |  2 | You picked up a silver key.                                        |
# |  3 | You picked up a spellbook.                                         |
# |  4 | Mario has finished Level One.                                      |
# ```
# 
# ````
# 
# ```{code-block} python
# ---
# linenos:
# ---
# character = "Mario"
# coins = 25
# potions = 5
# objects = [
#     "iron key",
# ]
# 
# def hide():
#   print("You cast a concealment spell. *poof* Nobody can see you")   
# 
# def pick_up(name):
#   objects.append(name)
#   print("You picked up a", name, ".")   
# 
# hide()
# pick_up("silver key")
# pick_up("spellbook")
# 
# print(character, "has finished Level One.")
# ```
# 
# An action is preformed on a variable when it is referenced. So even though the
# `character` variable is assigned on line `1`, it isn't referenced until line `19`.
