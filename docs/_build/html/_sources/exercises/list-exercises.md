List Exercises
==============

Hand of Cards
-------------
1. Make a list of cards like: \
    `cards = ["7H", "QC", "2S", "AD", "3C"]`
2. Iterate over the list and print each card symbol with a space after it. \
    Hint: To print without adding a newline use `print(... end="")`

**OUTPUT**
```
    Your hand: 7H QC 2S AD 3C
```

Table of Contents
-----------------
1. Make a list of chapters like:
```
  chapters = [
    "The Setup",
    "A Good First Program",
    "Comments And Pound Characters",
    "Numbers And Math"
  ]
```
2. Use the `enumerate()` function to iterate over the list and print each chapter number and title.

**OUTPUT**
```
  Table of Contents

  Chapter 1: The Setup
  Chapter 2: A Good First Program
  Chapter 3: Comments And Pound Characters
  Chapter 4: Numbers And Math
```

Running Calculator
------------------
1. Make a list of numbers.
2. Iterate over the list. For each element:
  *  Add the element value to the running total.
  *  Print the value and the balance.

**OUTPUT**
```
            =  0
    + 8     =  8
    + 5     = 13
```

Reformat CSV Line
-----------------
1. Start with the string: `"smith,john,415-555-5555"`
2. Split it into a list on `,` \
    Hint: To split on a different delimiter use `str.split(<delim>)`
3. Print the full name capitalized, then the phone number. \
    Hint: Access list elements with `varname[<index-number>]`

**OUTPUT**
```
    John Smith: 415-555-5555
```

Randomly Swap Character Case
----------------------------
1. Convert a string into a list of individual characters
2. Iterate over the list and randomly either switch the case of the character
   or leave it the way it is. \
    Hints:
      * String case functions `str.islower()`, `str.isupper()`, `str.upper()`
        and `str.lower()`
      * Change list values with `varname[<index-number>] = <newval>`
3. Join the list back into a new string.
4. Print the original string and the case-swapped string.

**OUTPUT**
```
    number: nUmBeR
```
