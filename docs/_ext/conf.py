"""config file for the myroles extension

See:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from docutils.nodes import make_id

# -- Project information -----------------------------------------------------

project = "python-class"
copyright = "2020, Alissa Huskey"
author = "Alissa Huskey <alissa.huskey@gmail.com>"

# The short X.Y version
version = '0.1'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# used with myst_heading_anchors (_config.yml) to generate anchor targets for
# headers. Instead of the default myst-parser style that mimics github, use
# docutils.make_id() for a more predictable and consistent format
# see:
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#anchor-slug-structure
myst_heading_slug_func = make_id
