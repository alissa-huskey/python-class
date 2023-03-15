"""
Create reference targets for all headers
"""

from pathlib import Path
from re import compile
from pprint import pformat  # noqa

from docutils import nodes
from rich import inspect, print  # noqa
from sphinx_exercise import nodes as exercises
from sphinx import addnodes
from sphinx.domains import Domain
from more_itertools import first, first_true

from logger import Logger


log = Logger(Path(__file__).stem, enabled=True, level="debug")


class Section():
    part_matcher = compile(r'^part-(?:(?:(\d+)-){1,2})')
    step_matcher = compile(r'^(?:([a-zA-Z])|(?:[Ss]tep (\d+)))[.:] ')
    step_subber = compile(r'^(?:([a-zA-Z])|(?:[Ss]tep-(\d+)))-')

    """Class for parsing a section node"""

    """Ignore this section if its parent node is one of these classes."""
    IGNORE_NAMES = (
        "exercise",
        "exercises",
    )

    """Ignore this section if its parent node is one of these classes."""
    IGNORE_PARENTS = (
        exercises.solution_node,
        exercises.exercise_enumerable_node,
    )

    """Ignore this section if it has a child node of one of these classes."""
    IGNORE_CHILDREN = (
        addnodes.glossary,
        addnodes.seealso,
    )

    def __init__(self, app, node):
        self.app = app
        self.node = node

        #  if self.docname == "tools/vscode":
        #      inspect(self.node, title="section node")

    @property
    def id(self) -> str:
        """Return the DOM id attribute for this section"""
        return first(self.attrs["ids"], None)

    @property
    def docname(self) -> str:
        """Return the name of the document that this section appears on"""
        return self.app.env.docname

    @property
    def attrs(self):
        return self.node.attributes

    @property
    def name(self):
        """Return the DOM name attibute for this section"""
        if "data-name" not in self.attrs:
            names = first_true(
                (self.attrs["names"], self.attrs["dupnames"]),
                [""],
            )
            self.attrs["name"] = names[0]
            return self.attrs["name"]

    @property
    def label(self):
        """Return a label for section in the format of:
            dir:page:normalized-header
        """
        if "data-label" not in self.attrs:
            if not self.id:
                log.error("No section id found:", self.node)
                inspect(self.node, title=f"No label: {type(self.node)}")
                return

            if not self.name:
                log.error("No section name found:", self.node)
                inspect(self.node, title=f"No name: {type(self.node)}")
                return

            docpath = self.docname.replace("/", ":")
            header = self.part_matcher.sub("", self.id)

            dom_path = [docpath, header]

            self.attrs["data-label"] = ":".join(dom_path)

        return self.attrs["data-label"]

    @property
    def parent(self) -> "Section":
        """Return a Section object for the parent node"""
        return self.__class__(self.app, self.node.parent)

    @property
    def target(self) -> nodes.target:
        """Return a target node for this section"""
        target = nodes.target('', '', ids=[self.label])
        target.parent = self.node
        return target

    @property
    def domain(self) -> Domain:
        """Return the std domain for this Sphinx app"""
        return self.app.env.get_domain('std')

    @property
    def title(self) -> nodes.title:
        """Return the first node of this section only if it is a title node"""
        title = first(self.node.children, None)
        if not isinstance(title, nodes.title):
            inspect(self.node, title=f"No title: {type(self.node)}")
            log.error("No title for section", pformat(self.node))
            return
        return title

    @property
    def part(self) -> str:
        """Parse the part number from section id, set it to DOM attribute
           data-part, and return."""
        if "data-part" not in self.attrs:
            found = self.part_matcher.match(self.id)
            if found:
                part = found.group(1)
            else:
                part = ""
            self.attrs["data-part"] = part

        return self.attrs["data-part"].replace("-", ".")

    @property
    def step(self) -> str:
        """Parse the step number from section name, set it to DOM attribute
           data-step, and return."""
        if "data-step" not in self.attrs:
            found = self.step_matcher.match(self.name)
            if found:
                step = first_true(found.groups())
            else:
                step = ""
            self.attrs["data-step"] = step.lower()
        return self.attrs["data-step"]

    def skipif_ignored_name(self) -> bool:
        """Return True if parent node is a node type to ignore"""
        return (self.name in self.IGNORE_NAMES)

    def skipif_ignored_parent(self) -> bool:
        """Return True if parent node is a node type to ignore"""
        return isinstance(self.node.parent, self.IGNORE_PARENTS)

    def skipif_ignored_children(self) -> bool:
        """Return True if any children are node types ignore"""
        """."""
        for klass in self.IGNORE_CHILDREN:
            children = tuple(self.node.findall(klass))
            if children:
                return True
        return False

        return isinstance(self.node.parent, self.IGNORE_PARENTS)

    def is_valid(self):
        """Return True if we can and should produce a target for this section."""
        should_ignore = (
            self.skipif_ignored_name(),
            self.skipif_ignored_parent(),
            self.skipif_ignored_children(),
            self.step,
        )

        return (
            (not (first_true(should_ignore)))
            and self.label and self.title
        )

    def update(self):
        """Add the target refrence"""
        self.attrs["ids"].insert(0, self.label)
        self.node.dupnames = []
        self.domain.labels[self.label] = (self.docname, self.id, self.name)
        self.node.document.note_explicit_target(self.node)


def show_labels(app, exception):
    """Print the list of labels in the standard domain to stderr"""
    domain = app.env.get_domain('std')
    print(domain.labels)


def process_header_nodes(app, doctree):
    """Add targets to all sections"""
    docname = app.env.docname
    log.info(f"{docname} ".ljust(80, "_"))

    for node in doctree.findall(nodes.section, descend=True, include_self=False):

        section = Section(app, node)

        if not section.is_valid():
            continue

        log.info(section.label)
        section.update()


def setup(app):
    app.connect("doctree-read", process_header_nodes)
    #  app.connect("build-finished", show_labels)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
