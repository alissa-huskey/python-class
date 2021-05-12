"""An off-the-cuff lesson on manipulating string paths"""

from pathlib import Path

def get_filename(location):
    """Extract the filename from a path that includes one or more directories"""
    seperator = "/"
    position = None

    for i, character in enumerate(location):
        if character == seperator:
            position = i

    position = position + 1
    return location[position:]

def demo_filenames():
    """Demonstration of getting filenames from path strings manually or using
       Path objects"""
    path = Path(r'docs\lessons\imports.md')
    print(f'the filename of "{path}" is: "{path.name}"')

    path = Path("something-else/data/contacts.txt")
    print(f'the filename of "{path}" is: "{path.name}"')

    path = Path("~/documents/README.md")
    print(f'the filename of "{path}" is: "{path.name}"')

def main():
    dirpath = Path.cwd() / "docs" / "lessons"

    for filepath in dirpath.iterdir():
        if filepath.is_dir():
            continue

        if filepath.suffix != ".md":
            continue

        print(filepath.name)

main()
