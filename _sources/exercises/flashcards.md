Flashcards Project
==================

This is the project to apply what we've learned in the [](../lessons/files) lessons.

The project is to write a program for running through flashcards. Card data is
stored in `csv` files in the `data/flashcards` directory.

Instructions
------------

### Part 1: Make a `csv` file

The flashcards data will be stored in `csv` files in a directory named
`data/flashcards`. The idea is to eventually have multiple files for different
topics that you might want to study like `paths.csv`, `functions.csv` and so
on. For now though, just make one file.

1. [ ] Create a folder `data/flashcards` if it doesn't already exist
2. [ ] Make a `csv` file with flashcard data
   * [ ] In the `data/flashcards` directory manually make file ending in
         `.csv`. For example `paths.csv`.
   * [ ] Each line should be one card with the format: {samp}`{text for front}, {text for back}`. \
        For example:
        ```text
        front, back
        import the Path class, from pathlib import Path
        check if Path object path exists, path.exists()
        check if Path object path is a file, path.is_file()
        check if Path object path is a directory, path.is_dir()
        ```

### Part 2: Start `flashcards.py`

Start your {file}`flashcards.py` file.

1. [ ] write a `main()` function
1. [ ] print any temporary debug message in it
1. [ ] call it

### Part 3: Start `load_csv()`

The `load_csv()` function should take one argument, a `Path` object to a csv
file. Eventually it will return a `list` where each item is a `dict` with `"front"`
and `"back"` keys, one for each row in the file except the header.

For now though, make a simple function that just takes a `Path` object, prints
the location, and makes sure the file exists.

```{rubric} load_csv()
```

1. [ ] write a `load_csv()` function that takes one argument: `path`
1. [ ] check to make sure the `csv` file exists. If not, print an error message
       that includes the path then return
1. [ ] print a temporary debug message: {samp}`loading file: {path}`

```{rubric} in main()
```

1. [ ] make a `Path` object to your `csv` file
1. [ ] call your `load_csv()` function, passing it your `Path` object as the
      argument, and assign the returned value to a variable named `cards`

### Part 4: Read each line of the csv file

Expand the `load_csv()` function to read and print every line in the file.

```{rubric} in load_csv()
```

1. [ ] open the csv file in read mode using the `open()` function
1. [ ] use `fp.readlines()` to iterate through each line in the file
1. [ ] for temporary debugging, print each line

### Part 5: Get the card data from the csv file

Continue expanding the `load_csv()` function to extract the card data from each
line, put it into a dictionary named `cards` with the keys `"front"` and
`"back"`.

```{rubric} in load_csv(), *in* the readlines() loop
```

1. [ ] make an empty `dict` assigned to a variable named `card`
1. [ ] split each line on the `","` using the `.split()` method and assign
       the result to a variable named `row`
1. [ ] check that there are two items in the row using the `len()` function.
       If not print an error message and return
1. [ ] assign `card["front"]` to the first item in the row, and `card["back"]` to
       the second
1. [ ] for temporary debugging, print the `card` `dict`


### Part 6: Return the card data to `main()`

Have `load_csv()` put all of the `card` dictionaries into one big `cards`
`list` and return that to `main()`.

```{rubric} in load_csv(), *before* the readlines() loop
```

1. [ ] make an empty `list` assigned to a variable named `cards`

```{rubric} in load_csv(), *at the end* of the readlines() loop
```

1. [ ] use the `.append()` method on the `cards` `list` with the argument `card`


```{rubric} in load_csv(), *after* the loop
```

1. [ ] return `cards`

```{rubric} in main()
```

1. [ ] if the `cards` `list` is falsy, `return`
1. [ ] otherwise, print the `cards` `list` for temporary debugging

### Part 7: Remove extra whitespace

In order to make sure that the flashcards are printed nicely and that the users
answers get matched up correctly, the trailing `"\n"` needs to be removed from
the end of each line. Any extra spaces that happen to be around the `","` or at
the beginning or end of the line also need to be removed.

```{rubric} in load_csv(), *in* the loop
```

1. [ ] remove leading and trailing whitespace by calling the `.strip()` method
       on `card["front"]` and `card["back"]`

### part 8: Skip the header row

To avoid having a flashcard pop up that reads `"front"`, don't append the
header row to the `cards` `list`.

