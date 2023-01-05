Writing Tests
=============


```{contents}
:backlinks: top
:local:
```

:::{important}

Be sure to go through the [](testing.md) lesson first if you haven't already.

:::

Part x: Good tests
------------------

* Fast -- 
* Complete -- The whole codebase should be tested and all possible cases.
* Resiliant -- won't break if your code changes in trivial ways. Don't wrongly
  fail or pass. Don't fail intermittently.
* Maintainable -- It should be easy to add new tests or make changes to your
  tests when your code changes.
* Isolated -- They set themselves up, and clean up after themselves.
  Tests need to set themselves up so that you can run tests individually. When
  working on a portion of code, you don’t want to have to waste time running
  the entire suite just to see output from a single test
* Expressive -- It should be easy to tell what is being tested. Testing is
  documentation.

Part x: TDD
-----------

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

- [ ] imports
- [ ] `if __name__ == "__main__"`
- [ ] testing is documentation
- [ ] write tests for happy paths, sad paths, ambiguous cases ; (invalid input, blank input, error cases)
- [ ] setup / teardown
- [ ] failure messages
- [ ] testing failures
- [ ] testing output
- [ ] red/green/refactor: https://medium.com/geekculture/test-driven-development-with-python-an-introduction-to-mocking-8ab6c1fe1c83
- [ ] tdd: https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/
- [ ] red/green/refactor: https://www.codecademy.com/article/tdd-red-green-refactor
- [ ] good tests: https://www.codecademy.com/article/tdd-u1-good-test
- [ ] [Testing Rails](https://books.thoughtbot.com/assets/testing-rails.pdf) book
