---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
File I/O
========

I/O is a shorthand way of referring to input and output. The `input()` and
`print()` functions are two examples of input and output. In this lesson
we'll learn another: how to read from and write to files.

```{include} ../toc.md
```

Part 1: Reading Files
---------------------

Sometimes in our programs we need to access information that is stored in a
file. In programming this is called reading a file and that's what we'll learn
first.

### Part 1.1: Reading whole files

In this section we will get the contents of a file containing a grocery list
then then print it to the screen.

#### A. Create `groceries.txt`

{{ leftcol }}

First we'll need a file to read from. Paste the following lines into a new file
{file}`groceries.txt`, located in the same directory you will be running the
script from, or the {term}`working directory`.

{{ rightcol }}

```{code-block} text
:caption: groceries.txt
:linenos:
- eggs
- milk
- flour
```

{{ endcols }}

#### B. Create `groceries.py`

1\. Create a second file {file}`groceries.py` also in the working directory.

2\. To interact with files we start by using Pythons built-in `open()` function.
It returns a {term}`file handler` object, which we'll assign to a variable
`fh`. The `open()` function takes at least one argument, the location of the
file to open. In this case we want a string with the filename:
{file}`"groceries.txt"`.

3\. The {term}`file handler` object represents the connection to the file and
provides methods for interacting with the file.  In this case, we are
interested in the `.read()` method which returns the entire contents of the
file as a string. We'll assign the string to the variable `contents`.

4\. We're done with the file now so we'll call the `.close()` method on `fh` to
free up the computer resources used to manage the file. It is important to
always close a file handler when its no longer needed to avoid bugs that may
slow down your computer or interfere with the file you opened.

5\. Finally, we'll print the title `"Groceries"` underlined with `=` followed by the
contents of the file.

```{code-block} python
:caption: groceries.py
:linenos:
# open the file and create a file handler object
fh = open("groceries.txt")

# get a string with the contents of the file
contents = fh.read()

# close the file handler
fh.close()

# print a header followed by the file contents
print("Groceries")
print("=========")
print(contents)
```

{{ leftcol }}

6\. When you run your script you should see a nicely formatted grocery list, all ready for a shopping trip.

{{ rightcol }}

```{code-block} text
:caption: output
Groceries
=========
- eggs
- milk
- flour
```

{{ endcols }}

### Part 1.2: Exercise

`````{exercise} reading files
:label: reading-files-exercise

In this exercise you'll be reading a file and printing its contents to the
screen, just like you did above but with a different file.

1. Copy the following text and paste it into a file named {file}`mug-brownie.md` in your working directory.
   :::{dropdown} mud-brownie.md
   ```{literalinclude} mug-brownie.md
   :language: md
   ```
   :::
2. Create a new file {file}`recipe.py` for this exercise.
3. Use the `open()` function to get a file handler for the {file}`mug-brownie.md` file.
4. Use the `.read()` method to get the contents of the file and assign it to a variable `recipe`.
5. Use the `.close()` method to close the file handler.
6. Print the `recipe`.

`````

`````{solution} reading-files-exercise
:class: dropdown

```{code-block} python
:caption: recipe.py
:linenos:
fh = open("mug-brownie.md")
recipe = fh.read()
fh.close()

print(recipe)
```
`````

### Part 1.3: Reading lines

Sometimes instead of getting the entire contents of a file at once, we want to
go through each line line for more fine grained control.

This is where the `.readlines()` method on file handler objects comes in. It
returns a list, where each element is one line from the file.

#### A. Modify `recipes.py`

In this section we'll modify the `recipes.py` file to use the `.readlines()`
method in a `for` loop.

1\. Since we'll be printing each line as it is read, first we'll need to move the
header lines to the beginning of the script so that they are printed first.

2\. As before, we'll need a file handler object from `open()`, so we can leave that
line unchanged.

3\. This time we'll replace the `.read()` line with a `for` loop, iterating over the
list returned by `fh.readlines()`. We'll call the item variable `line`, since
it will contain a line from the file in each iteration.

4\. Now the list returned by `.readlines()` retains the carriage return (`"\n"`) at
the end of each `line` string. So when we print each `line` in the for loop,
we'll tell the `print()` function not to add a newline by passing it the `end`
keyword argument with a value of `""`.

