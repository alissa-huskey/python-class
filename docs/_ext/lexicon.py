"""Lexicon Domain -- expanded glossary support"""

from sys import stderr, stdout
import logging
from pprint import pformat
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from sphinx.application import Sphinx as SphinxApplication
from sphinx.environment import BuildEnvironment
from sphinx.builders import Builder
from sphinx.domains import Domain
from sphinx.util import rst
from sphinx.util.nodes import make_id
from sphinx import addnodes
from sphinx.domains.std import Glossary as SphinxGlossary
from sphinx.util.docutils import register_directive
from docutils.parsers.rst import directives
from docutils import nodes
from docutils import statemachine
from more_itertools import first


class Logger():
    """Logging class"""

    """Width of decorative lines"""
    WIDTH: int = 75

    """Directory to write logfiles"""
    LOGDIR = Path(__file__).parents[2].joinpath("tmp")

    """Default log record format"""
    FMT: str = "%(asctime)s [%(levelname)s] %(message)s"

    """Default date format"""
    DATEFMT: str = "%Y-%m-%dT%H:%M:%S"

    """Long date format"""
    LONG_DATE: str = "%a, %b %d, %Y @ %I:%M%p %Z"

    """Log levels"""
    LEVELS: dict = {
        'NOTSET': 0,
        'DEBUG': 10,
        'INFO': 20,
        'WARNING': 30,
        'WARN': 30,
        'ERROR': 40,
        'CRITICAL': 50,
        'FATAL': 50,
    }

    """Available outputs"""
    OUTPUTS: tuple = ("file", "stderr", "stdout", "null")

    """logger interface"""
    logger: logging.Logger

    """logger name"""
    name: str

    """logging status"""
    enabled: bool

    """where to write log output
       determines handler
       see: OUTPUTS
      """
    output: str

    """Maximum log messages to emit
       see: LEVELS
    """
    level: int

    """Ouput format strings
       logging.Formatter, datefmt
       see: FMT: DATEFMT, LONGDATE
    """
    format: tuple

    """Output handler
       set through output
    """
    handler: logging.Handler

    def __init__(self, name: str, output: str="file",
                 enabled: bool=True, level=logging.DEBUG):
        """Initializer
        Params
        ------
        * name (str)                              : log name
        * output (str, default: "file")           : used to determine handler
                                                    (see Logger.OUTPUTS)
        * level (int|str, default: logging.debug) : log level
                                                    (see Logger.LEVELS)
        * enabled (bool, default: True)           : enable logging

        Examples
        --------
        >>> log("lexicon", enabled=False)
        >>> log("lexicon", output="stderr")
        >>> log("lexicon")
        """
        if not enabled:
            level, output = 0, "null"

        self._init_attrs_()
        self.logger = logging.getLogger(__file__)
        self.name = name
        self.enabled = enabled
        self.output = output
        self.level = level
        self.format = self.FMT, self.DATEFMT

        self._init_methods_()
        self._init_log_()

    def _init_attrs_(self):
        """Initialize internal property attributes"""
        for attr in ("nh", "fh", "eh", "sh", "handler", "format",
                     "date_format", "enabled", "level"):
            setattr(self, f"_{attr}", None)

    def _init_methods_(self):
        """Create logging methods for levels"""
        for lvl in list(self.LEVELS.keys())[1:]:
            level= getattr(logging, lvl)
            name = lvl.lower()
            method = self.mklog_fn(name, level)
            setattr(self, name, method)

    def _init_log_(self):
        """Write startup messages to log stream"""
        num, level = self._lvl_(self.level)
        output, handler = self.output, repr(self.handler)
        plain, line = " %(message)s", "="*self.WIDTH
        status = ("DISABLED", "ENABLED")[self.enabled]

        self.write(f"\n{line}")
        self.write(datetime.today().strftime(self.LONG_DATE), fmt=plain)
        self.write(f"Initializing {self.name} log: {status}", fmt=plain)
        self.write(f"Level {num}: {level}", fmt=plain)
        self.write(f"Output {output}: {handler}", fmt=plain)
        self.write(f"{line}\n")

    def __call__(self, *args, **kwargs):
        """Log using default log level when called"""
        self.log(*args, **kwargs)

    def _lvl_(self, lvl) -> tuple:
        """Normalize level, Return int, str"""
        if isinstance(lvl, str):
            level = lvl.upper()
            num = self._lvl_to_num_(lvl)
        elif isinstance(lvl, int):
            level = self._lvl_to_str_(lvl)
            num = lvl
        return num, level

    def _lvl_to_num_(self, level) -> int:
        """Return int for level str"""
        return self.LEVELS.get(str(level).upper(), level)

    def _lvl_to_str_(self, lvl) -> str:
        """Return str for level int"""
        mapping = dict(zip(self.LEVELS.values(), self.LEVELS.keys()))
        return mapping.get(lvl)

    def mkmsg(self, *args, **kwargs) -> str:
        """Return log message for args"""
        return " ".join(map(str, args))

    def write(self, *args, fmt="%(message)s", **kwargs):
        """write info message, with temp changes to output, level, and format
           as follows:

           * output: if null, switch to stdout
           * level: set to info
           * format: switch to fmt argument
        """
        output = "stdout" if self.output == "null" else self.output
        revert = self.level, self.output, self.format
        self.level, self.output, self.format = "info", output, fmt
        self.info(*args, **kwargs)
        self.level, self.output, self.format = revert

    def log(self, *args, **kwargs):
        """Write message to log stream
        Params
        ------
        * args: message
        * level (str|int, default: logging.DEBUG): level of log message
        """
        level = kwargs.get("level", logging.DEBUG)
        msg = self.mkmsg(*args, **kwargs)
        self.logger.log(level, msg)

    def mklog_fn(self, name: str, level: int):
        """Generage log function named name for log level level"""
        def log_fn(*args, **kwargs):
            """write log message"""
            kwargs['level'] = level
            self.log(*args, **kwargs)
        log_fn.__name__ = name
        return log_fn

    @property
    def null(self) -> logging.NullHandler:
        """Return log handler to disable printing log messages"""
        if not self._nh:
            self._nh = logging.NullHandler()
        return self._nh

    @property
    def stdout(self) -> logging.StreamHandler:
        """Return log handler to print to stdout"""
        if not self._sh:
            self._sh = logging.StreamHandler(stream=stdout)
        return self._sh

    @property
    def stderr(self) -> logging.StreamHandler:
        """Return handler to print to stderr"""
        if not self._eh:
            self._eh = logging.StreamHandler(stream=stderr)
        return self._eh

    @property
    def file(self) -> logging.FileHandler:
        """Return handler to print to file"""
        if not self._fh:
            self._fh = logging.FileHandler(self.LOGDIR.joinpath(f"{self.name}.log"))
        return self._fh

    @property
    def output(self) -> str:
        """output property"""
        return self._output

    @output.setter
    def output(self, value):
        """Set self._output and set handler to matching handler property
           see Logger.OUTPUTS for valid output strings
        """
        if value not in self.OUTPUTS:
            msg = f"No handler found for output: '{value}'\n"
            msg += "Must be one of: {self.outputs}"
            raise NameError(msg)
        self._output = value
        self.handler = getattr(self, self._output)

    @property
    def enabled(self) -> bool:
        """enabled property"""
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """set self._enabled
           setting to False sets level and output
        """
        self._enabled = enabled
        if not self._enabled:
            self.output = "null"
            self.level = 0

    @property
    def handler(self) -> logging.Handler:
        """handler property"""
        return self._handler

    @handler.setter
    def handler(self, handler):
        """set self._handler, add to logger, and remove old handler"""
        if self._handler and self.logger.handlers:
            self.logger.removeHandler(self._handler)
        self._handler = handler
        self.logger.addHandler(self._handler)

    @property
    def format(self) -> tuple:
        """format property
           tuple with two format strings:
           * logging.Formatter fmt
           * time.strftime fmt
        """
        return self._format, self._date_format

    @format.setter
    def format(self, fmts):
        """set _format and self._date_format and set the handler format
           if a single format string is passed, datefmt will default to
           self.DATEFMT"""
        if isinstance(fmts, str):
            fmts = (fmts, self.DATEFMT)
        self._format, self._date_format = fmts
        formatter = logging.Formatter(*fmts)
        self.handler.setFormatter(formatter)

    @property
    def level(self):
        """level property"""
        return self._level

    @level.setter
    def level(self, lvl):
        """set self._level and update logger and handler"""
        self._level, _ = self._lvl_(lvl)
        self.logger.setLevel(self._level)
        self.handler.setLevel(self._level)

