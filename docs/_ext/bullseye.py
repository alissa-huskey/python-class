"""
Create reference targets for all headers
"""

from pathlib import Path
from re import compile
from pprint import pformat  # noqa
from typing import Dict, Tuple, List, Optional
from collections import defaultdict
from textwrap import TextWrapper

from docutils import nodes
from rich import inspect, print  # noqa
from sphinx_exercise import nodes as exercises
from sphinx import addnodes
from sphinx.environment import BuildEnvironment
from sphinx.domains import Domain
from sphinx.util.nodes import make_refnode
from sphinx.builders import Builder
from more_itertools import first, first_true


from logger import Logger


log = Logger(Path(__file__).stem, enabled=True, level="debug")


class Section():
    """A class for a <section> tag"""
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

    """Flag to toggle logging"""
    enable_logging = True

    def make_wrapper(prefix):
        """Text wrapper for warning log messages"""
        indent = len(f"2023-03-15T21:17:24 [{prefix}]") * " "
        return TextWrapper(
            width=100,
            initial_indent=indent,
            subsequent_indent=indent,
        )

    warning_wrapper = make_wrapper("warning")
    error_wrapper = make_wrapper("error")
    info_wrapper = make_wrapper("info")
    debug_wrapper = make_wrapper("debug")

    def __repr__(self):
        self.enable_logging = False
        attrs = ("docname", "title", "label", "id", "name")
        values = {a: getattr(self, a) for a in attrs}
        strings = [f"{k}={v!r}" for k, v in values.items()]
        self.enable_logging = True

        return "Section <{}>".format(', '.join(strings))

    def __init__(self, env, node):
        self.env = env
        self.node = node

    @property
    def id(self) -> str:
        """Return the DOM id attribute for this section"""
        id = first(self.attrs["ids"], None)
        if not id:
            self.error("No section id found")
        return id

    @property
    def docname(self) -> str:
        """Return the name of the document that this section appears on"""
        return self.env.docname

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
            name = first(names, None)

            if not name:
                self.error("No section name found")

            self.attrs["name"] = name
            return self.attrs["name"]

    @property
    def label(self):
        """Return a label for section in the format of:
            dir:page:normalized-header
        """
        if "data-label" not in self.attrs:
            if not self.id:
                return
            docpath = self.docname.replace("/", ":")
            header = self.part_matcher.sub("", self.id)

            dom_path = [docpath, header]

            self.attrs["data-label"] = ":".join(dom_path)

        return self.attrs["data-label"]

    @property
    def parent(self) -> "Section":
        """Return a Section object for the parent node"""
        return self.__class__(self.env, self.node.parent)

    @property
    def domain(self) -> Domain:
        """Return the std domain for this Sphinx app"""
        return self.env.get_domain('std')

    @property
    def title(self) -> nodes.title:
        """Return the first node of this section only if it is a title node"""
        title = first(self.node.children, None)
        if not isinstance(title, nodes.title):
            self.debug("no title", "")
            return
        return title.rawsource

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

            if step:
                self.debug("step header", f"step: {step}")
        return self.attrs["data-step"]

    def error(self, msg):
        if not self.enable_logging:
            return
        text = self.error_wrapper.fill(repr(self))
        log.error(f"{msg}\n{text}")

    def debug(self, reason, msg):
        if not self.enable_logging:
            return
        text = self.debug_wrapper.fill(repr(self))
        indent = self.debug_wrapper.initial_indent
        self.debug_wrapper.initial_indent = ""
        msg = self.debug_wrapper.fill(msg)
        self.debug_wrapper.initial_indent = indent

        log.debug(f"Skipping ({reason}): {msg}\n{text}")

    def warn(self, reason, msg):
        if not self.enable_logging:
            return
        msg = self.warning_wrapper.fill(msg)
        text = self.warning_wrapper.fill(repr(self))
        log.warn(f"Skipping ({reason}): {msg}\n{text}")

    def skipif_ignored_name(self) -> bool:
        """Return True if parent node is a node type to ignore"""
        if self.name in self.IGNORE_NAMES:
            self.debug("ignored name", "name: {self.name}")
            return True
        return False

    def skipif_ignored_parent(self) -> bool:
        """Return True if parent node is a node type to ignore"""
        if isinstance(self.node.parent, self.IGNORE_PARENTS):
            self.debug("ignored parent", "parent: {type(self.node.parent)}")
            return True
        return False

    def skipif_ignored_children(self) -> bool:
        """Return True if any children are node types ignore"""
        for klass in self.IGNORE_CHILDREN:
            children = tuple(self.node.findall(klass, descend=False))
            if children:
                text = ", ".join([f"{type(c)!r}" for c in children])
                self.debug(f"{len(children)} ignored children", text)
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
            and self.id and self.name and self.label and self.title
        )

    def update(self):
        """Add the target refrence"""
        self.attrs["ids"].insert(0, self.label)
        self.node.dupnames = []


