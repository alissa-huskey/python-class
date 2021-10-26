---
substitutions:
  left:  '{{ leftcol | replace("col", "col-5") }}'
  right: '{{ rightcol | replace("col", "col-7") }}'
  row: '{{ newrow | replace("col", "col-5") }}'
  label: '<div class="text-right">Syntax:</div>'

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

Strings
=======

{{ leftcol | replace("col", "col-8")  }}

An ordered collection of characters accessed via index numbers.

```{contents} Table of Contents
:backlinks: top
:local:
```

{{ rightcol | replace("col", "col-4 text-right") }}

:::{fieldlist}

:Type:        `str`
:Synatx:      {samp}`"{char},..."`
:Bases:       Sequence, Iterable
:State:       Immutable
:Position:    Ordered
:Composition: Homogeneous
:Diversity:   Repeatable
:Access:      Subscriptable
:Value:       Hashable

:::

{{ endcols }}

Part 1: Introduction
--------------------

While most of the time we can think of strings as text data, under the hood
strings are a {term}`sequence` of characters.

### Part 1.1: Creating

{{ left }}

Strings store text data and can be enclosed in either single or double quotes.

{{ right }}

```{code-cell}
""
"Hello."
'Farewell.'
"It's a lovely day."
'"Well hello!", he said.'
```

{{ row }}

For a string that spans multiple lines, enclose it in triple double (`"""`) or
triple single (`'''`) quotes.

{{ right }}

```{code-cell}
rhyme = """Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""

print(rhyme)
```

{{ row }}

