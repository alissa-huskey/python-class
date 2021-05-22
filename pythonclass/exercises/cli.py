"""Module for CLI helpers"""

from contextlib import contextmanager

from blessed import Terminal


__all__ = [
    "abort",
    "await_keypress",
    "colorize",
    "output",
    "quit",
    "GracefulExit",
    "FatalError",
    "WIDTH",
]

TERM = Terminal()
WIDTH = TERM.width

HALIGN = {
    "right": "rjust",
    "center": "center",
}

class ArgumentError(BaseException): ...

class ExitState(SystemExit):
    prefix = ""

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__()

class GracefulExit(SystemExit):
    def __init__(self, code=0, message=""):
        super().__init__(code, message)

class FatalError(ExitState):
    prefix = "Error: "

    def __init__(self, code=1, message=""):
        super().__init__(code, message)

def quit(message="", code=0):
    """Raise GracefulExit"""
    raise GracefulExit(code, message)

def abort(message="", code=1):
    """Raise FatalError"""
    raise FatalError(code, message)

def colorize(text, colors: str):
   """"Change the text color to colors"""
   if not colors:
       return text
   func = getattr(TERM, colors)
   return func(text)

def align_horiz(text: str, alignment: str=None, width=WIDTH, **kwargs):
    """Return horizontally aligned text

       Params
       ------
       * text (str): string to align
       * alignment (None, str): how to align (center, right, default: None)
       * width (None, int): width to align text to (default: WIDTH)
       * kwargs: other arguments forwarded to str.center() or str.rjust()
    """
    if not alignment:
        return text
    if alignment not in HALIGN:
        raise ArgumentError(
            "the second argument to align()"
            "must be 'right' or 'center'")

    func = getattr(text, HALIGN[alignment])
    return func(width, **kwargs)

def output(*values, color=None, align=None, width=WIDTH, sep=" ", **kwargs):
    """fancy print

       Params
       ------
       * values (Any) -- values to print
       * color (str) -- change text to this color before printing
       * align (str) -- horizontal alignment of text (center, right, default: None)
       * width (int, None) -- width to align text to
       * kwargs -- other arguments forwarded to print()
    """

    text = sep.join(map(str, values))

    if align:
        text = align_horiz(text, align, width)

    if color:
        text = colorize(text, color)

    print(text, **kwargs)

def await_keypress():
    """Hides the cursor until the user presses a key then return it."""
    with TERM.cbreak(), TERM.hidden_cursor():
        return TERM.inkey()

def goto_middle(addlines = 0):
    """Go to the middle of the screen plus addlines"""
    line = int((TERM.height / 2) + addlines)
    execute(TERM.move_y(line))

def goto_bottom(sublines=1):
    """Go to the bottom of the screen minus sublines"""
    execute(TERM.move_y(TERM.height - sublines))

goback = TERM.location

def clear():
    """Clear the screen"""
    execute(TERM.clear)

def execute(characters: str):
    """Print terminal control characters to the screen without a newline"""
    print(characters, end="")

class symbols():
    """fancy unicode characters"""

    right = colorize("\u2714", "green")          # ✔
    wrong = colorize("\u2716", "red")            # ✖

    done            = "\u2705"                   # ✅
    sparkles        = "\u2728"                   # ✨
    star            = "\u2B50"                   # ⭐
    start2          = "\U0001F31F"               # 🌟
    start3          = "\U0001F4AB"               # 💫
    thumbsup        = "\U0001F44D"               # 👍
    trophy          = "\U0001F3C6"               # 🏆
    medal           = "\U0001F3C5"               # 🏅
    clap            = "\U0001F44F"               # 👏
    hundred         = "\U0001F4AF"               # 💯
    ok              = "\U0001F44C"               # 👌
    rock            = "\U0001F918"               # 🤘
