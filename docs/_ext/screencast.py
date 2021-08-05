"""
Add support for embedding asciinema screencasts.

* provides a screencast directive
* add all .cast files to config.html_extra_path so they are copied to _build

Requires:
    From the latest release:

    https://github.com/asciinema/asciinema-player/releases/

    Download these assets and add them to _static/:

    * asciinema-player.js
    * asciinema-player.css


See also:
    * https://github.com/asciinema/asciinema-player/blob/master/README.md
    * https://asciinema.org/
    * https://github.com/asciinema/asciinema

"""

from pathlib import Path
from pprint import pformat
from sys import stderr
from os.path import getmtime

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives

def info(*args):
    print("---------->", *args, file=stderr)

def add_cast_files(app, config):
    """Add all .cast files to config.html_extra_path"""
    srcdir = Path(app.srcdir)
    outdir = Path(app.outdir)

    for path in srcdir.glob("**/*.cast"):
        # skip files in _build
        if outdir in path.parents:
            continue

        # the same location in outdir
        newpath = outdir / path.relative_to(srcdir)

        # time file was modified
        mtime = int(getmtime(path))

        # do nothing more if it's already there and has not been modified
        if newpath.is_file() and int(getmtime(newpath)) >= mtime:
            continue

        # create directory in outdir if it doesn't exist
        if not newpath.parent.is_dir():
            newpath.parent.mkdir(parents=True)

        # copy file
        newpath.write_text(path.read_text())

class asciinema_player(nodes.General, nodes.Element):
    """Node for <asciinema-player> tag"""
    pass

class ScreencastDirective(SphinxDirective):
    """screencast directive returns an asciinema_player node"""
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        'cols': directives.positive_int,
        'rows': directives.positive_int,
        'autoplay': directives.unchanged,
        'preload': directives.unchanged,
        'loop': directives.unchanged,
        'start-at': directives.unchanged,
        'speed': directives.unchanged,
        'idle-time-limit': directives.unchanged,
        'poster': directives.unchanged,
        'font-size': directives.unchanged,
        'size': directives.unchanged,
        'theme': directives.unchanged,
        'title': directives.unchanged,
        't': directives.unchanged,
        'author': directives.unchanged,
        'author-url': directives.unchanged,
        'author-img-url': directives.unchanged,
        'path': directives.unchanged,
        'id': directives.unchanged,
    }
    required_arguments = 1
    optional_arguments = len(option_spec)

    def run(self):
        filename = self.arguments[0]
        path = self.options.pop("path", "")

        self.options["src"] = path + filename

        return [asciinema_player(options=self.options)]


def visit_asciinema_player_node(self, node):
    """Generate <asciinema-player> tag from an asciinema_player node"""
    options = node.get("options", {})

    attrs = " ".join([f'{k}="{v}"' for k,v in options.items()])
    html = f"<asciinema-player {attrs}></asciinema-player>"

    self.body.append(html)


def depart_asciinema_player_node(self, node):
    ...

def setup(app):
    app.connect("config-inited", add_cast_files)
    app.add_directive("screencast", ScreencastDirective)
    app.add_node(asciinema_player,
        html=(visit_asciinema_player_node, depart_asciinema_player_node)
    )

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
