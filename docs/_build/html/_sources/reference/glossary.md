Glossary
=========

Programming Concepts
--------------------

```{glossary}
Argument
  A {term}`value` that is sent as input to a function.

Assign
  A {term}`statement` that sets the {term}`value` of a variable name.

Call
  Code that tells the computer to {term}`execute` the code within a previously
  defined function.

Comment
  Parts in a source-code file which are ignored when the program is run. In
  Python add a `#` to the beginning a line to indicate that it is a comment.
  You can also comment out only part of a line by adding `#` followed by the
  comment text to the end of an expression. It is recommended to follow the `#`
  by a single space before the text of the comment.

Conditional
  A valid piece of code that, when evaluated, results in
  {term}`boolean<Boolean>` value.

Docstring
  Similar to a comment parts of code that are not executed but are used to
  document a segment of code. In Python it is surrounded by tripple
  double-quotes `"""` or tripple single-quotes `'''` and appears at the first
  expression in a file, module, class, or function.

Escaping
  How to indicate to the computer that an operator inside of a string should
  not be interpreted but instead be treated be treated as part of the string.
  For example, you would need to escape a single-quote in a string surrounded
  by single-quotes, a double-quote in a string surrounded by double-quotes, and
  the escape character in any sring. In Python (and many other languages) the
  escape character is a backslash (`\`).

Expression
  A valid piece of code that, when evaluated, results in a value.

Function
  A named block of reusable code. A function may or may not take arguments, and
  may or may not return a value. In Python it is recommended to use the
  `lower_case_with_underscores` for function names.

Identifier
  The name that refers to a some programming element, such as a variable,
  class, function or module.

Iterate
  To repeat over a unit of code, usually within a loop. Each repetition is
  called an *iteration*.

Key
  A value used to retrieve another value from a {term}`dictionary<Dictionary>`.

Keyword
  Reserved words that have special meanings in a programming language so that
  they cannot be used as an identifier. Some examples of keywords in Python are
  `for`, `if`, and `def`.

Module
  A file containing of reusable code that can be imported into other programs.

Namespace
  The group that a variable or function is part of. `print()` is part of the
  **global namespace** whereas `randint()` is part of the `random` module, and
  therefore part of the `random` namespace.

Operator
  A symbol with special meaning that tells the computer to do something (for
  example `=`, `+`, or `==`).

Parameters
  The named variables that appear in a function definition to specify what
  arguments it can accept.

Statement
  An instruction that Python can {term}`execute` as a unit.

String Concatenation
Concatenation
Concatenate
  Joining two or more strings together.

Syntax
  A set of rules that determine how a programming language is understood by the
  computer. Grammar, but for code.

Type
Data Type
  The classification of a value which tells Python what operations can be
  performed on it. Some examples include {term}`strings<String>`,
  {term}`integers<Integer>`, {term}`lists<List>`, and
  {term}`dictionaries<Dictionary>`.

Value
  A piece of data such as {term}`strings<String>`, {term}`integers<Integer>`
  and more.

Variable
  A name given to a value.

Loop
  A block of code that will repeat until a specified condition is reached. For
  example *for-loops* and *while-loops*. An *infinite-loop* occurs if there is
  no condition or the condition can never be met.

Immutable
  A value that cannot be changed. In Python these include numbers, strings and
  tuples.

Mutable
  A value that can be changed.
```

Data Types
-----

```{glossary}
Boolean
bool
  True or False values.

Dictionary
dict
  A collection of key-value pairs.

Floating-Point Number
float
  Fractions or numbers with decimal points.

Integer
int
  Whole numbers values.

List
  A collection of values. In Python lists are mutable and they are defined by
  surrounding the comma-seperated values with square-bracket (`[]`).

String
str
  Text values. They are surrounded by single or double quotes. In Python, there
  is no difference between using single or double quotes, except which
  characters you have to escape.

None
null
  A special value that indicates nothingness which is different from the value
  zero or an empty string. In Python it is referred to as None without quotes.
  In other languages: null, nil.
```


Software Development Concepts
-----------------------------

```{glossary}
Code Editor
  A text editing program specifically for code with features like syntax
  highlighting and code formatting. Some examples include VS Code, Atom,
  Sublime, Textmate and Vim.

Command Line
  In casual use, people usually mean accessing the operating system's shell,
  usually with a terminal emulator. See also, {term}`Console`,
  {term}`Terminal`.

Compile
  The process by which the computer translates source code from one programming
  language to a lower-level language to create an executable program. A
  language that must be compiled is called a compiled language and the
  program that does this for a particular programming language is called a
  compiler. Python is an interpreted language, so it does not need to be
  compiled. Some compiled langauges include C/C++, Java and Go.

Console
System console
  Comes from a time when early text-based computer systems with a keyboard and
  monitor interface were used to interact with servers or mainframes.  In
  modern usage people usually mean accessing the operating system's shell,
  usually with a terminal emulator. In repl.it, the right-most pane is referred
  to as the console.

Integrated Development Environment
IDE
  A program dedicated to software development usually including a code editor,
  debugger, version control management, and build/execution features. Examples
  include repl.it, Eclipse, Thonny, and Pycharm.

Interpret
  The process by which the computer directly executes source code without that
  code needing to be compiled first. The program that does this for a
  particluar programming language is called an intrepreter. A programming
  language that does not need to be compiled is called an interpreted
  language or sometimes a scripting language. Python is an interpreted
  language and Python code is executed by the Python Interprter.  Some other
  interpreted languages include Ruby, PHP and Perl.

Prompt
  Characters displayed by the interpreter to indicate that it is ready to take
  input from the user.

Read-Evaluate-Print-Loop
REPL
  An interactive tool or environment that takes code input,
  {term}`evaluates<evaluate>` or {term}`executes<execute>` it, and displays the
  output or resulting value to the user. {term}`Shells<Shell>` are a subset of
  REPLs. More advanced REPL tools and systems are comprised of an input or
  editor pane, and an output or results pane. Many online REPLs exist such as
  play.golang.org for Go, pythonfiddle.com for Python, try.ruby-lang.org for
  Ruby and repl.it.

Shell
Interactive Shell
Command Line Interpreter
  A text-based interface that runs code or command input. Operating systems
  have shells for system administration and operation such as Bash or Zsh in
  Unix-like systems or Powershell or the DOS Command Prompt in Windows. Some
  languages provide shells that execute code such as the Python Interactive
  Shell or the :abbr:`IRB (Interactive Ruby Shell)`.

Terminal
Terminal emulator
  In modern computing, an application that provides a text-based interface to
  the operating system's shell. Some examples include konsole and the Gnome
  Terminal in Unix-like systems, Terminal and iTerm2 on MacOs, and PuTTY,
  Cygwin mintty, the Windows Console, and the Windows Terminal for Windows.

  The term "console" and "terminal" are often used interchangaby, both
  historically to refer to a hardware server interface as well as the more
  modern colloqual meaning of accessing the operating system's shell.
```

Version Control
---------------

```{glossary}
branch
  A container that has a name and stores set of commits. Every repository is
  created with a default branch named {term}`master`.

Codebase
  A set source code files that make up a software system, application,
  component or project.

commit
revsion
change log
  A set of changes recorded in version control.

distributed version control
   As opposed to **Centralized Version Control Systems** that have one central
   repository that all other repositories were required to communicate with in
   order to commit changes. In distributed version control, every repo is self
   contained and any repo send changes to or receive changes from any other
   compatable repository.

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

Repository
repo
  The container for version-control information for a set of files.

SHA
hash
  A 40-character unique identifier that points to a the rest of the data
  related to the {term}`commit`. Basically, a commit ID. Here's an example:
  `d16085b3b913e5bc5e351c0a7461051e9973629a`

tree
  A snapshot of your files at the time of the {term}`HEAD` {term}`commit`.

Version Control
Source Control
Revision Control
  A method for keeping track of and managing changes to a set of files.

Version Control System
VCS
Revision Control System
Source Control Management System
SCM
  A tool or set of tools for version control. The most popular today is Git,
  but some other examples include Mercurial, Subversion, CVS and Perforce.

```
