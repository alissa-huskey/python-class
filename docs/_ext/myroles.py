"""spinx/docutils roles for alissa-huskey/python-class

https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html
https://docutils.sourceforge.io/docs/howto/rst-roles.html
https://doughellmann.com/blog/2010/05/09/defining-custom-roles-in-sphinx/
https://protips.readthedocs.io/link-roles.html
"""
import docutils.nodes as nodes

REPO_URL = "http://github.com/alissa-huskey/python-class"
BRANCH = "master"

def setup(app):
    app.add_role("lesson_py", lesson_py_role)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

def lesson_py_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """lessons_py role
       Add a link to the python script on github associated with a lesson.

       Usage
       -----

       # MyST
       {lesson_py}`dragonrealm/dragon_realm_part1.py`

       # reStructuredText
       :lesson_py:`dragonrealm/dragon_realm_part1.py`

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
    filename = text.split("/")[-1]
    url =  f"{REPO_URL}/blob/{BRANCH}/pythonclass/lessons/{text}"
    node = nodes.reference(rawtext, filename, refuri=url, **options)
    return [node], []

#  def github_url(path, branch="master") -> str:
#      """Return a URL to the github repo for path"""
#      return f"{REPO_URL}/blob/{branch}/{path}"

#  def lesson_script_link(filepath) -> str:
#      """Return a URL to the github repo for path"""

