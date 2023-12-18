Python Class
============

This repo is for the lessons and code related to the Python class that I've
been teaching to a few friends and family.

<h2 align="center"><a href="https://alissa-huskey.github.io/python-class/">» :book: Go to the lessons »</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>

Development Notes
-----------------

* [Poetry](https://python-poetry.org/): dependency management


| command                                      | description                                        |
|----------------------------------------------|----------------------------------------------------|
| `poetry install --no-root`                     | install dependencies                               |
| `poetry shell`                                 | start virtual env shell                            |


### Docs

* [Jupyter Book](https://jupyterbook.org/): document formatting and generation
  > note: current release is at 8.3 but manually pulled at f32176e
  > to get support for `local_extensions` config variable
* [The Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/index.html): theme


#### Build

Generated Static HTML files with `jupyter-book`.

```bash
jupyter-book build docs
```

#### Deploy

* [GitHub Pages](https://pages.github.com/): hosting of `gh-pages` branch
* [peaceiris/actions-gh-pages][actions-gh-pages] via [Github Actions][github-actions]: automatic deploy on push to master

([more info][jb-pages])

Production requirements are exported from the pyproject.toml using poetry as
configured in the github action.

##### Github Config

* Pages:
  * Branch: `gh-pages`
  * Folder: `/ (root)`
* Secrets & Deploy Key `ACTIONS_PAGES_DEPLOY_KEY`

<!-- references -->

[jb-pages]: https://jupyterbook.org/publish/gh-pages.html
[github-pages]: https://pages.github.com/
[github-actions]: https://github.com/features/actions
[actions-gh-pages]: https://github.com/peaceiris/actions-gh-pages
