"""Lexicon Domain -- expanded glossary support"""

from pprint import pformat  # noqa
from collections import defaultdict
from pathlib import Path

from sphinx.application import Sphinx as SphinxApplication
from sphinx.environment import BuildEnvironment
from sphinx.environment.collectors import EnvironmentCollector
from sphinx.builders import Builder
from sphinx.domains import Domain
from sphinx.directives import SphinxDirective
from sphinx import addnodes
from sphinx.domains.std import Glossary as SphinxGlossary
from docutils import nodes
from more_itertools import first

from logger import Logger


log = Logger("lexicon", enabled=False)


class OrphanedTermsDirective(SphinxDirective):

    def run(self):
        return [orphanedterms("")]


class MissingTermsCollector(EnvironmentCollector):
    """Class to collect terms that are missing."""

    def clear_doc(self, app, env, docname) -> None:
        if env.orphans[docname]:
            app.domains.get("lexicon").expire_orphans()
        env.orphans[docname] = set()

    def merge_other(self, app, env, docnames, other) -> None:
        for doc in docnames:
            if doc not in other.orphans:
                continue
            env.orphans[doc] = other.orphans[doc]

    def process_doc(self, app, doctree) -> None:
        ...


class Term(str):
    """Class for glossary Terms"""

    def normalize(self):
        """Return normalized term"""
        nodes.fully_normalize_name(self).rstrip("s")


class Glossary():
    """Glossary class -- objects for use with GlossaryDirective"""

    """document name"""
    doc: str

    """optional directive argument: category name"""
    category: str

    """Number of this glossary in Lexicon Domain"""
    num: int

    """glossary node created by sphinx Glossary directive"""
    glossary_node: addnodes.glossary

    """definition list node created by sphinx Glossary directive"""
    deflist_node: nodes.definition_list

    """top-level section node container"""
    _node: nodes.section

    def __init__(self, doc: str = None, category: str = "", num: int = None,
                 elements: list = [[None]]):
        """Initializer

        Params
        ------
        doc (str): document name
        category (str): optional directive argument
        num (int): umber of this glossary in Lexicon Domain
        elements (list[nodes.glossary[nodes.definition_list]]):
            list of nodes created by sphinx Glossary directive
        """
        self.doc = doc
        self.category = category
        self.num = num

        self.glossary_node = first(elements, None)
        self.deflist_node = first(self.glossary_node, None)
        self._node = None

    @property
    def title(self) -> str:
        """Return the string for the section title/header"""
        return self.category.replace("-", " ").title()

    @property
    def node(self) -> nodes.section:
        """Return the top-level section node for this glossary containing all
           child nodes"""
        assert self.glossary_node, "Glossary.glossary_node (nodes.glossary) required"

        if not self._node:
            self._node = nodes.section()
            self._node['ids'].append(f"glossary-{self.id}")
            if self.title:
                self._node += self.header_node
            self._node += self.glossary_node
        return self._node

    @node.setter
    def node(self, value):
        """self.node setter"""
        self._node = value

    @property
    def id(self) -> str:
        """Return unique portion of node id"""
        return self.category or str(self.num)

    @property
    def header_node(self) -> nodes.title:
        """Return self._header_node"""
        return self._header_node

    @header_node.setter
    def header_node(self, inline_nodes: tuple):
        """Create and set self._header_node to title node containing
           inline text element in inline_nodes, or None if blank self.title

           Params
           ------
           inline_nodes (tuple[list[nodes.Text], list[nodes.Text]]):
               tuple created by state.inline_text() containing
               lists of (inline elements, and system messges) text nodes

           Example
           -------
            >>> glossary.header_node = state.inline_text(
                glossary.title,
                lineno
            )

           More info
           ---------
           Implemented this way because inline_nodes must be created by
           state.inline_text(), which for some reason cannot be saved as member
           of Glossary without triggering exception:
               myst_parser.mocking.MockingError:
                   MockState has no attribute __getstate__
           """
        if not self.category:
            self._header_node = None
            return
        textnodes = inline_nodes[0]
        self._header_node = nodes.title(self.category, "", *textnodes)

    def __iter__(self):
        """Iterate over GlossaryListing objects for each
           nodes.definition_list_item in self.deflist_node"""
        assert self.deflist_node and \
            isinstance(self.deflist_node, nodes.definition_list), \
            "Glossary.deflist_node (nodes.definition_list) required"
        return (GlossaryListing(self, node) for node in self.deflist_node)