# log = Logger("lexicon")
log = Logger("lexicon", enabled=False)

class Term(str):
    """Class for Terms"""

    def normalize(self):
        """Provide trimmed sha string"""
        return self.lower().replace(" ", "-").rstrip("s")


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

    def __init__(self, doc: str=None, category: str="", num: int=None,
                 elements: list=[[None]]):
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

    def __init__(self, glossary: Glossary=None,
                 node: nodes.definition_list_item=None):
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

    directives = {
        'glossary': GlossaryDirective,
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
        """Return GlossaryListing object matching Term from self.data['terms'] or None"""
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
        self.data['missing-terms'][term.normalize()] = \
            MissingTerm(term, doc, lineno)

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

        refnode = nodes.reference("", "",
                                internal=True,
                                reftitle="",
                                refuri=refuri,
                                refid=f"termref-{term}")
        if not match:
            refnode['classes'].append("term-missing")

        refnode.append(textnode)
        return refnode


def setup(app):
    log("Lexicon Extension>", "setup()")

    # add Lexicon Domain
    app.add_domain(LexiconDomain)

    # handle missing-reference events with term_resolver
    app.connect("missing-reference", term_resolver)

    # replace sphinx glossary directive with GlossaryDirective
    #    and rename glossary to std:glossary
    std = app.registry.domains.get('std')
    del std.directives['glossary']
    app.add_directive('std:glossary', SphinxGlossary)
    app.add_directive("glossary", GlossaryDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


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