```{rubric} in load_csv(), in the readlines() loop, before append
```

1. [ ] check if `card["front"]` is `"front"` and `card["back"]` is `"back"`. If so,
    `continue` to avoid appending to the cards list

### Part 9: Start the `play()` function

This function should take one argument, the list of cards.
Eventually it will contain the user interface for running through each
card, getting the answers from the user, and printing the score.

For now 'll just write a `play()` function and call it.

```{rubric} play()
```

1. [ ] write a `play() f`unction that takes one argument: `cards`
1. [ ] for temporary debugging, print something from it

```{rubric} main()
```

1. [ ] call `play()` passing it the list of `cards`


### Part 10: Go through each card in random order

In this next part we'll be metaphorically drawing a card at random from the
deck until there are none left.

The trick is to make a {term}`while loop` that checks the {term}`truthy` value
of `cards`, so that it stops as soon as its empty. The inside the loop, use the
`random.choice()` method to pick a `card` at random, then remove it from the list.

```{rubric} at the top of your file
```

1. [ ] `import` the `random` module

```{rubric} in play()
```

1. [ ] make a while loop where the condition is: `cards`

```{rubric} in play(), in the loop
```

1. [ ] use `random.choice()` to get a random item from the `cards`
       list and assign it to a variable named `card`
1. [ ] call the `.remove()` method on `cards` with the argument `card` to
       remove the card from the list
1. [ ] for temporary debugging, print `card`

### Part 11: Test the user

This is where things start to get exciting! In this part we'll print the front
of the card, ask the user for their answer, and let them know if it was right
or not.

```{rubric} in play(), in the loop
```

1. [ ] print `card["front"]`
1. [ ] prompt the user for their answer using the `input()` function and assign
       the result to a variable named `answer`
1. [ ] check if the `answer` is the same as `card["back"]`
       * [ ] if so, increment `score` by one and print `"CORRECT"`
       * [ ] if not, print `"INCORRECT",` then `cards["back"]`
1. [ ] call `input()` asking if the user wants to continue

```{rubric} in play(), after the loop
```

### Part 12: Scorekeeping

Now lets keep track of which card the user is on, and what their score is.

```{rubric} in play(), above the loop
```

1. [ ] assign the length of cards to a variable `total`
1. [ ] make a `num` variable set to `1`
1. [ ] make a `score` variable set to `0`

```{rubric} in play(), in the loop
```

1. [ ] at the top of the loop print {samp}`card {num} of {total}`
1. [ ] when you check if the `answer` is the same as `card["back"]`
       * [ ] if so, increment `score` by one
1. [ ] at the end of the loop, increment `num` by `1`

```{rubric} in play(), after the loop
```

1. [ ] print {samp}`"{score} of {total}"`

### Part 13: Prettify flashcards

This part is about making the the flashcards look nicer. Feel free to adjust
these suggestions to your taste.


```{rubric} throughout your file
```

1. [ ] get rid of any debug `print()` statements

```{rubric} at the top of your file
```

1. [ ] make a global variable `WIDTH` and set it to around `75`

```{rubric} in play()
```

1. [ ] print a line to the beginning and end of each card
1. [ ] add some extra newlines around various elements
1. [ ] center any string by calling the `.center()` method on it and
       pass the argument `WIDTH`. For example, the `card["front"]` line.
1. [ ] right align any string by calling the .rjust() method on it and passing
       the argument `WIDTH`. For example, the {samp}`card {x} of {y}` line.
1. [ ] print {samp}`"{score} of {total}"` after the end of each card

Bonus ideas
-----------

* keep a log with dates and scores
* make extra flashcard files, then add a menu to allow the user to select
  which topic(s) they would like to be quizzed on
* add an optional limit argument to limit the number of cards to go
  through at a time
* add extra columns to flashcards files to keep track of each time you get the
* answer right and wrong, use this to generate reports

Reference
---------

You can view my completed scripts here:

* [flashcards.py][]
* [fancy-flashcards.py][]

[flashcards.py]:  http://github.com/alissa-huskey/python-class/blob/master/pythonclass/exercises/flashcards.py
[fancy-flashcards.py]:  http://github.com/alissa-huskey/python-class/blob/master/pythonclass/exercises/fancy-flashcards.py