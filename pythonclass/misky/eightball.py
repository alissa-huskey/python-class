"""Magic 8-ball"""

import random
import time
from shutil import get_terminal_size

import colorama
from console import bg, fg
from console.screen import sc

# seconds to delay between fade-in steps
DELAY = 0.3

# background and foreground colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# number of steps to fade from bg to fg color
STEPS = 11

# width of colored box
# note: must be > 26, the max length of ANSWERS
BOX_SIZE = 30

# possible answers
ANSWERS = [
    "It is Certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

def to_hex(rgb):
    """Convert iterable of rgb values to hex string

    >>> to_hex((255, 255, 255))
    'ffffff'
    """
    return '{:02x}{:02x}{:02x}'.format(*rgb)

def get_color(palette, color):
    """Return the console color in palette for rgb color

    Args:
        palette: console.fg or console.gb
        color: iterable of rgb values or hex string

    Returns:
        console.core._PaletteEntry object

    >>> get_color(fg, "000000").name
    'T_000000'
    >>> get_color(bg, (255, 255, 255)).name
    'T_FFFFFF'
    """
    if not isinstance(color, str):
        color = to_hex(color)
    return getattr(palette, f"t_{color}")

def gradient(start_rgb, end_rgb, steps):
    """Return a list of console colors in a gradient from start_rgb to end_rgb
       over number of steps

    >>> gradient((0, 0, 255), (255, 255, 255), 5)
    ['3333ff', '6666ff', '9999ff', 'ccccff', 'ffffff']
    """
    colors = []
    for step in range(1, steps+1):
        # calculate gradient: start_rgb + (step_amount=difference/steps)
        rgb = [
            int(start_rgb[i]+((end_rgb[i] - start_rgb[i])/steps * step))
            for i in range(3)]

        colors.append(to_hex(rgb))

    return colors

def main():
    """Magic 8-ball
       An answer to your yes-or-no question will be revealed.
    """
    # initialize terminal color and get the width
    colorama.init()
    width, _ = get_terminal_size()

    # number of spaces needed to center answer box
    margin = int((width - BOX_SIZE)/2)

    # choose a random answer
    answer = random.choice(ANSWERS)

    # hide the cursor while answering
    with sc.hidden_cursor():

        # print a canvas of three blank lines
        print("\n"*2)

        # generate a gradient of foreground colors from blue to white
        for fg_hex in gradient(BLUE, WHITE, STEPS):

            # make a palette composite object of fg and bg color
            style = get_color(fg, fg_hex) + bg.blue

            # return to the same location after each printing
            # to enable the fade-in effect
            with sc.location():

                # add a short delay
                time.sleep(DELAY)

                # put the cursor on the middle blank canvas line
                # then move to the right so the answer will be centered
                print(sc.move_up(2), sc.move_right(margin), end="")

                # print the answer
                print(style(answer.center(BOX_SIZE)), sep="", end="")


if __name__ == "__main__":
    main()
