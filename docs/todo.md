To Do
=====

Fundamentals
------------

[ ] stack
  [ ] https://sites.cs.ucsb.edu/~pconrad/cs8/topics.beta/theStack/06/
  [ ] https://sites.cs.ucsb.edu/~pconrad/cs8/topics.beta/theStack/02/

[ ] declaration
  [ ] function definition
  [ ] variable assignment

[ ] syntax
  [ ] comments
  [ ] blocks
  [ ] keywords

[x] expressions
  [x] operator
  [x] order of operation
  [x] evaluate

  [ ] atom
  [ ] assignment
  [ ] variable
  [ ] identifier
  [ ] literal

  [ ] attribute reference (dot-notation) <atom>.<member>
  [ ] subscripting  <atom>[<name>]

  [ ] functions

[ ] data types
   [ ] string
   [ ] int
   [ ] float
   [ ] bool
   [ ] sequences
     [ ] list
     [ ] dict

[ ] flow control
  [ ] if-statements


[ ] iterables -- an object capable of returning its members one at a time
  [ ] containers: (sequence: list, set, range, string), (mapping: dict)
  [ ] file
  [ ] enumerate

[ ] loops
  [ ] while
  [ ] for
  [ ] break, continue

[ ] exceptions
[ ] arguments

Exercises / Docs
----------------

[ ] bash intro
[ ] version control basics
[ ] arguments
[ ] Naming Conventions
    module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.

Concepts
--------

### Python

[.] f-string: String literals prefixed with 'f' or 'F' are commonly called
    "f-strings" which is short for formatted string literals.
[ ] Functions
  [ ] annotations
  [ ] default values
  [ ] call using keyword arguments
[ ] slices
[ ] loops: break, continue, else


### Programming

[ ] scope
[ ] encapsulation
[ ] Procedural programming: An approach to programming that uses functions to organize code
[ ] Object-oriented programming (OOP): An approach to programming that
    organizes code into user-defined types called classes which produce values
    called objects. An object contains behavior (methods) and data (attributes) so
    that it knows how to operate on itself.
    [ ] Attribute
    [ ] Class
    [ ] method: A function defined inside a class body
    [ ] Instance, Instantiation
    [ ] Inheratance
[ ] Typing Systems
  [ ] Strongly typed languages: Require explicitly declaring variable types, use
      static typing to verify type safety usually at compile time.
  [ ] Loosely (weakly) typed languages: Types are checked at runtime and may be implicitly converted
  [ ] Duck-typing: A system that determines if an object is valid for based on its
      behaviors and properties rather than its type. "If it walks like a duck and it
      quacks like a duck, then it must be a duck"
[x] Object: Any data with state (attributes or value) and defined behavior
    (methods). Also the ultimate base class of any new-style class.
[x] shebang: the first line of a script starting with `#!` followed by the
    *interperter directive*: the path to the interpreter to use for the script
    #!/usr/bin/env python

### Command Line

[ ] Command Line
  [ ] Path

### Version Control

[x] viewing changes:
    [x] git log
    [x] git show
    [x] git diff
    [x] git status

[ ] syncing changes:
    [ ] git fetch
    [ ] git pull --ff
    [ ] git push

[ ] getting repositories:
    [ ] git init
    [ ] git clone

[ ] managing changes:
    [ ] add
    [ ] rm
    [ ] mv - rename or move a file
    [ ] git commit -a -m '\<commit message\>'
    [ ] git commit --amend

[ ] undoing things:
    [ ] git reset --soft HEAD~1         undo last commit, leaving changes uncommited in your local repository
    [ ] git checkout \<filename\>         recover the last tracked version of a locally deleted file
    [ ] git reset HEAD \<filename\>       unstage file and keep local changes

Advanced

[ ] stash
    [ ] git stash push -u -m 'testing stashing my changes'
    [ ] git stash save -u testing stashing my changes
    [ ] git stash pop --index
    [ ] git stash --all
[ ] merge, mergetool
[ ] reset
[ ] cherry-pick
[ ] revert
[ ] checkout
[ ] git remote add origin https://github.com/cubeton/mynewrepository.git
[ ] git push -u origin master

Glossary Terms
--------------

### Programming

  [ ] **Object**:
  [ ] evaluate
  [ ] execute

### Version Control

[x] **Distributed Version Control System**
[x] **Commit**
[x] master: the default branch
[x] origin: the default remote repository
[x] reference: pointer to the the current commit in the current branch
[ ] **Push**
[ ] **Commit Message**
[ ] **Stage**
[ ] **Tracked files**
[ ] **Untracked files**
    [ ] modified: changes made to a file that only exist locally and that git has no record of
    [ ] staged: changes that will be included in the next commit
    [ ] committed: changes that git has recorded locally
[ ] **Diff**
- untracked file - a new file that git doesn't have a record of (isn't tracking)
- tracked file - a file that git has a historical version of (is tracking)
[ ] merge: to combine the changes from somewhere else with your local files fast-forward: 
[ ] pull: shorthand for fetching the record of changes from a remote repository, then merging those changes into your working directory
dirty - when your working directory has uncommited changes
clean - when your working directory has no uncommitted changes
HEAD~ - the last commit
HEAD~1 - the commit before the last commit

Later

[ ] pull request
[ ] pathspec - an argument that points to a file or set of files
[ ] conflict - what happens when git is unable to automatically merge a set of changes, because the changes overlap in some way
[ ] resolve - the process of manually combining two sets of changes from a merge conflict
[ ] tag - a bookmark to a commit, often used for release. (ie "v1.0")
[ ] fork
