Given, When, Then
=================

```{contents}
:backlinks: top
:local:
```

```{margin}
:::{important}

Be sure to go through the [](testing.md) lesson first if you haven't already.

:::
```

Introduction
------------

Given/When/Then is part of the Behaviour Driven Development (BDD) methodology,
which is is an approach to developing interactive programs. It advocates a
test-first approach to software development where tests are from the
perspective of the end user and framed within the context of plain-English
specifications.

While there are entire frameworks to support Given/When/Then and other aspects
of BDD, for our purposes we will simply be using it as a structure for thinking
about and writing tests for interactive programs.

Given/When/Then
---------------

The Given/When/Then formula structures tests around a written description of
how your program is supposed to work.

It is comprised of the following sections:

* **Given**: the preconditions or context.
* **When**: the action or behavior you are testing.
* **Then**: what should happen or the observable results and effects.


```python
# GIVEN: The situation is...

# WHEN: This happens...

# THEN: I expect...
```

```python
# GIVEN today is Sunday
# WHEN I ask whether it's Friday yet
# THEN I should be told "Nope"
```

```python
# GIVEN that there are 99 bottles of beer on the wall
# WHEN you take one down
# THEN there should be 98 bottles of beer on the wall
```

```python
# GIVEN a certain scenario
# WHEN an action takes place
# THEN this should be the outcome.
```

```python
# GIVEN the door is open
# WHEN a person tries to enter
# THEN the person is inside
```

```python
# GIVEN the door is closed
# AND the door is locked
# BUT the person does not have a key
# WHEN the person tries to enter
# THEN the person is still outside
# AND the door is still closed
# AND the door is still locked
```

```python
# GIVEN the door is closed
# AND the door is locked
# AND the person has a key
# WHEN the person tries to enter
# THEN the person is inside
# AND the door is unlocked
```



```python
# WHEN you call add() with two numbers
# THEN the sum of the numbers should be returned
```

```python
# GIVEN a dealer
# WHEN the round starts
# THEN the dealer gives itself two cards
```

```python
# GIVEN: The power is on

# WHEN: The power button is pressed

# THEN: The power should be off
```

```python
# GIVEN: The power is off

# BUT: The battery is dead

# WHEN: The power button is pressed

# THEN: The power should be off
```

```python
# GIVEN: The light is red

# WHEN: Your car approaches the intersection

# THEN: You should stop
```

* And, But

```python
# GIVEN: That a player is currently at home

# AND: the town square is to the east

# WHEN: The player goes east

# THEN: The players current place should be changed to the town square

# AND: it should tell the player that they went there
```

* GIVEN there is a [thing] with [these characteristics]
* AND the [user] has [a thing]

* WHEN the [user] [does] [the thing]
  WHEN the [user] [does] [the thing] with [the input]

* THEN [the output] should [not] be shown
* THEN [the user] should [not] see [the output]
* AND  [the value] should be returned
* AND [the data] should [not] be [modified]

### dos and don'ts

|                       DONT                          |                        DO                             |
|-----------------------------------------------------|-------------------------------------------------------|
| include code or specific values                     | write general, plain english descriptions             |
|                                                     |                                                       |
|   `# WHEN you call add() with 2 and 5`              |   `# WHEN you call add() with two positive integers`  |
|   `# THEN the returned value should be 7`           |   `# THEN the sum of both numbers should be returned` |
|                                                     |                                                       |
| include technical details                           | write conceptual descriptions                         |
|                                                     |                                                       |
|   `# WHEN place_remove() is called`                 |   `# WHEN place_removed() is called`                  |
|   `# THEN key shouldn't be in PLACES[key]["items"]` |   `# THEN the item should be removed from the place`  |
|                                                     |                                                       |
| use throw-away data                                 | use realistic data                                    |
|                                                     |                                                       |
|   `# GIVEN a person dictionary`                     |   `# GIVEN a person dictionary`                       |
|   `a = {"first": "abc", "last": "xyz"}`             |   `person = {"first": "Bob", "last": "Smith"}`        |
|                                                     |                                                       |

### Exercise

* write GWT descriptions for your states [alcohol laws][alcohol-laws].

[alcohol-laws]: https://en.wikipedia.org/wiki/List_of_alcohol_laws_of_the_United_States

```
# no
# 7am-2am
# beer, wine & liquor: 8am-midnight
  3.2 beer: 5am-midnight
# yes
# no*
# 21
# 21 excpetion: ok for religious, medical, educational, private, non-selling with parent
# spirits/malt in liquor stores only
  liquor stores closed xmas.

GIVEN:
```


Part x: Isolation
-----------------

Reference
---------

### Glossary

```{glossary} writing-tests

BDD
Behavior-driven development
  A testing practice that follows the idea of specification by example. The
  idea is to describe how the application should behave in a very simple
  user/business-focused language.

GWT
Given-When-Then
  A formula from BDD for structuring test scenarios which is oriented from the
  user perspective and is comprised of ordered "given", "when", or "then"
  steps.
```


### todo

- [ ] testing is documentation
- [ ] write tests for happy paths, sad paths, ambiguous cases ; (invalid input, blank input, error cases)
- [ ] setup / teardown
- [ ] given/when/then
- [ ] failure messages
- [ ] skipping tests
- [ ] testing failures
- [ ] testing output
- [ ] red/green/refactor: https://medium.com/geekculture/test-driven-development-with-python-an-introduction-to-mocking-8ab6c1fe1c83
- [ ] tdd: https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/
- [ ] red/green/refactor: https://www.codecademy.com/article/tdd-red-green-refactor
- [ ] good tests: https://www.codecademy.com/article/tdd-u1-good-test
- [ ] [Testing Rails](https://books.thoughtbot.com/assets/testing-rails.pdf) book
- [ ] expected exceptions
- [ ] testing with debugger
  - [ ] [pdb++](https://github.com/pdbpp/pdbpp)
  - [ ] [pdbr](https://pypi.org/project/pdbr/)
    (Note: need to )
- [ ] running with pytest
  - [ ] `-v`: verbose
  - [ ] `-x`: fail on first tests
  - [ ] `-k`: expression
  - [ ] `-tb=short`: shorter tracebacks
  - [ ] `--pdb`: start debugger on failures
  - [ ] `--trace`: start debugger with breakpoint at the beginning of each test
  - [ ] `--pdbcls=IPython.terminal.debugger:TerminalPdb`: use the ipython debugger
  - [ ] running single test, filtering to matching names
  - [ ] pytest plugins
    - [ ] pytest-parametrization
    - [ ] pytest-only
    - [ ] pytest-clarity
  - [ ] adding to `pyproject.toml`
    ```toml
    [tool.pytest.ini_options]
    testpaths = ["tests"]
    addopts = "-vx"
    ```