5\. Finally, we'll still want to `.close()` the file handler, so that line can stay
the way it is.

```{code-block} python
:caption: groceries.py
:emphasize-lines: "8-14"
:linenos:
# print a header
print("Groceries")
print("=========")

# open the file and create a file handler object
fh = open("groceries.txt")

# loop through each line of the file
for line in fh.readlines():

  # print the line which includes the trailing "\n"
  # and pass print an empty string for end
  # so it doesn't add an extra newline
  print(line, end="")

# close the file handler
fh.close()
```

{{ leftcol }}

6\. When you run your script the output should be the same.

{{ rightcol }}

```{code-block} text
:caption: output
Groceries
=========
- eggs
- milk
- flour
```

{{ endcols }}

### Part 1.4: Exercise

`````{exercise} reading lines
:label: readlines-exercise

In this exercise you'll be reading each line of a {file}`todo.txt` file using
the `.readlines()` method then printing each line with a `*` at the beginning.

1. Copy the following text and paste it into a file named {file}`todo.txt` in
   your working directory that contains a list of items to do.
   :::{dropdown} todo.txt
   ```{code-block} text
   :caption: "todo.txt"
   dishes
   laundry
   homework
   ```
   :::
2. Create a new file {file}`todo.py` for this exercise.
3. Use the `open()` function to get a file handler for the {file}`todo.txt` file.
4. Use a `for` loop to iterate over the list returned by `fh.readlines()` and
   name the item variable `line`.
5. In the for loop, print `"* "` followed by each `line` and tell `print()`
   not to add an extra newline by passing the `end` keyword argument with an empty
   string.
6. Use the `.close()` method to close the file handler.

{{ leftcol }}

Your output should look like this:

{{ rightcol }}

```{code-block} text
:caption: output
* dishes
* laundry
* homework
```

{{ endcols }}

`````

`````{solution} readlines-exercise
:class: dropdown

```{code-block} python
:caption: todo.py
:linenos:
fh = open("todo.txt")
for line in fh.readlines():
  print("*", line, end="")
fh.close()
```
`````

Part 2: Writing Files
---------------------

Sometimes we need to create or modify files. That's what we'll be learning in
this section.

### Part 2.1: Creating or truncating

The `open()` function takes an optional `mode` argument, which is a string that
indicates what we plan to do with the file. The default is `"r"` for read mode.

To write to a file though, we'll open it in write mode by passing the optional
mode argument `"w"` to `open()`. Write mode will either create or overwrite the
file and open it with permission to write.

#### A. Write to `packing.txt`

In this section we're going write the contents of a `to_pack` list to a
{file}`packing.txt` file.

1\. Create a file {file}`packing.py`, add a `create_packing()` function and
call it. The rest of your code in this section will go in this function.

2\. Add a `to_pack` list of strings, things to pack.

3\. Get a file handler `fh` by calling `open()` with the arguments `"packing.txt"`
and `"w"` for write mode. Be aware: the file is created or
{term}`truncated <truncate>` as soon as `open()` is called when in write mode.

4\. Using a `for` loop iterate over the `to_pack` list and name the item variable
`thing`.

5\. In write mode, file handler objects keep a {term}`buffer` where the text to be
written to the file is stored until `.close()` is called. Inside the loop we'll
add each `thing` to the buffer by calling the `.write()` method on `fh` with
the argument {samp}`"- {thing}\n"`. Don't forget to add a `"\n"` to the end
of each string or the file will all be smooshed onto one long line!

6\. As always, we need to `.close()` the file handler when we're done with the
file. It is especially important in write mode because that is when the buffer
is written to disk.

```{code-block} python
:caption: packing.py
:linenos:

def create_packing():
  """Create or overwrite packing.txt and write contents of to_pack list on each
     line"""

  # create a list of things to pack
  to_pack = [
    "phone charger",
    "passport",
    "weapons",
    "cash",
  ]

  # open packing.txt in write mode, which is
  # when the file is created or truncated
  fh = open("packing.txt", "w")

  # iterate through the to_pack list
  for thing in to_pack:
      # add each thing to the file buffer
      # with a "\n" suffix so its on its own line
      fh.write(f"- {thing}\n")

  # close the file handler, which is when the the file is written to disk
  fh.close()

if __name__ == "__main__":
  create_packing()
```

