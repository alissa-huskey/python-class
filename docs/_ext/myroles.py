"""spinx/docutils roles for alissa-huskey/python-class

    def role_functions(name, rawtext, text, lineno, inliner, options={}, content=[]):
       Params
       ------
       name: The role name actually used in the document.
       rawtext: The enitre interpreted text input, including the role and markup.
       text: The interpreted text content.
       lineno: The line number where the interpreted text begins.
       inliner: The calling docutils.parsers.rst.states.Inliner object.
       options: Directive options for customization (from the "role" directive).
       content: The directive content for customization (from the "role" directive).

       Returns
       -------
       * A list of nodes to be added to the document tree.
       * A list of system messages, added to the document tree after the current block.


    More info
    ---------

    - https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html
    - https://docutils.sourceforge.io/docs/howto/rst-roles.html
    - https://doughellmann.com/blog/2010/05/09/defining-custom-roles-in-sphinx/
    - https://protips.readthedocs.io/link-roles.html
    - https://repo.or.cz/docutils.git/tree/refs/heads/master:/docutils
    - https://repo.or.cz/docutils.git/blob/refs/heads/master:/docutils/docutils/parsers/rst/roles.py   # noqa
    - https://www.sphinx-doc.org/en/1.4.6/domains.html#the-restructuredtext-domain
"""
import docutils.nodes as nodes
from pathlib import Path

from sphinx.util.nodes import split_explicit_title

from logger import Logger
log = Logger(Path(__file__).stem, enabled=False, level="debug")

REPO = "alissa-huskey/python-class"
BRANCH = "master"
SCHEMA = "http"


def span_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Usage
    -----

    {span}`demo <pst-font-size-h1>` -> <span class="pst-font-size-h1">demo</span>

    Params
    ------
    name: The role name actually used in the document.
    rawtext: The enitre interpreted text input, including the role and markup.
    text: The interpreted text content.
    lineno: The line number where the interpreted text begins.
    inliner: The calling docutils.parsers.rst.states.Inliner object.
    options: Directive options for customization (from the "role" directive).
    content: The directive content for customization (from the "role" directive).

    Returns
    -------
    * A list of nodes to be added to the document tree.
    * A list of system messages, added to the document tree after the current block.
    """

    _, title, target = split_explicit_title(text)

    if title == target:
        title = ""

    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]

    log(rawtext, f"title={title!r}", f"target={target!r}")

    node = nodes.inline(rawtext, title)

    if target:
        for t in target.split():
            node.attributes["classes"].append(t)

    return [node], []


def setup(app):
    # print("DEBUG myroles.setup()>", app.config.overrides)
    app.add_role("span", span_role)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
