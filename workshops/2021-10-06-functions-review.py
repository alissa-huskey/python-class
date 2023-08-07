"""Functions review"""

DEBUG_MODE = False

def div(width=40, char="="):
    print(char*width)

def hello(name):
    print("hello" , name)

def goodbye(name, phrase="Adios"):
    print(phrase, name)

def debug(message):
    if not DEBUG_MODE:
        return
    print(message)

def header(title, width=40, char="~"):
    title = f" {title} "
    return f"{title:{char}^{width}}"

chapters = [
    "functions",
    "arguments",
    "returning",
    "actual OOP",
]

debug("start of lesson")

text = ""
text = text + header("OOP Lesson") + "\n"

for name in chapters:
    text = text + f"* {name}\n"

def tip(total, percent):
    return (total * (percent/100))

subtotal = 20
tip_amount = tip(subtotal, 10)
tax = 1.6

total = subtotal + tax + tip_amount
print(tip_amount)
print("your total is ", total)

def calculate_tax(total, percent):
    return (total*percent)

tax = calculate_tax(15, .08)
print("Your tax is", tax)

# print(text)

# div(30, "-")
# div(10, "&")
# div(20)
# div()

# div(char=".")
# div(char="~", width=5)

# hello("alissa")

# goodbye("Brain")
# goodbye("Pinky", phrase="So long,")