{{ leftcol }}

7\. Now open up your {file}`packing.txt` file. It should look something like this:

{{ rightcol }}

```{code-block} text
:caption: packing.txt
- phone charger
- passport
- weapons
- cash
```

{{ endcols }}

### Part 2.2: Exercise

`````{exercise} writing files
:label: writing-files-exercise

In this exercise you'll make a `people` list and write it to a
{file}`xmas_shopping.txt` file.

1. Create a file `xmas_shopping.py` for this script, add a
  `create_xmas_shopping()` function and call it. Put the rest of the code from
  this exercise in that function.
2. Add a `people` list of strings, names of people to shop for.
3. Open the file {file}`xmas_shopping.txt` in write mode and name the file
   handler object `fh`.
4. Iterate through your list of `people` using a `for` loop and name your items
   variable `name`.
5. In the loop `.write()` a line to the buffer: {samp}`"[ ] {name}\n"`.
6. `.close()` the file handler

{{ leftcol }}

{file}`xmas_shopping.txt` should look something like this:

{{ rightcol }}

```{code-block} text
:caption: xmas_shopping.txt
[ ] Buffy
[ ] Xander
[ ] Willow
[ ] Giles
```

{{ endcols }}

`````

`````{solution} writing-files-exercise
:class: dropdown

```{code-block} python
:caption: xmas_shopping.py
:linenos:
def create_xmas_shopping():
    """Create or overwrite xmas_shopping.txt and write contents of people list on each
       line"""

    people = [
        "Buffy",
        "Xander",
        "Willow",
        "Giles",
    ]

    fh = open("xmas_shopping.txt", "w")
    for name in people:
        fh.write(f"[ ] {name}\n")

    fh.close()

if __name__ == "__main__":
    create_xmas_shopping()
```
`````

### Part 2.3: Adding to files

Often instead of writing a whole file from scratch we just want to add to the
end of it.  That's when we want append mode.

#### A. Add to `packing.txt`

In this section we're going append a single line to the {file}`packing.txt`
file.

1\. Open the {file}`packing.py` file, add a `addto_packing()` function and call it. The
rest of your code in this section will go in this function.

2\. Get a file handler `fh` by calling `open()` with the arguments `"packing.txt"`
and `"a"` for append mode.

3\. Add a single line the buffer by calling the `.write()` method on `fh` with the
argument {samp}`"- {thing to pack}\n"`.

4\. Finally, `.close()` the file handler.


```{code-block} python
:linenos:
:lineno-start: 26
:caption: packing.py

def addto_packing():
  """Append a single line to the packing.txt file"""

  # open the file in append mode
  fh = open("packing.txt", "a")

  # add a single line to the file buffer
  fh.write("- first aid kit\n")

  # close the file handler, which is when the the file is written to disk
  fh.close()

if __name__ == "__main__":
  create_packing()
  addto_packing()
```

{{ leftcol }}

5\. After running your code the {file}`packing.txt` file should look something like this:

{{ rightcol }}

```{code-block} text
:caption: packing.txt
- phone charger
- passport
- weapons
- cash
- first aid kit
```

{{ endcols }}

### Part 2.4: Exercise

`````{exercise} appending to files
:label: appending-to-files-exercise

In this exercise you'll append a single line to the {file}`xmas_shopping.txt`
file.

1. Open the file `xmas_shopping.py`, add a `addto_xmas_shopping()` function and
   call it. Put the rest of the code from this exercise in that function.
2. Open the file {file}`xmas_shopping.txt` in append mode and name the file
   handler object `fh`.
3. `.write()` a line to the buffer: {samp}`"[ ] {name}\n"`.
4. `.close()` the file handler

{{ leftcol }}

You should see the new name in {file}`xmas_shopping.txt`, something like:

{{ rightcol }}

```{code-block} text
:caption: xmas_shopping.txt
[ ] Buffy
[ ] Xander
[ ] Willow
[ ] Giles
[ ] Angel
```

{{ endcols }}

`````

`````{solution} appending-to-files-exercise
:class: dropdown

```{code-block} python
:caption: xmas_shopping.py
:linenos:
:lineno-start: 17

