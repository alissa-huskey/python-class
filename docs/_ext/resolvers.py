"""missing xref resolvers
"""

from sys import stderr

import docutils.nodes as nodes
from more_itertools import first

def normalize(text):
    """Normalize terms for comparison"""
    return text.lower().replace("-", " ").rstrip("s")


def mkref(app, ident, doc, textnode):
    """Make a referenc node"""
    if ident:
        refuri, refid = app.builder.get_relative_uri(doc, ident), None
    else:
        refuri, refid = None, ident

    # create new refnode
    refnode = nodes.reference("", "",
                              internal=True,
                              reftitle="",
                              refuri=refuri,
                              refid=refid)
    if not ident:
        refnode['classes'].append("term-missing")

    refnode.append(textnode)
    return refnode

def find_matching_term(identifier, objects):
    """Find a term in the registry"""
    #   registry objects look like this:
    #   ('term', 'Loop'): ('reference/glossary', 'term-Loop')
    # terms = (k[1] for k in std.objects if k[0] == "term")
    matches = [(label, doc) for (cat, label), (doc, _) in objects.items()
               if cat == "term" and
               normalize(label) == normalize(identifier)]
    match = first(matches, (None, None))

    if len(matches):
        echo_debug(f"term_resolver> '{identifier}' FOUND ({len(matches)})")

    return match


def echo_debug(*args):
    """Print debug message to stderr"""
    print("\033[33mDEBUG>\033[0m", *args, file=stderr)


def setup(app):
    echo_debug("resolvers.py", "setup()")

    # on missing-reference event, call the term_resolver function
    app.connect("missing-reference", term_resolver)

    # create object type std domain to store unresolved terms
    app.add_object_type("term-missing", "missing")

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def term_resolver(app, env, orphan, textnode):
    """Triggered when a xref cannot be resolved, for resolving
       missing :term:`glossary-term` references.

       * Create a new referene node with the class "term-missing"
       * Add a "term-missing" object to the registry

       Params
       ------
       * app - sphinx.application.Sphinx object
       * env – the build environment (app.builder.env).
       * orphan – the pending_xref node to be resolved.
       * textnode – a inline text node (non-ref) version of orphan.
                   if resolved, return a node containing textnode as a child

       Returns
       -------
       * if refdomain is "std" and reftype is "term":
           a new reference node with class "term-missing",
           that contains textnode
       * otherwise:
           None
    """

    if orphan.get("reftype") != "term" or orphan.get("refdomain") != "std":
        return

    identifier = orphan.astext()

    std = env.domains["std"]
    match, doc = find_matching_term(identifier, std.objects)
    if not match:
        # add to missing-term registry
        std.add_object('term-missing', identifier, env.docname, "#")

    return mkref(app, match, doc, textnode)
