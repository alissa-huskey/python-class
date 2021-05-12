"""Print the filename and docstrings of *.py files"""

from pathlib import Path
import textwrap

DOCSTRING_QUOTES = ('"""', "'''")
MAXWIDTH = 88

def get_file_docstring(filepath: Path=None, contents: str=None):
    """Exract docstring from Python code

       Args
       ----
       filepath (Path): location of file to extract docstring from
       contents  (str): contents of file to extract docstring from
    """

    enclosing_quotes = None
    docstring = None

    # read contents of Path object
    if filepath and contents == None:
        contents = filepath.read_text()

    # error if neither contents nor filepath was passed
    if contents == None:
        raise TypeError("Missing required argument, one of: filepath (Path) or contents (str).")

    # iterate through lines
    for line in contents.splitlines():
        line = line.strip()

        # skip empty lines and comments
        if not line or line.startswith("#"):
            continue

        # line starts docstring
        if not enclosing_quotes and line[:3] in DOCSTRING_QUOTES:
            # single or double quotes
            enclosing_quotes = line[:3]

            # start the docstring
            docstring = line

        # line continues docstring
        elif enclosing_quotes:
            docstring += "\n" + line

        # if first non-empty, non-comment line of code is not a docstring
        # then there is no docstring in file
        else:
            break

        # docstring is closed
        # (handles opening docstring quotes alone on line)
        if len(docstring) > 6 and docstring.endswith(enclosing_quotes):
            break

    # remove enclosing quotes, strip leading and trailing whitespace
    if docstring:
        return docstring[3:-3].strip()

def main():
    srcdir = Path(__file__).parent.parent
    path = srcdir / "lessons"
    files = []

    # collect filenames and docstrings in list of tuples
    for f in path.glob("*.py"):
        docstring = get_file_docstring(f) or "---"
        files.append((f.name, docstring))

    # calculate left column size (maximumn filename length)
    margin = max([len(x[0]) for x in files]) + 1

    # print wrapped filenames in columns
    for name, desc in files:
        docstring = name.ljust(margin) + desc
        lines = textwrap.wrap(docstring, width=MAXWIDTH, subsequent_indent=margin*" ")

        print("\n".join(lines))
        print()

if __name__ == "__main__":
    main()