def addto_xmas_shopping():
  """Append a single line to the xmas_shopping.txt file"""

  # open the file in append mode
  fh = open("xmas_shopping.txt", "a")

  # add a single line to the file buffer
  fh.write("[ ] Angel\n")

  # close the file handler, which is when the the file is written to disk
  fh.close()

if __name__ == "__main__":
    create_xmas_shopping()
    addto_xmas_shopping()
```
`````

Part 4: Automatic file closing
------------------------------

There are lots of reasons that it is important to always `.close()` a file
handler object when you're done with it.

- In theory Python is supposed to close any open file handlers when a program
  ends, but it's not a guarantee.
- The more files are open, the more resources are used, and the more space is
  taken up in memory. Leaving things open unnecessarily could slow down your
  program and your computer while your program runs.
- File changes usually don't go into effect until you close the file handler.
  If another part of your program is counting on those changes, you'll run into
  unpleasant surprises if you haven't yet closed it.
- There are limits to how many files a computer can have open at a time. While
  it is rare to bump up against those limits in normal operation, it's
  certainly the kind of trouble a programmer can get themselves into by
  mistake. (Imagine opening files in an infinite loop!)
- Some operating systems treat open files as locked, which may prevent you from
  reading the file with another program or even deleting it.

But sometimes mistakes happen. It's easy to forget, and what if there is an
error after opening the file but before it is closed?

That's where the `with` statement and {term}`context managers <context manager>`
come in.

### Part 4.1: the `with` statement

File handlers in Python have the feature of being {term}`context managers`,
which are objects designed to know how to do their own housekeeping for use in
a `with` statement.

More on that later, but first lets take a quick look at the syntax of a `with`
statement:

{{ leftcol | replace("col", "col-5") }}

```{include} ../templates/syntax/with.md
```

For files it looks like:

```python
with open(...) as fh:
    # do stuff with fh
```

{{ rightcol | replace("col", "col-7") }}

```{include} ../templates/desc/with.md
```

{{ endcols }}

So, what does that do?

The `with` statement wraps a block of code with calls to internal setup and
teardown methods provided by the context manager. In particular, anything that
ends the execution of the block triggers a call to the teardown method; whether
it ended because it finished or because there was an error. Neither errors nor
{kbd}`^C` stays the `with` statement from completing the appointed teardown.

% The `with` statement wraps a block of code and ensures that internal setup and
% teardown methods provided by the context manager are called before the code is
% executed, and when it ends respectively.

File handlers know how to clean up after themselves. That means that when used
in a `with` statement `.close()` is called automatically at the end of the
statement, even if there is an error in the {samp}`{BODY}`.

Lets take a look at our very first `groceries.txt` code alongside the same code
written using a `with` statement.

{{ leftcol }}

```{code-block} python
:caption: groceries.py
:linenos:
:emphasize-lines: "2, 8"

# open the file
fh = open("groceries.txt")

# read the contents
contents = fh.read()

# close the file handler
fh.close()

# print the file contents
print("Groceries")
print("=========")
print(contents)
```

{{ rightcol }}

```{literalinclude} ../templates/examples/with.py
:caption: groceries.py
:linenos:
:emphasize-lines: "2, 7-8"
```

{{ endcols }}

```{seealso}

* [python.org language reference > With Statement Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
* [python.org language reference > the with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

```

### Part 4.2: `scores.txt`

In this section we are going to use a `with` statement to append a line with
random number to a `scores.txt` file.

1\. Create a new file {file}`scores.py`.

2\. Import the `random` module.

3\. Add a `add_scores()` function and call it.  The rest of your code in this
section will go in this function.

4\. Call `random.randint()` to get a random number between `0` and `100` and assign
it to the variable `score`.

5\. Use a `with` statement to open the {file}`"scores.txt"`:
  - the {samp}`{EXPN}` should be a call to `open()` with the arguments
    {file}`"scores.txt"` and `"a"` for append mode
  - give the {samp}`{VAR}` the name `fh`
  - in the {samp}`{BODY}` add a single line {samp}`"{score}\n"` the buffer by calling the
    `.write()` method on `fh`

