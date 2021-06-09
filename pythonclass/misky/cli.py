from cmd import Cmd
from os import _exit as exit
import sys
import shlex

class Thing(Cmd):
    """The Thing CLI"""
    intro = "Welcome. ('?' for help, 'q' to quit)"
    prompt = "> "
    file = None

    def __init__(self, *args, **kwargs):
        self.args = []
        self.cmd = ""

        super().__init__(*args, **kwargs)

    def debug(self, name, *args):
        """Print a debug message"""
        values = [f"({type(a)},) {a!r}" for a in args]
        print("-"*30)
        print(f"{name}() received:", "; ".join(values))
        print(f"{self.lastcmd=}")
        print(f"{self.cmd=} ; {self.args=}")
        print("-"*30, "\n")

    def default(self, *args):
        self.debug("default", *args)
        super().default(*args)

    def parseline(self, line):
        cmd, arg, line = super().parseline(line)

        self.cmd = cmd
        self.args = shlex.split(arg) if isinstance(arg, str) else arg

        print(f"parseline(): {cmd=} ; {self.args=}")
        return cmd, self.args, line

    def do_thing(self, *args):
        """Do the thing"""
        self.debug("thing", *args)

    def do_quit(self, *args):
        """Exit the program"""
        self.debug("quit", *args)
        exit(0)

    do_q = do_EOF = do_quit

if __name__ == "__main__":
    Thing().cmdloop()
