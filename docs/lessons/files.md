File I/O
========

I/O is a shorthand way of referring to input and output. The `input()` and
`print()` functions are two examples of input and output. In this lesson
we'll learn another: how to read from and write to files.

Reading Files
-------------

Create a file {file}`groceries.txt` in the directory you will be running the
script from, or the {term}`working directory`.

```{code-block} text
:caption: groceries.txt
- eggs
- milk
- flour
```

To read the contents of the file, we'll first use Python's built-in `open()`
function and pass it the name of the file to open. It will return a file
handler object which has methods for interacting with the file.

Next call the `read()` method on the handler which will return the entire
contents of the file as a string.

Finally, call the `close()` method. This frees up the computer resources used
to manage the file.

```{code-block} python
:caption: shopping.txt
fh = open("groceries.txt")
contents = fh.read()
fh.close()

print("Groceries")
print("=========")
print(contents)
```

### Reading lines

Often we want to read files one line at a time. The `readlines()` method on
the file handler object returns a list where each element is one line in the
file.

```{code-block} python
:caption: shopping.txt
print("Groceries")
print("=========")

fh = open("groceries.txt")
for line in fh.readlines():
    print(line, end="")
fh.close()

```

:::{note}

Each element in the list includes the carriage return (`"\n"`). So to avoid
printing double lines use the `end` keyword argument in the `print()`
function.

:::

Writing Files
-------------

To write to a file open it in write mode by passing the optional mode
argument `"w"` to `open()`. This will either create a new file if none
exists, or replace it with an empty text file if it does.

Call the `write()` method on the file handler object to add to the
{term}`buffer`, the stored text to be written to the file. Be sure to add a
`"\n"` at the end of every line, including the last line in the file.

Again, call the `close()` method. This will print the buffer to the file and
close the file connection.

```{code-block} python
:caption: todos.py
todos = [
    "laundry",
    "dishes",
]

fh = open("todo.txt", "w")
for item in todos:
    fh.write(f"- {item}\n")
fh.close() 
```

### Adding to files

Instead of writing a file from scratch we can instead just add to the end of
it by opening it in append mode by passing the mode mode argument `"a"` to
the `open()` function.

```{code-block} python
:caption: todos.py
fh = open("todo.txt", "a")
fh.write("vacuum\n")
fh.close() 
```

Automatic file closing
----------------------

It's important to always `close()` a file handler object, since this will
ensure that we don't have resources still tied up after the program ends that
we are actually done with. Moreover in write or append mode, nothing is
actually written until the file is closed.

But it's possible to either forget to close the file handler, or for our
program to encounter an error before it gets to the place where `close()` is
called.

Python provides a handy way of ensuring file objects are always closed, the
`with` compound statement.

```{code-block} python

with open("groceries.txt") as fp:
    contents = fp.read()

print("Groceries")
print("=========")
print(contents)
```

Reference
---------

### File Modes

These are the mode characters that can be used in the `open()` function.

| Type       | Char | Name               | Description                             |
|------------|------|--------------------|-----------------------------------------|
| writeability | `r`  | read               | read only (default)                     |
| writeability | `w`  | write              | create a new file or overwrite existing |
| writeability | `a`  | append             | add to the end of a file                |
| writeability | `x`  | exclusive create   | create a new file or fail if existing  |
| writeability | `+`  | read+write         | allow reading and writing               |
| format     | `t`  | text               | text files (default)                    |
| format     | `b`  | binary             | for images and other non-text files     |

They can be combined, for example:

| Mode   | Description                                                                                  |
|--------|----------------------------------------------------------------------------------------------|
| `a+`   | start at the end of the file and allow both reading and writing                              |
| `w+`   | create a new file or overwrite existing and allow reading and writing                        |
| `rb`   | open a file in binary mode for reading only                                                  |