class HeadingRefDomain(Domain):
    """A domain for resolving references to headings (or really, sections.)"""

    name = 'heading-refs'
    label = 'Heading Refs'

    @property
    def headings(self) -> Dict[str, Section]:
        """Return a dictionary target labels -> Section objects"""
        return self.data.setdefault('headings', {})

    @property
    def heading_refs(self) -> Dict[str, List[str]]:
        """Return a dictionary mapping docnames -> a list of target labels"""
        return self.data.setdefault(
            'heading_refs', defaultdict(list)
        )

    def process_doc(self, env: "BuildEnvironment", docname: str,
                    doctree: nodes.document) -> None:
        """Process a document after it is read by the environment."""
        log.info(f"{docname} ".ljust(80, "_"))

        for node in doctree.findall(nodes.section, descend=True, include_self=False):

            section = Section(env, node)

            if not section.is_valid():
                continue

            log.info(section.label)
            section.update()
            self.note_heading(section)

    def resolve_xref(self, env: "BuildEnvironment", docname: str,
                     builder: "Builder", typ: str, target: str,
                     node: addnodes.pending_xref,
                     contnode: nodes.Element) -> Optional[nodes.Element]:
        """Resolve pending_xref *node* with a specific *typ* *target*."""

        section = self.headings.get(target)

        if not section:
            return None

        return make_refnode(builder, docname, section.docname, section.label, contnode)

    def resolve_any_xref(self, env: "BuildEnvironment", docname: str,
                         builder: "Builder", target: str, node: addnodes.pending_xref,
                         contnode: nodes.Element) -> List[Tuple[str, nodes.Element]]:
        """Resolve the pending_xref *node* with the given *target*."""

        refnode = self.resolve_xref(
            env, docname, builder, 'ref', target, node, contnode
        )
        if refnode is None:
            return []
        else:
            return [('ref', refnode)]

    def note_heading(self, section: Section):
        """Add the target label to domain data for this heading"""
        #  self.domain.labels[self.label] = (self.docname, self.id, self.name)
        #  self.node.document.note_explicit_target(self.node)
        self.headings[section.label] = section
        self.heading_refs[section.docname].append(section.label)

    def clear_doc(self, docname: str) -> None:
        """Remove traces of a document in the domain-specific inventories."""
        for label in self.heading_refs[docname]:
            del self.headings[label]
        del self.heading_refs[docname]

    def merge_domaindata(self, docnames: List[str], otherdata: Dict) -> None:
        """Merge in data regarding *docnames* from a different domaindata
           inventory (coming from a subprocess in parallel builds).
        """
        for docname in docnames:
            self.heading_refs[docname] += otherdata['heading_refs'][docname]
        self.headings.update(self.otherdata['headings'])


#  def show_labels(app, exception):
#      """Print the list of labels in the standard domain to stderr"""
#      domain = app.env.get_domain('std')
#      print(domain.labels)


def setup(app):
    app.add_domain(HeadingRefDomain)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
