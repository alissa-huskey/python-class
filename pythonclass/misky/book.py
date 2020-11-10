"""Wherein I mess around with List Comprehensions and string formatting
https://realpython.com/list-comprehension-python/
https://docs.python.org/3/library/string.html
"""


class Printer:
    """."""
    elements: list
    width: int = 80
    head: str

    def __init__(self, head, *elements):
        self.head = head
        self.elements = elements

    def longest(self, *args) -> int:
        """Return the length of the longest argument
        Args:
            [string, ...]
        """
        return max([len(v) for v in list(args)])

    def print(self):
        """Format a the contents of a dict"""
        HeadPrinter(self.head).print()
        for item in self.elements:
            if isinstance(item, dict):
                DictPrinter(item).print()
        print()


class DictPrinter(Printer):
    """."""
    PADDING: int = 2

    items: dict
    colwidth: int

    def __init__(self, items: dict):
        self.items = items
        self.colwidth = self.longest(*list(self.items.keys())) + self.PADDING

    def print(self):
        """Print the formatted contents of a dict"""
        for key in self.items:
            title = TitlePrinter(key).print()
            val = ValuePrinter(self.items[key]).print()
            print(f"{title:>{self.colwidth}}: {val}")


class ValuePrinter(Printer):
    """."""
    val: any

    def __init__(self, val):
        self.val = val

    def print(self) -> str:
        if isinstance(self.val, bool):
            return BoolPrinter(self.val).print()
        else:
            return self.val


class HeadPrinter(Printer):
    """."""
    val: str

    def print(self) -> str:
        head = f" {self.head.title()} "
        print(f"{head:=^{self.width}}")


class BoolPrinter(ValuePrinter):
    """."""
    val: bool

    def print(self) -> str:
        if self.val:
            return "Yes"
        else:
            return "No"


class TitlePrinter(ValuePrinter):
    """."""
    val: str

    def print(self) -> str:
        """Print the formatted contents of a dict"""
        return self.val.replace("_", " ").title()


book = {
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'date_published': 1925,
    'in_stock': True
}

Printer("book", book).print()
