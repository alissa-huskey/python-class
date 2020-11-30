"""missing xref resolvers
"""

from sys import stderr

import docutils.nodes as nodes

def setup(app):
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
    # print("DEBUG> term_resolver>", "====================================", file=stderr)
    # print("DEBUG> term_resolver>", "FOUND MISSING TERM", identifier, file=stderr)

    std = env.domains["std"]

    # add term to registry
    #   registry objects look like this:
    #   ('term', 'Loop'): ('reference/glossary', 'term-Loop')
    std.add_object('term-missing', identifier, env.docname, "#")

    # missing_terms = { k:v for k,v in std.objects.items() if k[0] == "term-missing" }
    # print("DEBUG> term_resolver>", "missing-terms", missing_terms, file=stderr)

    # print("DEBUG> term_resolver>", "objects", std.objects, file=stderr)
    # print("DEBUG> term_resolver>", "textnode", type(textnode),
          # textnode.attributes, file=stderr)

    # create new refnode
    refnode = nodes.reference("", "", internal=True, refuri="#", reftitle="")
    refnode['classes'].append("term-missing")

    refnode.append(textnode)

    return refnode

