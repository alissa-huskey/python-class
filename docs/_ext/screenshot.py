"""Module containing screenshot directive"""

from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives
from PIL import Image
from selenium.webdriver import Chrome, ChromeOptions
from sphinx.util.docutils import SphinxDirective


class ScreenshotDirective(SphinxDirective):
    """Screenshot directive

       Directive to take a screenshot and render an image node
    """
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        'id': directives.positive_int,
        'title': directives.unchanged,
    }
    required_arguments = 1
    optional_arguments = len(option_spec)

    FORMAT = "png"
    VIEWPORT_SIZE = (1080, 900)
    THUMBNAIL_SIZE = (350, 264)

    @property
    def uri(self) -> str:
        """Return path relative to document"""
        return str(self.image.relative_to(self.docdir))

    @property
    def filename(self) -> 'str':
        """Return the filename for this screenshot"""
        if "filename" not in self.__dict__:
            choices = (
                self.options.get("id", ""),
                self.options.get("title", "").replace(" ", "_"),
                self.url,
            )

            for name in choices:
                if name:
                    self.__dict__["filename"] = f"{name}.{self.FORMAT}"
                    break
        return self.__dict__["filename"]

    @property
    def docdir(self) -> Path:
        """Return Path object of the current document directory"""
        path, _ = self.get_source_info()
        return Path(path).parent

    @property
    def imgdir(self) -> Path:
        """Return the path object where this screenshot is saved"""
        return self.docdir / "screenshots"

    @property
    def image(self) -> Path:
        """Return Path object to screenshot image"""
        return self.imgdir / self.filename

    def take_screenshot(self):
        """Take a screenshot of URL

           See also:
           * https://dzone.com/articles/how-to-take-a-screenshot-using-python-and-selenium  # noqa
        """
        if self.image.is_file():
            return

        if not self.imgdir.is_dir():
            self.imgdir.mkdir()

        options = ChromeOptions()
        options.add_argument('--headless')
        browser = Chrome(options=options)
        browser.set_window_size(*self.VIEWPORT_SIZE)
        browser.get(self.url)
        browser.get_screenshot_as_file(self.image)
        browser.quit()

    def save_thumbnail(self):
        """Resize the screenshot to a thumbnail"""
        img = Image.open(self.image)

        if (img.width, img.height) == self.THUMBNAIL_SIZE:
            return

        thumbnail = img.resize(self.THUMBNAIL_SIZE)

        with open(self.image, "wb") as fp:
            thumbnail.save(fp)

    def run(self):
        """Take a screenshot if needed then return an image node"""
        self.url = self.arguments[0]
        self.take_screenshot()
        self.save_thumbnail()

        return [nodes.image(uri=self.uri, src=self.uri)]


def setup(app):
    app.add_directive("screenshot", ScreenshotDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
