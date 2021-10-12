"""2021/10/11 Functions and arguments continued; ANSI escape codes

https://alissa-huskey.github.io/python-class/lessons/functions.html


console module
--------------

For more info:

https://github.com/mixmastamyk/console

To install, in the terminal do either:

pip install console

or

poetry add console

To see a demo of all the stuff it can do including color and style names:

python -m console.demos

"""

from console import fg, bg, fx

def message(greeting="", text=""):
    if greeting:
        greeting = f"{greeting}!"
    print(greeting, text)

def tip(subtotal, percentage=20, service=1):
    percentage = percentage * service
    amount = subtotal * percentage/100
    print(f"The tip for a ${subtotal:.02f} check with {percentage}% is ${amount:.02f}.")

def info(text, color="white", style="normal"):

    colors = {
        "white": 39,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
    }

    styles = {
        "normal": 8,
        "bold": 1,
        "dim": 2,
        "italic": 3,
        "underline": 4,
        "strike": 9,
    }

    color_code = colors[color.lower()]
    style_code = styles[style.lower()]
    escape_code = f"\033[{color_code};{style_code}m"
    print(f"({color}/{style})> {escape_code!r} {escape_code}{text}\033[0m")



message("Bonjourno", "Let's get some lunch")
message("Chiao", "I need to go to the library")
message("Aloha")
message()

tip(10)
tip(100, 15)
tip(100, 20, .5)
tip(100, 20, 1.5)

tip(service=1.25, subtotal=200)

print(555, 555, 5555, sep="-")

info("Hello there")
info("Goodbye", style="bold")
info("Just kidding", color="Blue")

# text = "\033[33moh hi there\033[0m"
# print(text)


print(fg.yellow("this is yellow"))
print(bg.blue("this is a blue background"))
print(fx.italic("this is italic"))

print(fx.dim("DEBUG: just so you know, I'm doing a thing now."))
print("thing")
print(fg.red("ERROR"), "failed to do a thing")
