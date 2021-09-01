from cmd import Cmd
import sys
import shlex
from more_itertools import first

class Thing(Cmd):
    """The Thing CLI"""
    intro = "Welcome. ('?' for help, 'q' to quit)"
    prompt = "> "

    def __init__(self, *args, **kwargs):
        self.args = []
        self.cmd = ""
        self.stopping = False
        self.is_debug = False

        super().__init__(*args, **kwargs)

    def debug(self, name, *args):
        """Print debug info about the command called"""
        if not self.is_debug:
            return

        values = [f"({a.__class__.__name__}) {a!r}" for a in args]
        self.info("-"*30)
        self.info(f"do_{name}() received:", "; ".join(values) or "(nothing)")
        self.info(f"{self.lastcmd=}")
        self.info(f"{self.cmd=} ; {self.args=}")
        self.info("-"*30, "\n")

    def info(self, *args):
        """Print verbose output if debug mode is enabled"""
        if not self.is_debug:
            return
        print(*args)

    ###########################################################################
    ## Overridden
    #
    #  * do_shell        called when command prefixed with ! is dispatched
    #  * precmd          called before command is dispatched, returnes line to
    #                    execute
    #  * default         called when command is not found
    #  * preloop         called once when cmdloop() is called
    #  * postloop        called once before cmdloop() returns
    ###########################################################################

    # called after command is finished
    # return True to quit
    def postcmd(self, stop, line):
        """Print an extra newline."""
        print()
        return stop or self.stopping

    # called when an empty line is entered
    def emptyline(self):
        """Do nothing"""

    # parse input line
    def parseline(self, line):
        self.cmd, arg, line = super().parseline(line)
        self.args = shlex.split(arg) if isinstance(arg, str) else arg

        self.info(f"parseline(): {self.cmd=} ; {self.args=}")
        self.debug(self.cmd, *self.args)

        return self.cmd, self.args, line

    ###########################################################################
    ## Help
    #  name functions help_TOPIC or help_COMMAND
    ###########################################################################

    # called when command starts with ? or help
    def do_help(self, args):
        """Hack to ensure that the argument sent to do_help is a string"""
        args = first(args, ())
        if isinstance(args, str):
            arg = args
        else:
            arg = first(args, "")

        return super().do_help(arg)

    ###########################################################################
    ## Commands
    #  name functions do_COMMAND
    ###########################################################################

    def do_debug(self, args):
        """Show debug mode status and optionally enable or disable.
           usage: debug [on|off|toggle]"""

        mode = first(args, "print")

        if mode in ["on", "off"]:
            self.is_debug = {"off": False, "on": True}[mode]
        elif mode in ["t", "toggle"]:
            self.is_debug = not self.is_debug

        print("Debug mode is:", ("off", "on")[self.is_debug])

    def do_thing(self, args):
        """Do the thing"""
        print(*args)

    def do_quit(self, *args):
        """Exit the program"""
        self.stopping = True

    do_q = do_EOF = do_quit

if __name__ == "__main__":
    Thing().cmdloop()