Backslashes (`\`) are used to escape quotes or to indicate special characters,
like `\n` for a new line.

{{ right }}

```{code-cell} python
print('It\'s a nice day.')
print("line one\nline two")
```

{{ row }}

For strings that contain backslashes use a double backslash (`\\`) or prefix
the string with the letter `r` for a raw string.

{{ right }}

```{code-cell} python
print('"\\n" is used to add a newline')
print(r"C:\Documents\nodes")
```

{{ endcols }}

### Part 1.2: Exercises

`````{exercise} String Creation
:label: string-create-exercise

1. Use a docstring to split the lymric or lullaby of your choice into a multi-line string
   and assign it to the variable `verse`, then print it.
2. Using one double-string or single-quoted string, print the words `"one"`,
   `"two"`, and `"three"` on three seperate lines.
3. Print a double quoted string that includes double quotes. Print a single
   quoted string that includes single quotes.
4. Print a string that includes backslashes by escaping the backslash. Print a
   second string that includes backslashes using an r-string.

`````

`````{solution} string-create-exercise

:::{dropdown} #1: Verse Docstring

```{code-block} python
:caption: "String Creation Exercise #1"
:class: full-width
:linenos:
verse = """Jack and Jill
Went up the hill
To fetch a pail of water
Jack fell down and broke his crown
And Jill came tumbling after."""

print(verse)
```

:::

:::{dropdown} #2: One, Two, Three lines, muah hah haa!

```{code-block} python
:caption: "String Creation Exercise #2"
:class: full-width
:linenos:
print("one\ntwo\nthree")
```

:::

:::{dropdown} #3: Quotable quotes

```{code-block} python
:caption: "String Creation Exercise #3"
:class: full-width
:linenos:
print('...for he\'s a jolly good fellow, that nobody can deny!')
print("She muttered, \"Well, I for one can deny it.\"")
```

:::

:::{dropdown} #4: Sometimes backslashes just want to be seen

```{code-block} python
:caption: "String Creation Exercise #4"
:class: full-width
:linenos:
print('This is a backslash: "\\".')
print(r'So is this: "\".')
```

:::

`````

### Part 1.2: Modifying

Strings are {term}`immutable`, which means that once created, they cannot be
changed.  But it's only the exact object stored in memory that can't be
changed. Most of the time, we don't care so much about the exact object, just
the end result.

What you can do is create a new string cobbled together from the parts of other
strings, and you can even assign it back to the same variable name.

{{ left }}

Strings can be {term}`concatenated <concatenate>` (joined together) by using
the `+` operator.

{{ right }}

```{code-cell} python
name = "coding class"
print("Welcome to " + name + ".")
```

{{ row }}

String literals (the ones in quotes) next to each other are automatically
concatenated.

{{ right }}

```{code-cell} python
text = "Today we're talking about" 'strings.'
print(text)
```

{{ row }}

You can take advantage of this to break long text into
multiple lines of code. Put strings on consecutive lines
without separating commas and enclose the whole expression
in parentheses `(` `)`.

{{ right }}

```{code-cell}
text = (
  "Lorem ipsum dolor sit amet, consectetur "
  "adipiscing elit, sed do eiusmod tempor "
  "incididunt ut labore et dolore magna "
  "aliqua. Ut enim ad minim veniam, quis "
  "nostrud exercitation ullamco laboris "
  "nisi ut aliquip ex ea commodo consequat."
)

print(text)
```

{{ row }}

To effectively append to an existing string, you can use the `+=` operator.

{{ right }}

```{code-cell} python
text = "Unfinished "
text += "business."
print(text)
```

{{ row }}

You can repeat a string multiple times using the `*` operator.

{{ right }}

```{code-cell} python
text = "The horror! " * 2
print(text)
```

{{ row }}

Similarly you can use the `*=` operator to effectively append a value to itself
a number of times.

{{ right }}

```{code-cell} python
text = "All work and no play makes Jack a dull boy.\n"
text *= 5
print(text)
```

{{ row }}

Use an f-string for string {term}`interpolation` by prefixing the string with the
letter `f` then enclose the variable or other evaluated code curly braces (`{` `}`).

{{ right }}

```{code-cell} python
price = 1.25
count = 5

print(f"I am buying {count} apples for ${price} each.")
print(f"The total is ${price*count}.")
```

{{ endcols }}

### Part 1.2: Exercise

`````{exercise} String Modification
:label: string-modify-exercise

1. Use the `+` operator to join two strings together and print the result.
2. Concatonate two string literals without using the `+` operator and print the result.
3. Choose a long paragraph of text. Break it up onto multiple lines **in your
   code** while still all on one line in the string itself. Assign it to the
   variable `paragraph` and print it.
4. Assign the string `"Four out of five dentists agree: "` to the varable `text`.
   Choose something the dentists agree on and on a new line, append it to
   `text`. Print `text`.
6. Use both the `+` and `*` operators to assign the string `"Noooooo!"` to the
   variable `text` then print it. Change the number of `"o"`s and print it again.
5. Pick something that Bart Simpson may have written on the blackboard and
   assign it to the variable `admonition`. Append it to itself `10` times then
   print it. \
   *Note: This should take no more than 2 lines of code.*
   *Bonus: Write a function to do this.*
6. Choose a name and assign it to the variable `name`. Using an f-string, print: \
   {samp}`"Hello my name is: {NAME}."`
7. Create a visual line by repeating the underscore character (`"_"`) some
   number of times, (say, `20`) and assign it to the variable `line`. Using an
   f-string, make a string with a single line of a sign-up sheet that looks
   something like this:

   `"Name: ____________________   Email: ____________________"`

   Assign it to the variable `row` and print it `25` times to generate a
   sign-up sheet.

`````

`````{solution} string-modify-exercise

:::{dropdown} #1: Concatonate with `+`

```{code-block} python
:caption: "String Modification Exercise #1"
:class: full-width
:linenos:
text = "Hello " + "world!"
print(text)
```

:::

:::{dropdown} #2: Concatonate without an operator

```{code-block} python
:caption: "String Modification Exercise #2"
:class: full-width
:linenos:
text = "Goodbye " "cruel world!"
print(text)
```

:::

:::{dropdown} #3: Paragraph concatonation

```{code-block} python
:caption: "String Modification Exercise #3"
:class: full-width
:linenos:
paragraph = (
  "Quo usque tandem abutere, Catilina, "
  "patientia nostra? Quam diu etiam "
  "furor iste tuus nos eludet? Quem "
  "ad finem sese effrenata iactabit "
  "audacia?"
)
print(paragraph)
```

:::

:::{dropdown} #4: Dentists conclude...

```{code-block} python
:caption: "String Modification Exercise #4"
:class: full-width
:linenos:
text = "Four out of five dentists agree: "
text += "that other guy is nuts."
print(text)
```

:::

:::{dropdown} #5a: Variously emphatic `"No!"`

```{code-block} python
:caption: "String Modification Exercise #5a"
:class: full-width
:linenos:
text = "N" + ("o"*1) + "!"
print(text)

text = "N" + ("o"*3) + "!"
print(text)

text = "N" + ("o"*8) + "!"
print(text)
```

:::

:::{dropdown} #5b: (Bonus) Efficient variously emphatic `"No!"`

```{code-block} python
:caption: "String Modification Exercise #5b"
:class: full-width
:linenos:
def no(ohs):
  text = "N" + ("o"*ohs) + "!"
  print(text)

no(1)
no(3)
no(8)
```

:::

:::{dropdown} #6: Chalkboard repetition

```{code-block} python
:caption: "String Modification Exercise #6"
:class: full-width
:linenos:
admonition = "I will not repeat myself.\n"
admonition *= 10
print(admonition)
```

:::

:::{dropdown} #7: Nametag

```{code-block} python
:caption: "String Modification Exercise #7"
:class: full-width
:linenos:
name = "Inigo Montoya"
print(f"Hello my name is: {name}.")
```

:::

:::{dropdown} #8: Sign-up Sheet

```{code-block} python
:caption: "String Modification Exercise #8"
:class: full-width
:linenos:
line = "_" * 20
row = f"Name: {line}    Email: {line}\n"
print(row * 25)
```

:::

`````

Part 2: Strings as sequences
----------------------------

Under the hood a string is a {term}`sequence` of characters. Let's take a simple example.

```{code-cell} python
word = "cat"
```

This could be visualized as:


```{kroki}
:type: ditaa
+----------------------------------------+
|                                        |
|   word (str)                           |
|                                        |
|   +----------+----------+----------+   |
|   |          |          |          |   |
|   | "c"      | "a"      | "t"      |   |
|   |          |          |          |   |
|   +----------+----------+----------+   |
|   |    0 cCFF|    1 cCFF|    2 cCFF|   |
|   +----------+----------+----------+   |
|   |   -3 cCCF|   -2 cCCF|   -1 cCCF|   |
|   +----------+----------+----------+   |
|                                        |
+----------------------------------------+

  /----\               /----\
  |cCFF| index number  |cCCF| negative index
  \----/               \----/

```

### Part 2.1: Sequence features

Since it is a sequence, that means you can do most of the same things you can
do with a list.

{{ leftcol }}

You can use `subscription` to access characters via negative or positive index
number.

{{ rightcol }}

```{code-cell} python
print(word[0])
print(word[-1])
```

{{ newrow }}

You can get part of a string via {term}`slice`.

{{ rightcol }}

```{code-cell} python
print(word[1:])
```

{{ newrow }}

You can get the length using the `len()` function.

{{ rightcol }}

```{code-cell} python
len(word)
```

{{ newrow }}

You can check if a single character or a substring is part of a string using
the `in` and `not in` operators.

{{ rightcol }}

```{code-cell} python
"c" in word
```

```{code-cell} python
"at" not in word
```

{{ newrow }}

You can check how many times a letter or substring occurs in a string using the `.count()` method.

{{ rightcol }}

```{code-cell} python
word.count("c")
```

```{code-cell} python
word.count("at")
```

{{ newrow }}

You can find out the index number of the first occurance of a letter or substring.

{{ rightcol }}

```{code-cell} python
word.index("c")
```

```{code-cell} python
word.index("at")
```

{{ newrow }}

You can iterate over every character.

{{ rightcol }}

```{code-cell} python
for char in word:
    print(char)
```

{{ newrow }}

However, since strings are immutable, you cannot modify a string via subscription.

{{ rightcol }}

```{code-cell} python
:tags: [raises-exception]
word[0] = "b"
```

{{ endcols }}

### Part 2.2: Exercises

`````{exercise} String as Sequence Exercise
:label: string-sequence-exercise

1. Make a list of words and assign it to the variable `sentence`. Iterate over
   the list and print the first letter in each word.
`````

`````{solution} string-sequence-exercise
:class: dropdown

```{code-block} python
:caption: "String as Sequence Exercise"
:class: full-width
:linenos:

sentence = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

for word in sentence:
    print(word[0])
```

`````
---


% TODO
% [x] `in`, `not in`
% [x] `len()`
% [x] subscription, characters, slicing
% [ ] chr() ord()


% [ ] replace
% [ ] methods, rmethods, lmethods
% [ ] templates
% [ ] strings <=> lists
%     [ ] str.join()
%     [ ] list(str)
%     [ ] str.partition()
%     [ ] str.split()
%     [ ] str.splitlines()
% [ ] textwrap
% [ ] regex
% [ ] bytes, b'chars', bytesarray
% [ ] string.ascii_lowercase, etc
% [ ] encodings: ascii, utf-8 (unicode), `ascii()`

% [x] `+`, `*`
% [x] escaping, raw, escape sequences
% [x] f-strings

% REFERENCE
% https://realpython.com/python-strings/


% EXERCISES
% [ ] merge text onto a single line and remove indentation
% [ ] convert underscore <=> camelcase
% [ ] check for word word variant (ing, ed, s)
% [ ] rot13 cypher
% [ ] check if two values are equal, ignoring case and leading or tailing whitespace
% [ ] remove the substring " and" from a string like "one, two, and three"
% [ ] get the sum of a list of numbers sent as a string: "10,20,30,40,50,60,70"
% [ ] format a credit card number: output: "1234-5678-9878-0434" input: may or may not include spaces or dashes
% [ ] print two columns
% [ ] indent the first line of each paragraph
% [ ] given list:
%     gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]
%     make dict:
%     { "Mobile Laptop": 100, "Camera": 310.28, ...}
% [ ] given text input like:
%     Mary|76 72 71 68 85 69,
%     John|69 67 68 71 68 67,
%     Anne|80 69 59 82 71 81,
%     Mark|79 81 74 71 69 73
%     make dict:
%     {"mary": 441, "john": 410}
% [ ] Caesar cipher
% [ ] find token in command
%     given string:
%     `"buy wood stove"`
%     and list:
%     ["stove", "wood stove"]
%     find:
%     "wood stove"
% [ ] check if a string is a url/phone number @regex
