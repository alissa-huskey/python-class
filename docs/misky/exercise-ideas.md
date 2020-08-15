Exercises
---------

"99 bottles of beer on the wall."
  - print every line of the song
  - when you reach 1 bottle left, the word "bottles" becomes singular.

Magic 8 ball:
https://en.wikipedia.org/wiki/Magic_8-Ball
- Make a list of 20 answers  where 10 are positive, 5 are non-committtal, and 5 are negative
- Allow the user to ask a question
- Display a progress message like "thinking..." and pause for effect
- Randomly display one of the answers

Rock, Paper, Scissors:
- Ask the player to pick one of rock, paper, or scissors
- Have the computer randomly select one of rock, paper, or scissors.
- Print the winner:
  - Rock beats scissors
  - Paper beats rock
  - Scissors beats paper

Mad Libs:
- Write a `< 500` word short story then choose 6-8 words to replace with blanks
  with lexical categories like noun, verb, place, part of body.
- Prompt the player for a response for each kind of word.
- Words
  - verb: action (run, fly, sit)
  - noun: person/place/thing  ()
  - adjective: describes a noun  (pretty, fast, stupid)
  - adverb: describes an action (slowly, mistakenly)
- Ideas:
  - letter from camp
  - personal ad
  - my evil plan to take over the world
  - what I did on my summer vacation
  - when the aliens arrived

Word Length
1. As the user for a input
2. Split the result into a list of words
3. Iterate over the list and print out each word on a new line
4. Next to the word, print how many characters are in the word using `len(word)`


Pig Latin Translator
1. As the user for a input
2. Split the result into a list of words
3. Iterate over every word and change it according to the following rules:
    a. if the first letter is a consonant, move it to the end and add "ay"
    b. if the first letter is a vowel just add "way" to the end 4. Join the words back into a sentence and print it.  

Pirate Translator
1. As the user for a input
2. Split the result into a list of words
3. Iterate over every word and and swap out words like:
    - am, is: be
    - and: 'n
    - buddy friend: matey
    - have: 'ave
    - hi, hello: ahoy!
    - I'm: I be
    - (suffix) ing: in'
    - it's: 'tis
    - my: me
    - note: nah
    - of: o'
    - people: scallywags
    - the: th'
    - there: thar
    - to: t'
    - you: ye


Make a todo list
1. Make a list of 3-5 todo items
2. Print each item on the list on a line, with a number next to it
3. Ask the user for input
4. If the user replies with a number, delete that item from the list using
   hint: you will need to convert the string to an int using 
   mylist.pop(<index-number>)
5. Otherwise, add their item to the list using
   mylist.append()
6. Print the revised list
See also: https://www.tutorialspoint.com/python/python_lists.htm
Emoji Translator
1. Take a sentence and split it into words.
2. Use a for loop to iterate over the list.
3. Use an if-statement to check every item
4. Set the list value for any matching emoji code to its emoji symbol.
    Pick any three from here: https://gist.github.com/rxaviers/7360908
    - :smile:         😄
    - :wink:          😉
    - :sunglasses:    😎

Replace space with underscore

rot13 encoding

Convert word to (not very good) password
1. Start with a string
2. Convert it into a list of individual characters
3. Iterate over the list and check each character. Replace the following:
```
    - a     : @
    - o     : *
    - S     : $
    - l     : 1
    - I     : !
    - E     : 3
    - O     : 0
    - B     : 8
    - space : _
```

Topics
------

comment
functions, calling, defining
if-statements, conditions, not, in, or, and
writing functions
  - docstring
  - arguments
  - return values

types
  - converting

input

lists, dictionaries, while-loop, for-loop

modules

python shell
- getting help

range
lower
print a line
