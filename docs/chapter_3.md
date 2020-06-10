Chapter 3: Guess the Number
===========================

> Based on: http://inventwithpython.com/invent4thed/chapter3.html

In this chapter, you’re going to make a Guess the Number game. The computer will think of a secret number from 1 to 20 and ask the user to guess it. After each guess, the computer will tell the user whether the number is too high or too low. The user wins if they can guess the number within six tries.

This is a good game to code because it covers many programming concepts in a short program. You’ll learn how to convert values to different data types and when you would need to do this. Since this program is a game, from now on we’ll call the user the player.


Part 1. Create a New Script
----------------------------

Follow the instructions in [Repl.it Tips](#docs/replit-tips.md) to create a new file called "guess.py" and change your `.replit` file to run it.

Add a comment to the first line of the script to describe it:

     # This is a Guess the Number game.



Part 2. Use the `random` Module
-------------------------------

Python has a limited set of functions built into it like the `print()` function that you are already familiar with. More functions can be accessed through  `modules`.

A `module` is a kind of reusable code that can be loaded into your scripts using the `import` keyword.

We are going to use the `random` module in this script. It has a function `randint()` which we will use to get a random number.

To call a function that is part of a module, put the module ***namespace*** in front of the function followed by a `.`.

The `randint()` function takes two arguments. The first is the minimum number, and the second is the maximum number.

Try it out in your Python shell:

    >>> imort random
    >>> random.randint(1,20)


#### Tip

The Python shell has a `help()` function that will give you information on functions, modules and more.

Try some of these in your Python shell:

    >>> help(print)
    >>> help(def)
    >>> help(if)

To get help for functions in a module, you must import it first.

    >>> import random
    >>> help(random.randint)
    Help on method randint in module random:

    randint(a, b) method of random.Random instance
      Return random integer in range [a, b], including both end points.

#### Edit Your Script

Now that you understand how importing works, import the module, then save
a random number to the `number` variable by calling `random.randint()`.

Let's also set the maximum number of guesses.

***guess.py***

```python3
# This is a Guess the Number game.
import random

number = random.randint(1, 20)
max_guesses = 6
```


Part 3: Welcome the Player
--------------------------

We've used the `input()` function before to get feedback from the user. It can take an optional ***argument*** the prompt string.

Let's use these functions together to greet the user.

#### Edit Your Script

***guess.py***

```python3
# This is a Guess the Number game.
import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")
print()
```

Note the space after the `?` in the `input()` line. This way there will be a space between the prompt and the cursor.


Part 4: Let the Player Guess
----------------------------

We've used the a `for` loop before to loop over items in a list. Here we
will use the `range()` function, which allows us to easily repeat the loop
a specific number of times. We will give it two arguments, the starting
number and the maximum number of guesses from earlier.

We've also the `print()` function before, but in the past we've always
passed it one argument. It can take as many arguments as you want, and it
will convert them each to strings and then print them with spaces
in-between. Let's use this handy way to print the guess number.


#### Edit Your Script

***guess.py***

```python3
# This is a Guess the Number game.
import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")

for guess_count in range(1, max_guesses):
    print("Guess", guess_count, "of", max_guesses)
    guess = input("Your guess: ")
```

Part 5: Check the Guess
-----------------------

The value in the `guess` variable is a string, because `input()` always
returns a string. But we need a number variable to check the guess. To
convert a string to an integer, we will use the `int()` function.

Once it is converted, we can use an ***if statement*** to check it. We'll
use the `break` keyword to exit the loop early if the guess is correct.

```python3
# This is a Guess the Number game.
import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")
print()

for guess_count in range(1, max_guesses):
    print("Guess", guess_count, "of", max_guesses)

    guess = input("Your guess: ")
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        break

    print()

```


Part 6: Check if the Player Won
-------------------------------

Once we have completed the ***for loop***, we both the `guess` and the
`guess_count` variable will still be set to the last value they were when
the loop ran.

We'll check the `guess` value to see if they've won using an if statement.

Both the `guess` variable and the `number` variable are integers, but we
need them to be strings in order to ***concatonate*** them within the
endgame message. To convert an int to a string, we'll use the `str()`
function.

#### Edit Your Script

***guess.py***

```python3
# This is a Guess the Number game.
import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")
print()

for guess_count in range(1, max_guesses):
    print("Guess", guess_count, "of", max_guesses)

    guess = input("Your guess: ")
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        break

    print()


if guess == number:
    guess_count = str(guess_count)
    print('Good job, ' + player + '! You guessed my number in ' + guess_count + ' guesses!')

else:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
```


Part 7: Make it your own
------------------------

Change it to make it your own. Here are some ideas.

- Check to make sure the guess is not out of range first. If it is, don't
  count the guess and let them try again.

- Ask the user if they want to play on easy, normal or hard mode when they
  start, then change the number of guesses or the range of possible
  numbers based on their answer.

- Keep track of how far away each guess is from the right number. If they
  get further away, print out an extra message to let them know.

- Don't end after the player wins or loses, but insted offer them the
  chance to play again. Keep track of their wins, losses and total number
  of games played and print it at the end of each round.




