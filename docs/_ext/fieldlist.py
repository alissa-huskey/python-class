"""Field list directive

See also
--------
https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-field-lists
https://docutils.sourceforge.io/docs/user/rst/quickref.html#field-lists
https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists
https://docutils.sourceforge.io/docs/ref/doctree.html#field-list
"""

from functools import partial, wraps
from textwrap import shorten

from docutils.core import publish_doctree
from docutils import nodes
from myst_parser.main import to_docutils
from more_itertools import padded
from sphinx.util.docutils import SphinxDirective


def private(func):
    """Redirects property name to private _name"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        name = kwargs.pop("name")
        internal = f"_{name}"
        return func(self, internal, *args, **kwargs)
    return wrapper


class Field():
    """Manage docutils nodes.field"""
    def __init__(self, node: nodes.field):
        self._node = node
        self._name, self._body = padded(node.children, n=2)

    def __repr__(self):
        return "<{0} name={1!r} body={2!r}>".format(
            self.__class__.__name__,
            self.name,
            shorten(self.body, 30)
        )

    @private
    def _get(self, name):
        """generic getter"""
        if not name in self.__dict__:
            setattr(self, name, None)
        return getattr(self, name)

    @private
    def _get_node(self, name):
        """generic node getter"""
        if not name in self.__dict__:
            setattr(self, name, None)
        node = getattr(self, name)
        return node.rawsource

    @private
    def _set(self, name, value):
        """generic setter"""
        setattr(self, name, value)

    @private
    def _del(self, name):
        """generic deleter"""
        if name in self.__dict__:
            delattr(self, name)

    def transform(self):
        """Re-parse field body as myst"""
        if not self._body.children:
            return

        # parse body as myst
        doc = to_docutils(self.body)
        if not doc.children:
            return

        # replace old body with new
        self._body.children.clear()
        for node in doc.children:
            #  breakpoint()
            self._body.append(node)

    def toxml(self):
        return self.node.asdom().toxml()

    def tostr(self, compact=False):
        options = {}
        if compact:
            options = {"indent": ""}
        return self.node.pformat(**options)


    node = property(
        partial(_get, name="node"),
        partial(_set, name="node"),
        partial(_del, name="node"),
        "field node object"
    )

    name = property(
        partial(_get_node, name="name"),
        partial(_set, name="name"),
        partial(_del, name="name"),
        "field name (str)"
    )

    body = property(
        partial(_get_node, name="body"),
        partial(_set, name="body"),
        partial(_del, name="body"),
        "field body (DOM Element: field)"
    )

class FieldListDirective(SphinxDirective):
    has_content = True

    def run(self):
        """Process the directive arguments, options and content, and return a
           list of nodes."""

        # create field_list node
        text = "\n".join(self.content)
        field_list = nodes.field_list(text)

        # parse directive content as list of rst fields
        doctree = publish_doctree(text)

        # iterate over every field node and
        # reparse the body as myst via the Field class
        # then add the field_list node
        for node in doctree.traverse(nodes.field):
            field = Field(node)
            field.transform()
            field_list.append(field.node)

        # return the field_list
        return [field_list]


def setup(app):
    app.add_directive("fieldlist", FieldListDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
