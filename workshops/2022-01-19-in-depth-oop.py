"""
2022-01-19 -- Data & In-Depth -- OOP

Attendees
---------
- Brian

Agenda
------
- Review OOP
    * classes
    * inheritance
- OOP
    [x] overwriting methods with super()
    [x] setattr and getattr
    [x] *args and *kwargs
    [x] dunder methods and attrs
          * __dict__
          * __str__
          * __repr__

"""

x = "hello"
func = getattr(x, "isnumeric")
print(func)

class Media():
    PARAMS = ("title", "year", "is_checked_out")

    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.is_checked_out = False

    def __getitem__(self, name):
        return self.__dict__[name]

    def __setitem__(self, name, val):
        self.__dict__[name] = val

    def __repr__(self):
        return f"<Book title={self.title!r} author={self.author!r}>"

    def __str__(self):
        return f"{self.title} ({self.year})"

    def check_out(self):
        self.is_checked_out = True

    def check_in(self):
        self.is_checked_out = False

    def __getattr__(self, name):
        """Return None if no matching attribute is found. (Instead of raising an
        AttributeError)."""
        return None

class Book(Media):
    PARAMS = ("title", "year", "author")

    def print(self, *strings, **kwargs):
        # *var : all _positional_ arguments are put in a _list_ with that variable name
        print(*strings, **kwargs)

    def __init__(self, **kwargs):
        # **var : all _keyword_ arguments are put in a _dict_ with that variable name

        for param, val in kwargs.items():
            if param in self.PARAMS:
                setattr(self, param, val)

        title = kwargs.pop("title", None)
        year = kwargs.pop("year", None)

        super().__init__(title, year)

class Movie(Media):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.director = director
        self.is_checked_out = False
        self.is_rewound = False

    def check_out(self, is_rewound=True):
        self.is_rewound = is_rewound
        super().check_out()




# this won't work with only **kwargs, but would work if we added *args
# book = Book('Lord of the Rings', 'JRR Tolkien', 1930)

book = Book(
    title='Lord of the Rings',
    author='JRR Tolkien',
    year=1930,
)

movie = Movie(
    title='Fellowship of the Ring',
    director='Peter Jackson',
    year=2002,
)

print(book["author"])

book.check_out()
# book.is_checked_out = "Yes"
book.pages = 800
print(book.is_checked_out)
print(book.title, book.xxx)

print(repr(book))
print(str(book))
