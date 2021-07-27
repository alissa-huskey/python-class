List String Exercises
=====================

Emoji Translator
----------------

1. Starting with a sentence like: \
    `"oh hai :smile:"`
2. Split it into a list of words
3. Replace the matching emoji code (`:smile:`) with its symbol (😄).
4. Join it back to a string and print the result.
5. Bonus:
    Pick any three (no more than three) from here: https://gist.github.com/rxaviers/7360908

**OUTPUT** \
`oh hai 😄`


leet converter
--------------
1. Start with a string like `"hello"`
2. Convert it into a list of individual characters
3. Replace the following characters:
```
    - a     : @
    - s     : $
    - l     : 1
    - i     : !
    - e     : 3
    - o     : 0
    - t     : 7
    - space : _
```
4. Join it back to a string and print the result.

**OUTPUT**
`h3110`

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
