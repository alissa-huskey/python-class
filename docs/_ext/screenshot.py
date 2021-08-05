"""Module containing screenshot directive"""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives

class screenshot(nodes.container):
    pass

def visit_screenshot_node(self, node):
    """Append div.thumbnail-container > div.thumbnail > iframe tags to body"""
    url = node.attributes.pop("url")
    options = {"onclick": f'window.location.href = "{url}";'}
    if "title" in node.attributes:
        options["title"] = node.attributes["title"]

    self.body.append(self.starttag(node, "div", CLASS="thumbnail-container", **options))
    self.body.append(self.starttag(nodes.container(), "div", CLASS="thumbnail"))
    self.body.append(self.starttag(
        node,
        "iframe",
        src=url,
        frameborder="0",
        scrolling="no",
        onload="this.style.opacity = 1",
        sandbox = "allow-same-origin",
        **{"is": "x-frame-bypass"},
    ))

def depart_screenshot_node(self, node):
    self.body.append('</iframe></div></div>\n')

class ScreenshotDirective(SphinxDirective):
    """Screenshot directive

       Directive to generate faux screenshot using an iframe

       See also:

       * https://medium.com/@jamesfuthey/simulating-the-creation-of-website-thumbnail-screenshots-using-iframes-7145269891db
    """
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        'id': directives.positive_int,
        'title': directives.unchanged,
    }
    required_arguments = 1
    optional_arguments = len(option_spec)

    def run(self):
        return [screenshot(url=self.arguments[0], **self.options)]

def setup(app):
    app.add_directive("screenshot", ScreenshotDirective)
    app.add_node(screenshot,
        html=(visit_screenshot_node, depart_screenshot_node)
    )

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