class GlossaryListing():
    """Glossary Listing class -- object for each grouping of term(s) and
      definition(s) a glossary directive"""

    """list of Term objects"""
    terms: list

    """List of definition strings"""
    definitions: list

    """Glossary object that this term belongs to"""
    glossary: Glossary

    """Node containing this listing"""
    node: nodes.definition_list_item

    def __init__(self, glossary: Glossary = None,
                 node: nodes.definition_list_item = None):
        """Initializer"""
        self.terms = []
        self.definitions = []
        self.glossary = glossary
        self.node = node

    @property
    def doc(self) -> str:
        """Return name of document that this listing appears on"""
        assert self.glossary, "GlossaryListing.glossary (Glossary) required"
        return self.glossary.doc

    @property
    def identifier(self) -> str:
        """The first glossary term"""
        assert self.terms, "At leat one GlossaryListing.term (Term) required"
        return first(self.terms)

    def add_term(self, term: Term):
        """Add a term to this listing"""
        assert term and isinstance(term, Term), "argument term (Term) required"
        self.terms.append(term)

    def add_definition(self, definition: str):
        """Add a definition to this listing"""
        assert isinstance(definition, str), "argument definition (str) required"
        self.definitions.append(definition)

    def __iter__(self):
        """Iterate over each definition_list_item child node, either a nodes.term or
        nodes.definition"""
        assert self.node and isinstance(self.node, nodes.definition_list_item), \
            "GlossaryListing.node (nodes.definition_list_item) required"
        return iter(self.node.children)


class MissingTerm():
    """MissingTerm class -- for tracking term references created using the
       :term: role where matching glossary listings were not found"""

    """the missing term"""
    term: Term

    """document name where term role was used"""
    doc: str

    """line number where term role was used"""
    lineno: int

    def __init__(self, term: Term, doc: str, lineno: int):
        """Initializer"""
        self.term = term
        self.doc = doc
        self.lineno = lineno

    def __hash__(self):
        return hash(self.term)


class GlossaryDirective(SphinxGlossary):
    optional_arguments = 1

    def is_term(self, node: nodes.Element) -> bool:
        """Return True if node is a term  node"""
        return isinstance(node, nodes.term)

    def is_definition(self, node: nodes.Element) -> bool:
        """Return True if node is a definition  node"""
        return isinstance(node, nodes.definition)

    def run(self):
        """Process the directive arguments, options and content, and return a
           list of nodes."""
        lex = self.env.get_domain('lexicon')
        location, _ = self.state_machine.get_source_and_line(self.lineno)
        rel_filename = str(Path(location).relative_to(self.env.srcdir))
        self.env.note_dependency(rel_filename)

        log("GlossaryDirective> location:", location)
        log("GlossaryDirective> rel_filename:", rel_filename)

        glossary = Glossary(
            doc=self.env.docname,
            category=first(self.arguments, ""),
            num=lex.next_glossary(),
            elements=super().run(),
        )

        glossary.header_node = self.state.inline_text(
            glossary.title,
            self.lineno)

        for listing in glossary:
            for node in listing:
                if self.is_term(node):
                    term = Term(node[0].astext())
                    listing.add_term(term)
                    lex.add_term(term, listing)
                elif self.is_definition(node):
                    listing.add_definition(node.astext())

        return [glossary.node]


class LexiconDomain(Domain):
    """Lexicon domain for expanded glossary support"""

    name = "lexicon"
    label = "Lexicon Domain"
    outdated = set()

    directives = {
        'glossary': GlossaryDirective,
        'orphanedterms': OrphanedTermsDirective,
    }

    initial_data = {
        'glossaries': 0,
        'terms': defaultdict(list),
        'missing-terms': defaultdict(list),
    }

    def next_glossary(self) -> int:
        """Increment and return self.data['glossaries']"""
        self.data['glossaries'] += 1
        return self.data['glossaries']

    def find_term(self, term: Term) -> GlossaryListing:
        """Return GlossaryListing object matching Term from self.data['terms']
           or None"""
        assert isinstance(term, Term), "argument term (Term) required"
        match = self.data['terms'].get(term.normalize())
        found = "FOUND" if match else ""
        log(f"term resolver> '{term}' {found}")
        return match

    def add_missing(self, term: Term, doc: str, lineno: int):
        """Create and save MissingTerm object in self.data['missing-terms']"""
        assert isinstance(term, Term), "argument term (Term) required"
        assert isinstance(doc, str), "argument doc (str) required"
        assert isinstance(lineno, int), "argument lineno (int) required"
        log(f"missing term> {term}")
        orphan = MissingTerm(term, doc, lineno)
        self.data['missing-terms'][term.normalize()] = orphan
        self.env.orphans[doc].add(orphan)
        self.expire_orphans()

    def expire_orphans(self):
        self.outdated.add("docs/orphans")

    def add_term(self, term: Term, listing: GlossaryListing):
        """Save GlossaryListing to list of defined self.data['terms']"""
        assert isinstance(term, Term), "argument term (Term) required"
        assert isinstance(listing, GlossaryListing), \
            "argument listing (GlossaryListing) required"
        log(f"glossary term> {term}")
        self.data['terms'][term.normalize()] = listing

    def mkref(self, builder: Builder, term: Term, match: GlossaryListing, textnode):
        """Make a referenc node"""
        refuri = None
        if match:
            refuri = builder.get_relative_uri(match.doc, match.identifier)

        refnode = nodes.reference(
            "", "",
            internal=True,
            reftitle="",
            refuri=refuri,
            refid=f"termref-{term}"
        )

        if not match:
            refnode['classes'].append("term-missing")

        refnode.append(textnode)
        return refnode