```{code-block} python
:linenos:
:caption: scores.py
import random

def add_scores():
    """Append a random score between 1 and 100 to scores.py"""

    # get a random number between 1 and 100
    score = random.randint(0, 100)

    # open scores.txt in append mode
    with open("scores.txt", "a") as fh:

        # add the score to the file buffer
        fh.write(f"{score}\n")

if __name__ == "__main__":
    add_scores()
```

{{ leftcol }}

6\. After you run your script {file}`scores.txt` should contain a single number, something like this:

{{ rightcol }}

```{code-block} text
:caption: scores.txt
85
```

{{ newrow }}

7\. Run your script a few more times. {file}`scores.txt` should have some new lines, something like this:

{{ rightcol }}

```{code-block} text
:caption: scores.txt
85
91
29
20
39
```

{{ endcols }}

### Part 4.3: Exercise

`````{exercise} with statements
:label: with-statement-exercise

In this exercise you'll be reading each line of the {file}`scores.txt` file using
the `.readlines()` method then printing the last line.

1. Open the {file}`scores.py` file, add a new function `last_score()`, and call it.
2. Use a `with` statement to open the {file}`"scores.txt"`:
   - the {samp}`{EXPN}` should be a call to `open()` with the argument
     {file}`"scores.txt"` to open the file in read mode.
   - give the {samp}`{VAR}` the name `fh`
   - in the {samp}`{BODY}`:
      * Use a `for` loop to iterate over the list returned by `fh.readlines()`
        and call the item variable `score`
      * You only need to for loop to assign the `score` variable, so in the
        body of the loop just `continue`.
3. After the `with` statement, `score` will still be assigned to the last line
   of the file.  Print {samp}`Your last score was: {score}` and use the `end`
   keyword argument to avoid adding an extra newline.

{{ leftcol }}

Your output should look something like this:

{{ rightcol }}

```{code-block} text
:caption: output
Your last score was: 18
```

{{ endcols }}

`````

`````{solution} with-statement-exercise
:class: dropdown

```{code-block} python
:caption: scores.py
:linenos:
:lineno-start: 15
def last_score():
    """Print the most recent score from the scores.text file"""

    # open scores.txt in read mode
    with open("scores.txt") as fh:

        # iterate through each line in the file
        for score in fh.readlines():

            # nothing to do in the loop since
            # we just need to assign the score variable
            continue

    # print the final value of score (the last line of the file)
    print(f"Your last score was: {score}", end="")

if __name__ == "__main__":
    add_scores()
    last_score()
```
`````

Reference
---------

### File Modes

These are the mode characters that can be used in the `open()` function.

| Type         | Char | Name               | Description                             |
|--------------|------|--------------------|-----------------------------------------|
| writeability | `r`  | read               | read only (default)                     |
| writeability | `w`  | write              | create a new file or overwrite existing |
| writeability | `a`  | append             | add to the end of a file                |
| writeability | `x`  | exclusive create   | create a new file or fail if existing   |
| writeability | `+`  | read+write         | allow reading and writing               |
| format       | `t`  | text               | text files (default)                    |
| format       | `b`  | binary             | for images and other non-text files     |

They can be combined, for example:

| Mode   | Description                                                                                  |
|--------|----------------------------------------------------------------------------------------------|
| `a+`   | start at the end of the file and allow both reading and writing                              |
| `w+`   | create a new file or overwrite existing and allow reading and writing                        |
| `rb`   | open a file in binary mode for reading only                                                  |

### See Also

```{seealso}

* [python.org > Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#tut-files)
* [python.org > Built-in Functions > open](https://docs.python.org/3/library/functions.html#open)

```

### Glossary

```{glossary} file-io

file-like object
file object
file handler
IO object
  An object used to connect to and interact with a file.

buffer
  A sort of temporary holding pen for data that is going from one place to
  another. For example, the default behavior of writable {term}`file handler`
  objects is to append the data passed to the `.write()` function to the write
  buffer, then write the buffer to disk when the handler is closed. This
  improves preformance by reducing the number of hard disk writes.

context manager
context manager objects
  Python objects that know how to do their own houskeeping. More precicely,
  objects that provide the {term}`dunder methods` `.__enter__()` and
  `.__exit__()` intended to be used by the `with` statement for setup and
  teardown tasks.

truncate
  To shorten something but cutting off a part. When a text file is opened in
  write mode, it is truncated to zero bytes, thereby removing all content from
  the file.
```
