Python Class
============

This repo is for the lessons and code related to the Python class that I've
been teaching to a few friends and family.

<h2 align="center"><a href="https://alissa-huskey.github.io/python-class/">» :book: Go to the lessons »</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2>

Development Notes
-----------------

* [Poetry](https://python-poetry.org/): dependency management


| command                        | description                    |
|--------------------------------|--------------------------------|
| `poetry install --no-root`       | install dependencies           |
| `poetry shell`                   | start virtual env shell        |


### Docs

* [Jupyter Book](https://jupyterbook.org/): document formatting and generation
  > note: current release is at 8.3 but manually pulled at f32176e
  > to get support for `local_extensions` config variable
* [The Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/index.html): theme


#### Build

Generate Static HTML files with `jupyter-book`.

```bash
jupyter-book build docs
```

#### Deploy

* [GitHub Pages](https://pages.github.com/): hosting
* [peaceiris/actions-gh-pages][actions-gh-pages] via [Github Actions][github-actions]: automatic deploy on push to master


Python modules needed for production docs are stored in `docs/.requirements.txt`.

To manually deploy the current build of `docs/` in `docs/_build/` to
`gh-import` branch:

```bash
ghp-import -n -p -f docs/_build/html
```

##### Github Settings

* Pages:
  * Branch: `gh-pages`
  * Folder: `/ (root)`
* Secrets & Deploy Key `ACTIONS_PAGES_DEPLOY_KEY`

See also: [GitHub Pages and Actions][jb-pages] on jupyterbook.org.

<!-- references -->

[jb-pages]: https://jupyterbook.org/publish/gh-pages.html
[github-pages]: https://pages.github.com/
[github-actions]: https://github.com/features/actions
[actions-gh-pages]: https://github.com/peaceiris/actions-gh-pages
