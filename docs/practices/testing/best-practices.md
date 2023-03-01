Writing Tests
=============


```{contents}
:backlinks: top
:local:
```

:::{important}

Be sure to go through the [](intro.md) lesson first if you haven't already.

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

TODO

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
