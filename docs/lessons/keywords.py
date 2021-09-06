"""Generate list of keywords and write to keywords.md """

from keyword import kwlist
from IPython.display import Markdown
from pathlib import Path

outfile = Path(__file__).with_suffix(".md")
keywords = [f"* `{kw}`" for kw in kwlist]
md = Markdown("\n".join(keywords))

outfile.write_text(md.data)

