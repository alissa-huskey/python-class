"""Script to find path of bin directory
    requires Python 3.4+
"""

from argparse import ArgumentParser
import os
from os import _exit as exit
import re
from pathlib import Path
import platform
from pprint import pprint
from string import Template
import subprocess
import sys

class Config:
    binname: str
    command: str
    homevar: str
    cmdmsg : str = ""

    def __new__(cls, osname):
        if osname == "Windows":
            klass = WindowsConfig
        else:
            klass = NixConfig
        return super(Config, cls).__new__(klass)

    @property
    def old_paths(self):
        if CFG.use_homevar not in ("all", "prev"):
            return CFG.pathvar

        dirs = {use_homevar(Path(d).absolute()) for d in os.get_exec_path()}
        return os.pathsep.join(map(str, dirs)) + os.pathsep


class NixConfig(Config):
    binname: str = "bin"
    homevar: str = '$HOME'
    pathvar: str = '$PATH'

    def ok(self, *args):
        return True

    @property
    def command(str):
        return 'export PATH="${new_paths}${old_paths}"'

    def shellrc(self):
        shell = os.getenv("SHELL", "")
        if shell:
            shell = re.sub(rf'^.*{os.sep}', '', shell)
            return f".{shell}rc"
        else:
            return "shell rc"

    @property
    def cmdmsg(self):
        """."""
        return f"Add the following to your {self.shellrc()} file."

class WindowsConfig(Config):
    path_limit: int = 1024
    binname: str = "Scripts"
    homevar: str = '%HOME%'
    pathvar: str = '%PATH%'
    cmdmsg:  str = ("Requires administrator mode. "
                    "(Enable with: net user administrator /active:yes)")

    def ok(self, new_paths):
        """Return False if the length of the new PATHS string will be more than
        maximum characters characters"""
        old_paths = CFG.old_paths
        path_text = f'{new_paths}{old_paths}'
        length = len(path_text)
        is_ok = length < self.path_limit
        if not is_ok:
            msg = [f"Error New PATH string will be longer than {self.path_limit}:",
                   f"      ({length}) '{path_text}'"]
            if not CFG.use_homevar:
                msg.append("Tip: Try shortening with --use-homevar option")

            print(*msg, sep=os.linesep, file=sys.stderr)

        return is_ok

    @property
    def command(self):
        set_cmd = f'setx path "$new_paths{CFG.old_paths}"'

        return f"runas /user:Administrator ^{os.linesep}'{set_cmd}'"


CFG = Config(platform.system())

def binpaths(include_base=False, only_missing=False):
    """Return a list of directory paths

    Params
    ------
    * include_base (bool, default=False) - search in base_prefix and
                                           base_exec_prefix for bin dirs too
    * only_missing (bool, default=False) - only include dirs missing from PATH
    """
    prefixes = {sys.prefix, sys.exec_prefix}

    if include_base:
        prefixes |= {sys.base_prefix, sys.base_exec_prefix}

    dirs = {Path(d, CFG.binname).resolve() for d in prefixes
            if Path(d, CFG.binname).is_dir()}

    if not dirs:
        print("No valid bin path found", file=sys.stderr)

    if only_missing:
        dirs = [d for d in dirs if d not in os.get_exec_path()]
        if not dirs:
            print("No bin paths missing from PATH", file=sys.stderr)

    return dirs

def use_homevar(path):
    """Replace path to home with CFG.homevar"""
    # return unmodified path if Path.home() is empty or if path doesn't exist
    if not (Path.home() or path.exists()):
        return path

    # return unmodified path if the path doesn't start with home
    if Path.home() not in path.resolve().parents:
        return path

    # return a new Path object starting with the home variable
    return Path(CFG.homevar, path.relative_to(Path.home()))

def print_cmd(paths):
    tpl = Template(CFG.command)
    new_paths = os.pathsep.join(map(str, paths)) + os.pathsep

    if not CFG.ok(new_paths):
        exit(1)

    if CFG.cmdmsg:
        print("Note:", CFG.cmdmsg, os.linesep, file=sys.stderr)
    print(tpl.substitute(new_paths=new_paths, old_paths=CFG.old_paths))

def main():
    parser = ArgumentParser( description="Find path(s) to Python executables")

    parser.add_argument("-b", "--include-base",
                        action="store_true", dest="include_base",
                        help="search in base_prefix and base_exec_prefix too")
    parser.add_argument("-m", "--only-missing",
                        action="store_true", dest="only_missing",
                        help="include only directories missing from PATH")
    parser.add_argument("-H", "--use-homevar", default=None, const="new",
                        choices=["all", "new", "prev", None],
                        nargs="?", dest="use_homevar",
                        help="Replace HOME in bin path(s) with variable")
    parser.add_argument("-w", "--windows",
                        action="store_true", dest="windows_mode",
                        help="Simulate windows mode on *nix OS.")
    parser.add_argument("-c", "--shell-cmd",
                        action="store_true", dest="shell_cmd",
                        help="Print command that that appends to PATH, to be be pasted into a shell")

    args = parser.parse_args()

    if args.windows_mode:
        global CFG
        CFG = Config("Windows")
        CFG.binname = NixConfig.binname

    CFG.use_homevar = args.use_homevar

    dirs = binpaths(args.include_base, args.only_missing)

    if args.use_homevar in ("new", "all"):
        dirs = [use_homevar(d) for d in dirs]

    if args.shell_cmd:
        print_cmd(dirs)
    else:
        print(*map(str, dirs), sep=os.linesep)


if __name__ == "__main__":
    main()
