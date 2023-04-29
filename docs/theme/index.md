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
Theme Demo
==========

This is a demo of the sphinx-book-theme components.

```{tableofcontents}
```

Toolchain
---------

:::{hlist}

* [Myst Parser > Syntax](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)

* [Bootstrap Docs](https://getbootstrap.com/docs/5.0/content/typography)

* [Sphinx > Roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html)
* [Sphinx > Directives](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)
* [Sphinx > reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
* [Sphinx > reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

* [reStructuredText Quickref](https://docutils.sourceforge.io/docs/user/rst/quickref.html)
* [reStructuredText Primer](https://docutils.sourceforge.io/docs/user/rst/quickstart.html)
* [reStructuredText Interpreted Text Roles](https://docutils.sourceforge.io/docs/ref/rst/roles.html)
* [reStructuredText Directives](https://docutils.sourceforge.io/docs/ref/rst/directives.html)

* [Jupyter Book > Narrative Content](https://jupyterbook.org/en/stable/content/content-blocks.html)
* [Jupyter Book > MyST syntax cheatsheet](https://jupyterbook.org/en/stable/reference/cheatsheet.html)

* [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/stable/content/content-blocks.html)
* [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/)
* [Sphinx Design Extension](https://sphinx-design.readthedocs.io/en/latest/index.html)
* [CommonMark Specification](https://spec.commonmark.org/current/)
* [CommonMark Quickref](https://commonmark.org/help/)
* [CommonMark Tutorial](https://commonmark.org/help/tutorial/)
* [The Docutils Document Tree](https://docutils.sourceforge.io/docs/ref/doctree.html)
* [Myst Tools](https://myst-tools.org/docs/mystjs/typography)
* [PyData Theme > Customize the CSS of light and dark themes](https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/light-dark.html)
* [PyData Theme > Sphinx Design Components](https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/web-components.html)

:::

Inspiration
-----------

### Dark Themes

* [Shibuya Sphinx Theme](https://shibuya.lepture.com/) -- colors and styles (especially for admonitions) taken from this theme
* [piccolo-theme](https://piccolo-theme.readthedocs.io/en/latest/demo.html)
* [Furo Theme](https://pradyunsg.me/furo/customisation/colors/)
* [nbsphinx](https://nbsphinx.readthedocs.io/en/furo-theme/index.html)
* [sphinx-pyscript](https://sphinx-pyscript.readthedocs.io/en/latest/example_md.html)
* [pyqtdarktheme](https://pyqtdarktheme.readthedocs.io/en/stable/reference/theme_color.html) -- seems like the same as sphinx-book
* [furo-topbar](https://furo-topbar.readthedocs.io/en/latest/)
* [click-extra](https://kdeldycke.github.io/click-extra/)
* [ansys](https://sphinxdocs.ansys.com/version/stable/examples/sphinx-design.html#sphinx-design)
* [Bootstrap > Color Modes](https://getbootstrap.com/docs/5.3/customize/color-modes/)
* [MkDocs Windmill Theme](https://noraj.github.io/mkdocs-windmill-dark/#) -- dark theme
* [Bootswatch Cyborg Theme](https://bootswatch.com/cyborg/) -- maybe some nice badge colors on black bg
* [Darkly Bootswatch Theme](https://bootswatch.com/darkly/) -- dark theme
* [Slate Bootswatch Theme](https://bootswatch.com/slate/) -- nice dark theme
* [Superhero Bootswatch Theme](https://bootswatch.com/superhero/) -- nice dark blue theme
* [Vapor Bootswatch Theme](https://bootswatch.com/vapor/) -- eye bleeding theme but dark purple background and bright colors for examples
* [Dracula MkDocs Theme](https://dracula.github.io/mkdocs/)

### Light Themes

* [Git Book > Markdown](https://docs.gitbook.com/content-creation/editor/markdown)
* [Minty Bootswatch Theme](https://bootswatch.com/minty/) -- just kind of nice cards and stuff (light)
* [Zepher Bootswatch Theme](https://bootswatch.com/zephyr/) -- light theme with nice colors
* [Coder Docs Bootstrap Theme](https://themes.3rdwavemedia.com/demo/bs5/prettydocs/faqs.html)

### Text Blocks

* [Fuext Blocksro Theme > Blocks](https://pradyunsg.me/furo/kitchen-sink/blocks/)
* [Bootstrap > Reboot > Summary](https://getbootstrap.com/docs/5.0/content/reboot/#summary)
* [Bootstrap > Reboot > Naming a Source](https://getbootstrap.com/docs/5.0/content/typography/#naming-a-source)
* [Cloud Sphinx Theme > Blocks > Line Blocks](https://sphinx-themes.org/sample-sites/cloud-sptheme/kitchen-sink/blocks/#line-blocks) -- the font (?) used for line blocks
* [Hachibee Sphinx Theme > Block Quotes](https://sphinx-themes.org/sample-sites/hachibee-sphinx-theme/kitchen-sink/blocks/) -- the quote image background on many of the blocks
* [Maisie Sphinx Theme > Blocks](https://sphinx-themes.org/sample-sites/maisie-sphinx-theme/kitchen-sink/blocks/) -- the background color and styling of the blocks. Also generally a nice looking light theme.
* [Python Documentation Sphinx Theme > Blocks > Line Blocks](https://sphinx-themes.org/sample-sites/python-docs-theme/kitchen-sink/blocks/#line-blocks) -- another good font for line blocks
* [Haiku Sphinx Theme > Blocks > Code Block](https://sphinx-themes.org/sample-sites/default-haiku/kitchen-sink/blocks/#code-block) -- the dotted line around the code block
* [devcard Bootstrap Template > Blog Post](https://themes.3rdwavemedia.com/devcard/bs5/2.0/blog-post.html) -- pull quote example
* [Instance Bootstrap Theme > Blog Post](https://themes.3rdwavemedia.com/instance/bs5/2.0/blog-post.html) -- pull quote
* [Tempo Bootstrap Theme](https://themes.3rdwavemedia.com/tempo/bs5/2.1/) -- pull quotes / epigraph
* [Tempo Bootstrap Theme](https://themes.3rdwavemedia.com/tempo/bs5/2.1/blog-single.html) -- pull quote
* [Sphere Bootstrap Theme](https://themes.3rdwavemedia.com/sphere/bs5/) -- pull quote / epigraph
* [College Green Bootstrap Theme > Testamonials](https://themes.3rdwavemedia.com/college-green/bs4/#) -- Epigraphs
* [Prospectus Bootstrap Theme > Testamonials](https://themes.3rdwavemedia.com/prospect/bs5/) -- epigraph
* [Academy Bootstrap Theme > About Us](https://themes.3rdwavemedia.com/academy/bs5/about.html) -- pull quote
* [Academy Bootstrap Theme > Blog Post](https://themes.3rdwavemedia.com/academy/bs5/blog-single.html) -- pull quote / epigraph

### Cards

* [Epicure Bootstrap Theme > News & Events](https://themes.3rdwavemedia.com/epicure/bs5/) -- Card Titles
* [Academy Bootstrap Theme > Jobs](https://themes.3rdwavemedia.com/academy/bs5/jobs.html) -- cards
* [Portal Bootstrap Theme](https://themes.3rdwavemedia.com/demo/portal/) -- generally nice, cards on help page

### Admonitions

* [Sphinx-Immaterial Theme > Admonitions](https://jbms.github.io/sphinx-immaterial/admonitions.html#admonition-directive) -- nice dark background, nice admonition colors, plus some custom ones, also interesting tabs

### Colors

* [Nameko Sphinx Theme > Blocks > Code Block](https://sphinx-themes.org/sample-sites/sphinx-nameko-theme/kitchen-sink/blocks/#code-block) -- the syntax highlighting of the code blocks
* [Sphinx-Immaterial Theme > Admonitions](https://jbms.github.io/sphinx-immaterial/admonitions.html#admonition-directive) -- nice dark background, nice admonition colors, plus some custom ones, also interesting tabs
* [Material Sphinx Theme](https://bashtage.github.io/sphinx-material/specimen.html) -- nice light background color
* [Bootswatch Cyborg Theme](https://bootswatch.com/cyborg/) -- maybe some nice badge colors on black bg
* [Pulse Bootswatch Theme](https://bootswatch.com/pulse/) -- nice colors
* [Simplex Bootswatch Theme](https://bootswatch.com/simplex/) -- nice colors
* [Soloar Bootswatch Theme](https://bootswatch.com/solar/) -- maybe nice colors
* [Vapor Bootswatch Theme](https://bootswatch.com/vapor/) -- eye bleeding theme but dark purple background and bright colors for examples
* [Zepher Bootswatch Theme](https://bootswatch.com/zephyr/) -- light theme with nice colors
* [CoderPro Bootstrap Theme](https://themes.3rdwavemedia.com/coderpro/bs5/2.0/docs-page.html#section-8) -- nice colors
* [Pretty Docs Bootstrap Theme](https://themes.3rdwavemedia.com/demo/bs5/prettydocs/faqs.html) -- nice FAQ

### Layout

* [Sphinx Press theme > Field lists](https://schettino72.github.io/sphinx_press_site/theme-demo/basic.html#field-lists) -- nice formatting
* [Sphinx Typlog Theme > Markup Style > Option Lists](https://sphinx-typlog-theme.readthedocs.io/en/latest/markup.html#options-lists) -- Nice option lists, also nice (similar) admonitions, and API reference
* [Sphinx Wagtail Theme > Progressive Disclosure](https://sphinx-wagtail-theme.readthedocs.io/en/latest/examples/progressive-disclosure.html) -- expand content with the `details` tag
* [Minty Bootswatch Theme](https://bootswatch.com/minty/) -- just kind of nice cards and stuff (light)

### Theme Directories

* [Awesome Sphinx](https://awesomesphinx.useblocks.com/) -- curated list of Sphinx extensions, themes and other Sphinx-related projects
* [MkDocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)
* [Bootswatch](https://bootswatch.com/) -- themes for bootstrap
* [PyPi.org » Framework::Sphinx::Theme](https://pypi.org/search/?c=Framework+%3A%3A+Sphinx+%3A%3A+Theme)
*
