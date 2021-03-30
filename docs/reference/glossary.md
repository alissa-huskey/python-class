Glossary
=========

```{glossary} programming-concepts

argument
  A {term}`value` that is sent as input to a function.

assign
  A {term}`statement` that sets the {term}`value` of a variable name.

call
  Code that tells the computer to {term}`execute` the code within a previously
  defined function.

comment
  Parts in a source-code file which are ignored when the program is run. In
  Python add a `#` to the beginning a line to indicate that it is a comment.
  You can also comment out only part of a line by adding `#` followed by the
  comment text to the end of an expression. It is recommended to follow the `#`
  by a single space before the text of the comment.

comparison operator
  An operator that compares the left-hand value to the right-hand value then
  evaluates to either True or False.

condition
conditional
  A valid piece of code that, when evaluated, results in
  {term}`boolean` value.

docstring
  Similar to a comment parts of code that are not executed but are used to
  document a segment of code. In Python it is surrounded by triple
  double-quotes `"""` or triple single-quotes `'''` and appears at the first
  expression in a file, module, class, or function.

escaping
  How to indicate to the computer that an operator inside of a string should
  not be interpreted but instead be treated be treated as part of the string.
  For example, you would need to escape a single-quote in a string surrounded
  by single-quotes, a double-quote in a string surrounded by double-quotes, and
  the escape character in any string. In Python (and many other languages) the
  escape character is a backslash (`\`).

expression
  A valid piece of code that, when evaluated, results in a value.

falsy
  A value that is False when evaluated in a `boolean` context, or when converted
  to a boolean using the `bool()` function.

function
  A named block of reusable code. A function may or may not take arguments, and
  may or may not return a value. In Python it is recommended to use the
  `lower_case_with_underscores` for function names.

identifier
  The name that refers to a some programming element, such as a variable,
  class, function or module.

if statement
  a compound statement that changes what code is executed depending on its conditions

iterate
iteration
iterating
  To repeat over a unit of code, usually within a loop. Each repetition is
  called an *iteration*.

key
  A value used to retrieve another value from a {term}`dictionary`.

keyword
  Reserved words that have special meanings in a programming language so that
  they cannot be used as an identifier. Some examples of keywords in Python are
  `for`, `if`, and `def`.

logical operator
  An operator that considers both left-hand value and right-hand value then
  evaluates to either True or False.

module
  A file containing of reusable code that can be imported into other programs.

namespace
  The group that a variable or function is part of. `print()` is part of the
  {term}`global namespace` whereas `randint()` is part of the `random` module, and
  therefore part of the `random` namespace.

operator
  A symbol with special meaning that tells the computer to do something (for
  example `=`, `+`, or `==`).

parameter
  The named variables that appear in a function definition to specify what
  arguments it can accept.

statement
  An instruction that Python can {term}`execute` as a unit.

string concatenation
concatenation
concatenate
  Joining two or more strings together.

syntax
  A set of rules that determine how a programming language is understood by the
  computer. Grammar, but for code.

truthy
  A value that is True when evaluated in a `boolean` context, or when converted
  to a boolean using the `bool()` function.

type
data type
  The classification of a value which tells Python what operations can be
  performed on it. Some examples include {term}`strings`,
  {term}`integers`, {term}`lists`, and
  {term}`dictionaries`.

value
  A piece of data such as {term}`strings`, {term}`integers`
  and more.

variable
  A name given to a value.

loop
  A block of code that will repeat until a specified condition is reached. For
  example *for-loops* and *while-loops*. An *infinite-loop* occurs if there is
  no condition or the condition can never be met.

immutable
  A value that cannot be changed. In Python these include numbers, strings and
  tuples.

mutable
  A value that can be changed.
```

```{glossary} data-types
boolean
bool
  True or False values.

dictionary
dict
  A collection of key-value pairs.

floating-point number
float
  Fractions or numbers with decimal points.

integer
int
  Whole numbers values.

list
  A collection of values. In Python lists are mutable and they are defined by
  surrounding the comma-separated values with square-bracket (`[]`).

string
str
  Text values. They are surrounded by single or double quotes. In Python, there
  is no difference between using single or double quotes, except which
  characters you have to escape.

none
null
  A special value that indicates nothingness which is different from the value
  zero or an empty string. In Python it is referred to as None without quotes.
  In other languages: null, nil.
```

```{glossary} software-development
code editor
  A text editing program specifically for code with features like syntax
  highlighting and code formatting. Some examples include VS Code, Atom,
  Sublime, Textmate and Vim.

command line
  In casual use, people usually mean accessing the operating system's shell,
  usually with a terminal emulator. See also, {term}`console`,
  {term}`terminal`.

compile
  The process by which the computer translates source code from one programming
  language to a lower-level language to create an executable program. A
  language that must be compiled is called a compiled language and the
  program that does this for a particular programming language is called a
  compiler. Python is an interpreted language, so it does not need to be
  compiled. Some compiled languages include C/C++, Java and Go.

console
system console
  Comes from a time when early text-based computer systems with a keyboard and
  monitor interface were used to interact with servers or mainframes.  In
  modern usage people usually mean accessing the operating system's shell,
  usually with a terminal emulator. In repl.it, the right-most pane is referred
  to as the console.

integrated development environment
IDE
  A program dedicated to software development usually including a code editor,
  debugger, version control management, and build/execution features. Examples
  include repl.it, Eclipse, Thonny, and Pycharm.

interpret
  The process by which the computer directly executes source code without that
  code needing to be compiled first. The program that does this for a
  particular programming language is called an interpreter. A programming
  language that does not need to be compiled is called an interpreted
  language or sometimes a scripting language. Python is an interpreted
  language and Python code is executed by the Python Interpreter.  Some other
  interpreted languages include Ruby, PHP and Perl.

prompt
  Characters displayed by the interpreter to indicate that it is ready to take
  input from the user.

read-evaluate-print-loop
REPL
  An interactive tool or environment that takes code input,
  {term}`evaluates` or {term}`executes` it, and displays the
  output or resulting value to the user. {term}`shells` are a subset of
  REPLs. More advanced REPL tools and systems are comprised of an input or
  editor pane, and an output or results pane. Many online REPLs exist such as
  play.golang.org for Go, pythonfiddle.com for Python, try.ruby-lang.org for
  Ruby and repl.it.

shell
interactive shell
command line interpreter
  A text-based interface that runs code or command input. Operating systems
  have shells for system administration and operation such as Bash or Zsh in
  Unix-like systems or Powershell or the DOS Command Prompt in Windows. Some
  languages provide shells that execute code such as the Python Interactive
  Shell or the {abbr}`IRB (Interactive Ruby Shell)`.

terminal
terminal emulator
  In modern computing, an application that provides a text-based interface to
  the operating system's shell. Some examples include konsole and the Gnome
  Terminal in Unix-like systems, Terminal and iTerm2 on MacOs, and PuTTY,
  Cygwin mintty, the Windows Console, and the Windows Terminal for Windows.

  The term "console" and "terminal" are often used interchangaby, both
  historically to refer to a hardware server interface as well as the more
  modern colloquial meaning of accessing the operating system's shell.
```

```{glossary} version-control
branch
  A container that has a name and stores set of commits. Every repository is
  created with a default branch named {term}`master`.

codebase
  A set source code files that make up a software system, application,
  component or project.

commit
revision
change log
  A set of changes recorded in version control.

distributed version control
   As opposed to {term}`centralized version control` systems that have one central
   repository that all other repositories were required to communicate with in
   order to commit changes. In distributed version control, every repo is self
   contained and any repo send changes to or receive changes from any other
   compatible repository.

HEAD
  A reference to the current commit on the current branch. A reference is like
  a bookmark to a commit.

index
  A snapshot of your files at the time of the `HEAD` commit plus the changes
  you've staged for commit.

master
main
  The default branch. Until recently the default branch was named master, but
  recently there has been a shift to naming the default branch main.

object database
  The history of all commits and the relationships between them.

origin
  The default {term}`remote repository`.

patch
  The file detailing the exact changes between two versions in a structured
  format that git and other programs understand. It's very similar to the
  output of `git diff`.

reference
  A pointer to a specific {term}`commit`.

remote repository
upstream repo
  A repository that you send changes to.

repository
repo
  The container for version-control information for a set of files.

SHA
hash
  A 40-character unique identifier that points to a the rest of the data
  related to the {term}`commit`. Basically, a commit ID. Here's an example:
  `d16085b3b913e5bc5e351c0a7461051e9973629a`

tree
  A snapshot of your files at the time of the {term}`HEAD` {term}`commit`.

version control
source control
revision control
  A method for keeping track of and managing changes to a set of files.

version control system
VCS
revision control system
source control management system
SCM
  A tool or set of tools for version control. The most popular today is Git,
  but some other examples include Mercurial, Subversion, CVS and Perforce.

```
