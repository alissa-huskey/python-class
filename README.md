Python Class
============

This repo is for the lessons and code related to the Python class that I've
been teaching to a few friends and family.

<h2 align="center"><a href="https://alissa-huskey.github.io/python-class/">» :book: Go to the lessons »</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>

Development Notes
-----------------

### Tools

* [Jupyter Book](https://jupyterbook.org/): document formatting and generation
  > note: current release is at 8.3 but manually pulled at f32176e
  > to get support for `local_extensions` config variable
* [The Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/index.html): theme
* [GitHub Pages](https://pages.github.com/): hosting
* [Poetry](https://python-poetry.org/): dependency management


### Process

| stage     | command                                      | description                                        |
|-----------|----------------------------------------------|----------------------------------------------------|
| dev       | `poetry install --no-root`                     | install dependencies                               |
| dev       | `poetry shell`                                 | start virtual env shell                            |
| build     | `jb build docs`                                | generate jupyter book from source                  |
| publish   | `cd docs && ghp-import -n -p -f _build/html`   | publish to GitHub Pages ([more info][jb-pages])    |

[jb-pages]: https://jupyterbook.org/publish/gh-pages.html
