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
    - https://repo.or.cz/docutils.git/blob/refs/heads/master:/docutils/docutils/parsers/rst/roles.py
    - https://www.sphinx-doc.org/en/1.4.6/domains.html#the-restructuredtext-domain
"""
import docutils.nodes as nodes
from sphinx import roles
import re

REPO = "alissa-huskey/python-class"
BRANCH = "master"
SCHEMA = "http"

def setup(app):
    # print("DEBUG myroles.setup()>", app.config.overrides)
    app.add_role("lesson_py", lesson_py_role)
    app.add_role("repo", repo_role)
    app.add_role("repo_raw", repo_raw_role)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def repo_url(text, relroot="", raw=False):
    """Return (title, url) to the file in the repo for text
       Params
       ------
       text    (str)          : "path" or "title <path>"
       relroot (str, optional): relative root dir to prepend to path

       Examples
       --------
#
       >>> repo_url("download <pythonclass/template.py>", raw=True)
       ('download', 'http://raw.githubusercontent.com/alissa-huskey/python-class/master/pythonclass/template.py')
       >>> repo_url("template <template.py>")
       ('template', 'http://github.com/alissa-huskey/python-class/blob/master/template.py')
       >>> repo_url("dir/file.py")
       ('file.py', 'http://github.com/alissa-huskey/python-class/blob/master/dir/file.py')
       >>> repo_url("title <dir/file.py>")
       ('title', 'http://github.com/alissa-huskey/python-class/blob/master/dir/file.py')
       >>> repo_url("lists.py", relroot="pythonclass/lessons")
       ('lists.py', 'http://github.com/alissa-huskey/python-class/blob/master/pythonclass/lessons/lists.py')
       >>> repo_url("lists <lists.py>", relroot="pythonclass/lessons")
       ('lists', 'http://github.com/alissa-huskey/python-class/blob/master/pythonclass/lessons/lists.py')
       >>> repo_url("Part One <part1.py>")
       ('Part One', 'http://github.com/alissa-huskey/python-class/blob/master/part1.py')
    """

    title, path, url = [""] * 3

    if match := re.search(r"^(?P<title>.+) <(?P<path>.+)>$", text):
        title = match.group("title")
        path = match.group("path")
    else:
        title = text.split("/")[-1]
        path = text

    path = f"{relroot}/{path}" if relroot else path

    if raw:
        url = f"{SCHEMA}://raw.githubusercontent.com/{REPO}/{BRANCH}/{path}"
    else:
        url = f"{SCHEMA}://github.com/{REPO}/blob/{BRANCH}/{path}"

    return title, url

def repo_raw_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """repo_raw role
       Role to generate a link to raw file in the repo.

       Usage
       -----

       # MyST
       {repo_raw}`path`
       {repo_raw}`title <path>`.

       # reStructuredText
       :repo_raw:`path`
       :repo_raw:`title <path>`.

    """
    title, url = repo_url(text, raw=True)
    node = nodes.reference(rawtext, title, refuri=url, **options)
    return [node], []

def repo_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """repo role
       Role to generate a link to a file in the repo.

       Usage
       -----

       # MyST
       {repo}`path`
       {repo}`title <path>`.

       # reStructuredText
       :repo:`path`
       :repo:`title <path>`.

    """
    title, url = repo_url(text)
    node = nodes.reference(rawtext, title, refuri=url, **options)
    return [node], []

def lesson_py_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """lessons_py role
       Add a link to the python script in the repo associated with a lesson.

       Usage
       -----

       # MyST
       {lesson_py}`path`
       {lesson_py}`title <path>`

       # reStructuredText
       :lesson_py:`path`
       :lesson_py:`title <path>`

    """
    title, url = repo_url(text, relroot="pythonclass/lessons")
    node = nodes.reference(rawtext, title, refuri=url, **options)
    return [node], []


def lesson_py_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """lessons_py role
       Add a link to the python script in the repo associated with a lesson.

       Usage
       -----

       # MyST
       {lesson_py}`path`
       {lesson_py}`title <path>`

       # reStructuredText
       :lesson_py:`path`
       :lesson_py:`title <path>`

    """
    title, url = repo_url(text, relroot="pythonclass/lessons")
    node = nodes.reference(rawtext, title, refuri=url, **options)
    return [node], []
