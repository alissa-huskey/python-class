Glossary
=========

Programming Concepts
--------------------

* **Argument**: A value that is sent as input to a function.

* **Assign**: A statement that sets the value of a variable name.

* **Call**: Code that tells the computer to run (execute) the code within a
  previously defined function.

* **Comment**: Parts in a source-code file which are ignored when the program
  is run. In Python add a `#` to the beginning a line to indicate that it is a
  comment. You can also comment out only part of a line by adding `#` followed
  by the comment text to the end of an expression. It is recommended to follow
  the `#` by a single space before the text of the comment.

* **Conditional**: A valid piece of code that, when evaluated, results in boolean
  value (True or False).

* ***Define***: The code that specifies the data or code block that an
  identifier refers to. A variable is defined when it is assigned. A function
  is defined by the statements that form the body of the function. In Python a
  function definition starts with the keyword `def`.

* **Docstring**: Similar to a comment parts of code that are not executed but
  are used to document a segment of code. In Python it is surrounded by tripple
  double-quotes `"""` and appears at the first expression in a file, module,
  class, or function.

* **Escaping**: How to indicate to the computer that an operator inside of a
  string should not be interpreted but instead be treated be treated as part of
  the string. For example, you would need to escape a single-quote in a string
  surrounded by single-quotes, a double-quote in a string surrounded by
  double-quotes, and the escape character in any sring. In Python (and many
  other languages) the escape character is a backslash (`\`).

* **Expression**: A valid piece of code that, when evaluated, results in
  a value.

* **Function**: (elsewhere: subroutine, method, procedure) A named block of
  reusable code. A function may or may not take arguments, and may or may not
  return a value. In Python it is recommended to use the
  `lower_case_with_underscores` for function names.

* **Identifier**: The name that refers to a some programming element. In Python
  a variable, class, function or module.

* **Iterate**: To repeat over a unit of code, usually within a loop. Each
  repetition is called an *iteration*.

* **Key**: A value used to retrieve another value from an array (list) or
  associative array (dictionary).

* **Keyword**: Reserved words that have special meanings in a programming
  language so that they cannot be used as an identifier. Some
  examples of keywords in python are `for`, `if`, and `def`.

* **Module**: A kind of reusable code that can be imported into other
  programs.

* **Namespace**: The group that a variable or function is part of. `print()` is
  part of the **global namespace** whereas `randint()` is part of the `random`
  module, and therefore part of the `random` namespace.

* **Operator**: A symbol with special meaning that tells the computer to do
  something (for example `=`, `+`, or `==`).

* **Parameters**: The named variables that appear in a function definition to
  specify what arguments it can accept.

* **Statement**: A line of code that can be executed. Different from an
  expression because it does not result in a value.

* **String Concatenation**: Joining two (or more) strings together.

* **Syntax**: A set of rules that determine how a programming language is
  understood by the computer. Grammar, but for code. In Python for example,
  that strings are surrounded by quotes, that code blocks are determined by
  indentation level, and that boolean values must be capitalized.

* **Suite, Block, Code Block**: A set of statements grouped together to form a
  contextual unit. For example, a block of code that is part of an
  if-statement, a while-loop, or a function. In Python, blocks are called
  suites and are indicated by indentation level.

* **Type (Data Type)**: The classification of a value which tells the
  computer how it will be used and what operations can be performed on it. Some
  examples include, strings, integers, lists, dictionaries, and user-defined
  classes.

* **Value**: A piece of data which can be numbers, strings, and more.

* **Variable**: A name given to a value. It is recommended to use the
  `lower_case_with_underscores` style for local variables.

* **Loop**: A block of code that will repeat until a specified condition is
  reached. An *infinite-loop* occurs if there is no condition or the condition
  can never be met. In Python there are *for-loops* and *while-loops*.

* **Immutable**: A value that cannot be changed. In Python these include
  numbers, strings and tuples.

* **Mutable**: A value that can be changed.

Types
-----

* **Boolean (bool)**: True or False values. In Python they must be
  capitalized and not surrounded by single or double quotes.

* **Dictionary (dict, associative-array, hash)**: A collection of key-value
  pairs.

* **Floating-Point Number (float, double)**: Fractions or numbers with
  decimal points.

* **Integers (int)**: Whole numbers values.

* **List (array)**: A collection of values. In Python lists are mutable and
  they are defined by surrounding the comma-seperated values with
  square-bracket (`[]`).

* **Strings (str)**: Text values. They are surrounded by single or double
  quotes. In Python, there is no difference between using single or double
  quotes, except which characters you have to escape. It is recommended to pick
  one and stick to it. I choose to use double-quotes (`"`) unless the string
  contains a double-quote or for hash keys.

* **None**: (elsewhere: null, nil) A special value that indicates nothingness
  which is different from the value zero or an empty string. In Python it is
  referred to as None without quotes.


Software Development Concepts
-----------------------------

* **Console, System console**: Comes from a time when early text-based
  computer systems with a keyboard and monitor interface were used to interact
  with servers or mainframes.  In modern usage people usually mean accessing
  the operating system's shell, usually with a terminal emulator. In repl.it,
  the right-most pane is referred to as the console.

* **REPL (Read-Evaluate-Print-Loop)**: An interactive tool or environment
  that takes code input, evaluates (executes) it, and displays the results to
  the user. Shells are a subset of REPLs. More advanced REPL tools and systems
  are comprised of an input or editor pane, and an output or results pane. Many
  online REPLs exist such as play.golang.org for Go, pythonfiddle.com for
  Python, try.ruby-lang.org for Ruby and of course the multi-language platform
  repl.it.

* **Shell, Interactive Shell, Command Line Interpreter**: A text-based
  interface that runs code or command input. Operating systems have shells for
  system administration and operation such as Bash or Zsh in Unix-like systems
  or Powershell or the DOS Command Prompt in Windows. Some languages provide
  shells that execute code such as the Python Interactive Shell or the
  Interactive Ruby Shell (IRB).

* **Terminal, Terminal emulator**: In modern computing, an application that
  provides a text-based interface to the operating system's shell. Some
  examples include konsole and the Gnome Terminal in Unix-like systems,
  Terminal and iTerm2 on MacOs, and PuTTY, Cygwin mintty, the Windows Console,
  and the Windows Terminal for Windows.

  The term "console" and "terminal" are often used interchangaby, both
  historically to refer to a hardware server interface as well as the more
  modern colloqual meaning of accessing the operating system's shell.

* **Interpret**: The process by which the computer directly executes source
  code without that code needing to be compiled first. The program that does
  this for a particluar programming language is called an *intrepreter*. A
  programming language that does not need to be compiled is called an
  *interpreted language* or sometimes a *scripting language*. Python is an
  interpreted language and Python code is executed by the Python Interprter.
  Some other interpreted languages include Ruby, PHP and Perl.

* **Compile**: The process by which the computer translates source code from
  one programming language to a lower-level language to create an executable
  program. A language that must be compiled is called a *compiled language* and
  the program that does this for a particular programming language is called a
  *compiler*. Python is an interpreted language, so it does not need to be
  compiled. Some compiled langauges include C/C++, Java and Go.


Version Control
---------------

* **Codebase**: A set source code files that make up a software system,
  application, component or project.

* **Repository (aka repo)**: The container for version-control information for
  a set of files.

* **Version Control (Source Control, Revision Control)**: A method for
  keeping track of and managing changes to a set of files.

* **Version Control System (VCS), Revision Control System, Source Control
  Management System (SCM)**: A tool or set of tools for version control. The
  most popular today is Git, but some other examples include Git, Mercurial,
  Subversion, CVS and Perforce.
