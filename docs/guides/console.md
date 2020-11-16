A Brief Tour of the Console
===========================

We've talked about the **Python Shell** -- it is an interface where you can
type in python code, and it will run it and print out the results.

When people use the term ***console***, ***command-line*** or ***shell***, they
mean the ***Operating System Shell***. Here the input we type is in a language
called ***bash*** then run by the underlying operating system.

### Part 1.1: Open "The Shell"

We're going to learn a new way to access the console, and that is using a
Repl.it feature they call "The Shell".  You can open it by by pressing
`ctrl+shift+S` or `cmd+shift+S`.

Go ahead and collapse the left two panes so you only see The Console and The
Shell panes.

You should see something like this in the new pane:

```bash
~$
```

This is the ***bash prompt***, which is the same thing you get in the Console
pane when you see `>`.


### Part 1.2: Anatomy of A Command

The most basic kind of command has the form of:

`<program-name> [<argument> <argument>...]`

For example, to start the Python shell we use the command:

```bash
python3
```

* `python3` is the name of the program
* in this case there are no arguments

Or, to run our PyPet script, the command would be:

```bash
python3 pypet.py
```

* `python3` is the program name
* `pypet.py` is an argument -- in this case, the filename for our script

This tells the Python Interpreter (`python3`) to run the code found inside the
file `pypet.py`.


This, by the way, is exactly how the Run button works. It reads our `.replit`
file and takes the value of the `run` variable inside of it, and sends it to
the bash prompt in the Console pane.


### Part 1.2: Subcommands and Flags

A program may take all sorts of arguments or none at all.

Some programs have their own set of commands, known as `subcommands`.

`git` is one such command. For example in the command:

```bash
git status
```

* `git` is the name of the program
* `status` is a subcommand argument

When an argument starts with a `-` or `--` it is called a ***flag*** or an
***option flag***. Usually this tells a program or its subcommand to set an
option so that it behaves in a certian way.

For example, in the command:

```bash
git diff --staged
```

* `git` is the name of the program
* `diff` is a subcommand argument
* `--staged` is an option flag argument

Flags take a number of common forms.

* `git status -s               #` Short flags start with one dash (`-`) and a single letter
* `git log --oneline           #` Long flags have two dashes (`--`) followed by a word
* `git log --pretty=oneline    #` Sometimes option flags take a value following the equal sign (`=`)
* `python3 -c 'print("hello")' #` Sometimes option flags take the next argument passed as a value


### Part 1.3: Common Arguments


* `-h` \| `--help` show usage information for this command
* `<program> help <subcommand>` show the usage information for the <subcommand>
* `-V` \| `--version` show the programs version
* `-v` \| `--verbose` print extra detailed information while running a command
* `-q` \| `--quiet` print less detailed information or none at all while running a command
* `--` this means that any arguments following it should not be considered options

### Part 1.2: Try Some Commands

Here are some commands. Pick a few and try them for yourself.

* `cal`
* `cal -h`
* `cal -3`
* `ncal -e`
* `file pypet.py`
* `whoami`
* `uname -a`
* `uptime`
* `date`
* `echo hello`
