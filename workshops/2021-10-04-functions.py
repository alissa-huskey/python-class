"""2021/10/4 Functions Live Share
https://alissa-huskey.github.io/python-class/lessons/functions.html#table-of-contents

Exercise
--------

In your flashcards.py file:

[ ] If you don't already have one, make a global variable DEBUG
[ ] Write a function named: debug with one parameter: message
[ ] In the function, check if DEBUG is True (or truthy)
    [ ] If so, then print message
    [ ] Bonus: Print someting before it like "DEBUG: ", or "# ", so you can more
        easily tell that it is a debug message
[ ] Throughout your code, anywhere where you are printing something that is not
    directly related to the flashcards program (ie. "loading {path}..."), call
    your new debug function instead of printing it.
[ ] Also look for any comment out print statements, change print to debug, and uncomment them.
[ ] Perhaps add a few extra debug messages. For example, you might want to print
    the function name at the beginning of each function.
[ ] Test with DEBUG set to True as well as with DEBUG set to False

Example:

    DEBUG = True

    def load_csv(path):
        ...
        debug(f"loading {path}...")

    def menu():
        debug(f"The files available are: {TOPICS}")
        ...
        debug(f"You picked: {reply}")
        ...
        debug(f"The files you picked are: {selected}")
        ...
        return selected
"""

def header(title):
    title = f" {title} "
    print(f"\n{title:~^50}\n")

def subheader(title):
    title = f"{title} "
    print(f"{title:_<30}\n")

def hello(times):
    subheader("Exercise #4!")
    return "hello" * times

def main():
    variable_name = "some value"

    header("10/4 Live Share!")
    subheader("Parameters")
    text = hello(1)
    print(text, "\n")

    text = hello(3)
    print(text, "\n")

if __name__ == "__main__":
    main()