def term_resolver(app: SphinxApplication, env: BuildEnvironment,
                  orphan: addnodes.pending_xref, textnode: nodes.inline):
    """Triggered when a xref cannot be resolved. For resolving
       missing :term:`glossary-term` references.

       * Create a new referene node with the class "term-missing"
       * Add a MissingTerm object lexicon domain data

       Params
       ------
       * app (sphinx.application.Sphinx): application object
       * env (app.builder.env): the build environment
       * orphan (nodes.pending_xref): node to be resolved
       * textnode (nodes.inline): the text node porition of orphan ref, used to
                                  create a new refnode if resolved

       Returns
       -------
       * if refdomain is "std" and reftype is "term":
           a new reference node that contains textnode
           with class "term-missing" and no href if not found
       * otherwise:
           None
    """

    if orphan.get("reftype") != "term" or orphan.get("refdomain") != "std":
        return

    domain = env.domains.get("lexicon")
    term = Term(orphan.astext())
    listing = domain.find_term(term)

    if not listing:
        domain.add_missing(term, env.docname, orphan.line)

    return domain.mkref(app.builder, term, listing, textnode)


class orphanedterms(nodes.General, nodes.Element):
    pass


def visit_orphanedterms_node(self, node):
    self.visit_container(node)


def depart_orphanedterms_node(self, node):
    self.depart_container(node)


def generate_missing_glossary(app, doctree, docname):
    """."""
    domain = app.builder.env.domains.get("lexicon")

    log("generate_missing_glossary> missing-terms:", len(domain.data["missing-terms"]))
    log("generate_missing_glossary> env.orphans:", len(app.env.orphans))

    children = []

    for doc, orphans in app.env.orphans.items():
        if not orphans:
            continue

        ref = nodes.paragraph("", "", nodes.reference(
            "", "",
            nodes.Text(doc),
            internal=True,
            refuri=app.builder.get_relative_uri(docname, doc),
        ))
        children.append(ref)

        for orphan in orphans:
            children.append(nodes.literal_block("", f"{orphan.term}\n  ..."))

    for glossary in doctree.traverse(orphanedterms):
        log("orphanedterms>", glossary)
        glossary.children = children


def init(app):
    """Initialize collector storage objects"""
    app.builder.env.orphans = defaultdict(set)


def get_outdated_docs(app, env, added, changed, removed):
    lexicon = app.env.domains.get("lexicon")
    log("get_outdated_docs>", len(lexicon.outdated))
    return changed.union(lexicon.outdated)


def setup(app):
    log("Lexicon Extension>", "setup()")

    # add Lexicon Domain
    app.add_domain(LexiconDomain)

    # handle missing-reference events with term_resolver
    app.connect("missing-reference", term_resolver)

    app.connect("builder-inited", init)
    app.connect("env-get-outdated", get_outdated_docs)

    # replace sphinx glossary directive with GlossaryDirective
    #    and rename glossary to std:glossary
    std = app.registry.domains.get('std')
    sphinx_glossary = std.directives.pop('glossary')
    app.add_directive('std:glossary', sphinx_glossary)
    app.add_directive("glossary", GlossaryDirective)

    app.add_env_collector(MissingTermsCollector)

    app.add_node(orphanedterms,
                 html=(visit_orphanedterms_node, depart_orphanedterms_node))

    app.add_directive("orphanedterms", OrphanedTermsDirective)
    app.connect("doctree-resolved", generate_missing_glossary)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
